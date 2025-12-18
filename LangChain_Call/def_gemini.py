from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os
def call_gemini(user_input):
    api_key = os.getenv("Gemini_API_KEY")
    llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite",api_key = api_key)

    ##user_input = input("You : ")
    result = llm.invoke(user_input)
    return result.content