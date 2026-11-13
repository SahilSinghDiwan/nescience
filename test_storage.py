# ==========================================================
# NESCIENCE — testimony storage safety (NESC hardening)
#
# participants.json is the only copy of every testimony. These tests
# guard the two ways it could be lost: concurrent writers overwriting
# each other, and a damaged file being read as empty and overwritten.
# ==========================================================

import glob
import json
import multiprocessing
import os

import pytest

import database


@pytest.fixture
def store(tmp_path, monkeypatch):
    path = tmp_path / "participants.json"
    monkeypatch.setattr(database, "FILE_NAME", str(path))
    return path


def _writer(path, n, barrier):
    database.FILE_NAME = path
    barrier.wait()  # release every writer at once to force contention
    database.save_interview({"Case File": {"n": n}})


def test_parallel_writes_are_not_lost(store):
    ctx = multiprocessing.get_context("fork")
    barrier = ctx.Barrier(24)
    procs = [ctx.Process(target=_writer, args=(str(store), n, barrier)) for n in range(24)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
        assert p.exitcode == 0
    saved = json.loads(store.read_text())
    assert sorted(r["Case File"]["n"] for r in saved) == list(range(24))


def test_corrupt_file_is_kept_aside_and_not_overwritten(store):
    store.write_text('[{"half": ')
    with pytest.raises(database.StoreCorruptError):
        database.save_interview({"new": 1})
    aside = glob.glob(str(store) + ".corrupt-*")
    assert len(aside) == 1
    assert open(aside[0]).read() == '[{"half": '


def test_corrupt_file_reads_as_empty_without_destroying_it(store):
    store.write_text("not json")
    assert database.load_interviews() == []
    assert store.read_text() == "not json"


def test_save_leaves_no_temp_files_and_is_valid_json(store):
    database.save_interview({"a": 1})
    database.save_interview({"b": 2})
    assert json.loads(store.read_text()) == [{"a": 1}, {"b": 2}]
    assert [f for f in os.listdir(store.parent) if f.endswith(".tmp")] == []


def test_prepare_runs_under_lock_with_existing_records(store):
    database.save_interview({"a": 1})
    seen = []
    index = database.save_interview({"b": 2}, prepare=lambda existing: seen.append(len(existing)))
    assert seen == [1]
    assert index == 1


def test_submission_to_a_corrupt_archive_is_refused_not_erased(store):
    import app as flaskapp
    store.write_text("[{broken")
    resp = flaskapp.app.test_client().post("/api/interview", json={
        "name": "Ada", "published": False,
        "Module I — Experience": {"Question 1": "a memory"},
    })
    assert resp.status_code == 503
    assert store.read_text() == "[{broken"
