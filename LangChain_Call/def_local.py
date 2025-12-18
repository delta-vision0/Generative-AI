from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

def call_local(user_input):
    url = "http://127.0.0.1:1234/v1"
    chat = ChatOpenAI(base_url= url,model="google/gemma-3-4b",api_key="dummy-key")

    #user_input = input("You : ")

    result = chat.invoke(user_input)

    return result.content



# input  = input("you : ")
# result = call_local(input)
# print("AI : ",result)