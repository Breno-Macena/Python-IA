import json
from llm_client import get_llm_response

lista_de_resenhas = []

with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as file:
    for line in file:
        lista_de_resenhas.append(line.strip())

lista_de_resenhas_json = []

for resenha in lista_de_resenhas:
    resenha_json = get_llm_response(resenha)
    resenha_json = resenha_json.replace("```json", "").replace("```", "").strip()

    try:
        resenha_dict = json.loads(resenha_json, strict=False)
    except json.JSONDecodeError as error:
        print(f"Erro ao converter para JSON: {error}")
        print(resenha_json)
        continue

    lista_de_resenhas_json.append(resenha_dict)

def contador_e_juntador(lista_de_dicionarios):
    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0
    lista_de_dicionarios_string = []

    for dicionario in lista_de_dicionarios:
        if dicionario["avaliacao"] == "positiva":
            contador_positivas += 1
        elif dicionario["avaliacao"] == "negativa":
            contador_negativas += 1
        else:
            contador_neutras += 1

        lista_de_dicionarios_string.append(str(dicionario))

    resenhas_unidas = "##########\n".join(lista_de_dicionarios_string)
    return contador_positivas, contador_negativas, contador_neutras, resenhas_unidas

positivas, negativas, neutras, resenhas_unidas = contador_e_juntador(lista_de_resenhas_json)
print(f"Resenhas positivas: {positivas}")
print(f"Resenhas negativas: {negativas}")
print(f"Resenhas neutras: {neutras}")

with open("resenhas_unidas.txt", "w", encoding="utf-8") as file:
    file.write(resenhas_unidas)