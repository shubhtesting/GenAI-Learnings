from ollama import chat

response = chat(
    model = "gemma3:1b",
    messages=[
        {
            "role": "User",
            "content": "Explain nlp in one sentence"
        }
    ]
)

print(response.message.content)