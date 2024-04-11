The included scripts were generated in a study project, where a dataset from Aalen University was generated using the ChatGPT API. The dataset was then finetuned on a small LLM. The final work is in the repo and linked [here](https://github.com/pattplatt/llm_dataset_creation_and_finetuning/blob/master/Customization_of_Large_Language_Models_to_User_Defined_Data.pdf).

### Use the data generator script
To use dataset_generator.ipynb you have to get an OpenAI API key and import it into the script or set it as an environment variable.

### How to finetune with the dataset

Here we finetune TinyLlama-1.1B using the [litgpt](https://github.com/Lightning-AI/litgpt/) framework:

Create a new conda environment and install the needed packages:
```bash
conda env -n finetuning python==3.10 
pip install requirements.txt
```
Now the model weights must be downloaded with:
```bash
litgpt download --repo_id TinyLlama/TinyLlama-1.1B-Chat-v1.0
```
Run the following in the terminal to start fine-tuning with the dataset:

```bash
litgpt finetune lora --checkpoint_dir '/mnt/d/dev/llm_dataset_testing/checkpoints/TinyLlama/TinyLlama-1.1B-Chat-v1.0' --data JSON --data.json_path data/ --train.micro_batch_size 1 --train.global_batch_size 1 --train.epochs 1
```
The training took ~13 minutes on a 3060Ti and ~48 minutes on a M1 Pro, using 7.45 GB of memory.

You can use the eval.ipynb to evaluate the finetuning. To do this the weights need to be converted into the HuggingFace Transformer format:
```bash
litgpt convert from_litgpt     --checkpoint_dir out/finetune/lora/final    --output_dir out/hf_checkpoint
```
