# GPT-2 Fine-Tuning Project (Hugging Face)

This project fine-tunes OpenAI's GPT-2 model on a custom dataset using the Hugging Face `transformers` library.  
It includes training, saving the model, and generating text from the fine-tuned model.

---

## 📂 Project Structure

```
gpt2-project1/
├── project1.txt                 # Your training data (plain text)
├── main.py                      # Fine-tunes GPT-2 on your data
├── generate.py                  # Generates text using the fine-tuned model
├── gpt2-finetuned/              # Folder where the model is saved
├── venv/                        # Python virtual environment (not uploaded)
```

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
.
env\Scripts ctivate
```

### 2. Install Dependencies

```bash
pip install transformers torch datasets accelerate
```

---

## 🚀 How to Use

### 🏋️‍♂️ Train the Model

```bash
python main.py
```

This uses `project1.txt` to train GPT-2 and saves the model in `./gpt2-finetuned/`.

### ✍️ Generate Text from Fine-Tuned Model

```bash
python generate.py
```

The script loads the saved model and generates text based on a custom prompt.

---

## 📝 Customize

- **Edit `custom_data.txt`** to train the model on your own text.
- **Change the prompt** in `generate.py` to explore different outputs.

---

## 🛠 Requirements

- Python 3.7+
- PyTorch
- transformers
- accelerate
- datasets

---

## 🧠 Credit

Built using:
- [🤗 Hugging Face Transformers](https://huggingface.co/transformers/)
- GPT-2 language model
