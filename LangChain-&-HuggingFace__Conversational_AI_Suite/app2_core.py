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

# **********************************************PROMPT TEMPLATE FUNCTION(opTION-SPECIFIC)******************************************************
def generate_conversational_response(selected_option,AI_assistant_role):
    # template=f'Behave as Humorous AI generator assistant & construct a {option_based_template} based on given context word in a comma seperated list'
    template=AI_assistant_role
    human_template="{text1}"
    chatprompt=ChatPromptTemplate.from_messages([
        ("system",template),
        ("human",human_template)


    ])
    # **************************************EXECUTE CHAIN & streamlit simultaneously***********************************************************
    st.subheader(selected_option)
    # st.subheader("Enter a context word to generate Sonnets")
    class Commaseperatedoutput(BaseOutputParser):
        def parse(self,text:str):
            return text.strip().split("\n")

    chain1=chatprompt|chat_llm2_model|Commaseperatedoutput()
    # chain1.invoke({"text1":"Furious"})
    # context_word=input("context word of poem")
    context_word=st.text_input(F"Enter a context word for {selected_option} below:-",)
    # chain1.invoke({"text1":context_word})
    if st.button("result"):
        output=chain1.invoke({"text1":context_word})
        return output
        # st.write(output)

# """**************************************************DEVICING CUSTOM PROMPT TEMPLATE (opTION-SPECIFIC)***********************************************************************"""
st.title("LLM POWERED AI TRIO")

# Radio button selection for functionality
selected_option = st.radio("Choose an AI experience:", ("Wordplay Wizard AI", "Sonnet Generator","Q/A chatbot"))
if (selected_option == "Q/A chatbot"):
    # Q/A System
    # st.write(" Describe any additional parameter to constraint AI assistant to answer the question")
    constraints = st.text_input("Describe any additional parameter to constraint AI assistant to answer the question")
    # if st.button("Generate"):
    AI_assistant_role=f"Play the role of Q/A Chat assistant take into account of {constraints} provided by user"
    answer = generate_conversational_response(selected_option,AI_assistant_role)
    st.write(answer)
elif(selected_option == "Wordplay Wizard AI"):
    # Conversational AI
    # st.subheader("Enter a message to get a response")
    # user_input = st.text_input("Enter a message")
    # st.write(" Describe any additional parameter to constraint AI assistant in generating riddles")
    constraints = st.text_input("Describe any additional parameter to constraint AI assistant to generate riddles")
    # if st.button("Generate"):
    AI_assistant_role=f"Play the role of Riddle AI assistant generator take into account of {constraints} provided by user"
    # if st.button("Generate"):
    response = generate_conversational_response(selected_option,AI_assistant_role)
    st.write(response)
elif(selected_option == "Sonnet Generator"):
    # Sonnet Generator
    # st.write(" Describe any additional parameter to constraint AI assistant in generating sonnets")
    constraints = st.text_input("Describe any additional parameter to constraint AI assistant in generating sonnets")
    # if st.button("Generate"):
    AI_assistant_role=f"Play the role of humorous Sonnet generator AI assistant take into account of {constraints} provided by user"
    # st.subheader("Enter a context word to generate Sonnets")
    # context_word = st.text_input("Enter a context word")
    # if st.button("Generate"):
    sonnet = generate_conversational_response(selected_option,AI_assistant_role)
    st.write(sonnet)

