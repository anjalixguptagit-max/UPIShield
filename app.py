import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="UPIShield | Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #080d18;
    color: #f5f7fb;
}

/* Main container */
.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0d1424;
    border-right: 1px solid #1d2940;
}

section[data-testid="stSidebar"] * {
    color: #dce5f5;
}

/* Header */
.hero {
    padding: 10px 0 25px 0;
}

.logo {
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 2px;
    color: #7dd3fc;
    text-transform: uppercase;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    margin: 8px 0 5px 0;
    letter-spacing: -2px;
}

.hero-subtitle {
    color: #8fa2bd;
    font-size: 16px;
}

/* Cards */
.card {
    background: #101827;
    border: 1px solid #1e2b42;
    border-radius: 18px;
    padding: 24px;
    margin-bottom: 18px;
}

.card-title {
    font-size: 14px;
    font-weight: 700;
    color: #8fa2bd;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 15px;
}

/* Metrics */
.metric-card {
    background: linear-gradient(145deg, #111c2e, #0d1523);
    border: 1px solid #22314b;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
}

.metric-label {
    color: #8fa2bd;
    font-size: 13px;
}

.metric-value {
    font-size: 28px;
    font-weight: 800;
    margin-top: 5px;
}

/* Risk result */
.risk-card {
    background: linear-gradient(145deg, #111c2e, #0b1321);
    border: 1px solid #263854;
    border-radius: 20px;
    padding: 28px;
    text-align: center;
}

.risk-label {
    color: #8fa2bd;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.risk-score {
    font-size: 58px;
    font-weight: 800;
    margin: 5px 0;
}

.risk-low {
    color: #4ade80;
}

.risk-medium {
    color: #fbbf24;
}

.risk-high {
    color: #fb7185;
}

.risk-category {
    font-size: 20px;
    font-weight: 700;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 48px;
    font-weight: 700;
    border: 1px solid #334766;
    background: #17243a;
    color: white;
    transition: 0.2s;
}

.stButton > button:hover {
    border-color: #7dd3fc;
    background: #1b2d48;
}

/* Inputs */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    background-color: #111a2a;
    border-color: #263852;
    border-radius: 10px;
}

label {
    color: #b7c5d9 !important;
}

/* Divider */
hr {
    border-color: #1d2940;
}

/* Footer */
.footer {
    text-align: center;
    color: #61738d;
    font-size: 12px;
    padding-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        "<div style='font-size:28px;font-weight:800;'>🛡️ UPIShield</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='color:#7dd3fc;'>Fraud Intelligence System</p>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### SYSTEM")

    st.success("● Detection Engine Online")

    st.markdown("""
    **India Transaction Monitor**

    Analyzes transaction-level risk indicators and generates a simple risk assessment.
    """)

    st.divider()

    st.caption("UPIShield v1.0")
    st.caption("Hackathon Prototype")

# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

<div class="logo">INDIA DIGITAL PAYMENTS • SECURITY</div>

<div class="hero-title">
UPIShield
</div>

<div class="hero-subtitle">
India-Specific Digital Transaction Fraud Risk Analysis System
</div>

</div>
""", unsafe_allow_html=True)

# =========================================================
# TOP METRICS
# =========================================================

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-label">TRANSACTIONS</div>
    <div class="metric-value">250K</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-label">FRAUD CASES</div>
    <div class="metric-value">480</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-label">FRAUD RATE</div>
    <div class="metric-value">0.192%</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-label">STATES COVERED</div>
    <div class="metric-value">10</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# MAIN SECTION
# =========================================================

left, right = st.columns([1.05, 0.95])

# =========================================================
# INPUT PANEL
# =========================================================

with left:

    st.markdown("""
    <div class="card">
    <div class="card-title">Transaction Analysis</div>
    """, unsafe_allow_html=True)

    amount = st.number_input(
        "Transaction Amount (₹)",
        min_value=1,
        max_value=1000000,
        value=500
    )

    hour = st.slider(
        "Transaction Hour",
        min_value=0,
        max_value=23,
        value=14
    )

    device = st.selectbox(
        "Device Type",
        ["Android", "iOS", "Web"]
    )

    network = st.selectbox(
        "Network Type",
        ["3G", "4G", "5G", "WiFi"]
    )

    transaction_type = st.selectbox(
        "Transaction Type",
        ["P2P", "P2M", "Bill Payment", "Recharge"]
    )

    weekend = st.selectbox(
        "Weekend Transaction?",
        ["No", "Yes"]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    analyze = st.button(
        "🔍  ANALYZE TRANSACTION"
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# RESULT PANEL
# =========================================================

with right:

    st.markdown("""
    <div class="card">
    <div class="card-title">Risk Assessment</div>
    """, unsafe_allow_html=True)

    if analyze:

        score = 0
        reasons = []

        if amount > 5000:
            score += 2
            reasons.append("High transaction amount")

        if hour in [0, 1, 2, 3, 4, 23]:
            score += 2
            reasons.append("Late-night transaction")

        if device == "Web":
            score += 1
            reasons.append("Web-based transaction")

        if network == "WiFi":
            score += 1
            reasons.append("WiFi network")

        if weekend == "Yes":
            score += 1
            reasons.append("Weekend activity")

        if score >= 4:
            category = "HIGH RISK"
            risk_class = "risk-high"

        elif score >= 2:
            category = "MEDIUM RISK"
            risk_class = "risk-medium"

        else:
            category = "LOW RISK"
            risk_class = "risk-low"

        st.markdown(f"""
        <div class="risk-card">

        <div class="risk-label">
        TRANSACTION RISK SCORE
        </div>

        <div class="risk-score {risk_class}">
        {score}
        </div>

        <div class="risk-category {risk_class}">
        {category}
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("**Detected Risk Indicators**")

        if reasons:

            for reason in reasons:
                st.write("•", reason)

        else:

            st.success("No major risk indicators detected.")

    else:

        st.markdown("""
        <div class="risk-card">

        <div class="risk-label">
        READY FOR ANALYSIS
        </div>

        <div class="risk-score" style="color:#7dd3fc;">
        —
        </div>

        <div class="risk-category" style="color:#8fa2bd;">
        Enter transaction details
        </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# INFORMATION STRIP
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.info("🌙 **Late Night**  \nTransactions during unusual hours receive additional risk weight.")

with c2:
    st.info("💻 **Device Signal**  \nWeb-based transactions receive additional monitoring weight.")

with c3:
    st.info("📶 **Network Signal**  \nNetwork type is considered as one of the transaction risk indicators.")

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
UPIShield • India Digital Transaction Fraud Risk Analysis
<br>
Hackathon Prototype • Risk-based monitoring system
</div>
""", unsafe_allow_html=True)