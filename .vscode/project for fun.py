# main.py

# ------------------------------------------------------
# 1) IMPORTS & SETUP
# ------------------------------------------------------
import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

# ------------------------------------------------------
# 2) INITIAL GREETING
# ------------------------------------------------------
print(f"{Fore.CYAN}👋 Welcome to Sentiment Spy! 🕵️{Style.RESET_ALL}")

# ------------------------------------------------------
# 3) USER NAME INPUT
# ------------------------------------------------------
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()

if not user_name:
    user_name = "Mystery Agent"

print(f"{Fore.CYAN}Hello, {user_name}! 🕵️{Style.RESET_ALL}")

# ------------------------------------------------------
# 4) CONVERSATION HISTORY
# ------------------------------------------------------
conversation_history = []

# ------------------------------------------------------
# 5) INSTRUCTIONS
# ------------------------------------------------------
print(f"{Fore.YELLOW}Commands:{Style.RESET_ALL}")
print(f"{Fore.YELLOW}• Type 'reset' to clear conversation history{Style.RESET_ALL}")
print(f"{Fore.YELLOW}• Type 'history' to view conversation history{Style.RESET_ALL}")
print(f"{Fore.YELLOW}• Type 'exit' to end the program{Style.RESET_ALL}")

# ------------------------------------------------------
# 6) MAIN INTERACTION LOOP
# ------------------------------------------------------
while True:
    user_input = input(f"\n{Fore.WHITE}You: {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.YELLOW}⚠️ Please enter something.{Style.RESET_ALL}")
        continue

    # 6.1) 'exit' COMMAND
    if user_input.lower() == "exit":
        print(f"{Fore.CYAN}👋 Goodbye, {user_name}! Thanks for using Sentiment Spy! 🕵️{Style.RESET_ALL}")
        break

    # 6.2) 'reset' COMMAND
    if user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.GREEN}🔄 Conversation history has been reset.{Style.RESET_ALL}")
        continue

    # 6.3) 'history' COMMAND
    if user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}📭 No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")

            for text, polarity, sentiment_type in conversation_history:
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😢"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(
                    f"{color}{emoji} {text} | "
                    f"Polarity: {polarity:.2f} | "
                    f"Sentiment: {sentiment_type}"
                    f"{Style.RESET_ALL}"
                )
        continue

    # 6.4) SENTIMENT ANALYSIS
    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😢"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    conversation_history.append(
        (user_input, polarity, sentiment_type)
    )

    print(
        f"{color}{emoji} Sentiment: {sentiment_type} | "
        f"Polarity: {polarity:.2f}{Style.RESET_ALL}"
    )

# ------------------------------------------------------
# END
# ------------------------------------------------------