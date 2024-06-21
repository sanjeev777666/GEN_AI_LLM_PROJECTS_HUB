import sys,os
import streamlit as st

from langchain.schema import HumanMessage,AIMessage,SystemMessage
from langchain_community.llms import HuggingFaceHub
from langchain_community.chat_models import ChatHuggingFace,ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
# """INTUITIVE CONVERSATION SYSTEM INCLUSIVE OF HUMAN FEEDBACK"""
# """NOTE: CLEAR CACHE AS & WHEN REQUIRED"""
# """Rudimentary streamlit app"""
original_title = '<p style="font-family:Courier; color: White; font-size: 35px;"><b>Human F/b aided CONVERSATIONAL SYSTEM </b></p>'
st.markdown(original_title, unsafe_allow_html=True)
# st.title(" ",)
st.subheader("Hey , How can I Assist You today?")

# """Model building"""
llm3_hf=HuggingFaceHub(repo_id="HuggingFaceH4/zephyr-7b-beta",huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),model_kwargs={"temperature":0.7,"max_new_tokens":1024})
# """chatmodel building"""
chat_llm2_model=ChatHuggingFace(llm=llm3_hf)

# """prompt template format"""
system_template="Behave as an AI assistant & answer in cohesive fashion"
Human_template=st.text_input("Embark on Conversational Journey")
# print(type(Human_template))
chat_prompt1=ChatPromptTemplate.from_messages(messages=[
    SystemMessage(content=system_template),
    HumanMessage(content=Human_template),
])
# print("*************************",chat_prompt1,HumanMessage(content=Human_template))

# """" To build Cohesive response retaining/preserving context of prior conversation by the USER Construct SESSION #-MAP STORE |||AR TO HASHMAP"""
# """initalization of session state appending bootstrap messages from system & human"""
if "key" not in st.session_state:
    st.session_state[ "key"]= [SystemMessage(content=system_template)]
def generate_conversational_response(Human_template):

    st.session_state["key"].append(HumanMessage(content=Human_template))
    st.write("CHECK",st.session_state["key"])
    answer=chat_llm2_model(st.session_state["key"])
    
    st.write("View answerrrrrrrrrr",answer,"\n"," ANSWER TYPE& CLASS ENTAILED IN",type(answer))
    st.session_state["key"].append(AIMessage(content=answer.content))
    # st.write("ANSWER",answer,st.session_state["key"])
    return answer.content

x=st.button("click")
if(x):
    st.subheader("Here is your response")
    st.write("*************111111************",chat_prompt1,HumanMessage(content=Human_template))
    st.write(generate_conversational_response(Human_template))