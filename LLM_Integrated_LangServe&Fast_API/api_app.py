import sys,os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI,HuggingFaceHub,Ollama
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langserve import add_routes

from fastapi import FastAPI
import uvicorn


load_dotenv()
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.getenv("LANGCHAIN_API_KEY")


"""Construction of Prompts"""
prompt1=PromptTemplate(input_variables=["text1","text2" ],template="Provide a brief overview about{text1} in {text2} paragraphs")
prompt2=PromptTemplate(input_variables=["text1","text2"],template="<|user|>\Provide a brief overview about{text1} in {text2} paragraphs <|end|>\n<|assistant|>")
prompt3=PromptTemplate(input_variables=["text1","text2"],template="Provide a brief overview about{text1} in {text2}  paragraphs") 

"""build models"""
llm1=Ollama(model="llama3:latest")
llm2=HuggingFaceHub(repo_id="microsoft/Phi-3-mini-4k-instruct",huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")   , model_kwargs={"temperature":0.2,"max_new_tokens":1024})
llm3=Ollama(model="mistral:latest")

"""a. execute using llmchains"""
llm1_chain=LLMChain(llm=llm1,prompt=prompt1)
llm2_chain=LLMChain(llm=llm2,prompt=prompt2)
llm3_chain=LLMChain(llm=llm3,prompt=prompt3)

"""b. execute using Chain operator on 'CHATPROMPTTEMPLATE where chatpromptemplates for above 3 models are as follows'"""
# *****DOESNT WORK FOR INVOKKE OR FIND AN ALTERNTAIVE SINCE IT DOESNT EXTRACT THE KEY TEXT1 FROM FRONT ENED*******chatprompt1=ChatPromptTemplate.from_messages([SystemMessage(content="Behave as a Ai assistant to answer."),HumanMessage(content="Provide a brief overview about {text1} in 1 paragraphs")])

chatprompt1=ChatPromptTemplate.from_messages([("human","Provide a brief overview about {text1} in {text2}  paragraphs "),SystemMessage(content="Behave as Ai Assistant to answer.")])
chatprompt2=ChatPromptTemplate.from_messages([("human","<|user|>\Provide a brief overview about {text1} in {text2}  paragraphs <|end|>\n"),
                                             ("system","<|assistant|>")])

chatprompt3=ChatPromptTemplate.from_template("Provide a brief overview about{text1} in {text2}  paragraphs")

"""building AN API USING FAST API  """
app= FastAPI(
    title="Building LLM Apis through LangServe",
    description="A Rudimentary API for LangChain",
    version="1.0.0"
  )
"""adding routes via LANGSERVE TO LLM MODELS"""
add_routes(
    app,
    llm1_chain,
    path="/model1")

add_routes(
    app,
    llm2_chain,
    path="/model2")

add_routes(
    app,
    llm3_chain,
    path="/model3")


add_routes(
   app,
   chatprompt1 | llm1 ,
   path="/chat_model1"
    )

add_routes(
    app,
    chatprompt2 | llm2 ,
    path="/chat_model2"
    )

add_routes(
    app,
    chatprompt3 | llm3 ,
    path="/chat_model3"
    )
    
if __name__ =="__main__":
    uvicorn.run(app,host="localhost",port=8080)


