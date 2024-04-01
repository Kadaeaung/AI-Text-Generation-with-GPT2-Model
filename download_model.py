import gpt_2_simple as gpt2

def download_gpt2_model():
    # Download the 124M GPT-2 model
    gpt2.download_gpt2(model_name="124M")

if __name__ == "__main__":
    download_gpt2_model()
