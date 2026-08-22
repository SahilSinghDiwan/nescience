"""NESC-13 — Investigation Notes: the public methodology drawer.

Covers the markdown subset (including the escaping the template's |safe
depends on), the loader, and the two routes."""

import pytest

import notes
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


# ----------------------------------------------------------
# Markdown subset
# ----------------------------------------------------------

def test_paragraphs_and_inline_marks():
    html = notes.render_markdown("A **bold** and *italic* line with `code`.")
    assert "<strong>bold</strong>" in html
    assert "<em>italic</em>" in html
    assert "<code>code</code>" in html
    assert html.startswith("<p>")


def test_headings_lists_quotes_and_rules():
    html = notes.render_markdown("## Head\n\n- one\n- two\n\n> quoted\n\n---")
    assert "<h2>Head</h2>" in html
    assert "<ul><li>one</li><li>two</li></ul>" in html
    assert "<blockquote>quoted</blockquote>" in html
    assert '<hr class="rule">' in html


def test_list_items_may_wrap_across_lines():
    """Authored notes hard-wrap prose; a wrapped bullet is still one bullet."""
    html = notes.render_markdown(
        "- first item that keeps\n  going on the next line\n- second item"
    )
    assert "<ul><li>first item that keeps going on the next line</li>" in html
    assert "<li>second item</li></ul>" in html


def test_h1_is_demoted_so_the_page_keeps_one_h1():
    assert "<h2>Title</h2>" in notes.render_markdown("# Title")


def test_authored_html_is_escaped_not_rendered():
    """The template marks body_html |safe, so escaping must happen here."""
    html = notes.render_markdown('<script>alert("x")</script> & <b>raw</b>')
    assert "<script>" not in html
    assert "<b>raw</b>" not in html
    assert "&lt;script&gt;" in html
    assert "&amp;" in html


def test_links_are_internal_only():
    """No outbound links: the exhibit makes no network calls anywhere."""
    internal = notes.render_markdown("see [notes](/archive/notes)")
    assert '<a href="/archive/notes">notes</a>' in internal

    external = notes.render_markdown("see [site](https://example.com)")
    assert "<a" not in external
    assert "site" in external


# ----------------------------------------------------------
# Loader
# ----------------------------------------------------------

def test_notes_load_with_parsed_headers():
    loaded = notes.all_notes()
    assert loaded, "expected authored notes under docs/notes/"
    for note in loaded:
        assert note["title"]
        assert note["number"].isdigit()
        assert note["slug"]
        assert note["body_html"]
        # The header block must be consumed, never rendered into the body.
        assert "title:" not in note["body_html"]
        assert "summary:" not in note["body_html"]


def test_notes_are_ordered_by_number():
    numbers = [n["number"] for n in notes.all_notes()]
    assert numbers == sorted(numbers)


def test_get_by_slug_and_miss():
    first = notes.all_notes()[0]
    assert notes.get(first["slug"])["title"] == first["title"]
    assert notes.get("no-such-note") is None


# ----------------------------------------------------------
# Routes
# ----------------------------------------------------------

def test_index_lists_every_note(client):
    body = client.get("/archive/notes").get_data(as_text=True)
    assert "INVESTIGATION NOTES" in body
    for note in notes.all_notes():
        assert note["title"] in body
        assert f"/archive/notes/{note['slug']}" in body


def test_note_page_renders_body(client):
    note = notes.all_notes()[0]
    body = client.get(f"/archive/notes/{note['slug']}").get_data(as_text=True)
    assert note["title"].upper() in body
    # Rendered as markup, not as escaped source.
    assert "<p>" in body


def test_unknown_note_404s(client):
    assert client.get("/archive/notes/not-a-note").status_code == 404


def test_hub_links_to_notes_not_a_placeholder(client):
    """[006] is a real drawer now — the hub must not send it to /pending."""
    body = client.get("/archive").get_data(as_text=True)
    assert "/archive/notes" in body
    assert "/archive/pending/notes" not in body
