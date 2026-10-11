from google import genai
import numpy as np

client = genai.Client()

documents = [
    "Refund requests are allowed within 7 days.",
    "Python classes happen monday to friday.",
    "Students can get 3 interview opportunities.",
    "Course access is available for 6 months."
]

question = "Can I get my money back after 5 days."

# question = "How many interview opportunities can I get?"

# question = "What is duration of course availability?"

### Try question which dont have required context in provided documents

# question = "When is a last date to enroll to course?"

document_vectors = []

# Convert each document into vector
for document in documents:
    result = client.models.embed_content(
        model = "gemini-embedding-2",
        contents = document,
    )
    
    vector = result.embeddings[0].values
    document_vectors.append(vector)
    

# Convert question into question_vector
question_result = client.models.embed_content(
        model = "gemini-embedding-2",
        contents = question,
    )

question_vector = question_result.embeddings[0].values

# Use cosine simalarity to retrieve anaswer
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

# Retrieve best match
best_index = np.argmax(scores)
best_doc = documents[best_index]

print("Question:", question)
print("\nSimilarity scores:", (round(score,3)))
print("\nBest matching document:")
print(best_doc)
