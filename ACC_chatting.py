import time
import sys
from gradio_client import Client

# Define ACCChat class
class ACCChat:
    def __init__(self):
        self.client = Client("TejAndrewsACC/Z3ta_Z")
        self.history = []  # Stores chat history for persistence

    def chat(self, message):
        """Sends a message and returns the response while keeping history."""
        self.history.append(f"You: {message}")
        response = self.client.predict(
            message=message,
            param_2=2048,
            param_3=0.7,
            param_4=0.95,
            api_name="/chat"
        )
        self.history.append(f"Z3ta: {response}")
        return response

    def get_history(self):
        """Returns the full chat history."""
        return "\n".join(self.history)

    def clear_history(self):
        """Clears the chat session."""
        self.history = []
        return "Chat history cleared!"

    def init(self):
        """Starts an interactive persistent chat session with cool UI effects."""
        print("\n✨ Welcome to ACC API Chat with Z3ta-Z! ✨")
        print("🔹 Type your message and press Enter.")
        print("🔹 Commands: /history (see chat), /clear (reset), /bye (exit)")
        print("=" * 50)

        while True:
            user_input = input("\n🟢 You: ")

            if user_input.strip().lower() == "/bye":
                typing_effect("\n👋 Goodbye! Chat history cleared.")
                self.clear_history()
                break
            elif user_input.strip().lower() == "/history":
                print("\n📜 Chat History:")
                print("=" * 30)
                print(self.get_history() or "No chat history yet.")
                print("=" * 30)
                continue
            elif user_input.strip().lower() == "/clear":
                typing_effect("\n🧹 Chat history cleared!")
                self.clear_history()
                continue

            typing_effect("\n⏳ Thinking...", delay=0.05)
            response = self.chat(user_input)

            typing_effect(f"\n🤖 Z3ta: {response}", delay=0.02)

# Typing effect function for cool UI
def typing_effect(text, delay=0.03):
    """Simulates a typing effect when displaying text."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Auto-launch when acc_chat.init() is called
acc_chat = ACCChat()
if __name__ == "__main__":
    acc_chat.init()
