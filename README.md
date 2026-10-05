# 📰 TituladorGPT — A IA Mancheteira Oficial do Século XXI

*“Se a notícia é boa, ela faz render. Se é ruim, ela inventa um título melhor!”*

---

## 🤖 Introdução

**TituladorGPT** é uma inteligência artificial especializada na **geração criativa de títulos jornalísticos**. Seja para matérias sérias, sensacionalistas ou satíricas, ela cria manchetes que chamam atenção — como um verdadeiro editor de redação em estado de café puro.

O objetivo do projeto é automatizar e acelerar o processo de criação de títulos jornalísticos com qualidade editorial, fluidez linguística e impacto comunicativo, usando modelos de linguagem de última geração.

---

## 🧠 Modelo Utilizado

- 🔷 **Modelo atual:** [LLaMA 3](https://huggingface.co/meta-llama)
- 🔮 **Próxima etapa:** Integração com o [**LLaMA 4**]((https://ai.meta.com/llama/)) (em desenvolvimento ou aguardando liberação)

O LLaMA (Large Language Model Meta AI) é um dos modelos mais avançados em compreensão e geração de linguagem natural, tornando-o ideal para tarefas criativas como criação de títulos.

---

## 🛠️ Ambiente de Desenvolvimento

O ambiente do projeto foi totalmente containerizado para garantir **reprodutibilidade, portabilidade e escalabilidade**.

### 🐳 Tecnologias utilizadas:

- **Docker**: infraestrutura portátil e isolada
- **Docker Compose**: orquestração de serviços (modelo, API, etc.)
- **Python 3.13.4** com as principais bibliotecas:

```txt
transformers
peft
bitsandbytes
datasets
scikit-learn
accelerate
trl
pandas
```

> O ambiente também suporta uso de GPU com CUDA/cuBLAS/cuDNN para treinamento acelerado.

---

## 🧪 Método de Ajuste Fino

Para adaptar o LLaMA-3 à tarefa específica de criação de títulos, utilizei o método:

### 🔧 `qLoRA` (Quantized Low-Rank Adaptation)

- Permite ajuste fino de grandes modelos com **baixo custo de memória**
- Usa quantização 4-bit para reduzir footprint computacional
- Ideal para treinar em GPUs com VRAM limitada

### 📌 Futuras explorações:

Pretendo experimentar outras estratégias de ajuste fino, como:

- 🔹 `LoRA` (Low-Rank Adaptation)
- 🔹 `Transformer Acceleration` (Fine-tuning Using Transformer Acceleration)
- 🔹 `Full Fine-Tuning` (ajuste completo dos pesos do modelo)
- 🔹 `Adapter Tuning`
- 🔹 `Prompt Tuning` ou `Prefix Tuning`

Esses métodos serão avaliados com base em custo computacional, desempenho e flexibilidade de aplicação.

---

## 🚧 Progresso Atual

- ✅ Dataset com títulos reais e criativos coletados de fontes jornalísticas
- ✅ Fine-tuning inicial com qLoRA no LLaMA-3
- 🛠️ Em desenvolvimento: avaliação automática de qualidade dos títulos gerados (BLEU, ROUGE, métricas humanas)
- 💡 Em planejamento: interface web (Streamlit ou FastAPI) para gerar títulos via textarea

---

## 📦 Como rodar o projeto (preview)

```bash
# Build da imagem
docker build -t tituladorgpt .

# Subir container
docker run --gpus all -p 7860:7860 tituladorgpt
```

---

## 📑 Exemplos de Entrada e Saída

**🔍 Entrada:**
> Texto: "O governo anunciou hoje um novo pacote de estímulos à economia..."

**🧠 IA responde:**
> "Governo Tira Coelho da Cartola e Injeta Bilhões na Economia"

---

## 👨‍🔬 Autor e Contato

Desenvolvido por **[Seu Nome]**, pesquisador entusiasta da interseção entre **jornalismo, linguagem natural e IA**.

📫 Contato: [seu-email@exemplo.com]

---

## ⚖️ Licença

MIT — sinta-se livre para usar, remixar e criar suas próprias manchetes absurdas com IA.

---

> “Se a IA vai dominar o mundo, que pelo menos ela escreva as manchetes com estilo.” ✍️
```
