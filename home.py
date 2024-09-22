import streamlit as st

st.title("Low Li Wen's E-portfolio")
pg = st.navigaton([st.Page("about_me.py",title="Info about me"),st.Page("achievements.py",title="All my achievements in one place :D"),st.Page("experiences.py",title="My different experiences"),st.Page("projects.py",title="My coding projects")])
