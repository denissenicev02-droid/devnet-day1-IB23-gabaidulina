# Day 2 Report — Git + Data Formats + Tests

## 1) Student
- Name: Габайдулина Найля
- Group: IB23
- Token: D1-IB-23-5b-05-A84D
- Repo: [\[link\]](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/tree/feature/day2-dataformats)
- PR link (day2): (also in artifacts/day2/pr_link.txt) https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/pull/1

## 2) NetAcad progress
- Module 2.2 done: [Yes] + screenshot
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/scren2.1.png)
- Module 3.1–3.6 done: [list what completed] + screenshot
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/scren2.2.png)

## 3) Git evidence
- File `artifacts/day2/git_log.txt` exists: [Yes]
- File `artifacts/day2/conflict_log.txt` exists: [Yes]
- Conflict note (1–2 lines): Ветки `feature/day2-readme-A` и `feature/day2-readme-B` изменили одну и ту же строку в README.md в разделе `## Progress`. Конфликт решён вручную — оставлены обе строки, сделан коммит с сообщением "Resolve README conflict (Day2)"

## 4) Generated artifacts (Day2)
- normalized.json: [Yes]
- normalized.yaml: [Yes]
- normalized.xml: [Yes]
- normalized.csv: [Yes]
- summary.json: [Yes]

## 5) Commands output (paste EXACT output)
### 5.1 Generator
{
  "computed": {
    "title_len": 18
  },
  "generated_utc": "2026-03-17T10:09:08.798450+00:00",
  "input": {
    "path": "artifacts/day1/response.json",
    "sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "outputs": {
    "normalized_csv_sha256": "e5c068e83eeb2b135a86729d09c358ba3854a20e6b19f789a053e7ec2c34e2fd",
    "normalized_json_sha256": "c7ccda691930e8e768bfefa36aade3241588f7ebb02e660a1a125dd9ea2ea650",
    "normalized_xml_sha256": "9702f8081ee6e8a2bbdbeb25d064867bea9e86b077fe78434675ddfbf1c5302b",
    "normalized_yaml_sha256": "a77e1c8987e27a342ec0bde5e213e5c816310923c4ff42db7d543f1df89f0f8b"
  },
  "schema_version": "2.0",
  "student": {
    "group": "IB23",
    "name": "Gabaidulina",
    "token": "D1-IB-23-5b-05-A84D",
    "token_hash8": "cb1163ec"
  }
}


### 5.2 Tests
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/scren2.4.png)

## 6) What I learned (3–6 bullets)
- Как создавать ветки, открывать PR и сливать их в GitHub
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/scren2.3.png)
- Как возникают merge-конфликты когда две ветки меняют одну строку
- Как вручную решать конфликты в VS Code
- Как сериализовать данные в JSON, YAML, XML и CSV из одной Python-модели
- Как работает валидация JSON Schema через jsonschema
- Как вычислять SHA-256 хэш токена для уникальности артефактов


## 7) Problems & fixes (at least 1)
- Problem: `git push` падал с ошибкой "no upstream branch"
- Fix: `git push --set-upstream origin master`
- Proof (command/file): `git push` работали без флагов

...