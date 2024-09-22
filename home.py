import streamlit as st
import requests
st.title("Low Li Wen's E-portfolio")
st.sidebar.title("Sidebar")
page = st.sidebar.radio("Go to", ["About me","Achievements","Experiences","Projects"])
if page == "About me":
  st.subheader("Welcome to the about me page")
elif page == "Achievements":
  st.subheader("Welcome to the achievements page")
  col1, col2, col3 = st.columns(3)
  with col1:
    file_id = "1w_-hWtGOEDcUNGMx70Mot8E3eolxe9zW"
    url = f"https://drive.google.com/uc?export=view&id={file_id}"
    response = requests.get(url)
    st.image(response.content)
elif page == "Experiences":
  st.subheader("Welcome to the experiences page")
else:
  st.subheader("Welcome to the projects page")

