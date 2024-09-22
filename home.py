import streamlit as st
st.title("Low Li Wen's E-portfolio")
pg = st.navigation([st.Page("pages/about_me.py"),st.Page("pages/achievements.py"),st.Page("pages/experiences.py"),st.Page("pages/projects.py")])
pg.run()
