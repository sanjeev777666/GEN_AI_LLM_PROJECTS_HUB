import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI, HuggingFaceHub, CTransformers,Ollama
# """GGML Library: |||||AR TO SCI-KIT LEARN OR SKLEARN THAT OFFERS VARIOUS CONVENTIONAL ml MODELS TO BE EMPLOYED OVER THE DATASETS
# GGML (General Gradient Matrix Library) is a high-performance library for training and deploying various machine learning models, including Transformers.
# It leverages optimizations and techniques to achieve efficient training and inference on various hardware platforms.
# CTransformers Library:

# CTransformers bridges the gap between LangChain and GGML models.
# It provides Python bindings, essentially acting as a translator, allowing you to use GGML-trained Transformer models within your LangChain workflows.
# This enables you to leverage the benefits of both LangChain's modular pipeline structure and the efficiency of GGML-trained Transformers for your NLP tasks.
# """
def generateLLAMA_RESPONSE(input_text2,word_count2,user_type2):
    # """Construct model"""
    # ************or using ctransformer********************
    # LLM1=CTransformers(model_name="path with .bin extension only",model_type="LLAMA-2-7B",config={"max_new_tokens":1024,"temperature":0.01})
    # *********************************
    llm1=Ollama(model="llama2")
    # """Construct prompt"""
    template_specific_usecase=f"Generate blog on the topic{input_text2} with total_word count of {word_count2} towards {user_type2}"
    prompt1=PromptTemplate(input_variables=["input_text2","word_count2","user_type2"],template=template_specific_usecase)
    # **********or using chaining from single input**********************
    # chain=llm1|prompt1
    # x=chain.invoke( {"question":input_text1})
    # ********************************
    # st.write(type(prompt1),prompt1)
    
    x=llm1(prompt1.format(input_text2=input_text2,word_count2=word_count2,user_type2=user_type2))
    print(x)
    return x
original_title = '<p style="font-family:Jokerman; color: White; font-size: 35px;"><b>Blog Generation using LlAMA-2 </b></p>'
st.markdown(original_title, unsafe_allow_html=True)
# st.header("Blog Generation using LlAMA-2")

input_text = st.text_input("Enter your input text to generate blog On-:")

colmn1,colmn2=st.columns([10,5])

with colmn1:
    word_count=st.text_input("Enter word_count")
with colmn2:
    user_type=st.selectbox("Enter word_count to",("Researchers","Data Scientists","Engineers"))
output=st.button("Generate Blog")
if(output):
    st.write(generateLLAMA_RESPONSE(input_text,word_count,user_type))