import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# === Caminhos ===
base_model_path = "./../../models/pretrained/models--meta-llama--Llama-3.2-3B-Instruct/snapshots/0cb88a4f764b7a12671c53f0838cd831a0843b95"
adapter_path = "./../../models/trained/title-ai-trained-llama32-3B/checkpoint-6000"

# === Carrega tokenizer do adapter ===
tokenizer = AutoTokenizer.from_pretrained(adapter_path)

# === Carrega modelo base e ajusta o tamanho da embedding ===
model = AutoModelForCausalLM.from_pretrained(
    base_model_path,
    torch_dtype=torch.float16,
    device_map="auto"
)
model.resize_token_embeddings(len(tokenizer))

# === Carrega os pesos do adapter (LoRA) ===
model = PeftModel.from_pretrained(model, adapter_path)
model.eval()

# === Loop interativo ===
print("Digite o texto da matéria (ou 'sair' para encerrar):\n")

while True:
    user_input = input("📰 Texto: ")
    if user_input.strip().lower() == "sair":
        break

    prompt = f"Crie um título jornalístico para o seguinte texto:\n\n{user_input}\n\nTítulo:"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=64,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            eos_token_id=tokenizer.eos_token_id
        )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    generated_title = decoded.split("Título:")[-1].strip()
    print(f"\n🧠 Título gerado: {generated_title}\n")
