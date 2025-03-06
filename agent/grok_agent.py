from transformers import GPT2Tokenizer, GPT2LMHeadModel
from .tools import web_search, analyze_text, search_x_posts
from .personality import apply_personality
from utils.config import MODEL_NAME

class GrokAgent:
    def __init__(self):
        # Load GPT-2 model and tokenizer
        self.tokenizer = GPT2Tokenizer.from_pretrained(MODEL_NAME)
        self.model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
        self.model.eval()  # Set to evaluation mode

    def generate_response(self, prompt, max_length=150):
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(
            inputs,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    def process_input(self, user_input):
        if "search" in user_input.lower():
            query = user_input.replace("search", "").strip()
            return web_search(query)
        elif "analyze" in user_input.lower():
            text = user_input.replace("analyze", "").strip()
            return analyze_text(text)
        elif "x posts" in user_input.lower():
            query = user_input.replace("x posts", "").strip()
            return search_x_posts(query)
        else:
            # Use GPT-2 for general responses
            prompt = f"User: {user_input}\nGrok: "
            response = self.generate_response(prompt)
            return apply_personality(response)

class GrokAgent:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("./grok_finetuned")
        self.model = GPT2LMHeadModel.from_pretrained("./grok_finetuned")
        self.model.eval()
