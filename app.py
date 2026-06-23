import streamlit as st

st.set_page_config(
    page_title="SIDBI MSME Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #050B18 0%, #071326 45%, #090B1F 100%);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #061A35 0%, #031025 100%);
}

[data-testid="stSidebar"] * {
    color: white;
}

.main-title {
    font-size: 34px;
    font-weight: 800;
    color: #ffffff;
}

.sub-title {
    font-size: 17px;
    color: #B8C4D6;
    margin-bottom: 25px;
}

.metric-card {
    padding: 28px;
    border-radius: 18px;
    color: white;
    min-height: 180px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.35);
}

.blue-card {
    background: linear-gradient(135deg, #005BEA, #001E72);
}

.green-card {
    background: linear-gradient(135deg, #00B875, #006B58);
}

.purple-card {
    background: linear-gradient(135deg, #7B2FF7, #2C0B59);
}

.orange-card {
    background: linear-gradient(135deg, #FF8C00, #A33D00);
}

.metric-title {
    font-size: 18px;
    font-weight: 700;
}

.metric-value {
    font-size: 27px;
    font-weight: 800;
    margin-top: 12px;
}

.metric-growth {
    font-size: 22px;
    color: #77FF9B;
    font-weight: 700;
    margin-top: 20px;
}

.panel {
    background: rgba(7, 25, 55, 0.75);
    border: 1px solid rgba(0, 150, 255, 0.6);
    border-radius: 18px;
    padding: 28px;
    min-height: 330px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.28);
}

.panel-purple {
    background: rgba(24, 10, 55, 0.78);
    border: 1px solid rgba(145, 70, 255, 0.7);
    border-radius: 18px;
    padding: 28px;
    min-height: 330px;
}

.panel-title {
    font-size: 25px;
    font-weight: 800;
    color: white;
    margin-bottom: 20px;
}

.info-box {
    border: 1px solid #007BFF;
    background: rgba(0, 60, 130, 0.28);
    padding: 24px;
    border-radius: 15px;
    font-size: 17px;
    line-height: 1.7;
    color: #EAF2FF;
}

.insight {
    padding: 13px 0;
    border-bottom: 1px solid rgba(255,255,255,0.14);
    font-size: 16px;
    color: #F2F5FA;
}

.small-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(100,180,255,0.35);
    padding: 18px;
    border-radius: 14px;
    text-align: center;
}

.small-num {
    font-size: 25px;
    font-weight: 800;
    color: white;
}

.footer {
    margin-top: 28px;
    padding: 24px;
    background: rgba(0, 45, 95, 0.55);
    border-radius: 14px;
    font-size: 20px;
    font-weight: 700;
    color: #00D9FF;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 📊 SIDBI Dashboard")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
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

st.markdown('<div class="main-title">Impact of SIDBI Credit Schemes on MSME Growth in India</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Interactive dashboard for SIDBI financial performance and MSME ecosystem growth, 2010–2025.</div>', unsafe_allow_html=True)
st.markdown("---")

if page == "Home":

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card blue-card">
            <div class="metric-title">₹ SIDBI Credit</div>
            <div class="metric-value">₹4.96 Lakh Cr</div>
            <div class="metric-growth">↑ +1207%</div>
            <div>Growth (2010–2025)</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card green-card">
            <div class="metric-title">🏦 Total Assets</div>
            <div class="metric-value">₹5.68 Lakh Cr</div>
            <div class="metric-growth">↑ +993%</div>
            <div>Growth (2010–2025)</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card purple-card">
            <div class="metric-title">📈 Net Profit</div>
            <div class="metric-value">₹4,811 Cr</div>
            <div class="metric-growth">↑ +1043%</div>
            <div>Growth (2010–2025)</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card orange-card">
            <div class="metric-title">👥 MSME Registrations</div>
            <div class="metric-value">650 Lakh</div>
            <div class="metric-growth">↑ +2500%</div>
            <div>Growth (2010–2025)</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    left, right = st.columns([1, 1])

    with left:
        st.markdown("""
        <div class="panel">
            <div class="panel-title">📊 Dashboard Overview</div>
            <div class="info-box">
                This dashboard analyzes SIDBI credit trends, asset growth, profitability,
                MSME registrations, employment, GDP contribution, state-wise performance,
                sector-wise allocation and correlation insights.
            </div>
            <br>
            <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap:15px;">
                <div class="small-card"><div class="small-num">16+</div><div>Key Indicators</div></div>
                <div class="small-card"><div class="small-num">15</div><div>Years Data</div></div>
                <div class="small-card"><div class="small-num">36</div><div>States/UTs</div></div>
                <div class="small-card"><div class="small-num">3</div><div>Major Sectors</div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="panel-purple">
            <div class="panel-title">💡 Key Insights</div>
            <div class="insight">✅ SIDBI credit has grown by over 1207% from 2010 to 2025.</div>
            <div class="insight">✅ Total assets increased by 993%, reflecting strong financial expansion.</div>
            <div class="insight">✅ MSME registrations surged by 2500%, strengthening the entrepreneurial ecosystem.</div>
            <div class="insight">✅ Strong positive correlation exists between SIDBI financing and MSME growth indicators.</div>
            <div class="insight">✅ Top 3–4 schemes contribute around 70–80% of total credit disbursement.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        ⭐ Empowering MSMEs. Building India. Supporting Entrepreneurship.
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown(f"## {page}")
    st.info("This section will contain charts, tables and insights.")
