import streamlit as st
st.title("Low Li Wen's E-portfolio")
st.sidebar.title("Sidebar")
page = st.sidebar.radio("Go to", ["About me","Achievements","Experiences","Projects"])
if page == "About me":
  st.subheader("Welcome to the \"about me"\ page")
elif page == "Achievements":
  st.subheader("Welcome to the \"achievements"\ page")
elif page == "Experiences":
  st.subheader("Welcome to the \"experiences"\ page")
else:
  st.subheader("Welcome to the \"projects"\ page")

