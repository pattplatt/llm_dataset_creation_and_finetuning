from datasets import load_dataset

dataset = load_dataset("Puidii/aalen_university_faculty_computer_science")

litgpt finetune lora --checkpoint_dir '/Users/patrickmuller/Documents/dev/custom_llm_finetuning/litgpt/checkpoints/TinyLlama/TinyLlama-1.1B-Chat-v1.0' --data JSON --data.json_path litgpt/data/data/
