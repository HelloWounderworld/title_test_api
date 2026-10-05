import pandas as pd
import os
import json
import csv
import sys

lista_paths = [
    'bbc-news-articles/bbc_news_20220307_20240703.csv',
    'bbc-news/bbc_news.csv',
]

dados_convertidos = []

for path in lista_paths:
    # 📝 Caminho do arquivo .xlsx
    arquivo_excel = './../../data/raw/' + path  # Ex: 'dados/noticias.xlsx'

    # 📖 Ler o arquivo Excel (primeira planilha por padrão)
    df = pd.read_csv(arquivo_excel)

    for _, linha in df.iterrows():
        item = {
            "instruction": "Crie um título jornalístico para o seguinte texto:",
            "input": linha['description'],   # coluna com o corpo/texto da matéria
            "output": linha['title']         # coluna com o título da matéria
        }
        dados_convertidos.append(item)

    # 📝 Caminho do arquivo .xlsx
    arquivo_excel = './../../data/raw/news-of-the-site-folhauol/articles.csv'  # Ex: 'dados/noticias.xlsx'

    # 📖 Ler o arquivo Excel (primeira planilha por padrão)
    df = pd.read_csv(arquivo_excel)

    for _, linha in df.iterrows():
        item = {
            "instruction": "Crie um título jornalístico para o seguinte texto:",
            "input": linha['text'],   # coluna com o corpo/texto da matéria
            "output": linha['title']         # coluna com o título da matéria
        }
        dados_convertidos.append(item)

    # 📝 Caminho do arquivo .xlsx
    arquivo_excel = './../../data/raw/new-york-times-tech-news-oct-25-nov-27/new_york_times_tech.csv'  # Ex: 'dados/noticias.xlsx'

    # 📖 Ler o arquivo Excel (primeira planilha por padrão)
    df = pd.read_csv(arquivo_excel)

    for _, linha in df.iterrows():
        item = {
            "instruction": "Crie um título jornalístico para o seguinte texto:",
            "input": linha['Description'],   # coluna com o corpo/texto da matéria
            "output": linha['Headline']         # coluna com o título da matéria
        }
        dados_convertidos.append(item)

    # 📝 Caminho do arquivo .xlsx
    arquivo_excel = './../../data/raw/newspaper-text-summarization-cnn-dailymail/cnn_dailymail/train.csv'  # Ex: 'dados/noticias.xlsx'

    # 📖 Ler o arquivo Excel (primeira planilha por padrão)
    df = pd.read_csv(arquivo_excel)

    for _, linha in df.iterrows():
        item = {
            "instruction": "Crie um título jornalístico para o seguinte texto:",
            "input": linha['article'],   # coluna com o corpo/texto da matéria
            "output": linha['highlights']         # coluna com o título da matéria
        }
        dados_convertidos.append(item)

     # 📝 Caminho do arquivo .xlsx
    arquivo_excel = './../../data/raw/folha-news-of-the-brazilian-newspaper-2024/FolhaArticles.csv'  # Ex: 'dados/noticias.xlsx'

    # 📖 Ler o arquivo Excel (primeira planilha por padrão)
    csv.field_size_limit(sys.maxsize)
    df = pd.read_csv(arquivo_excel, sep='\t', engine='python')

    for _, linha in df.iterrows():
        item = {
            "instruction": "Crie um título jornalístico para o seguinte texto:",
            "input": linha['Content'],   # coluna com o corpo/texto da matéria
            "output": linha['Title']         # coluna com o título da matéria
        }
        dados_convertidos.append(item)

# Salvar em um novo arquivo JSON
with open("./../../data/processed/filtrado.json", "w", encoding="utf-8") as f:
    json.dump(dados_convertidos, f, ensure_ascii=False, indent=2)

print("✅ Arquivo 'filtrado.json' criado com sucesso!")
