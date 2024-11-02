import streamlit as st
from langchain.llms import OpenAI



st.title('En såndär LLM Chatbot')
st.caption("...som använder OpenAI")


col1, col2 = st.columns([1,2])
with col1:
    openai_api_key = st.text_area('OpenAI API-nyckel')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))
with col2:
    with st.form('my_form', border=False):
        text = st.text_area('Skriv text:', placeholder='T.ex. Varför är himlen blå?')
        submitted = st.form_submit_button('Skicka')
        try:
            generate_response(text)
        except Exception as e:
            st.warning("Jaadu nåt gick fel här, checka OpenAI-nyckel...!")


"---"
st.caption("Gjord av Gabriel 🏖️")