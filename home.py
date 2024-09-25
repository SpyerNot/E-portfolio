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
    st.image("C:\Users\T0930368A\AppData\Local\Temp\10b57a11-515d-4e87-a30e-0cc681aa0832_2024_ApLMSPMS001_LOW+LI+WEN.zip.832\1727158029439-6a41bfa3-70ed-4cec-a352-9aade17fc658_1.jpg")
elif page == "Experiences":
  st.subheader("Welcome to the experiences page")
else:
  st.subheader("Welcome to the projects page")

