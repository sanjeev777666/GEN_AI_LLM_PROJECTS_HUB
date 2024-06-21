import os
import sys  
from constants import openai_api_key,google_api_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI 
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_api_key

st.title("LANG CHAIN _INITIATION")
INPUT_TXT=st.text_input("EMBARK Searching Over Fascinating Topic of Your Choice")

#   
llm1=OpenAI(temperature=0.8)
if(INPUT_TXT):
    st.write(llm1(INPUT_TXT))
    
prompt_first=st.write("enter input text below")
INPUT_TXT2=st.text_input("input your text here")

"""usually used to bujild custom prompt"""
"""here the input variable consists of LIST of KEYS(SUCHA S NAME, PLACE etc. TO) which would be used intemplate"""
llm2=PromptTemplate(
    input_variables=["name"],
    template="briefly describe about {names}}",

)

# If there is no env variable set for API key, you can pass the API key
# to the parameter `google_api_key` of the `ChatGoogleGenerativeAI` function:
# `google_api_key="key"`.
# st.subheader("GEMINI CHAIN _INITIATION")
# INPUT_TXT2=st.text_input("continue Searching Over Fascinating Topic of Your Choice")

# os.environ['GOOGLE_API_KEY'] = google_api_key
# llm2 = ChatGoogleGenerativeAI(model="gemini-pro",
#                  temperature=0.7, top_p=0.85)
# if(INPUT_TXT2):
  
#     st.write(llm2([INPUT_TXT2])) 
