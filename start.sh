huggingface-cli login

autotrain llm --train --model ${MODEL_NAME} --project-name ${PROJECT_NAME} --data-path data/ --text-column text --lr ${LEARNING_RATE} --batch-size ${BATCH_SIZE} --epochs ${NUM_EPOCHS} --block-size ${BLOCK_SIZE} --warmup-ratio ${WARMUP_RATIO} --lora-r ${LORA_R} --lora-alpha ${LORA_ALPHA} --lora-dropout ${LORA_DROPOUT} --weight-decay ${WEIGHT_DECAY} --gradient-accumulation ${GRADIENT_ACCUMULATION} $( [[ "$USE_FP16" == "True" ]] && echo "--fp16" ) $( [[ "$USE_PEFT" == "True" ]] && echo "--use-peft" ) $( [[ "$USE_INT4" == "True" ]] && echo "--use-int4" ) --merge-adapter