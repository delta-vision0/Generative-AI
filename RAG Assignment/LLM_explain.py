from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model(
    model = "llama-3.3-70b-versatile",
    model_provider = "openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("groq_api_key")
)

def explain(resume_text , job_description):
    prompt = f"""You are a Senior Technical Recruiter. Evaluate the candidate for the following role:
    
    JOB DESCRIPTION: 
    {job_description}
    
    CANDIDATE RESUME: 
    {resume_text}
    
    INSTRUCTIONS:
    Provide exactly three bullet points in the following format:
    1. **Candidate Name**: [Extract full name]
    2. **Professional Summary**: [A 2-3 sentence overview of their technical background and expertise]
    3. **Shortlisting Justification**: [A 2-3 sentence explanation of why their specific skills are a perfect match for this job description]
    
    Keep the tone formal and objective. Do not use generic filler words."""
    response = llm.invoke(prompt)
    return response.content
