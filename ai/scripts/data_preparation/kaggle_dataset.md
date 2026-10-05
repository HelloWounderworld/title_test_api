# Kaggle DataSet
Boa pergunta! 👇 Vamos esclarecer passo a passo como funciona o uso do `kagglehub` ou do pacote `kaggle` para baixar datasets diretamente do Kaggle via **código Python**.

---

### ✅ **1. `kagglehub` é uma alternativa, mas não é o método oficial do Kaggle**

O método **oficial e mais estável** para baixar datasets do Kaggle via terminal ou Python é com o pacote `kaggle`, **não `kagglehub`**.

---

### ⚠️ **Se quiser usar `kagglehub`, sim, você precisa autenticar antes**

Por padrão, o `kagglehub` (assim como o `kaggle`) precisa que você tenha um **token de autenticação** da sua conta Kaggle, que fica em um arquivo chamado `kaggle.json`. Ele é necessário para autorizar os downloads.

---

## ✅ **Método Oficial (Recomendado): Usando o pacote `kaggle`**

### 1. Instale o pacote:

```bash
pip install kaggle
```

### 2. Gere o token da sua conta:

* Vá até [https://www.kaggle.com/settings](https://www.kaggle.com/settings)
* Clique em **"Create New API Token"**
* Um arquivo chamado `kaggle.json` será baixado

### 3. Mova esse token para o local correto:

```bash
mkdir -p ~/.kaggle
mv /caminho/do/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

### 4. Baixe o dataset via terminal:

```bash
kaggle datasets download -d bhavikjikadara/bbc-news-articles
unzip bbc-news-articles.zip -d bbc_news_data/
```

---

## ✅ **Usando o pacote `kaggle` via Python**

```python
import kaggle
import zipfile
import os

# Baixar o dataset
!kaggle datasets download -d bhavikjikadara/bbc-news-articles -p ./data

# Descompactar
with zipfile.ZipFile("./data/bbc-news-articles.zip", "r") as zip_ref:
    zip_ref.extractall("./data/bbc_news")
```

---

## ❌ Sobre `kagglehub.dataset_download(...)`

Esse método pode funcionar, mas depende de bibliotecas menos suportadas e não é a via oficial do Kaggle. Se você já configurou o `kaggle.json`, talvez funcione, mas **não há garantia de estabilidade ou suporte futuro** como há com o pacote oficial `kaggle`.

---

## 📌 Resumo

| Método                               | Autenticação Necessária? | Estável e Suportado? | Recomendado? |
| ------------------------------------ | ------------------------ | -------------------- | ------------ |
| `kagglehub.dataset_download`         | ✅ Sim (kaggle.json)      | ⚠️ Parcialmente      | ❌ Não        |
| `kaggle` (oficial) via CLI ou Python | ✅ Sim (kaggle.json)      | ✅ Sim                | ✅ Sim        |

---

Claro! Aqui está um **script Python completo** que:

1. **Verifica se o pacote `kaggle` está instalado**
2. **Baixa o dataset BBC News Articles do Kaggle**
3. **Descompacta os arquivos**
4. **Lê os dados usando `pandas`** (caso estejam em CSV)

---

### ✅ Pré-requisitos:

* Você **já deve ter feito o download do `kaggle.json`** (token de API) no [Kaggle > Settings](https://www.kaggle.com/settings)
* Esse arquivo deve estar salvo em `~/.kaggle/kaggle.json` (o script abaixo verifica isso)

---

### 📜 **Script Completo: `download_and_load_bbc_news.py`**

```python
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
download_dir = "./data"
extract_dir = os.path.join(download_dir, "bbc_news")
os.makedirs(download_dir, exist_ok=True)

# 3. Baixa o dataset usando a CLI do kaggle
print("📦 Baixando dataset do Kaggle...")
subprocess.run(
    ["kaggle", "datasets", "download", "-d", "bhavikjikadara/bbc-news-articles", "-p", download_dir],
    check=True
)

# 4. Descompacta
zip_path = os.path.join(download_dir, "bbc-news-articles.zip")
print("📂 Extraindo arquivos...")
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_dir)

# 5. Procura e carrega os arquivos CSV
print("🧠 Carregando arquivos CSV...")
csv_files = [f for f in os.listdir(extract_dir) if f.endswith(".csv")]
if not csv_files:
    raise FileNotFoundError("Nenhum arquivo CSV encontrado no dataset.")

# Lê o primeiro CSV encontrado
csv_path = os.path.join(extract_dir, csv_files[0])
df = pd.read_csv(csv_path)

# 6. Exibe amostra
print("\n✅ Dataset carregado com sucesso! Primeiras linhas:")
print(df.head())

# Exibe informações básicas
print("\n📊 Informações do Dataset:")
print(df.info())
```

---

### ✅ Saída esperada:

```bash
📦 Baixando dataset do Kaggle...
📂 Extraindo arquivos...
🧠 Carregando arquivos CSV...

✅ Dataset carregado com sucesso! Primeiras linhas:
       category                                             text
0        sport  a last-gasp goal by nigeria captain austin ...
1     business  worldcom inc. filed for bankruptcy protectio...
...

📊 Informações do Dataset:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2225 entries, 0 to 2224
Columns: 2
```

