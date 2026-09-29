from google import genai

client = genai.Client()

stream = client.interactions.create(
    model = "gemini-3.6-flash",
    input = "Explain Machine learning in details.",
    stream = True

)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)
