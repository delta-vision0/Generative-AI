from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import init_embeddings

def load_pdf_resumes(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    resume_content = ""
    for page in docs:
        resume_content += page.page_content
    metadata = {
        "source" : pdf_path,
        "page_count" : len(docs),
    }
    return resume_content,metadata

path = "D:/SunBeam/IIT-08-B-Generative-AI-94543/Fake_Resumes/resume-014.pdf"
resume_text , meta =load_pdf_resumes(path)
print(resume_text)
print(meta)