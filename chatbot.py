# ==========================================
# Rule-Based AI Chatbot
# Project 1 - DecodeLabs AI Internship
# Author: Namitha L
# ==========================================

def chatbot():
    print("=" * 48)
    print("🤖 Welcome to Rule-Based AI Chatbot")
    print("=" * 48)
    print("Type 'help' to see available commands.")
    print("Type 'exit' to quit.\n")

    while True:
        user = input("You : ").strip().lower()

        # Exit
        if user in ["exit", "quit", "bye"]:
            print("Bot : Goodbye! Have a wonderful day ❤️")
            break

        # Greetings
        elif user in ["hi", "hello", "hey", "good morning", "good evening"]:
            print("Bot : Hello! Nice to meet you.")

        # Asking name
        elif "your name" in user:
            print("Bot : My name is RuleBot. I am a Rule-Based AI Chatbot.")

        # Asking age
        elif "how old are you" in user:
            print("Bot : I don't have an age. I was created using Python.")

        # Asking creator
        elif "who created you" in user:
            print("Bot : I was created by a Python programmer.")

        # Asking time
        elif "time" in user:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M %p")
            print(f"Bot : Current Time is {current_time}")

        # Asking date
        elif "date" in user:
            from datetime import date
            today = date.today().strftime("%B %d, %Y")
            print(f"Bot : Today's Date is {today}")

        # Asking about Python
        elif "python" in user:
            print("Bot : Python is a easy and powerful programming interpreted language.")

        # Asking AI
        elif "artificial intelligence" in user or user == "ai":
            print("Bot : Artificial Intelligence enables machines to mimic  like human intelligence.")

        # Asking internship
        elif "internship" in user:
            print("Bot : Internships help you gain practical industry experience.")

        # Help
        elif user == "help":
            print("\nAvailable Commands:")
            print("----------------------------")
            print("hello")
            print("hi")
            print("your name")
            print("how old are you")
            print("who created you")
            print("python")
            print("artificial intelligence")
            print("internship")
            print("time")
            print("date")
            print("exit\n")

        # Thank you
        elif "thankyou" in user:
            print("Bot : You're welcome!")

        # How are you
        elif "how are you" in user:
            print("Bot : I'm doing great! Thanks for asking.")

        # Default response
        else:
            print("Bot : Sorry, I don't understand that. Type 'help' for available commands.")


# Main Program
if __name__ == "__main__":
    chatbot()