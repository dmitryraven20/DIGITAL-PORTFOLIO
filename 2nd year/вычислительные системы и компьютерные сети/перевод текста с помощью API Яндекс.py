import json
import requests

folder_id = 'b1gtf3dqupicap0o7l1v'
IAM_TOKEN = 't1.9euelZqSjp7NzJucyp6QjcuUm82Kle3rnpWais-QkJ7OlZOcic6Llpaenprl8_cYQFti-e98aikk_N3z91huWGL573xqKST8.tV0Ncjnvyy3_5IRm0WwpkA3lDvSAkS7b6XVzjmPeaN80boQ_JujQZU_Qq2usPvboTFzct92hl6Eu2LQtgSsDBA'
target_language = 'ru'
url = "https://translate.api.cloud.yandex.net/translate/v2/translate"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + IAM_TOKEN
}
body = {
    "targetLanguageCode": target_language,
    "texts": '',
    "folderId": folder_id
}

name = 'text.txt'
answer = 'answer.txt'
lines = []
an = 0

with open(name, 'r', encoding="utf-8") as file:
    for line in file:
        lines.append(line.strip())

print(lines)

with open("answer.txt", 'w') as file:
    for line in open(name, 'r', encoding="utf-8"):
        body["texts"] = line.strip()
        response = requests.post(url, headers=headers, json=body)
        file.write(json.dumps(response.json(), ensure_ascii=False) + "\n")

with open("answer.txt", 'r') as file:
    an = file.readline()

print("Готово: \n", an)