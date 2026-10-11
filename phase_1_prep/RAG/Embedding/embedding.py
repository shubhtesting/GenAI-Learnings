from google import genai

client = genai.Client()

result = client.models.embed_content(
    model = "gemini-embedding-2",
    contents = "Refund requests are allowed within7 days.",
)

# print(result.embeddings)   # or we can also do only print(result) -- same output

vector = result.embeddings[0].values
print(vector)

