# -*- coding: utf-8 -*-
"""
Rule-Based AI Chatbot
DecodeLabs AI Internship - Project 1
Author: Namitha L

A feature-rich, modular, rule-based AI chatbot built purely using Python
control flow (if-elif-else statements) without any external libraries or APIs.
"""

import random
import sys
from datetime import datetime

# Configure stdout to UTF-8 so emojis display correctly on Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(  # type: ignore[union-attr]
        encoding="utf-8", errors="replace"
    )


# =====================================================================
# DATA STORES — Jokes, Quotes, Tips, Facts, Motivation
# =====================================================================

JOKES: list[str] = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
    "There are 10 types of people: those who understand binary, "
    "and those who don't. 🤖",
    "Why did the Python programmer get dynamic vision? "
    "They didn't like C-ing things! 🐍😄",
    "A SQL query walks into a bar and asks two tables... 'Can I join you?' 🍺",
    "Hardware is what you kick; software is what causes the pain. 💻😜",
]

QUOTES: list[str] = [
    '"First, solve the problem. Then, write the code." — John Johnson 💡',
    (
        '"Experience is the name everyone gives to their mistakes."'
        " — Oscar Wilde 🚀"
    ),
    (
        '"Simplicity is prerequisite for reliability."'
        " — Edsger W. Dijkstra ✨"
    ),
    (
        "\"Code is like humor. When you have to explain it, it's bad.\""
        " — Cory House 🎯"
    ),
    '"Make it work, make it right, make it fast." — Kent Beck ⚡',
]


TIPS: list[str] = [
    "💡 Write clear, self-explanatory variable names "
    "— avoid cryptic short names.",
    "💡 Always test your code with edge cases to make it robust and reliable.",
    "💡 Break large problems into smaller, manageable functions.",
    "💡 Comment your code to explain *why*, not just *what* is being done.",
    "💡 Keep learning — programming is a journey of continuous practice!",
]

FUN_FACTS: list[str] = [
    (
        "🎉 Fun Fact: Python was named after the British comedy series "
        "'Monty Python's Flying Circus', not the snake!"
    ),
    (
        "🎉 Fun Fact: The word 'bug' in computing dates back to 1947 when "
        "Grace Hopper found a real moth stuck inside a computer relay!"
    ),
    (
        "🎉 Fun Fact: Guido van Rossum created Python as a holiday hobby "
        "project during Christmas 1989!"
    ),
    (
        "🎉 Fun Fact: The first AI program, written in 1951 by Christopher "
        "Strachey, played a game of checkers!"
    ),
    (
        "🎉 Fun Fact: Over 80% of machine learning models worldwide "
        "are built using Python!"
    ),
]

MOTIVATION_MESSAGES: list[str] = [
    "🌟 You are capable of accomplishing great things! Keep pushing forward!",
    "🚀 Every expert was once a beginner. Keep coding and learning every day!",
    "💪 Mistakes are proof that you are trying. Don't give up!",
    "✨ Believe in yourself. Great projects take time and dedication!",
    "🔥 Success is the sum of small efforts repeated day in and day out!",
]


# =====================================================================
# HELPER FUNCTIONS
# =====================================================================

def display_banner() -> None:
    """Prints a clean, attractive welcome banner at startup."""
    print("=" * 65)
    print("      🤖 Welcome to DecodeLabs Rule-Based AI Chatbot 🤖      ")
    print("=" * 65)
    print("  Hi! I am RuleBot, your friendly interactive AI assistant.")
    print("  💡 Type 'help' to see all available commands and topics.")
    print("  👋 Type 'exit', 'quit', or 'bye' to exit the chatbot.")
    print("=" * 65 + "\n")


def display_help() -> None:
    """Displays a well-structured, categorized menu of available commands."""
    print("\n📋 =========== CHATBOT COMMAND MENU =========== 📋")

    print("\n👋 1. GREETINGS & COURTESY")
    print("   • hi / hello / hey / good morning / good evening")
    print("   • good afternoon / greetings / what's up")
    print("   • how are you / thank you")

    print("\n🤖 2. CHATBOT INFORMATION")
    print("   • name                 : Ask chatbot name")
    print("   • age                  : Ask chatbot age")
    print("   • creator / created    : Ask who built this chatbot")
    print("   • what can you do      : View chatbot capabilities")

    print("\n📚 3. EDUCATIONAL & TECH TOPICS")
    print("   • python               : Python programming")
    print("   • ai / artificial intelligence : Artificial Intelligence")
    print("   • ml / machine learning        : Machine Learning")
    print("   • java                 : Java language")
    print("   • c / c programming    : C language")
    print("   • dsa / data structures: Data Structures")
    print("   • algorithms           : Algorithms")
    print("   • full stack           : Full Stack Development")
    print("   • web dev / web development : Web Development")
    print("   • internship           : DecodeLabs Internship info")

    print("\n⏰ 4. UTILITIES & TOOLS")
    print("   • date                 : View current date")
    print("   • time                 : View current time")
    print("   • calc / calculator    : Simple calculator (+, -, *, /)")

    print("\n🎉 5. FUN & INSPIRATION")
    print("   • motivate me          : Get a motivational message")
    print("   • joke                 : Hear a programming joke")
    print("   • quote                : Get an inspiring tech quote")
    print("   • tip                  : Get a useful programming tip")
    print("   • fact                 : Discover a fun AI/Python fact")

    print("\n🚪 6. SYSTEM COMMANDS")
    print("   • help                 : Display this command menu")
    print("   • exit / quit / bye    : Exit the chatbot")
    print("=" * 50 + "\n")


def get_current_date() -> str:
    """Returns the formatted current date string."""
    return datetime.now().strftime("%B %d, %Y")


def get_current_time() -> str:
    """Returns the formatted current time string."""
    return datetime.now().strftime("%I:%M %p")


def _compute(num1: float, num2: float, op: str) -> str:
    """
    Performs arithmetic on two floats using the given operator.
    Returns a formatted result string, or an error message string.
    """
    result: float

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0.0:
            return "Bot 🤖: Error! Division by zero is not allowed. ❌"
        result = num1 / num2
    else:
        return "Bot 🤖: Invalid operator! Use +, -, *, or /. ❌"

    # Display as integer when there's no fractional part (e.g. 100.0 → 100)
    display = int(result) if result == int(result) else round(result, 4)
    return f"Bot 🤖: {num1} {op} {num2} = {display} 🧮"


def run_calculator(user_input: str) -> str:
    """
    Handles basic arithmetic calculations (+, -, *, /).
    Parses an inline expression (e.g. 'calc 10 + 20') or falls back
    to an interactive prompt.
    """
    # Strip command keywords to isolate the expression
    expr = (
        user_input
        .replace("calculate", "")
        .replace("calculator", "")
        .replace("calc", "")
        .strip()
    )

    # Try to parse an inline expression like "10 + 20"
    for op in ["+", "-", "*", "/"]:
        if op in expr:
            parts = expr.split(op, maxsplit=1)
            if len(parts) == 2:
                left = parts[0].strip()
                right = parts[1].strip()
                if left and right:
                    try:
                        return _compute(float(left), float(right), op)
                    except ValueError:
                        pass  # Fall through to interactive mode

    # Interactive mode — prompt the user for values
    print("Bot 🤖: Simple Calculator 🧮")
    try:
        n1_str = input("   Enter first number  : ").strip()
        op_str = input("   Enter operator (+,-,*,/): ").strip()
        n2_str = input("   Enter second number : ").strip()
        return _compute(float(n1_str), float(n2_str), op_str)
    except ValueError:
        return "Bot 🤖: Invalid input! Please enter valid numeric values. ❌"


def show_capabilities() -> str:
    """Returns a string describing all chatbot capabilities."""
    lines = [
        "Bot 🤖: Here is what I can do for you:",
        "  1. Answer questions about Python, AI, ML, Java, DSA, Web Dev 📚",
        "  2. Show current Date and Time ⏰",
        "  3. Perform simple math calculations 🧮",
        "  4. Tell programming jokes, fun facts & inspiring quotes 🎭",
        "  5. Provide coding tips and motivational boosts 🚀",
        "  Type 'help' anytime to see all available commands!",
    ]
    return "\n".join(lines)


# =====================================================================
# MAIN CHATBOT ENGINE — Rule-based if-elif-else logic
# =====================================================================

def chatbot() -> None:
    """Main execution loop for the Rule-Based AI Chatbot."""
    display_banner()

    while True:
        # Get user input, strip extra spaces, and convert to lowercase
        user_input = input("You 👤: ").strip().lower()

        # Handle empty input gracefully
        if not user_input:
            print("Bot 🤖: Please type something so I can respond! 😊")
            continue

        # 1. Exit Commands
        if user_input in ["exit", "quit", "bye"]:
            print("Bot 🤖: Goodbye! Have a wonderful day and happy coding! ❤️✨")
            break

        # 2. Help Command
        elif user_input == "help":
            display_help()

        # 3. Greetings
        elif user_input in [
            "hi", "hello", "hey", "good morning", "good evening",
            "good afternoon", "greetings", "what's up", "sup",
        ]:
            print("Bot 🤖: Hello there! How can I assist you today? 😊")

        # 4. Chatbot Name
        elif "name" in user_input:
            print(
                "Bot 🤖: My name is RuleBot! "
                "I am a Rule-Based AI Chatbot built for DecodeLabs. 🤖"
            )

        # 5. Chatbot Age
        elif "age" in user_input or "how old" in user_input:
            print(
                "Bot 🤖: As an AI chatbot, I don't age — "
                "but I was built recently using Python! 🐍⚡"
            )

        # 6. Chatbot Creator
        elif (
            "created" in user_input
            or "creator" in user_input
            or "who made you" in user_input
        ):
            print(
                "Bot 🤖: I was created by Namitha L as part of "
                "the DecodeLabs AI Internship project! 🚀💻"
            )

        # 7. Capabilities — "what can you do?"
        elif (
            "what can you do" in user_input
            or "capabilities" in user_input
            or "features" in user_input
        ):
            print(show_capabilities())

        # 8. Date Query
        elif "date" in user_input:
            print(f"Bot 🤖: Today's date is 📅 {get_current_date()}.")

        # 9. Time Query
        elif "time" in user_input:
            print(f"Bot 🤖: The current time is ⏰ {get_current_time()}.")

        # 10. Python Information
        elif "python" in user_input:
            print(
                "Bot 🤖: Python is a powerful, easy-to-learn language "
                "widely used in AI, Data Science, and Web Dev! 🐍🔥"
            )

        # 11. Artificial Intelligence Information
        elif "artificial intelligence" in user_input or user_input == "ai":
            print(
                "Bot 🤖: Artificial Intelligence (AI) refers to systems that "
                "simulate human intelligence to solve complex problems! 🧠🤖"
            )

        # 12. Machine Learning Information
        elif "machine learning" in user_input or user_input == "ml":
            print(
                "Bot 🤖: Machine Learning (ML) is a subset of AI that enables "
                "systems to learn and improve from data without explicit "
                "programming! 📊🤖"
            )

        # 13. Java Information
        elif "java" in user_input:
            print(
                "Bot 🤖: Java is an object-oriented language famous for its "
                "'Write Once, Run Anywhere' portability! ☕💻"
            )

        # 14. C Programming Information
        elif (
            "c programming" in user_input
            or user_input == "c language"
            or user_input == "c"
        ):
            print(
                "Bot 🤖: C is a foundational procedural language created by "
                "Dennis Ritchie in 1972 — it powers modern OS and compilers! ⚡"
            )

        # 15. Data Structures Information
        elif "data structure" in user_input or "dsa" in user_input:
            print(
                "Bot 🤖: Data Structures (Arrays, Linked Lists, Stacks, "
                "Queues, Trees, Graphs) organize data efficiently! 🗂️⚡"
            )

        # 16. Algorithms Information
        elif "algorithm" in user_input:
            print(
                "Bot 🤖: An Algorithm is a step-by-step set of rules designed "
                "to solve a specific problem or complete a task! ⚙️💡"
            )

        # 17. Full Stack Development
        elif "full stack" in user_input:
            print(
                "Bot 🤖: Full Stack Development covers both frontend (UI) and "
                "backend (server/database) of web applications! 🌐🖥️"
            )

        # 18. Web Development
        elif "web development" in user_input or "web dev" in user_input:
            print(
                "Bot 🤖: Web Development uses HTML, CSS, JavaScript, "
                "and backend frameworks to build websites! 🌐💻"
            )

        # 19. Internship Information
        elif "internship" in user_input or "decodelabs" in user_input:
            print(
                "Bot 🤖: Internships provide hands-on industry experience! "
                "This chatbot is built for the DecodeLabs AI Internship. 🎓💼"
            )

        # 20. How Are You
        elif "how are you" in user_input or "how r u" in user_input:
            print(
                "Bot 🤖: I'm doing fantastic! Thank you for asking. "
                "How are you doing today? 😊"
            )

        # 21. Thank You
        elif "thank" in user_input:
            print("Bot 🤖: You're very welcome! Happy to help. 🙌✨")

        # 22. Motivation Command
        elif (
            "motivate" in user_input
            or "motivation" in user_input
            or "inspire" in user_input
        ):
            print(f"Bot 🤖: {random.choice(MOTIVATION_MESSAGES)}")

        # 23. Joke Command
        elif "joke" in user_input:
            print(f"Bot 🤖: {random.choice(JOKES)}")

        # 24. Quote Command
        elif "quote" in user_input:
            print(f"Bot 🤖: {random.choice(QUOTES)}")

        # 25. Tip Command
        elif "tip" in user_input:
            print(f"Bot 🤖: {random.choice(TIPS)}")

        # 26. Fun Fact Command
        elif "fact" in user_input:
            print(f"Bot 🤖: {random.choice(FUN_FACTS)}")

        # 27. Calculator Command
        elif (
            "calc" in user_input
            or "calculator" in user_input
            or "calculate" in user_input
        ):
            print(run_calculator(user_input))

        # 28. Default Fallback Response
        else:
            print(
                "Bot 🤖: Sorry, I don't understand that command. 😅 "
                "Type 'help' to see all available commands!"
            )


# Program Entry Point
if __name__ == "__main__":
    chatbot()