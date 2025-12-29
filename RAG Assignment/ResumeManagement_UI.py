import streamlit as st 
import chromadb
import pdf_text
import embedding
import os
import ChromaStore
import LLM_explain

st.title("Resume Screening Application")
uploaded_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"{len(uploaded_files)} files uploaded")

UPLOAD_DIR = "uploaded_resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)
if st.button("Store Resumes"):
    if uploaded_files:
        for file in uploaded_files:
            save_path = os.path.join(UPLOAD_DIR,file.name)
            with open(save_path,"wb") as f:
                f.write(file.read())
        
            ChromaStore.store_db(save_path)
        st.success("All resumes have been stored in the database.")
    else :
        st.error("Please upload at least one PDF file.")
        st.divider()


st.header("2. Shortlist resumes")

job_description = st.text_area(
    "Enter Job Description",
    height=100
)
top_k = st.slider("Number of Top Resumes to Retrieve", min_value=1, max_value=10, value=3)

if st.button("ShortList"):
    if not job_description.strip():
        st.error("Enter A Job Description..")
    else:
        results = ChromaStore.search_resume(job_description,top_k)
        st.subheader("Shortlisted Resumes")

        ids = results["ids"][0]
        metas = results["metadatas"][0]

        documents = results["documents"][0]
        metas = results["metadatas"][0]

        for i , meta in enumerate(metas):
            # Use 'resume_id' instead of "resume_id"
            display_id = meta.get("resume_id", ids[i])
            st.write(f"**{i+1}. Resume ID :** {display_id}")
            st.divider()

            explain = LLM_explain.explain(documents[i],job_description)
            st.markdown(explain)
            st.divider()