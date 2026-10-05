from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import torch

# Caminho do modelo base e do modelo com adapter
base_model_path = "./../../models/pretrained/models--meta-llama--Llama-3.2-3B-Instruct/snapshots/0cb88a4f764b7a12671c53f0838cd831a0843b95"
adapter_path = "./../../models/trained/title-ai-trained-llama32-3B/checkpoint-6000"

# Carregar tokenizer (da base, com tudo funcionando)
# tokenizer = AutoTokenizer.from_pretrained(base_model_path)
tokenizer = AutoTokenizer.from_pretrained(adapter_path)

# Carregar o modelo base
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_path,
    torch_dtype=torch.float16,
    device_map="auto"
)

# 3. Atualiza a embedding do modelo para bater com o novo vocabulário
base_model.resize_token_embeddings(len(tokenizer))

# Carregar o adapter treinado com PEFT
model = PeftModel.from_pretrained(base_model, adapter_path)

# Modo de inferência
model.eval()

# Função de geração de título
def gerar_titulo(texto_materia):
    prompt = f"<|begin_of_text|><|user|>\nCrie um título jornalístico para o seguinte texto:\n{texto_materia}<|end_of_text|>\n<|assistant|>\n"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=64,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.pad_token_id,
        )

    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    resposta = output_text.split("<|assistant|>\n")[-1].strip()
    return resposta

# Teste
if __name__ == "__main__":
    texto_exemplo = """
    O governo anunciou um novo plano de investimentos em infraestrutura para impulsionar a economia nos próximos anos, com foco em rodovias e ferrovias.
    """
    titulo = gerar_titulo(texto_exemplo)
    print("📰 Título gerado:", titulo)
