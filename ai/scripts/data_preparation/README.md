# Fontes onde estou buscando os dados brutos

Você pode encontrar **conjuntos de dados públicos de notícias e matérias jornalísticas** em várias plataformas e repositórios de dados abertos. Aqui estão algumas das melhores opções:

---

## 🗂️ **1. Kaggle Datasets**

[Kaggle](https://www.kaggle.com/datasets) é um excelente ponto de partida:

* 🔹 [News Category Dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset) — artigos da HuffPost categorizados (política, tecnologia, esportes etc.).
* 🔹 [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) — matérias verdadeiras e falsas.
* 🔹 [BBC News Dataset](https://www.kaggle.com/datasets/cpitel/bbc-news) — notícias da BBC divididas por tópicos.

Voce tera que criar um token por aqui

    https://www.kaggle.com/settings

## 📰 **2. The Guardian Open Platform**

* 🌐 [https://open-platform.theguardian.com/](https://open-platform.theguardian.com/)
* API para acessar notícias da *The Guardian* com filtros por data, seção, conteúdo etc.
* Requer **chave de API gratuita** (uso razoável).

---

## 🧾 **3. GDELT Project**

* 🌍 [https://www.gdeltproject.org/](https://www.gdeltproject.org/)
* Banco gigantesco com **notícias globais em tempo real**, metadados, sentimentos, localização geográfica, etc.
* Disponível como CSVs públicos ou via API.

---

## 📚 **4. Common Crawl (via NewsCrawl)**

* 🔗 [https://commoncrawl.org/](https://commoncrawl.org/)
* Oferece grandes dumps da web, incluindo sites de notícias.
* Mais técnico: precisa processar arquivos WARC.

---

## 📰 **5. Reuters News Dataset (Reuters-21578, RCV1)**

* 🔹 [Reuters-21578](https://www.kaggle.com/datasets/nltkdata/reuters) — antigo, mas ainda usado para classificação de texto.
* 🔹 [RCV1](https://trec.nist.gov/data/reuters/reuters.html) — disponível mediante aceite de termos.

---

## 🔎 **6. Hugging Face Datasets**

* [Datasets Library](https://huggingface.co/datasets)
* Use diretamente em código com:

```python
from datasets import load_dataset
dataset = load_dataset("ag_news")  # Exemplo de dataset de notícias
```

Outros datasets interessantes no Hugging Face:

* `"ag_news"` — 4 categorias: World, Sports, Business, Sci/Tech.
* `"cnn_dailymail"` — resumos de notícias.
* `"multi_news"` — resumos de múltiplas fontes.

---

## ✅ Qual escolher?

| Caso de uso                            | Dataset recomendado                            |
| -------------------------------------- | ---------------------------------------------- |
| Classificação de notícias              | `ag_news`, `BBC`, `HuffPost`                   |
| Detecção de fake news                  | `Fake and Real News Dataset`                   |
| Resumo automático (text summarization) | `CNN/DailyMail`, `Multi-News`                  |
| Treinamento LLM / RAG                  | `Common Crawl`, `GDELT`, `HuggingFace` corpora |
| Noticiário internacional               | `GDELT`, `The Guardian API`                    |

## ✅ **Instale as dependências primeiro**

Se ainda não tiver:

```bash
pip install datasets
```

---

## 📄 **Código: carregando diferentes datasets de notícias**

```python
from datasets import load_dataset

# 1. AG News (classificação em 4 categorias)
ag_news = load_dataset("ag_news")
print("\nAG News exemplo:")
print(ag_news["train"][0])

# 2. CNN/DailyMail (sumarização de notícias)
cnn_dailymail = load_dataset("cnn_dailymail", "3.0.0")
print("\nCNN/DailyMail exemplo:")
print(cnn_dailymail["train"][0]["article"][:300])  # Imprime os primeiros 300 caracteres

# 3. Multi-News (sumarização a partir de múltiplas fontes)
multi_news = load_dataset("multi_news")
print("\nMulti-News exemplo:")
print(multi_news["train"][0]["document"][:300])  # Primeiro documento concatenado

# 4. Fake and Real News (de Kaggle via Hugging Face)
fake_news = load_dataset("liar")  # Alternativa textual com etiquetas de veracidade
print("\nFake News LIAR exemplo:")
print(fake_news["train"][0])
```

---

### 🧠 Explicação rápida:

| Dataset         | Tarefa                        | Colunas principais          |
| --------------- | ----------------------------- | --------------------------- |
| `ag_news`       | Classificação de tópicos      | `"text"`, `"label"`         |
| `cnn_dailymail` | Sumarização                   | `"article"`, `"highlights"` |
| `multi_news`    | Sumarização (multi-documento) | `"document"`, `"summary"`   |
| `liar`          | Verificação de fato           | `"statement"`, `"label"`    |

---

### 💡 Extras:

* Você pode salvar os dados em `.csv` com `pandas`:

```python
import pandas as pd
df = pd.DataFrame(ag_news['train'])
df.to_csv("ag_news.csv", index=False)
```

## ✅ **1. Instale dependências (se necessário)**

```bash
pip install pandas
```

---

## 📦 **2. Baixe os datasets no Kaggle**

Você precisa de uma conta no [Kaggle](https://www.kaggle.com) e aceitar os termos de uso dos datasets. Alguns exemplos famosos:

| Dataset                        | Link                                                                                                                                                     |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **BBC News Classification**    | [https://www.kaggle.com/datasets/crowdflower/bbc-news-classification](https://www.kaggle.com/datasets/crowdflower/bbc-news-classification)               |
| **HuffPost News**              | [https://www.kaggle.com/datasets/rmisra/news-category-dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset)                             |
| **Fake and Real News Dataset** | [https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset) |
| **Reuters News**               | [https://www.kaggle.com/datasets/nltkdata/reuters](https://www.kaggle.com/datasets/nltkdata/reuters)                                                     |

---

## 🧑‍💻 **3. Código para carregar os CSVs com `pandas`**

### 🔹 Exemplo: **BBC News Classification**

```python
import pandas as pd

# Substitua o caminho abaixo pelo local onde você salvou o arquivo CSV
df_bbc = pd.read_csv("bbc-text.csv")

print("Colunas:", df_bbc.columns)
print(df_bbc.head())
```

### 🔹 Exemplo: **HuffPost News Dataset**

```python
df_huffpost = pd.read_json("News_Category_Dataset_v3.json", lines=True)

print("Categorias únicas:", df_huffpost['category'].unique())
print(df_huffpost[['headline', 'short_description']].head())
```

### 🔹 Exemplo: **Fake and Real News Dataset**

```python
df_fake = pd.read_csv("Fake.csv")
df_real = pd.read_csv("True.csv")

print("Fake News exemplo:")
print(df_fake[['title', 'text']].head())

print("Real News exemplo:")
print(df_real[['title', 'text']].head())
```

---

## 📁 **Dica de Organização**

Você pode armazenar os datasets assim:

```
news_datasets/
├── bbc-text.csv
├── News_Category_Dataset_v3.json
├── Fake.csv
├── True.csv
```

---

Se quiser, posso te ajudar com:

* Scripts para pré-processamento de texto (remoção de HTML, normalização, etc)
* Balanceamento dos dados
* Preparar para tokenização em Transformers (Hugging Face)

Deseja seguir para alguma dessas etapas?


