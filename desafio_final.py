import json
import llm_client

lista_de_resenhas = []

with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as file:
    for line in file:
        lista_de_resenhas.append(line.strip())

lista_de_resenhas_json = []

for resenha in lista_de_resenhas:
    resenha_json = llm_client.get_llm_response(resenha)
    resenha_dict = json.loads(resenha_json)
    lista_de_resenhas_json.append(resenha_dict)

print(lista_de_resenhas_json)