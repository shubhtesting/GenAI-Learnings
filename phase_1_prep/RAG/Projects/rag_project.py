from google import genai
import numpy as np

client = genai.Client()

documents = [
    "Refund requests are allowed within 7 days.",
    "Python classes happen monday to friday.",
    "Students can get 3 interview opportunities.",
    "Course access is available for 6 months."
]

question = "Can I get my money back after 5 days?"

# question = "How many interview opportunities can I get?"

# question = "What is duration of course availability?"

### Try question which dont have required context in provided documents

# question = "When is a last date to enroll to course?"

document_vectors = []

# Step 1: Convert each document into vector
for document in documents:
    result = client.models.embed_content(
        model = "gemini-embedding-2",
        contents = document,
    )
    
    vector = result.embeddings[0].values
    document_vectors.append(vector)
    

# Step 2: Convert question into question_vector
question_result = client.models.embed_content(
        model = "gemini-embedding-2",
        contents = question,
    )

question_vector = question_result.embeddings[0].values

# Step 3: Use cosine simalarity to retrieve answer
def cosine_simalarity(a,b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a,b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )

scores = [] 

for doc_vector in document_vectors :
    score = cosine_simalarity(question_vector, doc_vector)
    scores.append(score)

# Step 4: Retrieve best matching document
best_index = np.argmax(scores)
best_doc = documents[best_index]

print("Best matching document:")
print(best_doc)

# Step 5: Send retrieved chunk to LLM
prompt = f"""
Answer the question using only the context below.

Context:
{best_doc}

Question:
{question}
"""

# Step 6: Generate final answer:
response = client.models.generate_content(
    model = "gemini-3.6-flash",
    contents = prompt
)

print("Final Answer:")
print(response.text)

