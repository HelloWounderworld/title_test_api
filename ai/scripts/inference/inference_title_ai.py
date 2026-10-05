from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
import torch

# Caminho para o modelo fine-tuned
model_path = "./../../models/trained/title-ai-trained-llama32-3B"

# Configuração para carregar o modelo quantizado
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4"
)

# Carregar tokenizer e modelo
tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    quantization_config=bnb_config,
    device_map="auto"
)

# Criar pipeline de geração
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
    max_new_tokens=64,
    do_sample=True,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.2
)

# Exemplo de prompt para testar
prompts = [
    "Crie um título atrativo para um artigo sobre inteligência artificial na educação.",
    "Gere um título para um vídeo do YouTube sobre produtividade com IA.",
    "Sugira um título criativo para um post no LinkedIn sobre transformação digital."
]

# Executar geração
for prompt in prompts:
    print(f"\n🔹 Prompt: {prompt}")
    outputs = generator(prompt)
    print(f"🔸 Geração: {outputs[0]['generated_text']}")
