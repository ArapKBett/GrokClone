from agent.grok_agent import GrokAgent
from utils.io_handler import get_user_input, display_response

def main():
    agent = GrokAgent()
    print("GrokClone: Hello! I’m your DIY Grok, inspired by xAI. How can I assist you?")
    
    while True:
        user_input = get_user_input()
        if user_input.lower() in ["exit", "quit"]:
            print("GrokClone: Goodbye! It was fun being helpful.")
            break
        response = agent.process_input(user_input)
        display_response(response)

if __name__ == "__main__":
    main()
