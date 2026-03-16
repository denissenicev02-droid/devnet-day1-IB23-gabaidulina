# Day 1 Report — DevNet Sprint

## 1. Student
- Name: Gabaidulina Nailya
- Group: IB-23-5b
- GitHub repo: https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/tree/master
- Day1 Token: D1-IB-23-5b-05-A84D

## 2. NetAcad progress (Module 1)
- Completed items: [1.1 / 1.2 / 1.3] и повторила безовые команды Linux and Python
- Screenshot(s): 
  - [СКРИНШОТ_1: прогресс NetAcad]
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/scren1.png)

## 3. VM evidence
- File: `artifacts/day1/env.txt` exists:Yes
- Screenshot(s):
  - [СКРИНШОТ_2: терминал в DEVASC VM + hostnamectl/date]
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/scren2.png)

## 4. Repo structure (must match assignment)
- `src/day1_api_hello.py` : [Yes]
- `tests/test_day1_api_hello.py` : [Yes]
- `schemas/day1_summary.schema.json` : [Yes]
- `artifacts/day1/summary.json` : [Yes]
- `artifacts/day1/response.json` : [Yes]

## 5. Commands run (paste EXACT output)
### 5.1 Script run
```text
response.json:
{
  "completed": false,
  "id": 1,
  "title": "delectus aut autem",
  "userId": 1
}

summary.json:
{
  "api": {
    "response_sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe",
    "status_code": 200,
    "url": "https://jsonplaceholder.typicode.com/todos/1",
    "validation_errors": [],
    "validation_passed": true
  },
  "generated_utc": "2026-03-16T10:24:19.575953+00:00",
  "run": {
    "platform": "linux",
    "python": "3.8.2"
  },
  "schema_version": "1.0",
  "student": {
    "group": "IB23",
    "name": "Gabaidulina Nailya",
    "token": "D1-IB-23-5b-05-A84D"
  }
}

### Pytest
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/scren3.png)

## 6. Что я изучил сегодня (3–6 bullets)
- Повторила основные аспекты линукса и питона
- базовый GET запрос к REST API
- JSON Schema для проверки структуры отчета
- минимальный unit test с pytest и jsonschema

## 7. Проблемы и решения (как минимум 1)

- Problem: Не правильный юзернейм, из-за ошибки(случайно написала с вместо полного имени и его нельзя было искоренить в файлах)
- Fix: замена с помощью команды 
- Proof (file/screenshot/command): echo "STUDENT_NAME=Gabaidulina Nailya" > .env