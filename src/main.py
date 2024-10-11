from transformers import AutoTokenizer
import transformers
import torch

model = "sh2orc/Llama-3.1-Korean-8B-Instruct"
messages = [{"role": "user", "content": "RAG가 어떤거야?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation", model=model, torch_dtype=torch.float16, device_map="auto"
)

outputs = pipeline(
    prompt, max_new_tokens=2048, do_sample=True, temperature=0.7, top_k=50, top_p=0.95
)
print(outputs[0]["generated_text"])