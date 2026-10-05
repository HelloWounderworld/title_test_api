# import kaggle
# import zipfile
# import os

# # Baixar o dataset
# !kaggle datasets download -d bhavikjikadara/bbc-news-articles -p ./data

# # Descompactar
# with zipfile.ZipFile("./data/bbc-news-articles.zip", "r") as zip_ref:
#     zip_ref.extractall("./data/bbc_news")

# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("bhavikjikadara/bbc-news-articles")

# print("Path to dataset files:", path)

# # Download latest version
# path = kagglehub.dataset_download("gpreda/bbc-news")

# print("Path to dataset files:", path)

# # Download latest version
# path = kagglehub.dataset_download("rmisra/news-category-dataset")

# print("Path to dataset files:", path)

# # Download latest version
# path = kagglehub.dataset_download("mauryansshivam/new-york-times-tech-news-oct-25-nov-27")

# print("Path to dataset files:", path)

# # Download latest version
# path = kagglehub.dataset_download("aryansingh0909/nyt-articles-21m-2000-present")

# print("Path to dataset files:", path)

# # Download latest version
# path = kagglehub.dataset_download("tumanovalexander/nyt-articles-data")

# print("Path to dataset files:", path)

# # Download latest version
# path = kagglehub.dataset_download("devorvant/economic-calendar")

# print("Path to dataset files:", path)

# # Download latest version
# path = kagglehub.dataset_download("marlesson/news-of-the-site-folhauol")

# print("Path to dataset files:", path)

# # Download latest version
# path = kagglehub.dataset_download("everydaycodings/global-news-dataset")

# print("Path to dataset files:", path)

# # Download latest version
# path = kagglehub.dataset_download("hacker-news/hacker-news-corpus")

# print("Path to dataset files:", path)

import os
import zipfile
import pandas as pd
import subprocess

# 1. Verifica se o token do Kaggle está configurado
kaggle_token_path = os.path.expanduser("~/.kaggle/kaggle.json")

if not os.path.exists(kaggle_token_path):
    raise FileNotFoundError(
        "Arquivo kaggle.json não encontrado em ~/.kaggle/. "
        "Vá em https://www.kaggle.com/settings, gere um token de API e salve-o nesse caminho."
    )

# 2. Cria pastas para download e extração
download_dir = "./../../data/raw"
os.makedirs(download_dir, exist_ok=True)

datasets_to_download = [
    "bhavikjikadara/bbc-news-articles",
    "gpreda/bbc-news",
    "mauryansshivam/new-york-times-tech-news-oct-25-nov-27",
    "marlesson/news-of-the-site-folhauol",
    "gowrishankarp/newspaper-text-summarization-cnn-dailymail",
    "luisfcaldeira/folha-news-of-the-brazilian-newspaper-2024"
]

# 3. Baixa o dataset usando a CLI do kaggle
print("📦 Baixando dataset do Kaggle...")
for dataset_slug in datasets_to_download:
    print(f"🔽 Baixando: {dataset_slug}")
    subprocess.run(
        ["kaggle", "datasets", "download", "-d", dataset_slug, "-p", download_dir],
        check=True
    )

# 4. Descompacta
zip_files = [f for f in os.listdir(download_dir) if f.endswith(".zip")]

for zip_filename in zip_files:
    zip_path = os.path.join(download_dir, zip_filename)
    extract_subdir = os.path.join(download_dir, zip_filename.replace(".zip", ""))
    
    print(f"📂 Extraindo {zip_filename}...")
    os.makedirs(extract_subdir, exist_ok=True)
    
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_subdir)
