import streamlit as st

st.title("SIM STUDY PLANNING APP")

option_school = st.selectbox(
    "Your school",
    ("UOL", "UOW", "RMIT"),
    key="school"
)


option_degree = st.selectbox(
    "Your degree",
    ("Computer Science", "Business Management", "Data Science", "Finance"),
    key="degree"
)


option_year = st.selectbox(
    "Your year",
    ("Year 1", "Year 2", "Year 3", "Pre-U"),
    key="year"
)

if st.button("Generate Plan!"):
    st.markdown("*Streamlit* is **really** ***cool***.")
