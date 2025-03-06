from transformers import pipeline
from .tools import web_search, analyze_text
from .personality import apply_personality
from utils.config import MODEL_NAME

class GrokAgent:
    def __init__(self):
        # Load a lightweight language model
        self.nlp = pipeline("question-answering", model=MODEL_NAME)

    def process_input(self, user_input):
        if "search" in user_input.lower():
            query = user_input.replace("search", "").strip()
            return web_search(query)
        elif "analyze" in user_input.lower():
            text = user_input.replace("analyze", "").strip()
            return analyze_text(text)
        else:
            # Default: Simple Q&A response
            response = self.nlp({"question": user_input, "context": "I’m Grok, created by xAI."})
            return apply_personality(response["answer"])
