from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model = "gemini-3.6-flash",
    input = "Explain Machine learning in one line.",
    # generation_config = {
    #     "temprature" : 1.0,
    #     "max_output_tokens" : 1000,
    # }

)

print(interaction.output_text)