import os
import json
import hashlib
import pytest

BASE = "artifacts/day5"

def load_json(path):
    with open(path) as f:
        return json.load(f)

def file_contains(path, text):
    with open(path, "r", errors="ignore") as f:
        return text in f.read()

# --- Артефакты существуют и не пустые ---

REQUIRED_FILES = [
    f"{BASE}/yang/ietf-interfaces.yang",
    f"{BASE}/yang/pyang_version.txt",
    f"{BASE}/yang/pyang_tree.txt",
    f"{BASE}/webex/me.json",
    f"{BASE}/webex/rooms_list.json",
    f"{BASE}/webex/room_create.json",
    f"{BASE}/webex/message_post.json",
    f"{BASE}/webex/messages_list.json",
    f"{BASE}/pt/external_access_check.json",
    f"{BASE}/pt/serviceTicket.txt",
    f"{BASE}/pt/network_devices.json",
    f"{BASE}/pt/hosts.json",
    f"{BASE}/pt/postman_collection.json",
    f"{BASE}/pt/postman_environment.json",
    f"{BASE}/pt/pt_internal_output.txt",
    f"{BASE}/summary.json",
]

@pytest.mark.parametrize("path", REQUIRED_FILES)
def test_artifact_exists_and_nonempty(path):
    assert os.path.exists(path), f"Missing: {path}"
    assert os.path.getsize(path) > 0, f"Empty: {path}"

# --- Summary валиден ---

def test_summary_schema_version():
    s = load_json(f"{BASE}/summary.json")
    assert s["schema_version"] == "5.0"

def test_token_hash8_correct():
    s = load_json(f"{BASE}/summary.json")
    token = os.environ.get("STUDENT_TOKEN", "")
    expected = hashlib.sha256(token.encode()).hexdigest()[:8]
    assert s["student"]["token_hash8"] == expected

def test_yang_ok():
    s = load_json(f"{BASE}/summary.json")
    assert s["yang"]["ok"] is True

def test_yang_tree_contains_interfaces():
    assert file_contains(f"{BASE}/yang/pyang_tree.txt", "+--rw interfaces")

def test_yang_tree_contains_enabled():
    assert file_contains(f"{BASE}/yang/pyang_tree.txt", "enabled")

def test_webex_room_title_contains_hash8():
    s = load_json(f"{BASE}/summary.json")
    assert s["webex"]["room_title_contains_hash8"] is True

def test_webex_ok():
    s = load_json(f"{BASE}/summary.json")
    assert s["webex"]["ok"] is True

def test_pt_empty_ticket_seen():
    s = load_json(f"{BASE}/summary.json")
    assert s["pt"]["empty_ticket_seen"] is True

def test_pt_ok():
    s = load_json(f"{BASE}/summary.json")
    assert s["pt"]["ok"] is True

def test_pt_network_devices_version():
    assert file_contains(f"{BASE}/pt/network_devices.json", '"version": "1.0"')

def test_pt_hosts_version():
    assert file_contains(f"{BASE}/pt/hosts.json", '"version": "1.0"')

def test_validation_passed():
    s = load_json(f"{BASE}/summary.json")
    assert s["validation_passed"] is True