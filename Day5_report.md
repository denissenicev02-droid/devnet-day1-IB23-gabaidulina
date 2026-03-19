# Day 5 Report — Module 8 Capstone

## 1) Student
- Name: Gabaidulina
- Group:  IB23
- Token: D1-IB-23-5b-05-A84D
- Repo: https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/tree/feature/day5

## 2) YANG (8.3.5)
- Evidence files:
  - artifacts/day5/yang/ietf-interfaces.yang y
  - artifacts/day5/yang/pyang_version.txt y
  - artifacts/day5/yang/pyang_tree.txt y
- Screenshot (optional): pyang tree output y

## 3) Webex (8.6.7)
- Room title contains token_hash8: Yes
- Message text contains token_hash8: Yes
- Evidence files:
  - me.json / rooms_list.json / room_create.json / message_post.json / messages_list.json y

## 4) Packet Tracer Controller REST (8.8.3)
- external_access_check contains “empty ticket”: Yes
- serviceTicket saved: Yes
- Evidence files:
  - external_access_check.json / network_devices.json / hosts.json y
  - postman_collection.json / postman_environment.json y
  - pt_internal_output.txt y

## 5) Commands output (paste exact)

### python src/day5_summary_builder.py
```text
Summary saved to artifacts/day5/summary.json
{
    "schema_version": "5.0",
    "student": {
        "token": "D1-IB-23-5b-05-A84D",
        "token_hash8": "cb1163ec",
        "name": "",
        "group": ""
    },
    "yang": {
        "ok": true,
        "evidence_sha": "949de5d3ee156508fe0af9f6a93bb6b16cf3e397ba9f6ba226e1c50bb5256edb"
    },
    "webex": {
        "ok": true,
        "room_title_contains_hash8": true,
        "evidence_sha": "3b72f8816324c171bef1957ca0906119ee4d8d6273b81a24428d5e0a1eeb03d2"
    },
    "pt": {
        "ok": true,
        "empty_ticket_seen": true,
        "evidence_sha": "78633c6cd7f2940fd665c6d81c10c7d7da1678ed338de544335a80d2e8a3d9cc"
    },
    "bonus": {
        "optional_ok": false,
        "evidence_sha": null
    },
    "validation_passed": true
}
```
### pytest -q
```text
................................                  [100%]
32 passed in 0.85s
```

## 6) Problems & fixes (at least 1)
- Problem 1: pyang -v > pyang_version.txt — файл оказался пустым
- Fix: pyang -v 2> artifacts/day5/yang/pyang_version.txt
- Proof: cat artifacts/day5/yang/pyang_version.txt показал версию pyang.

- Problem 2: Python скрипт внутри Packet Tracer возвращал 403 с ошибкой TypeError: string indices must be integers, not str on line 15
- Fix: Переписалa скрипт так, чтобы он сам получал ticket через POST к 192.168.101.254/api/v1/ticket внутри PT, и сразу использовал его для GET
- Proof: Вывод консоли PT показал ('Request status: ', 200) и список всех хостов.
...