import os

with open('wh40k.txt', 'r') as f:
    text_data = f.readlines()

clean = []

for line in text_data:
  if "pp." not in line and "pg." not in line and len(line.split(' ')) >= 4:
    clean.append(line.strip())

print(clean[0:5])

import csv

csv_filename = "data/train.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["text"])
    for text in clean:
        writer.writerow([text])

#@markdown ---
#@markdown #### Project Config
#@markdown Note: if you are using a restricted/private model, you need to enter your Hugging Face token in the next step.
project_name = 'llama_wh40k_2' # @param {type:"string"}
model_name = 'meta-llama/Llama-2-7b-chat-hf' # @param {type:"string"}

#@markdown ---
#@markdown #### Push to Hub?
#@markdown Use these only if you want to push your trained model to a private repo in your Hugging Face Account
#@markdown If you dont use these, the model will be saved in Google Colab and you are required to download it manually.
#@markdown Please enter your Hugging Face write token. The trained model will be saved to your Hugging Face account.
#@markdown You can find your token here: https://huggingface.co/settings/tokens
push_to_hub = False # @param ["False", "True"] {type:"raw"}
repo_id = "username/repo_name" #@param {type:"string"}

#@markdown ---
#@markdown #### Hyperparameters
learning_rate = 2e-4 # @param {type:"number"}
num_epochs = 1 #@param {type:"number"}
batch_size = 8 # @param {type:"slider", min:1, max:32, step:1}
block_size = 256 # @param {type:"number"}
trainer = "sft" # @param ["default", "sft"] {type:"raw"}
warmup_ratio = 0.1 # @param {type:"number"}
weight_decay = 0.01 # @param {type:"number"}
gradient_accumulation = 4 # @param {type:"number"}
use_fp16 = False # @param ["False", "True"] {type:"raw"}
use_peft = True # @param ["False", "True"] {type:"raw"}
use_int4 = True # @param ["False", "True"] {type:"raw"}
lora_r = 16 #@param {type:"number"}
lora_alpha = 32 #@param {type:"number"}
lora_dropout = 0.05 #@param {type:"number"}

os.environ["PROJECT_NAME"] = project_name
os.environ["MODEL_NAME"] = model_name
os.environ["PUSH_TO_HUB"] = str(push_to_hub)
os.environ["REPO_ID"] = repo_id
os.environ["LEARNING_RATE"] = str(learning_rate)
os.environ["NUM_EPOCHS"] = str(num_epochs)
os.environ["BATCH_SIZE"] = str(batch_size)
os.environ["BLOCK_SIZE"] = str(block_size)
os.environ["WARMUP_RATIO"] = str(warmup_ratio)
os.environ["WEIGHT_DECAY"] = str(weight_decay)
os.environ["GRADIENT_ACCUMULATION"] = str(gradient_accumulation)
os.environ["USE_FP16"] = str(use_fp16)
os.environ["USE_PEFT"] = str(use_peft)
os.environ["USE_INT4"] = str(use_int4)
os.environ["LORA_R"] = str(lora_r)
os.environ["LORA_ALPHA"] = str(lora_alpha)
os.environ["LORA_DROPOUT"] = str(lora_dropout)

