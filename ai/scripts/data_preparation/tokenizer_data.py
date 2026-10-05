import json
from transformers import AutoTokenizer
from datasets import Dataset

# ✅ Carregar dataset diretamente do arquivo
# Nome do modelo Hugging Face (pode ser trocado pelo que você for usar)
model_checkpoint = "./../../models/pretrained/models--meta-llama--Llama-3.2-1B-Instruct/snapshots/9213176726f574b556790deb65791e0c5aa438b6"

# Carrega o tokenizer do modelo (ex: LLaMA)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, use_fast=False)

# Define pad_token se necessário
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# 🔁 Edite este caminho com o local real do seu arquivo JSONL/JSON
json_path = "./../../data/processed/filtrado.json"  # ou .json

# Carregar os dados JSON
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Verifica se é uma lista
if not isinstance(data, list):
    raise ValueError("O JSON deve conter uma lista de exemplos.")

# Função para preparar a entrada no estilo "instrução + entrada = saída"
def tokenize(example):
    prompt = f"{example['instruction']}\n\n{example['input']}"
    completion = example['output']

    # Concatenar e tokenizar entrada e saída
    model_input = tokenizer(prompt, truncation=True, padding="max_length", max_length=512)
    model_output = tokenizer(completion, truncation=True, padding="max_length", max_length=128)

    model_input["labels"] = model_output["input_ids"]
    return model_input

# Transforma em dataset Hugging Face para facilitar o processamento
hf_dataset = Dataset.from_list(data)
tokenized_dataset = hf_dataset.map(tokenize, remove_columns=hf_dataset.column_names)

# Visualizar alguns exemplos
print(tokenized_dataset[0])
