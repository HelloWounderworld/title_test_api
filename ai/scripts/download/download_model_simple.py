from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"  # Exemplo de LLM

print(f"Downloading model and tokenizer from: {MODEL_NAME}")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Salvar localmente
model.save_pretrained("./models/base_model/")
tokenizer.save_pretrained("./models/base_model/")
print("Model and tokenizer saved in ./models/base_model/")
