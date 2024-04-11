Example of how to finetune with the dataset:
Here we finetune TinyLlama-1.1B using the [litgpt](https://github.com/Lightning-AI/litgpt/) framework:

Create a new conda environment and install the needed packages:
```bash
conda env -n finetuning python==3.10 
pip install requirements.txt

litgpt download --repo_id TinyLlama/TinyLlama-1.1B-Chat-v1.0

```
In a jupyter notebook or python file run the following lines:
```python

litgpt finetune lora --checkpoint_dir '/mnt/d/dev/llm_dataset_testing/checkpoints/TinyLlama/TinyLlama-1.1B-Chat-v1.0' --data JSON --data.json_path data/ --train.micro_batch_size 1 --train.global_batch_size 1 --train.epochs 1

litgpt convert from_litgpt     --checkpoint_dir out/finetune/lora/final    --output_dir out/hf_checkpoint
```
You can use the validation.ipynb to evaluate the finetuning.

One Epoch:
Training time 3060Ti: 770.28s
Training Time M1:2885.12s
Memory used: 7.45 GB