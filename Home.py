import hashlib
import streamlit as st
import requests
import json

# Streamlit interface
st.title('Intent Classification and evaluation')

collection_name = st.text_input('Enter vector db collection name (optional):', value='test')
user_query = st.text_input('Enter user query (mandatory):', value='', max_chars=50, key=None, type='default')
api_key = st.text_input('Enter OpenAI-API key:', type='password')

# Hash the API key
hashed_key = hashlib.sha256(api_key.encode()).hexdigest()

def get_intents(hashed_key, collection_name, user_query):
    url = "https://fastapi-getting-started.onrender.com/predict"
    data = {"api_key": hashed_key, "collection_name": collection_name, "user_query": user_query}
    response = requests.post(url, data=json.dumps(data))
    return response  # return the entire response object

if st.button('Predict'):
    if not user_query:
        st.error('Please enter user query.')
    elif not api_key:
        st.error('Please enter API key.')
    else:
        response = get_intents(hashed_key, collection_name, user_query)
        if response.status_code == 200:  # OK
            intents = response.json()  # get the JSON content from the response
            st.text_area('Response:', value='\n'.join(intents['intents']), height=200)
        elif response.status_code == 500:  # Internal Server Error
            st.text_area('Response:', value='Internal server error. Please try again later.', height=200)
        else:  # Other errors
            st.text_area('Response:', value=f'Error: {response.status_code}. Please try again later.', height=200)