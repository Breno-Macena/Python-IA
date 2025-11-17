from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
)

def get_llm_response(prompt):
    response = client.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[
            {
                "role": "system", 
                "content": """Você é um especialista em análise de dados e conversão de dados para o formato JSON.
                Você receberá uma linha de texto de um aplicativo em um marketplace online.
                Eu quero que você analise a linha de texto e retorne um JSON com os seguintes campos:
                - usuario: o nome do usuário que fez a resenha
                - resenha_original: a resenha no idioma original que foi escrita pelo usuário
                - resenha_pt: a resenha traduzida para o português
                - avaliacao: uma avaliação se essa resenha é positiva, negativa ou neutra

                Exemplo de entrada:
                53409593$Safoan Riyad$J'aimais bien ChatGPT. Mais la derniÃ¨re mise Ã  jour a tout gÃ¢chÃ©. Elle a tout oubliÃ©.
                Exemplo de saída:
                {
                    "usuario": "Safoan Riyad",
                    "resenha_original": "J'aimais bien ChatGPT. Mais la derniÃ¨re mise Ã  jour a tout gÃ¢chÃ©. Elle a tout oubliÃ©.",
                    "resenha_pt": "Eu gosto muito do ChatGPT. Mas a última atualização quebrou tudo. Ela esqueceu de tudo.",
                    "avaliacao": "negativa"
                }

                Regra importante: você deve retornar apenas o JSON, sem nenhum outro texto adicional.
                """
            },
            {
                "role": "user",
                "content": f"Analise a seguinte resenha: {prompt}"
            }
        ],
        temperature=0
    )

    print(response.choices[0].message.content)
    return response.choices[0].message.content
