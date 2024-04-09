Example of how to finetune with the dataset:
Here we finetune TinyLlama-1.1B using the [litgpt](https://github.com/Lightning-AI/litgpt/) framework:

Create a new conda environment and install the needed packages:
```bash
conda env -n finetuning python==3.10 
pip install requirements.txt
```
In a jupyter notebook or python file run the following lines:
```python
from datasets import load_dataset

dataset = load_dataset("Puidii/aalen_university_faculty_computer_science")
dataset.save_to_disk("/path/to/your/folder")
litgpt finetune lora --checkpoint_dir '/Users/patrickmuller/Documents/dev/custom_llm_finetuning/litgpt/checkpoints/TinyLlama/TinyLlama-1.1B-Chat-v1.0' --data JSON --data.json_path path/to/your/folder
```
You can use the validation.ipynb to evaluate the finetuning.
