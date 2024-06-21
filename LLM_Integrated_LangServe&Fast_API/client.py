import requests
import streamlit as st
# # ***********************************pertained to Promptemplates option A********************************************************************
def getLLm1Response(input_text1, input_text2):
    response=requests.post(url="http://localhost:8080/model1/invoke",json={'input':{'text1':input_text1, 'text2':input_text2}})
    st.write("********",response.text)
    return response.json()

def getLLm2Response(input_text1, input_text2):
    response=requests.post(url="http://localhost:8080/model2/invoke",json={"input":{"text1":input_text1 ,'text2':input_text2}})
    return response.json()

def getLLm3Response(input_text1, input_text2):
    response=requests.post(url="http://localhost:8080/model3/invoke",json={"input":{"text1":input_text1, 'text2':input_text2}})
    return response.json()
# ********************************************************************************************************************************************

# ***********************************pertained to CHATPROMPTTEMPLATE option B********************************************************************
def getchatLLm1Response(input_text1, input_text2):
    response=requests.post(url="http://localhost:8080/chat_model1/invoke",json={'input':{"text1":input_text1, 'text2':input_text2}})
    return response.json()

def getchatLLm2Response(input_text1, input_text2):
    response=requests.post(url="http://localhost:8080/chat_model2/invoke",json={"input":{"text1":input_text1, 'text2':input_text2}})
    return response.json()

def getchatLLm3Response(input_text1, input_text2):
    response=requests.post(url="http://localhost:8080/chat_model3/invoke",json={"input":{"text1":input_text1, 'text2':input_text2}})
    return response.json()
# ********************************************************************************************************************************************
st.title("COnversation App interacting with LangServe")
input1,input12=st.text_input("Enter your input text to LLama"),st.text_input("Enter your input para to LLama")
input2,input22=st.text_input("Enter your input text to HuggingFace"),st.text_input("Enter your input para to HuggingFace")
input3,input32=st.text_input("Enter your input text to mistral"),st.text_input("Enter your input para to mistral")


input1_chat,input12_chat=st.text_input("Enter your input text to LLama --chatPrompt version"),st.text_input("Enter Para count text to LLama --chatPrompt version")
input2_chat,input22_chat=st.text_input("Enter your input text to HuggingFace --chatPrompt version"),st.text_input("Enter para Count  to HuggingFace --chatPrompt version")
input3_chat,input32_chat=st.text_input("Enter your input text to mistral--chatPrompt version"),st.text_input("Enter Para count to mistral--chatPrompt version")

submit=st.button("Get Response")


# ************************************************************************************************
if(input1 and submit):
    st.write(getLLm1Response(input1,input12))

elif(input2 and submit):
    st.write(getLLm2Response(input2,input22))

elif(input3 and submit):
    st.write(getLLm3Response(input3,input32))
    
elif(input1_chat and input12_chat and submit):
    st.write(getchatLLm1Response(input1_chat,input12_chat))

elif(input2_chat and input22_chat and submit):
    st.write(getchatLLm2Response(input2_chat,input22_chat))

elif(input3_chat and input32_chat and submit):
    st.write(getchatLLm3Response(input3_chat,input32_chat))
#*************************************************************************************************
