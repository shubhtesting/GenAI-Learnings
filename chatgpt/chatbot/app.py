import os
from openai import OpenAI, RateLimitError
from phase_1_prep.chatgpt.chatbot.config import SYSTEM_PROMPT, MODEL_NAME, MEMORY_LIMIT, LOG_FILE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "chat.log")

os.makedirs(LOG_DIR, exist_ok=True)


# Log function to save conversation
def log_message(role, content):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{role.upper()}: {content}\n")

def chat():
    messages = []

    print("Chatbot is ready! Type 'exit' to stop.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        log_message("user", user_input)
        messages.append({
            "role": "user",
            "content": user_input
        })

        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages
            )

            assistant_message = response.choices[0].message.content

            print("Bot:", assistant_message)

            messages.append({
                "role": "assistant",
                "content": assistant_message
            })

        except RateLimitError as e:
            print("\nAPI error: Your API credits are exhausted.")
            print("Please add credits to your OpenAI API account.")
            break

if __name__ == "__main__":
    chat()




































# # Following bot only works before 2023 its outdated!!!!!!

# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# # Load environment variable for API key
# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def chat():
#     print("Chatbot is ready! Type 'exit' to stop.\n")

#     messages = [
#         {"role": "system", "content": "You are a helpful assistant."}
#     ]

#     while True:
#         user_input = input("You: ")

#         if user_input.lower() == "exit":
#             print("Chatbot: Goodbye! 👋")
#             break

#         messages.append({"role": "user", "content": user_input})

#         response = client.chat.completions.create(
#             model="gpt-4.1-mini",
#             messages=messages
#         )

#         reply = response.choices[0].message.content
#         print("Chatbot:", reply)

#         # Add assistant response to memory
#         messages.append({"role": "assistant", "content": reply})

# if __name__ == "__main__":
#     chat()
