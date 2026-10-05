import pandas as pd
import os
import glob
import csv
import sys

# 📁 Caminho raiz onde estão os subdiretórios com os arquivos
caminho_base = './../../data/raw'

# 🔍 Buscar todos os arquivos .csv nos subdiretórios
arquivos_csv = glob.glob(os.path.join(caminho_base, '**', '*.csv'), recursive=True)

# 📊 Ler e exibir os 5 primeiros registros de cada arquivo
for caminho_arquivo in arquivos_csv:
    print(f"\n📄 Arquivo: {caminho_arquivo}")
    try:
        df = pd.read_csv(caminho_arquivo)
        print(df.head(10))  # Exibir as 5 primeiras linhas
    except Exception as e:
        csv.field_size_limit(sys.maxsize)
        df = pd.read_csv(caminho_arquivo, sep='\t', engine='python')
        print(df.head(10))
        print(f"❌ Erro ao ler {caminho_arquivo}: {e}")