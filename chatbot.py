import google.generativeai as genai
import PIL.Image as Image
import streamlit as st
import google.ai.generativelanguage as glm


genai.configure(api_key='AIzaSyCQaNXncOCEH4SAO0KCkN1xESzZbI7hqFY')
model = genai.GenerativeModel('gemini-pro')
model1 = genai.GenerativeModel('gemini-pro-vision')

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
st.title("Chat with AI")

def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        

if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt,stream=True)
    response.resolve()
    with st.chat_message("assistant"):
        st.markdown(response.text)

#                 )
#             ),
#         ],
#     ),
#     stream=True)
