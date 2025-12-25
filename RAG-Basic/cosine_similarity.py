from sentence_transformers import SentenceTransformer
import numpy as np

def cosine_similarity(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

model = SentenceTransformer('all-MiniLM-L6-v2')
sentences = ["I Love Football" , "Soccer is my fevorite sport" , "i enjoy cooking pasta"]
embeddings = model.encode(sentences)

a = cosine_similarity(embeddings[0] , embeddings[1])
b = cosine_similarity(embeddings[0] , embeddings[2])

print("Sentance 1 & 2 : ",a)
print("Sentance 1 & 3 : ",b)