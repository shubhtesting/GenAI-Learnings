from google import genai
import numpy as np

client = genai.Client()

documents = [
    "Refund requests are allowed within 7 days.",
    "Python classes happen monday to friday",
    "Students get 3 interview opportunities"
]

question = "Can I get my money back after 5 days."

document_vector = []

# Convert each document into vector
for doc in documents:
    result = client.models.embed_content(
        model = "gemini-embedding-2",
        contents = question,
    )
    
    vector = result.embeddings[0].values
    document_vector.append(vector)
    

# Convert question into question_vector
question_result = client.models.embed_content(
        model = "gemini-embedding-2",
        contents = question,
    )

question_vector = question_result.embeddings[0].values

def cosine_simalarity(a,b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a,b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )
    
for document, vector in zip(documents, document_vector):
    score = cosine_simalarity(vector, question_vector)
    print(round(score,3),document)