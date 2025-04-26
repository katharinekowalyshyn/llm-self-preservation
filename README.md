# LLM Probing for Self-Preservation

This repository contains code for probing internal activations of the **Llama 3.2 1B Instruct** model.  
We use a pretrained Sparse Autoencoder from [qresearch's HuggingFace page](https://huggingface.co/qresearch/Llama-3.2-1B-Instruct-SAE-l9).  
The repo also includes supporting code for dataset generation and result analysis.

## Usage

A Google Colab link is provided at the top of `llm_probing.ipynb`.  
You can follow that link to run the code interactively.


### Requirements

- A **Google Colab Pro** account may be needed due to compute requirements.  
  (Experiments were run on an **A100 GPU**.)
- Access to **Meta Llama 3.2 1B Instruct** on Hugging Face.  
  - [Request access here](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) — typically granted within about an hour.
- You must authenticate with Hugging Face in `llm_probing.ipynb` to download the model.