import os
import json
import hashlib

BASE = "artifacts/day5"

def sha256_file(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def file_contains(path, text):
    if not os.path.exists(path):
        return False
    with open(path, "r", errors="ignore") as f:
        return text in f.read()

def build_summary():
    student_token = os.environ.get("STUDENT_TOKEN", "")
    token_hash8 = hashlib.sha256(student_token.encode()).hexdigest()[:8]

    # YANG checks
    yang_tree = f"{BASE}/yang/pyang_tree.txt"
    yang_ok = file_contains(yang_tree, "+--rw interfaces")

    # Webex checks
    room_create = f"{BASE}/webex/room_create.json"
    webex_hash_ok = False
    if os.path.exists(room_create):
        with open(room_create) as f:
            try:
                data = json.load(f)
                webex_hash_ok = token_hash8 in data.get("title", "")
            except Exception:
                pass
    webex_ok = webex_hash_ok

    # PT checks
    ext_check = f"{BASE}/pt/external_access_check.json"
    net_dev   = f"{BASE}/pt/network_devices.json"
    hosts     = f"{BASE}/pt/hosts.json"

    empty_ticket_seen = file_contains(ext_check, "empty ticket")
    pt_version_ok = (
        file_contains(net_dev, '"version": "1.0"') and
        file_contains(hosts,   '"version": "1.0"')
    )
    pt_ok = empty_ticket_seen and pt_version_ok

    summary = {
        "schema_version": "5.0",
        "student": {
            "token": student_token,
            "token_hash8": token_hash8,
            "name": os.environ.get("STUDENT_NAME", ""),
            "group": os.environ.get("STUDENT_GROUP", "")
        },
        "yang": {
            "ok": yang_ok,
            "evidence_sha": sha256_file(yang_tree)
        },
        "webex": {
            "ok": webex_ok,
            "room_title_contains_hash8": webex_hash_ok,
            "evidence_sha": sha256_file(room_create)
        },
        "pt": {
            "ok": pt_ok,
            "empty_ticket_seen": empty_ticket_seen,
            "evidence_sha": sha256_file(net_dev)
        },
        "bonus": {
            "optional_ok": False,
            "evidence_sha": None
        },
        "validation_passed": yang_ok and webex_ok and pt_ok
    }

    out_path = f"{BASE}/summary.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=4)
    print(f"Summary saved to {out_path}")
    print(json.dumps(summary, indent=4))
    return summary

if __name__ == "__main__":
    build_summary()