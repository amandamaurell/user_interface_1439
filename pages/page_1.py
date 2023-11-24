import requests
import streamlit as st

url = 'https://api.giphy.com/v1/gifs/random'

api_key = st.secrets.GIPHY.key

gif = st.text_input('Whi giphy would you like to see?', value='cat')

param = {'api_key':api_key, 'tag':gif}

response = requests.get(url, params=param).json()

response_gif = response['data']['embed_url']

st.write(f"<iframe src={response_gif}>", unsafe_allow_html=True)
