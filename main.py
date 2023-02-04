from transformers import set_seed, GPT2LMHeadModel, GPT2Tokenizer, pipeline

#get large GPT2 tokenizer and GPT2 model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
model = GPT2LMHeadModel.from_pretrained("gpt2-large")

textgen = pipeline(
    'text-generation',
    model=model, 
    tokenizer=tokenizer)

sentence = "What is Love?"
output = textgen(sentence)
message = tokenizer.decode(output)
print(message)
