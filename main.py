import streamlit as st

st.title('Ai Web Scraper')
url = st.text_input('Enter the URL : ')

if st.button("Scrap Site"):
    st.write('Scraping the Site')