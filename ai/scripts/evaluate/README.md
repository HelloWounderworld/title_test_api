Perfeito! Vamos incluir **métricas de avaliação mais informativas** durante o treinamento com `Seq2SeqTrainer` para que você consiga monitorar melhor o desempenho do seu modelo fine-tunado com LoRA.

---

## ✅ **Métricas recomendadas**

Como seu modelo é do tipo **CausalLM com LoRA**, e seus dados estão no formato `.jsonl`, assumo que a tarefa é **geração de texto (instrucional, conversacional ou similar)**.

As métricas mais úteis nesse contexto são:

| Métrica        | O que mede                                                  | Relevância           |
| -------------- | ----------------------------------------------------------- | -------------------- |
| **Perplexity** | Quão "surpreendido" o modelo fica com os dados de validação | Muito útil em LM     |
| **BLEU**       | Similaridade com textos-alvo (baseado em n-gramas)          | Boa para instrução   |
| **ROUGE**      | Cobertura e sobreposição de palavras-chave                  | Boa para sumarização |
| **Accuracy**   | Se há uma resposta exata esperada (menos comum em LLMs)     | Opcional             |

---

## 📦 1. **Instale dependências se necessário**

Se ainda não tem, instale:

```bash
pip install evaluate nltk
```

---

## 🧠 2. **Função de cálculo de métricas**

Adicione este código no seu script, **antes de chamar o `Seq2SeqTrainer`**:

```python
import evaluate
import numpy as np
import nltk
nltk.download('punkt')

# Inicializa métricas
bleu = evaluate.load("bleu")
rouge = evaluate.load("rouge")
perplexity = evaluate.load("perplexity")

def compute_metrics(eval_preds):
    preds, labels = eval_preds

    # Remove -100 usados para ignorar tokens no cálculo da loss
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)

    # Converte IDs para strings
    decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

    # Tokenização para BLEU/ROUGE
    decoded_preds = [nltk.word_tokenize(pred.strip()) for pred in decoded_preds]
    decoded_labels = [[nltk.word_tokenize(label.strip())] for label in decoded_labels]

    # Cálculo das métricas
    bleu_result = bleu.compute(predictions=decoded_preds, references=decoded_labels)
    rouge_result = rouge.compute(predictions=[" ".join(p) for p in decoded_preds],
                                 references=[" ".join(r[0]) for r in decoded_labels])
    ppl_result = perplexity.compute(predictions=preds.tolist(), model_id=args.model_name_or_path)

    return {
        "bleu": bleu_result["bleu"],
        "rougeL": rouge_result["rougeL"],
        "perplexity": ppl_result["perplexity"]
    }
```

---

## 🧪 3. **Adicione ao `Seq2SeqTrainer`**

Altere a parte onde você inicializa o `trainer` para incluir:

```python
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,  # <-- aqui!
)
```

---

## 📊 4. **Resultado**

Agora, ao final de cada avaliação (`eval_steps`, `epoch` ou `eval_only`), você verá algo como:

```json
{
  'eval_loss': 1.95,
  'eval_bleu': 0.45,
  'eval_rougeL': 0.62,
  'eval_perplexity': 4.85
}
```

---

## 💡 Dicas Finais

* **Perplexity** ideal: quanto mais baixo, melhor. Abaixo de 10 já é ótimo.
* **BLEU e ROUGE**: para tarefas de QA, instrução, sumarização, os valores vão de 0 (ruim) até 1 (ótimo). Acima de **0.3-0.5** já é decente.
* Se você estiver fazendo *instruct fine-tuning*, podemos refinar a métrica para avaliar a completude e exatidão da resposta também.

---

Se quiser que eu analise o formato do seu dataset para refinar ainda mais o cálculo dessas métricas (ex.: instruções com múltiplas respostas válidas), posso ajudar nisso também — é só me mandar uma amostra do seu `.jsonl`. Deseja isso?
