#!/bin/bash
python train_qlora.py \
  --model_name ./../../models/pretrained/models--meta-llama--Llama-3.2-3B-Instruct/snapshots/0cb88a4f764b7a12671c53f0838cd831a0843b95 \
  --output_dir ./../../models/trained/title-ai-trained-llama32-3B \
  --dataset_name ./../../data/processed/filtrado.json \
  --max_steps 3000 \
  --logging_steps 10 \
  --save_strategy steps \
  --save_steps 50 \
  --save_total_limit 40 \
  --logging_strategy steps \
  --remove_unused_columns False \
  --do_train \
  --dataloader_num_workers 2 \
  --group_by_length \
  --lora_r 64 \
  --lora_alpha 16 \
  --lora_modules all \
  --double_quant \
  --quant_type nf4 \
  --bf16 False \
  --bits 4 \
  --warmup_ratio 0.03 \
  --lr_scheduler_type cosine \
  --gradient_checkpointing \
  --source_max_len 128 \
  --target_max_len 512 \
  --per_device_train_batch_size 2 \
  --gradient_accumulation_steps 8 \
  --learning_rate 2e-4 \
  --adam_beta2 0.999 \
  --max_grad_norm 0.3 \
  --lora_dropout 0.1 \
  --weight_decay 0.0 \
  --seed 0 \
  --use_peft

# python train_qlora.py \
#   --model_name ./../../models/pretrained/models--meta-llama--Llama-3.2-3B-Instruct/snapshots/0cb88a4f764b7a12671c53f0838cd831a0843b95 \
#   --output_dir ./../../models/trained/title-ai-trained-llama32-3B \
#   --dataset_name ./../../data/processed/filtrado.json \
#   --validation_file ./../../data/processed/val.json \
#   --do_train \
#   --do_eval \
#   --evaluation_strategy steps \
#   --eval_steps 100 \
#   --save_strategy steps \
#   --save_steps 100 \
#   --save_total_limit 3 \
#   --max_steps 6000 \
#   --logging_strategy steps \
#   --logging_steps 10 \
#   --remove_unused_columns False \
#   --dataloader_num_workers 2 \
#   --group_by_length \
#   --lora_r 64 \
#   --lora_alpha 16 \
#   --lora_modules all \
#   --double_quant \
#   --quant_type nf4 \
#   --bf16 False \
#   --bits 4 \
#   --warmup_ratio 0.03 \
#   --lr_scheduler_type cosine \
#   --gradient_checkpointing \
#   --source_max_len 128 \
#   --target_max_len 512 \
#   --per_device_train_batch_size 2 \
#   --gradient_accumulation_steps 8 \
#   --learning_rate 2e-4 \
#   --adam_beta2 0.999 \
#   --max_grad_norm 0.3 \
#   --lora_dropout 0.1 \
#   --weight_decay 0.0 \
#   --seed 0 \
#   --use_peft \
#   --report_to none

# python train_qlora.py \
#   --model_name ./../../models/pretrained/models--meta-llama--Llama-3.2-3B-Instruct/snapshots/0cb88a4f764b7a12671c53f0838cd831a0843b95 \
#   --output_dir ./../../models/trained/title-ai-trained-llama32-3B \
#   --dataset_name ./../../data/processed/filtrado.json \
#   --validation_file ./../../data/processed/val.json \
#   --do_train \
#   --do_eval \
#   --evaluation_strategy steps \
#   --eval_steps 100 \
#   --save_strategy steps \
#   --save_steps 100 \
#   --save_total_limit 3 \
#   --max_steps 6000 \
#   --logging_strategy steps \
#   --logging_steps 10 \
#   --remove_unused_columns False \
#   --dataloader_num_workers 2 \
#   --group_by_length \
#   --lora_r 32 \
#   --lora_alpha 64 \
#   --lora_modules all \
#   --double_quant \
#   --quant_type nf4 \
#   --bf16 False \
#   --bits 4 \
#   --warmup_ratio 0.05 \
#   --lr_scheduler_type cosine \
#   --gradient_checkpointing \
#   --source_max_len 128 \
#   --target_max_len 512 \
#   --per_device_train_batch_size 2 \
#   --gradient_accumulation_steps 8 \
#   --learning_rate 5e-5 \
#   --adam_beta2 0.999 \
#   --max_grad_norm 0.3 \
#   --lora_dropout 0.1 \
#   --weight_decay 0.0 \
#   --seed 0 \
#   --use_peft \
#   --report_to none
