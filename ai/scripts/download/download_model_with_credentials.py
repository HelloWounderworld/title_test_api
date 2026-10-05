import os
from huggingface_hub import login, snapshot_download
from transformers import AutoModel, AutoTokenizer

# Configurações do usuário
HUGGINGFACE_USERNAME = ""
HUGGINGFACE_TOKEN = ""
MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"  # Nome do modelo que deseja baixar
SAVE_DIRECTORY = "./../../models/pretrained"  # Diretório onde o modelo será salvo

# Realizar login no Hugging Face
login(HUGGINGFACE_TOKEN)

# Criar diretório local se não existir
os.makedirs(SAVE_DIRECTORY, exist_ok=True)

# Baixar o modelo e salvar no diretório especificado
model_path = snapshot_download(repo_id=MODEL_NAME, cache_dir=SAVE_DIRECTORY)

print(f"Modelo {MODEL_NAME} baixado e salvo em: {model_path}")

# Carregar o modelo e tokenizer para verificar se tudo está correto
model = AutoModel.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

print("Modelo e tokenizer carregados com sucesso!")