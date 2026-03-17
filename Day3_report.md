# Day 3 Report — Lab 4.5.5 + Auto-check artifacts

## 1) Student
- Name: Габайдулина Найля
- Group: IB23
- Token: D1-IB-23-5b-05-A84D
- Repo: https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/tree/feature/day3-api-lab

## 2) Lab 4.5.5 completion evidence
- API docs (Try it out) screenshots:
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/3.2.png)
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/3.3.png)
- Postman screenshots:
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/3.4.png)
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/3.5.png)
- Python run screenshot:
![Image alt](https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/raw/master/screns/3.1.png)

## 3) Artifacts checklist
- artifacts/day3/books_before.json: Yes
- artifacts/day3/books_sorted_isbn.json: Yes
- artifacts/day3/mybook_post.json: Yes
- artifacts/day3/books_by_me.json: Yes
- artifacts/day3/add100_report.json: Yes
- artifacts/day3/postman_collection.json: Yes
- artifacts/day3/postman_environment.json: Yes
- artifacts/day3/curl_get_books.txt: Yes
- artifacts/day3/curl_get_books_isbn.txt: Yes
- artifacts/day3/curl_get_books_sorted.txt: Yes
- artifacts/day3/summary.json: Yes

## 4) Command outputs (paste exact)
### 4.1 Script run
```text
{
  "schema_version": "3.1",
  "generated_utc": "2026-03-17T22:18:10.383357+00:00",
  "student": {
    "token": "D1-IB-23-5b-05-A84D",
    "token_hash8": "cb1163ec",
    "name": "Gabaidulina",
    "group": "IB23"
  },
  "lab": {
    "apihost": "http://library.demo.local",
    "must_use": {
      "login_endpoint": "http://library.demo.local/api/v1/loginViaBasic",
      "books_endpoint": "http://library.demo.local/api/v1/books",
      "api_key_header": "X-API-KEY"
    }
  },
  "artifacts_sha256": {
    "books_before": "de7439d08160b40ca443789183c91456256cb8df41b0cf1a412459699657e782",
    "books_sorted_isbn": "881a0fe47f7532269c160c4c145db9f0281f6a2e191d3ec8d2af7f5e7f4bd46d",
    "mybook_post": "cbe1d5a33e8702679a1cd7b6b2c566c4e5cded28f1ae32fc21f1030be17feb18",
    "books_by_me": "3dfef600baead5fd016823d5d1ca04a33abb1aa49d69c0033f713981baacd845",
    "add100_report": "8247e31cfd94ceb499fcd43336c22b612a78d2a2fc42c453150562245079a624",
    "postman_collection": "b87a9a2a2e8143bef5317e3ef8271cf93eacf94ef216ed4b376cd1bd3703fb5d",
    "postman_environment": "28ee6a23d5aa199ce30cfd1f789f39805009c36306e462748f63f285dc74c005",
    "curl_get_books": "de64bae22fde03848fbeb14e2a6c661cf7e9eed12f29b574d596224bf5bf6bf9",
    "curl_get_books_isbn": "ee1093008a5d89a75d9aaf8a2c8a7987c8841bce0c4028d02d32e78f083fb227",
    "curl_get_books_sorted": "6e87e9da9e47b139ee6633b979ddefac161bd7ee3006a66118067b2b866bcef5"
  },
  "validation": {
    "must_have_mybook_title_contains_token_hash8": true,
    "must_have_added_100": true
  }
}
```

### 4.2 Tests
```text
3 passed in 0.38s
```

## 5) Problems & fixes (at least 1)
- Problem: Папка artifacts/day3 не существовала 
- Fix: tee не мог записать файл
- Proof: решила через mkdir -p artifacts/day3, потом повторила curl-команды
...