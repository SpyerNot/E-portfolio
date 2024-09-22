import streamlit as st
st.title("Low Li Wen's E-portfolio")
st.sidebar.title("Sidebar")
page = st.sidebar.radio("Go to", ["About me","Achievements","Experiences","Projects"])
if page == "About me":
  st.subheader("Welcome to the about me page")
elif page == "Achievements":
  st.subheader("Welcome to the achievements page")
  col1, col2, col3 = st.columns(3)
  with col1:
    st.image("https://drive.google.com/file/d/1w_-hWtGOEDcUNGMx70Mot8E3eolxe9zW/view?usp=sharing")
  with col2:
elif page == "Experiences":
  st.subheader("Welcome to the experiences page")
else:
  st.subheader("Welcome to the projects page")

