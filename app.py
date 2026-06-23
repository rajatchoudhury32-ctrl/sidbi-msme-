import streamlit as st

st.set_page_config(
    page_title="SIDBI MSME Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.big-title {
    font-size: 40px;
    font-weight: 800;
    color: #0B1F3A;
}
.sub-title {
    font-size: 18px;
    color: #6c757d;
}
.card {
    background: white;
    padding: 22px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.12);
    text-align: center;
}
.card h3 {
    font-size: 18px;
    color: #0B1F3A;
}
.card p {
    font-size: 25px;
    font-weight: 700;
    color: #005BAC;
}
.insight-box {
    background: #EEF5FF;
    padding: 18px;
    border-left: 6px solid #005BAC;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 📊 SIDBI Dashboard")

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

if page == "Home":
    st.markdown('<div class="big-title">Impact of SIDBI Credit Schemes on MSME Growth in India</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Interactive dashboard for SIDBI financial performance and MSME ecosystem growth, 2010–2025.</div>', unsafe_allow_html=True)

    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="card"><h3>SIDBI Credit</h3><p>₹4.96 Lakh Cr</p><span>+1207%</span></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>Total Assets</h3><p>₹5.68 Lakh Cr</p><span>+993%</span></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><h3>Net Profit</h3><p>₹4,811 Cr</p><span>+1043%</span></div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card"><h3>MSME Registrations</h3><p>650 Lakh</p><span>+2500%</span></div>', unsafe_allow_html=True)

    st.write("")
    st.markdown("### Dashboard Overview")

    st.markdown("""
    <div class="insight-box">
    This dashboard analyzes SIDBI credit trends, asset growth, profitability, MSME registrations,
    employment, GDP contribution, state-wise performance, sector-wise allocation and correlation insights.
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown(f"## {page}")
    st.info("This section will contain charts, tables and insights.")
