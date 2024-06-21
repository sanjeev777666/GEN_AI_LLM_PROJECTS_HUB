import os,sys
from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
from langchain_community.chat_models import ChatHuggingFace
# from langchain.chat_models import ChatOpenAI,ChatHuggingFace
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser,HumanMessage,SystemMessage,AIMessage
import streamlit as st
load_dotenv()
#************************************BUILD  MODEL************************************************************
llm3_HF = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",

    # task="text-generation",
    huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"] ,
    model_kwargs={
        "max_new_tokens": 512,
        # "top_k": 30,
        "temperature":0.8,
        # "repetition_penalty": 1.03,
    },
)
# *************************************CONSTRUCT CHAT MODEL BASED ON GIVEN LLM MODEL BUILT***********************************************************
chat_llm2_model=ChatHuggingFace(llm=llm3_HF)
print(chat_llm2_model.model_id)

# ******************************************RENDER PROMPT TEMPLATE******************************************************
template="Behave as Humorous AI sonnets generator assistant & construct a sonnets based on given word  in a comma seperated list"
human_template="{text1}"
chatprompt=ChatPromptTemplate.from_messages([
    ("system",template),
    ("human",human_template)


])
# **************************************EXECUTE CHAIN & streamlit simultaneously***********************************************************
st.title("Sonnet Surprise Studio Generator")
st.subheader("Enter a context word to generate Sonnets")
class Commaseperatedoutput(BaseOutputParser):
    def parse(self,text:str):
        return text.strip().split("\n")

chain1=chatprompt|chat_llm2_model|Commaseperatedoutput()
# chain1.invoke({"text1":"Furious"})
# context_word=input("context word of poem")
context_word=st.text_input("")
# chain1.invoke({"text1":context_word})
if st.button("Generate"):
    """NOTE:HERE TEXT1 ACTS A KEY WHIVH IS PASSED AS INPUT TO HUMAN TEMPLATE IN CHATPROMPT TEMPLATE"""
    poem=chain1.invoke({"text1":context_word})
    st.write(poem)

# ****************************************************************

