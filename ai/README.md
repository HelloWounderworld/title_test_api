# Fine-Tuning using qLoRA

## 🧠 Model References

* [LLaMA-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)
* [LLaMA-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf)

## ⚙️ Hyperparameters in LLM and Fine-Tuning

### Introductory Guides:

* [Model Parameters vs Hyperparameters](https://machinelearningmastery.com/difference-between-a-parameter-and-a-hyperparameter/)
* [Guide to Hyperparameter Tuning](https://www.analyticsvidhya.com/blog/2022/02/a-comprehensive-guide-on-hyperparameter-tuning-and-its-techniques/)
* [Hyperparameters for qLoRA](https://www.reddit.com/r/LocalLLaMA/comments/1aq1u3n/qlora_hyperparameters_for_small_finetuning_task/)
* [EntryPointAI: LoRA Fine-Tuning](https://www.entrypointai.com/blog/lora-fine-tuning/)

### Hyperparameters Specific to Fine-Tuning:

* [Encord Blog](https://encord.com/blog/fine-tuning-models-hyperparameter-optimization/)
* [Fine-Tuning Hyperparameters](https://www.entrypointai.com/blog/fine-tuning-hyperparameters/)

## 📏 Evaluation: BLEU and Other Metrics

To evaluate performance, 10% of the dataset will be used as a reference.

* [BLEU, ROUGE, METEOR Metrics](https://mlexplained.blog/2023/07/08/large-language-model-llm-evaluation-metrics-bleu-and-rouge/)
* [Google Cloud AutoML Evaluation](https://cloud.google.com/translate/docs/advanced/automl-evaluate?hl=pt-br)

## 🧩 Fine-Tuning Philosophy

1. Create a `.gguf` file — a "brain" base for the model.
2. Fine-tune the model **offline**, without internet.

## 🐳 Docker Setup

### Configure Proxy (Optional):

* [Docker Proxy Docs](https://docs.docker.com/engine/daemon/proxy/)

### NVIDIA Toolkit Setup:

* Validate NVIDIA setup:

  ```bash
  nvidia-smi
  nvcc --version
  ```
* [NVIDIA Docker Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
* Install CUDA:
  [CUDA Toolkit 12.x](https://developer.nvidia.com/cuda-12-2-0-download-archive)

## 🛠️ Fine-Tuning Step-by-Step

### Learning Resources:

* [Kan Hatakeyama Note 1](https://note.com/kan_hatakeyama/n/ncd09c52d26c7)
* [Kan Hatakeyama Note 2](https://note.com/kan_hatakeyama/n/n5941dd9d3af4)
* [Medium - Fine-Tuning with qLoRA](https://medium.com/@dillipprasad60/qlora-explained-a-deep-dive-into-parametric-efficient-fine-tuning-in-large-language-models-llms-c1a4794b1766)

### Testing & Verification:

* [Ollama: Local LLaMA2 Execution](https://ollama.com/blog/run-llama2-uncensored-locally)
* [Zenn Guide](https://zenn.dev/if001/articles/6c507e15cd958b)

### Model Downloads:

* **Fugaku 13B**: [Fugaku-LLM-13B-instruct-gguf](https://huggingface.co/Fugaku-LLM/Fugaku-LLM-13B-instruct-0325b-q5_k_m.gguf)
* Necessary files:

  * `config.json`
  * `tokenizer.json`, `tokenizer_config.json`, `special_tokens_map.json`
  * Model files: `pytorch_model-*.bin` or `*.safetensors`

### Hugging Face Authentication:

* Create Access Token: [Hugging Face Security Tokens](https://huggingface.co/docs/hub/security-tokens)
* Login via CLI:

  ```bash
  huggingface-cli login
  ```

## 🚀 Training Commands

### Generic Training Example:

```bash
python qlora.py \
  --model_name model/Fugaku-LLM-13B-instruct-0325b-q5_k_m.gguf \
  --output_dir ./output/test_peft \
  --dataset_name shi3z/anthropic_hh_rlhf_japanese \
  --max_steps 1000 \
  --use_auth \
  --logging_steps 10 \
  --save_strategy steps \
  --save_steps 50 \
  --lora_r 64 \
  --lora_alpha 16 \
  --double_quant \
  --quant_type nf4 \
  --bf16 \
  --bits 4 \
  --warmup_ratio 0.03 \
  --lr_scheduler_type constant \
  --gradient_checkpointing \
  --do_train \
  --output_dir peft_test
```

### LLaMA 2 Example:

```bash
python qlora.py \
  --model_name meta-llama/Llama-2-7b-hf \
  --output_dir ./output/test_peft \
  --dataset_name shi3z/anthropic_hh_rlhf_japanese \
  --max_steps 1000 \
  --do_train \
  --lora_r 64 \
  --lora_alpha 16 \
  --quant_type nf4 \
  --use_auth \
  --bits 4 \
  --bf16 \
  --save_total_limit 40 \
  --group_by_length
```

---

## 🧪 Python & Conda Environment Notes

* Python 3.13.0 (host) / 3.10.15 (conda environment)
* Use virtual environments to manage compatibility

---

## 🧷 Tips

* Always check CUDA version compatibility.
* Use `--cache_dir` to manage Hugging Face downloads.
* Ensure GPU is visible with `nvidia-smi` and `nvcc`.
* Download model weights manually if `huggingface-cli` fails.

---

Aqui está uma versão aprimorada da seção **References**, organizada com uma apresentação mais limpa, numerada automaticamente, agrupada por tópicos e com títulos mais descritivos:

---

## 📚 References

### 🔧 NVIDIA & Docker Setup

1. [PyTorch Container (NVIDIA NGC)](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch)
2. [NVIDIA Driver Download (Windows)](https://www.nvidia.com/content/DriverDownloads/confirmation.php?url=/Windows/531.61/531.61-desktop-win10-win11-64bit-international-dch-whql.exe&lang=us&type=GeForce)
3. [NVIDIA Container Toolkit Release Notes](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.14.4/release-notes.html)
4. [NVIDIA Container Toolkit Documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.14.4/index.html)
5. [NVIDIA Container Toolkit (Latest)](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
6. [Docker Hub: NVIDIA CUDA](https://hub.docker.com/r/nvidia/cuda)
7. [CUDA 12.2 Runtime (Ubuntu)](https://hub.docker.com/layers/nvidia/cuda/12.2.0-runtime-ubuntu20.04/images/sha256-3faf586290da5a86115cbf907f3a34ba48e97875a8e148fa969ddaa6b1472b93)
8. [Docker GPU Support Guide](https://docs.docker.com/compose/how-tos/gpu-support/)
9. [NVIDIA Docker Compose Setup (NixOS)](https://github.com/suvash/nixos-nvidia-cuda-python-docker-compose/blob/main/03-nvidia-docker-compose-setup.org)

### 🧠 Fine-Tuning & LLM Resources

10. [HuggingFace Transformers Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index)
11. [LLM JP: Fine-Tuning](https://github.com/llm-jp/llm-jp-sft)
12. [LLM JP: Tokenizer](https://github.com/llm-jp/llm-jp-tokenizer)
13. [LLM JP: DPO (High GPU Usage)](https://github.com/llm-jp/llm-jp-dpo)
14. [LoRA Fine-Tuning (Microsoft)](https://github.com/microsoft/LoRA)
15. [qLoRA Fine-Tuning (Artidoro)](https://github.com/artidoro/qlora)
16. [qLoRA Paper (ArXiv)](https://arxiv.org/abs/2305.14314)
17. [Phi-3 Cookbook (Microsoft)](https://github.com/microsoft/Phi-3CookBook)
18. [Phi-3 Fine-Tuning (Zenn)](https://zenn.dev/headwaters/articles/55f648399c1820)

### 🧪 LLM Research & Prompt Engineering

19. [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165)
20. [Chain-of-Thought Prompting (Reasoning in LLMs)](https://arxiv.org/abs/2201.11903)

### 🧩 Configuração & Testes

21. [Ollama Modelfile Parameters](https://github.com/ollama/ollama/blob/main/docs/modelfile.md#parameter)
22. [Simple CUDA Test with PyTorch](https://stackoverflow.com/questions/48152674/how-do-i-check-if-pytorch-is-using-the-gpu)
23. [Setting Proxy in `.bashrc` (Qiita 1)](https://qiita.com/Fal318/items/338521feb42197a3aee5)
24. [Setting Proxy in `.bashrc` (Qiita 2)](https://qiita.com/nullsnet/items/66590b0ff33e15db7532)

### 💡 Insights & Misc

25. [Best Open Source LLMs for Content Creation](https://byrayray.medium.com/llama-3-2-vs-llama-3-1-vs-gemma-2-finding-the-best-open-source-llm-for-content-creation-1f6085c9f87a)
26. [Clustering Overview (IBM)](https://www.ibm.com/topics/clustering)
