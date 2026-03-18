# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name: Gabaidulina
- Group:  IB23
- Token: D1-IB-23-5b-05-A84D
- Repo: https://github.com/denissenicev02-droid/devnet-day1-IB23-gabaidulina/tree/feature/day4

## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: y
- artifacts/day4/docker/sampleapp_token_proof.txt: y
- artifacts/day4/docker/sampleapp_docker_ps.txt: y
- artifacts/day4/docker/sampleapp_build_log.txt: y

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt: y
- artifacts/day4/jenkins/buildapp_console.txt: y
- artifacts/day4/jenkins/testapp_console.txt: y
- artifacts/day4/jenkins/pipeline_script.groovy: y
- artifacts/day4/jenkins/pipeline_console.txt: y
- artifacts/day4/jenkins/jenkins_url.txt: y

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_ping.txt: y
- artifacts/day4/ansible/ansible_hello.txt: y
- artifacts/day4/ansible/ansible_playbook_install.txt: y
- artifacts/day4/ansible/ports_conf_after.txt: y
- artifacts/day4/ansible/curl_apache_8081.txt: y

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt: y
- artifacts/day4/security/login_v1.txt: y
- artifacts/day4/security/signup_v2.txt: y
- artifacts/day4/security/login_v2.txt: y
- artifacts/day4/security/db_tables.txt: y
- artifacts/day4/security/db_user_hash_sample.txt: y

## 3) Commands output

### python src/day4_summary_builder.py
```text
{
  "schema_version": "4.1",
  "generated_utc": "2026-03-18T21:44:14.220799+00:00",
  "student": {
    "token": "D1-IB-23-5b-05-A84D",
    "token_hash8": "cb1163ec",
    "name": "Gabaidulina",
    "group": "IB23"
  },
  "checks": {
    "docker_token_in_page": true,
    "docker_tokenproof": true,
    "ansible_port_8081": true,
    "jenkins_pipeline_has_stages": true,
    "security_db_has_tables": true
  },
  "evidence_sha256": {
    "docker_sampleapp_curl": "bec89afb35fa8430d16393a7ccfe9b8d6fdd24a0543c0fdaeba4c4c1a6830fc8",
    "docker_ps": "c26f1a0d46edebc2fae32238d5ad3b54ceb3f6ad19a4c4184450746235f8d6c8",
    "docker_build_log": "ebe38fd5f003b0582a433da8e9f704bb83e263faf1fc408e743ab539cc2a72d3",
    "docker_token_proof": "0161a6688f9e1f314c94f7633bcdc554d3d4621de36ea8e11ba89288e73a580a",
    "jenkins_docker_ps": "fe9fb44ae9a606a5c15595ce03bca49c32ac6faf4cdef9e3436298a2d6592510",
    "buildapp_console": "0352b8f04d91085413398893ca5286870270e9f5a2235b51052ce8899d5aa876",
    "testapp_console": "cb5182fac0742a2ba1f35d551d28127b51e007da213c80091fa90556600a41b4",
    "pipeline_script": "659ffcab7df8137c32443aa6982688cc802be2519b7821d4d5ab27c8bb5e3293",
    "pipeline_console": "d6bf85f91411ca365a0d89d75822118953b47a000d03cf76cd187a139c2345fb",
    "jenkins_url": "185f195598830dbc315eb3a6741f97eace245e9d9d2a7225c5da77b87f27f3fc",
    "ansible_ping": "3013fd2ffe5a5734968d58204af7d4d50dcd5ba11be1cba123c8b7f684274fe0",
    "ansible_hello": "58bb784bf78fcac95c276184b5f2f0e0ad287c0908a29e9f23683821e603bc81",
    "ansible_playbook_install": "62b7486c8dbbf456f9d63ba7fe7059eadd001d760cef4092b4456d6ac8a82d95",
    "ports_conf_after": "c41a881f6b628b5bc2771dfa6125eb0744f272b666aead54c09b20a8c766c72d",
    "curl_apache_8081": "e870932d034a48187d6685a82452e2dfbd36db1ae9840a89275eaab07b73a009",
    "signup_v1": "d299da4792553b50de72449cda41e26da947f741018a6c11f3a94b009be6579f",
    "login_v1": "4e885c0fa26fb9497717e18e8a289a45d1cce748c0bd91a401302c729ca48cfc",
    "signup_v2": "d299da4792553b50de72449cda41e26da947f741018a6c11f3a94b009be6579f",
    "login_v2": "4e885c0fa26fb9497717e18e8a289a45d1cce748c0bd91a401302c729ca48cfc",
    "db_tables": "587369782e04120a6186e0781b9a40356c51c4041422222614df4f98f02961c8",
    "db_user_hash_sample": "65641d0204c4cb61d53442d2475ffb5fe3bd38932c87ba565eef9202cf618d33"
  },
  "validation_passed": true,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}
```

### pytest -q
```text
....                              [100%]
4 passed in 1.28s
```
## 4) Short reflection (5–8 lines)
- What was the hardest part today and why?
```text
Самым сложным оказался Docker.Также возникла трудность с передачей переменной STUDENT_TOKEN внутрь контейнера — она не передаётся автоматически, нужно явно указывать
```
- One security mistake you avoided (or made and fixed):
```text
python:latest (версия 3.14) не совместим с Flask из-за ошибки RuntimeError: can't start new thread
```

## 5) Problems & fixes (at least 1)
- Problem 1: TOKEN_HASH8=e3b0c442 — хэш пустой строки вместо токена.
- Fix: -e STUDENT_TOKEN="$STUDENT_TOKEN" в команду docker run внутри sample-app.sh
- Proof: artifacts/day4/docker/sampleapp_token_proof.txt содержит TOKEN_HASH8=cb1163ec

- Problem 3: Jenkins не запускался — ошибка Failed to create worker thread
- Fix: Добавить флаг --privileged в docker run для Jenkins
- Proof: artifacts/day4/jenkins/jenkins_docker_ps.txt — контейнер jenkins_server запущен.
...