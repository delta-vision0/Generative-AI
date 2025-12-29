from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import init_embeddings
import chromadb
import os
import embedding
import read_pdf as r
import pdf_text

client = chromadb.PersistentClient(path = "./knowledgebase")
collection = client.get_or_create_collection(name = "resumes")
def store_db(resume_path):
    resume_text, resume_info = r.load_pdf_resumes(resume_path)
    # Use the same model for both storing and searching
    vector = embedding.embed_model.embed_documents([resume_text])[0]
    unique_id = os.path.basename(resume_path)
    
    # Ensure metadata has the key your Streamlit app is looking for
    resume_info["resume_id"] = unique_id
    
    collection.upsert(
        ids=[unique_id],
        documents=[resume_text],
        embeddings=[vector],
        metadatas=[resume_info]
    )
    print(f"Successfully added to database: {unique_id}")

def search_resume(job_description, top_k):
    # Use the same model object here as well
    query_vector = embedding.embed_model.embed_query(job_description)
    
    search_results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )
    return search_results
# my_job_requirement = "Looking for a cyber security position"
# print(f"Searching for: {my_job_requirement}...\n")

# top_candidates = search_resume(my_job_requirement)

# print(top_candidates)