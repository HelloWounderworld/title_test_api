# **Fine-Tuning QLoRa**
Ótimo! O **QLoRA (Quantized LoRA)** é uma extensão do LoRA tradicional que permite realizar fine-tuning de LLMs com muito menos memória — ideal para quem tem uma GPU de 8GB a 24GB. A seguir, trago **um guia completo e estruturado no formato README.md** com as **principais fontes para estudar, aplicar e dominar QLoRA**, incluindo tutoriais, repositórios e papers.

---

# 🧠 Fine-Tuning com QLoRA – Guia Completo

> **QLoRA** é uma técnica de ajuste fino eficiente para LLMs que combina:
>
> * **Quantização 4-bit (NF4)** para reduzir o uso de memória.
> * **LoRA (Low-Rank Adaptation)** para ajustar apenas partes específicas do modelo.
> * Permite **treinar modelos de bilhões de parâmetros em GPUs de baixo custo**.

---

## 📚 Recursos Essenciais

### 🔹 1. **Repositório oficial do QLoRA**

* **Artidoro Pagnoni – GitHub:**
  📎 [https://github.com/artidoro/qlora](https://github.com/artidoro/qlora)

* **Paper (ArXiv):**
  📄 [https://arxiv.org/abs/2305.14314](https://arxiv.org/abs/2305.14314)
  *QLoRA: Efficient Finetuning of Quantized LLMs*

---

### 🔹 2. **Tutoriais e Aplicações Práticas**

| Título                                         | Link                                                                                                                                 | Conteúdo            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| **Fine-tune Falcon 7B com QLoRA (Colab)**      | [https://github.com/huggingface/blog/blob/main/fine-tune-qlora.md](https://github.com/huggingface/blog/blob/main/fine-tune-qlora.md) | Passo a passo       |
| **Phil Schmid: Fine-tuning LLaMA-2 com QLoRA** | [https://www.philschmid.de/fine-tune-llama-2](https://www.philschmid.de/fine-tune-llama-2)                                           | Tutorial atualizado |
| **How to Fine-tune LLaMA2 with QLoRA**         | [https://www.datacamp.com/tutorial/fine-tune-llama-2-qlora](https://www.datacamp.com/tutorial/fine-tune-llama-2-qlora)               | Fácil de seguir     |
| **Sebastian Raschka: HuggingFace QLoRA**       | [https://sebastianraschka.com/blog/2023/qlora.html](https://sebastianraschka.com/blog/2023/qlora.html)                               | Detalhado e técnico |

---

### 🔹 3. **Repositórios com Código Pronto (para copiar/adaptar)**

* **QLoRA com Hugging Face (PEFT + bitsandbytes):**
  📎 [https://github.com/huggingface/peft/tree/main/examples/peft\_qlora](https://github.com/huggingface/peft/tree/main/examples/peft_qlora)
  Inclui: `LlamaForCausalLM`, `Trainer`, `DataCollatorForLanguageModeling`, etc.

* **QLoRA + DPO (Preference Tuning)**
  📎 [https://github.com/huggingface/trl/tree/main/examples/scripts/sft](https://github.com/huggingface/trl/tree/main/examples/scripts/sft)
  Usa `transformers` + `trl` + `datasets`

* **QLoRA com datasets personalizados**
  📎 [https://github.com/hiyouga/LLaMA-Efficient-Tuning](https://github.com/hiyouga/LLaMA-Efficient-Tuning)

---

### 🔹 4. **Ambiente e Instalação**

#### Bibliotecas principais:

```bash
pip install -q \
  bitsandbytes \
  transformers \
  datasets \
  peft \
  accelerate \
  trl
```

#### Requisitos de GPU:

* QLoRA permite fine-tuning de modelos de 7B–13B com **apenas 24GB de VRAM** (ou menos, com ajustes).

---

## ⚙️ Fluxo de Fine-Tuning com QLoRA

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import prepare_model_for_kbit_training, LoraConfig, get_peft_model
import torch

# 1. Carregar modelo com quantização 4-bit
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf",
    load_in_4bit=True,
    device_map="auto",
    quantization_config={
        "bnb_4bit_compute_dtype": torch.float16,
        "bnb_4bit_use_double_quant": True,
        "bnb_4bit_quant_type": "nf4"
    }
)

# 2. Preparar modelo para LoRA
model = prepare_model_for_kbit_training(model)

# 3. Configurar LoRA
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

# 4. Aplicar LoRA
model = get_peft_model(model, lora_config)
```

---

## 📌 Dicas importantes

| Item | Dica                                                                   |
| ---- | ---------------------------------------------------------------------- |
| 🧠   | Use modelos já quantizados (ou quantize você mesmo com `bitsandbytes`) |
| 📝   | Use datasets pequenos para testes e escale progressivamente            |
| 🧪   | Combine com técnicas como SFT (Supervised Fine-Tuning) e DPO           |
| 💾   | Salve apenas os adapters (LoRA weights), e não o modelo completo       |
| 🐳   | Pode ser usado com Docker e Colab Pro para treinos mais rápidos        |

---

## 🔗 Links Complementares

* Hugging Face PEFT + QLoRA notebook
  📎 [https://colab.research.google.com/github/huggingface/peft/blob/main/examples/peft\_qlora.ipynb](https://colab.research.google.com/github/huggingface/peft/blob/main/examples/peft_qlora.ipynb)

* Bitsandbytes (quantization engine)
  📎 [https://github.com/TimDettmers/bitsandbytes](https://github.com/TimDettmers/bitsandbytes)

* PEFT Documentation
  📎 [https://huggingface.co/docs/peft/index](https://huggingface.co/docs/peft/index)

---

Se quiser, posso te gerar um **repositório base com estrutura para rodar QLoRA no seu ambiente local (ou em Colab)**. Deseja isso?

# **Passos para Realizar o Ajuste Fino**

## Rodando o script

  python train_qlora.py \
    --model_name ./../../models/pretrained/models--meta-llama--Llama-3.2-1B-Instruct/snapshots/9213176726f574b556790deb65791e0c5aa438b6 \
    --output_dir ./../../models/trained/title-ai-trained-llama32-1B \
    --dataset_name ./../../data/processed/filtrado.json\
    --max_steps 1000 \
    --use_auth \
    --logging_steps 10 \
    --save_strategy steps \
    --data_seed 42 \
    --save_steps 50 \
    --save_total_limit 40 \
    --max_new_tokens 32 \
    --dataloader_num_workers 1 \
    --group_by_length \
    --logging_strategy steps \
    --remove_unused_columns False \
    --do_train \
    --lora_r 64 \
    --lora_alpha 16 \
    --lora_modules all \
    --double_quant \
    --quant_type nf4 \
    --bf16 False \
    --bits 4 \
    --warmup_ratio 0.03 \
    --lr_scheduler_type constant \
    --gradient_checkpointing \
    --dataset hh-rlhf \
    --source_max_len 16 \
    --target_max_len 512 \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --eval_steps 187 \
    --learning_rate 0.0002 \
    --adam_beta2 0.999 \
    --max_grad_norm 0.3 \
    --lora_dropout 0.1 \
    --weight_decay 0.0 \
    --seed 0 \
    --use_peft \
    --batch_size 4 \
    --gradient_accumulation_steps 2
