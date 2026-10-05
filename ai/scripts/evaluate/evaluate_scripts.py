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
