import os
import sys  
from constants import openai_api_key,google_api_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain   
from langchain.chains import SimpleSequentialChain,SequentialChain
from langchain.memory import ConversationBufferMemory
# from langchain_google_genai import ChatGoogleGenerativeAI 
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_api_key

st.title("DISTINGUISHED_AUTHOR_SEARCH_ENGINE")
DISTINGUISHED_AUTHOR_name_input=st.text_input("EMBARK ON RENDERING NAME OF YOUR DISTINGUISHED_AUTHOR")


llm_used=OpenAI(temperature=0.8)

"""***********************MEMORY********************************"""
person_memory = ConversationBufferMemory(input_key='DISTINGUISHED_AUTHOR_name_input', memory_key='chat_history')
indegene_memory = ConversationBufferMemory(input_key='celebrity_name_output_as_person_name_below', memory_key='chat_history')
achievemnt_memory = ConversationBufferMemory(input_key='indegene_output_as_nativity', memory_key='description_history')
"""*************************************************************"""


"""***********************PROMPT-1********************************"""
"""******usually used to CONSTRUCT custom prompt\-
here the input variable consists of **LIST OF KEYS**(SUCHA S NAME, PLACE etc. TO) which would be used intemplate****"""
prompt_1=PromptTemplate(
    input_variables=["DISTINGUISHED_AUTHOR_name_input"],
    template="briefly describe about {DISTINGUISHED_AUTHOR_name_input}",
)
llm_chain1=LLMChain(llm=llm_used,prompt=prompt_1,verbose=True,output_key="celebrity_name_output_as_person_name_below",memory=person_memory)
"""*******************************************************"""

"""*************************PROMPT-2******************************"""
prompt_2=PromptTemplate(
    input_variables=["celebrity_name_output_as_person_name_below"],
    template="Render Indigene of {celebrity_name_output_as_person_name_below}",
)
llm_chain2=LLMChain(llm=llm_used,prompt=prompt_2,verbose=True,output_key="indegene_output_as_nativity",memory=indegene_memory)
"""*******************************************************"""


"""**********************PROMPT-3*********************************"""
prompt_3=PromptTemplate(
    input_variables=["indegene_output_as_nativity"],
    template="Render most recent achievemnt of  {indegene_output_as_nativity}",
)
llm_chain3=LLMChain(llm=llm_used,prompt=prompt_2,verbose=True,output_key="nativity_output_as_achievement",memory=achievemnt_memory)
"""*******************************************************"""


"""***********************CONSOLIDATED_PROMPT-CHAINS(BOTH SEQUENTIAL & SIMPLESEQUENTIAL)********************************"""
"""A. Though it retains prior context , it renders output for the Most recent prompt from the chain( here  indigene ) as resultant output"""
Consolidated_Prompt_A=SimpleSequentialChain(chains=[llm_chain1,llm_chain2,llm_chain3],verbose=True)

""" B. To return complete resultant output from beginning--addtionally provide input_variables and output_variables """
Consolidated_Prompt_B=SequentialChain(chains=[llm_chain1,llm_chain2,llm_chain3],input_variables=["DISTINGUISHED_AUTHOR_name_input"],output_variables=["celebrity_name_output_as_person_name_below","indegene_output_as_nativity","nativity_output_as_achievement"], verbose=True)
"""*******************************************************"""

"""******************if name provided by the user************************************************"""
if(DISTINGUISHED_AUTHOR_name_input):
    
    st.subheader("Consolidated prompt_A output")
    try:
        st.write(Consolidated_Prompt_A.run(DISTINGUISHED_AUTHOR_name_input))
        
    except:
        st.write("Sorry, I'm Unable to render the output of consolidate_prompt_B the celebrity name provided by you due to GPT Memory Exceed")
    
    st.subheader("Consolidated prompt_B output")
    
    try:
        st.write(Consolidated_Prompt_B.run(DISTINGUISHED_AUTHOR_name_input))
        with st.expander('Person ouput Name'): 
            st.info(person_memory.buffer)

        with st.expander('Indigene output Memory'): 
            st.info(indegene_memory.buffer)
        
        with st.expander('Achievement output Memory'): 
            st.info(achievemnt_memory.buffer)
            
    except:
        st.write("Sorry, I'm Unable to render the output of consolidate_prompt_B the celebrity name provided by you due to GPT Memory Exceed")

else:
    st.header(r"\**DISTINGUISHED_AUTHOR Name not provided**")
"""*****************************THE END***********************************************************"""

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
