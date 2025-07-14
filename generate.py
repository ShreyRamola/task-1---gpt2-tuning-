from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

model = GPT2LMHeadModel.from_pretrained("./gpt2-finetuned")
tokenizer = GPT2Tokenizer.from_pretrained("./gpt2-finetuned")

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

prompt = "In the heart of the forest,"
output = generator(prompt, max_length=100, num_return_sequences=1)

print(output[0]['generated_text'])
