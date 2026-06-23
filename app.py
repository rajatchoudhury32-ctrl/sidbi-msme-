import streamlit as st

st.set_page_config(
    page_title="SIDBI MSME Dashboard",
    layout="wide"
)

st.title("Impact of SIDBI Credit Schemes on MSME Growth in India")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Section",
    [
        "Home",
        "SIDBI Financial Trends",
        "MSME Growth Indicators",
        "Growth Analysis",
        "Correlation Heatmap",
        "Scheme Analysis",
        "State-wise Analysis",
        "Sector-wise Analysis",
        "Conclusion"
    ]
)

st.write("Selected Page:", page)
