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
    response = "file:///C:/Users/T0930368A/Downloads/2024_ApLMSPMS001_LOW+LI+WEN.pdf"
    st.image(response.content)
elif page == "Experiences":
  st.subheader("Welcome to the experiences page")
else:
  st.subheader("Welcome to the projects page")

