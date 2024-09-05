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


# uploaded_file = st.file_uploader("Upload a pdf, docx, or txt file",
#                                 type=['png', 'jpg', 'jpeg', "pdf", "docx", "txt"])

# if uploaded_file is not None:
#     uploaded_file = Image.open(uploaded_file)
#     model1 = genai.GenerativeModel('gemini-pro-vision')
#     response = model1.generate_content(["Generate the output for the image",uploaded_file],stream=True)
#     response.resolve()
#     st.markdown(response.text)
#     st.write(response.text)

if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt,stream=True)
    response.resolve()
    with st.chat_message("assistant"):
        st.markdown(response.text)



# model = genai.GenerativeModel('gemini-pro-vision')
# response = model.generate_content(
#     glm.Content(
#         parts = [
#             glm.Part(text="Write a short, engaging blog post based on this picture."),
#             glm.Part(
#                 inline_data=glm.Blob(
#                     mime_type='image/jpeg',
#                     data=pathlib.Path('image.jpg').read_bytes()
#                 )
#             ),
#         ],
#     ),
#     stream=True)