import requests  
import os        
import sqlite3

def salvar_em_sqlite(dados, nome_arquivo="sentimentos.db"):
    try:
        conn = sqlite3.connect(nome_arquivo)
        cursor = conn.cursor()

        # Cria tabela se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analise_sentimentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comentario TEXT,
                sentimento TEXT
            )
        """)

        # Insere dados
        for comentario, sentimento in dados:
            cursor.execute(
                "INSERT INTO analise_sentimentos (comentario, sentimento) VALUES (?, ?)",
                (comentario, sentimento)
            )

        conn.commit()
        conn.close()
        print(f"Dados salvos com sucesso no banco SQLite ({nome_arquivo}).")

    except Exception as e:
        print("Erro ao salvar no SQLite:", e)


# Função para buscar comentários/reviews da Steam
def buscar_reviews_steam(app_id, quantidade=10, idioma="portuguese"):
    # Monta a URL da API da Steam com o app_id (ID do jogo), quantidade de reviews e idioma
    url = f"https://store.steampowered.com/appreviews/{app_id}?json=1&num_per_page={quantidade}&language={idioma}&filter=recent"
    
    # Faz a requisição GET à API da Steam
    response = requests.get(url)

    # Converte a resposta para JSON
    data = response.json()
    
    comentarios = []  # Lista para armazenar os comentários extraídos

    # Verifica se há reviews na resposta
    if "reviews" in data:
        for review in data["reviews"]:
            # Extrai apenas o texto do comentário
            comentarios.append(review["review"])
    
    # Retorna a lista de comentários
    return comentarios

# Função para classificar os sentimentos dos comentários usando a API da Groq
def classificar_emocao_groq(comentarios):
    # Lê a chave da API da variável de ambiente
    groq_api_key = os.getenv("GROQ_API_KEY")

    # URL da API da Groq para chamadas no estilo ChatCompletion
    url = "https://api.groq.com/openai/v1/chat/completions"

    # Cabeçalhos da requisição HTTP com autenticação e tipo de conteúdo
    headers = {
        "Authorization": f"Bearer {groq_api_key}",  # Insere a chave da API
        "Content-Type": "application/json"          # Define o tipo de conteúdo como JSON
    }

    # Modelo atual da Groq (o anterior foi descontinuado)
    modelo = "llama3-70b-8192"

    # Lista para guardar os resultados (comentário, sentimento)
    resultados = []

    # Itera sobre cada comentário recebido
    for comentario in comentarios:
        # Prompt enviado para o modelo: pede apenas o sentimento detectado
        prompt = (
            "Classifique a emoção do comentário a seguir. "
            "Responda apenas com o sentimento detectado (exemplo: 'positivo', 'negativo', 'neutro'):\n\n"
            f"{comentario}"
        )

        # Corpo da requisição enviado para a API
        payload = {
            "model": modelo,
            "messages": [
                {"role": "user", "content": prompt}  # Mensagem enviada pelo "usuário" (nós)
            ],
            "temperature": 0.2  # Temperatura baixa para evitar variação nas respostas
        }

        # Envia a requisição POST para a API da Groq
        response = requests.post(url, headers=headers, json=payload)

        try:
            # Converte a resposta da API para JSON
            resposta = response.json()
            print("Resposta crua da API:", resposta)  # Linha de debug (pode remover depois)

            # Se a resposta não contiver a chave "choices", houve erro na requisição
            if "choices" not in resposta:
                raise ValueError("Resposta inválida ou modelo com erro")

            # Extrai o conteúdo da resposta (texto com o sentimento)
            sentimento = resposta["choices"][0]["message"]["content"].strip()

        except Exception as e:
            # Se der erro, imprime e define o sentimento como erro
            print(f"Erro ao processar comentário: {comentario}")
            print(f"Erro: {e}")
            sentimento = "erro_na_resposta"

        # Adiciona o resultado (comentário, sentimento) à lista
        resultados.append((comentario, sentimento))

    # Retorna todos os comentários com seus respectivos sentimentos
    return resultados


def main(app_id, quantidade=10, idioma="portuguese"):
    comentarios = buscar_reviews_steam(app_id, quantidade, idioma)
    resultados = classificar_emocao_groq(comentarios)  # ou classificar_emocao_langchain
    
    for comentario, sentimento in resultados:
        print(f"Comentário: {comentario}\nSentimento: {sentimento}\n")
        
    salvar_em_sqlite(resultados)


# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main(app_id=730)  # 730 é o app_id do CS:GO na Steam
