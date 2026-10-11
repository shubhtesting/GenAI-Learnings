from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model = "gemini-3.6-flash",
    input = "Explain Machine learning in one sentence."

)

print(interaction.output_text)