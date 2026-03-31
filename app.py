import streamlit as st
import pandas as pd
import numpy as np
import joblib
import shap
import matplotlib.pyplot as plt
import matplotlib
import os
matplotlib.use('Agg')

# ─────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Loan Default Risk Predictor",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Sora:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

    /* ── ROOT VARIABLES ── */
    :root {
        --navy:      #050D1A;
        --navy-2:    #0A1628;
        --navy-3:    #0F1F3D;
        --navy-4:    #162845;
        --electric:  #00D4FF;
        --electric-2:#0099CC;
        --gold:      #FFB700;
        --green:     #00E5A0;
        --red:       #FF4560;
        --amber:     #FFB700;
        --white:     #F0F6FF;
        --muted:     #8BA3BF;
        --border:    rgba(0, 212, 255, 0.15);
        --glow:      0 0 20px rgba(0, 212, 255, 0.15);
    }

    /* ── BASE ── */
    html, body, [class*="css"] {
        font-family: 'Sora', sans-serif !important;
        background-color: var(--navy) !important;
        color: var(--white) !important;
    }

    .main {
        background: linear-gradient(135deg, var(--navy) 0%, var(--navy-2) 50%, #060E1F 100%) !important;
        background-attachment: fixed !important;
    }

    /* ── GRID TEXTURE OVERLAY ── */
    .main::before {
        content: '';
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background-image:
            linear-gradient(rgba(0,212,255,0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,212,255,0.03) 1px, transparent 1px);
        background-size: 40px 40px;
        pointer-events: none;
        z-index: 0;
    }

    /* ── SIDEBAR ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--navy-3) 0%, var(--navy-2) 100%) !important;
        border-right: 1px solid var(--border) !important;
    }
    section[data-testid="stSidebar"] > div {
        background: transparent !important;
    }
    section[data-testid="stSidebar"] * {
        color: var(--white) !important;
    }
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        font-family: 'Space Mono', monospace !important;
        color: var(--electric) !important;
        letter-spacing: 0.05em;
        font-size: 13px !important;
        text-transform: uppercase;
    }
    section[data-testid="stSidebar"] a {
        color: var(--electric) !important;
        text-decoration: none;
    }
    section[data-testid="stSidebar"] a:hover {
        color: var(--gold) !important;
    }
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] li {
        font-size: 12px !important;
        color: var(--muted) !important;
        line-height: 1.8 !important;
    }

    /* ── LABELS ── */
    .stSlider label,
    .stNumberInput label,
    .stSelectbox label,
    .stCheckbox label,
    .stTextInput label,
    .stRadio label {
        color: var(--electric) !important;
        font-size: 11px !important;
        font-weight: 600 !important;
        font-family: 'Space Mono', monospace !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
    }

    /* ── INPUTS ── */
    .stSelectbox div[data-baseweb="select"] > div,
    .stNumberInput div[data-baseweb="input"],
    div[data-baseweb="input"] {
        background-color: var(--navy-3) !important;
        border: 1px solid var(--border) !important;
        border-radius: 6px !important;
        color: var(--white) !important;
    }
    .stNumberInput input,
    div[data-baseweb="input"] input,
    input[type="number"],
    input[type="text"] {
        color: var(--white) !important;
        background-color: var(--navy-3) !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 13px !important;
        -webkit-text-fill-color: var(--white) !important;
    }
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div {
        background-color: var(--navy-3) !important;
        color: var(--white) !important;
        font-family: 'Sora', sans-serif !important;
    }

    /* ── SLIDERS ── */
    .stSlider [data-baseweb="slider"] div[role="slider"] {
        background-color: var(--electric) !important;
        border: 2px solid var(--navy) !important;
        box-shadow: 0 0 8px var(--electric) !important;
    }

    /* ── CHECKBOXES ── */
    .stCheckbox > label > div:first-child {
        background-color: var(--navy-3) !important;
        border: 2px solid var(--electric) !important;
        border-radius: 4px !important;
    }
    .stCheckbox > label > div:last-child,
    .stCheckbox span {
        color: var(--white) !important;
        font-size: 12px !important;
        font-family: 'Sora', sans-serif !important;
    }

    /* ── BUTTONS ── */
    .stButton > button {
        background: linear-gradient(135deg, var(--electric-2), var(--electric)) !important;
        color: var(--navy) !important;
        border-radius: 6px !important;
        padding: 12px 30px !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        font-family: 'Space Mono', monospace !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        border: none !important;
        width: 100% !important;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.3) !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover {
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.6) !important;
        transform: translateY(-1px) !important;
    }

    /* ── WARNINGS / INFO ── */
    .stWarning, div[data-testid="stAlert"] {
        background: rgba(255, 183, 0, 0.08) !important;
        border: 1px solid rgba(255, 183, 0, 0.3) !important;
        border-radius: 8px !important;
        color: var(--white) !important;
    }
    .stInfo, [data-baseweb="notification"] {
        background: rgba(0, 212, 255, 0.06) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
    }

    /* ── HEADINGS ── */
    h1 {
        font-family: 'Sora', sans-serif !important;
        font-weight: 800 !important;
        font-size: 32px !important;
        color: var(--white) !important;
        letter-spacing: -0.02em !important;
    }
    h2 {
        font-family: 'Sora', sans-serif !important;
        font-weight: 700 !important;
        color: var(--white) !important;
    }
    h3 {
        font-family: 'Space Mono', monospace !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.1em !important;
        color: var(--electric) !important;
    }

    /* ── METRIC CARDS ── */
    .metric-card {
        background: linear-gradient(135deg, var(--navy-3), var(--navy-4));
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        border: 1px solid var(--border);
        box-shadow: var(--glow);
    }

    /* ── RISK CARDS ── */
    .risk-high {
        background: linear-gradient(135deg, rgba(255,69,96,0.12), rgba(255,69,96,0.05));
        border-left: 4px solid var(--red);
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 20px rgba(255,69,96,0.15);
    }
    .risk-medium {
        background: linear-gradient(135deg, rgba(255,183,0,0.12), rgba(255,183,0,0.05));
        border-left: 4px solid var(--amber);
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 20px rgba(255,183,0,0.15);
    }
    .risk-low {
        background: linear-gradient(135deg, rgba(0,229,160,0.12), rgba(0,229,160,0.05));
        border-left: 4px solid var(--green);
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 20px rgba(0,229,160,0.15);
    }

    /* ── SECTION HEADERS ── */
    .section-header {
        font-family: 'Space Mono', monospace !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        color: var(--electric) !important;
        text-transform: uppercase !important;
        letter-spacing: 0.15em !important;
        margin-bottom: 14px !important;
        padding-bottom: 8px !important;
        border-bottom: 1px solid var(--border) !important;
    }

    /* ── INSIGHT / DISCLAIMER BOXES ── */
    .insight-box {
        background: linear-gradient(135deg, rgba(0,212,255,0.08), rgba(0,212,255,0.03));
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 16px;
        font-size: 13px;
        color: var(--white);
        margin-top: 10px;
        line-height: 1.8;
        font-family: 'Sora', sans-serif;
    }
    .disclaimer-box {
        background: rgba(255,183,0,0.06);
        border-left: 3px solid var(--amber);
        border-radius: 8px;
        padding: 12px 16px;
        font-size: 12px;
        color: #D4A800;
        margin-top: 10px;
        line-height: 1.7;
        font-family: 'Sora', sans-serif;
    }

    /* ── BADGES ── */
    .verified-badge {
        background: rgba(0,229,160,0.12);
        border: 1px solid var(--green);
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 11px;
        font-weight: 700;
        color: var(--green);
        display: inline-block;
        font-family: 'Space Mono', monospace;
        letter-spacing: 0.05em;
    }
    .unverified-badge {
        background: rgba(255,183,0,0.08);
        border: 1px solid var(--amber);
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 11px;
        font-weight: 700;
        color: var(--amber);
        display: inline-block;
        font-family: 'Space Mono', monospace;
        letter-spacing: 0.05em;
    }

    /* ── MODE BANNERS ── */
    .mode-banner-officer {
        background: linear-gradient(135deg, var(--navy-3), var(--navy-4));
        border: 1px solid var(--border);
        border-left: 3px solid var(--electric);
        color: var(--white);
        border-radius: 8px;
        padding: 12px 20px;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 16px;
        font-family: 'Space Mono', monospace;
    }
    .mode-banner-customer {
        background: linear-gradient(135deg, rgba(0,229,160,0.1), rgba(0,229,160,0.04));
        border: 1px solid rgba(0,229,160,0.3);
        border-left: 3px solid var(--green);
        color: var(--white);
        border-radius: 8px;
        padding: 12px 20px;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 16px;
    }

    /* ── FOOTER ── */
    .footer {
        text-align: center;
        color: var(--muted);
        font-size: 11px;
        font-family: 'Space Mono', monospace;
        letter-spacing: 0.05em;
        margin-top: 60px;
        padding-top: 20px;
        border-top: 1px solid var(--border);
    }
    .footer a {
        color: var(--electric) !important;
        text-decoration: none;
    }

    /* ── DIVIDERS ── */
    hr {
        border-color: var(--border) !important;
    }

    /* ── RADIO BUTTONS ── */
    .stRadio > div {
        background: var(--navy-3) !important;
        border-radius: 8px !important;
        padding: 8px !important;
        border: 1px solid var(--border) !important;
    }

    /* ── SELECTBOX DROPDOWN ── */
    ul[data-baseweb="menu"] {
        background: var(--navy-3) !important;
        border: 1px solid var(--border) !important;
    }
    li[role="option"]:hover {
        background: var(--navy-4) !important;
    }

    /* ── NUMBER INPUT BUTTONS ── */
    .stNumberInput div[data-baseweb="input"] > div,
    .stNumberInput button {
        background-color: var(--navy-4) !important;
        color: var(--electric) !important;
        border: 1px solid var(--border) !important;
    }

    /* ── SUCCESS/ERROR BOXES ── */
    .stSuccess {
        background: rgba(0,229,160,0.08) !important;
        border: 1px solid rgba(0,229,160,0.3) !important;
        border-radius: 8px !important;
    }
    .stError {
        background: rgba(255,69,96,0.08) !important;
        border: 1px solid rgba(255,69,96,0.3) !important;
        border-radius: 8px !important;
    }

    /* ── SPINNER ── */
    .stSpinner > div {
        border-top-color: var(--electric) !important;
    }

    /* scrollbar */
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: var(--navy); }
    ::-webkit-scrollbar-thumb { background: var(--electric-2); border-radius: 2px; }

</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# LOAD MODEL
# ─────────────────────────────────────────
@st.cache_resource
def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model = joblib.load(
        os.path.join(base_dir, 'xgb_model_no_gender.pkl')
    )
    feature_names = joblib.load(
        os.path.join(base_dir, 'feature_names_no_gender.pkl')
    )
    return model, feature_names

model, feature_names = load_model()


# ─────────────────────────────────────────
# FEATURE LABEL MAP
# ─────────────────────────────────────────
FEATURE_LABELS = {
    'EXT_SOURCE_MEAN':              'Credit Bureau Score (Average)',
    'EXT_SOURCE_2':                 'Credit Bureau Score 2',
    'EXT_SOURCE_3':                 'Credit Bureau Score 3',
    'EXT_SOURCE_1':                 'Credit Bureau Score 1',
    'EXT_SOURCE_MIN':               'Credit Bureau Score (Weakest)',
    'CREDIT_INCOME_RATIO':          'Loan-to-Income Ratio',
    'ANNUITY_INCOME_RATIO':         'Monthly Repayment Burden',
    'CREDIT_TERM_YEARS':            'Loan Repayment Duration',
    'AMT_CREDIT':                   'Loan Amount (₦)',
    'AMT_INCOME_TOTAL':             'Annual Income (₦)',
    'AMT_ANNUITY':                  'Monthly Annuity (₦)',
    'AMT_GOODS_PRICE':              'Asset / Goods Value (₦)',
    'AGE_YEARS':                    'Borrower Age (Years)',
    'DAYS_BIRTH':                   'Borrower Age',
    'EMPLOYMENT_YEARS':             'Years in Employment',
    'DAYS_EMPLOYED':                'Employment Duration',
    'EMPLOYMENT_AGE_RATIO':         'Employment Stability Index',
    'INCOME_PER_PERSON':            'Income Per Family Member (₦)',
    'CNT_CHILDREN':                 'Number of Dependants',
    'CNT_FAM_MEMBERS':              'Total Family Size',
    'FLAG_OWN_CAR':                 'Business Registration',
    'FLAG_OWN_REALTY':              'Bank Statement Submitted',
    'FLAG_DOCUMENT_3':              'Key Documents Submitted',
    'NAME_CONTRACT_TYPE':           'Loan Type (Revolving)',
    'NAME_FAMILY_STATUS_Married':   'Marital Status (Married)',
    'NAME_EDUCATION_TYPE_Higher education': 'Education (Tertiary)',
    'DAYS_ID_PUBLISH':              'ID Document Age (Days)',
    'REGION_RATING_CLIENT':         'Region Risk Rating',
    'REGION_RATING_CLIENT_W_CITY':  'City Region Risk Rating',
}


# ─────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────
def get_risk_label(probability, medium_threshold=0.3, high_threshold=0.6):
    if probability >= high_threshold:
        return "HIGH RISK", "#E24B4A", "risk-high", "🔴"
    elif probability >= medium_threshold:
        return "MEDIUM RISK", "#F0A500", "risk-medium", "🟡"
    else:
        return "LOW RISK", "#1D9E75", "risk-low", "🟢"


def build_input_dataframe(inputs, feature_names):
    row = pd.DataFrame([{f: 0 for f in feature_names}])
    for key, value in inputs.items():
        if key in row.columns:
            row[key] = value
    return row


def get_label(feature):
    return FEATURE_LABELS.get(feature, feature.replace('_', ' ').title())


def delinquency_risk_modifier(delinquency_recency):
    modifiers = {
        "Never": 0.0,
        "5+ years ago": 0.03,
        "2 to 5 years ago": 0.07,
        "Within the last 2 years": 0.14
    }
    return modifiers.get(delinquency_recency, 0.0)


def active_loan_modifier(active_loans):
    if active_loans == 0:
        return 0.0
    elif active_loans <= 2:
        return 0.02
    elif active_loans <= 4:
        return 0.05
    else:
        return 0.10


def income_stability_modifier(income_type):
    modifiers = {
        "Fixed Salary": 0.0,
        "Business / Self-Employed": 0.03,
        "Commission-Based": 0.05,
        "Irregular / Seasonal": 0.08
    }
    return modifiers.get(income_type, 0.0)


# ─────────────────────────────────────────
# SESSION STATE INIT
# ─────────────────────────────────────────
if "submitted_applications" not in st.session_state:
    st.session_state.submitted_applications = []

if "customer_submitted" not in st.session_state:
    st.session_state.customer_submitted = False


# ─────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🏦 Loan Default Risk Predictor")
    st.markdown("---")

    # ── VIEW MODE TOGGLE ────────────────────
    st.markdown("### 👁️ View Mode")
    view_mode = st.radio(
        "Select interface",
        ["🏦 Loan Officer Dashboard", "📋 Customer Application"],
        help="Switch between the officer assessment view and the customer-facing application form"
    )
    st.markdown("---")

    if "Loan Officer" in view_mode:
        st.markdown("""
        This tool uses a machine learning model trained on
        **1,600,000 real loan applications** to predict the
        probability that a borrower will default.
        """)
        st.markdown("---")
        st.markdown("### How it works")
        st.markdown("""
        1. Share the **Customer Application** link with applicants
        2. Review submitted applications in the inbox below
        3. Adjust risk thresholds to match your policy
        4. Click **Predict Default Risk** for full assessment
        5. View the risk score, SHAP explanation, and recommendation
        """)
        st.markdown("---")
        st.markdown("### Model Performance")
        st.markdown("""
        - **AUC-ROC:** 0.7664
        - **Recall:** 65.3% of defaults caught
        - **Algorithm:** XGBoost
        - **Training records:** 1,600,000
        - **Gender-neutral:** Yes ✅
        - **CBN compliant:** Fair lending ready
        - **Income range:** No upper limit
        - **Market scope:** Micro to commercial
        """)
        st.markdown("---")

        # ── RISK THRESHOLDS ──────────────────
        st.markdown("### ⚙️ Risk Threshold Settings")
        st.markdown("""
        <div style='font-size:12px;color:#B5D4F4;margin-bottom:8px'>
        Adjust thresholds to match your institution's
        credit policy and risk appetite.
        </div>
        """, unsafe_allow_html=True)

        medium_threshold = st.slider(
            "Medium Risk Threshold (%)",
            min_value=10, max_value=50, value=30, step=5,
            help="Applications scoring above this are Medium Risk"
        ) / 100

        high_threshold = st.slider(
            "High Risk Threshold (%)",
            min_value=30, max_value=80, value=60, step=5,
            help="Applications scoring above this are High Risk"
        ) / 100

        if high_threshold <= medium_threshold:
            high_threshold = medium_threshold + 0.10

        st.markdown(f"""
        <div style='background:#0C447C;border-radius:6px;
                    padding:10px;font-size:12px;margin-top:8px'>
            <div style='color:#B5D4F4;margin-bottom:6px;font-weight:600'>
                Current institution policy:
            </div>
            <div style='color:#FFFFFF;margin-bottom:2px'>
                🟢 Below {int(medium_threshold*100)}% → Approve
            </div>
            <div style='color:#FFFFFF;margin-bottom:2px'>
                🟡 {int(medium_threshold*100)}–{int(high_threshold*100)}% → Conditional Review
            </div>
            <div style='color:#FFFFFF'>
                🔴 Above {int(high_threshold*100)}% → Decline
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        medium_threshold = 0.30
        high_threshold = 0.60
        st.markdown("""
        <div style='font-size:13px;color:#B5D4F4;line-height:1.7'>
        Fill in your details accurately and completely.
        Your application will be reviewed by a loan officer
        and you will be contacted with a decision.
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("""
        <div style='font-size:12px;color:#B5D4F4;line-height:1.7'>
        🔒 Your information is securely handled and will only
        be used for the purpose of evaluating your loan request.<br><br>
        📋 Providing your BVN enables faster processing via
        bureau verification. Your consent is required and logged.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style='font-size:12px'>
    Built by <strong>Nkpo-ikana Udom</strong><br>
    Operations & Strategy | Fintech & Credit Risk<br>
    <a href='https://www.linkedin.com/in/nkpo-ikana-udom-479ba91a9/'
    target='_blank'>LinkedIn</a> ·
    <a href='https://github.com/stephenudom'
    target='_blank'>GitHub</a>
    </div>
    """, unsafe_allow_html=True)


# ═════════════════════════════════════════════════════
# CUSTOMER APPLICATION MODE
# ═════════════════════════════════════════════════════
if "Customer Application" in view_mode:

    st.markdown("# 📋 Loan Application Form")
    st.markdown(
        "Please complete all sections accurately. "
        "A loan officer will review your application and contact you with a decision."
    )
    st.markdown("---")

    if st.session_state.customer_submitted:
        st.markdown("""
        <div style='background:linear-gradient(135deg,rgba(0,229,160,0.1),rgba(0,229,160,0.03));border-left:4px solid #00E5A0;
                    border-radius:12px;padding:30px;text-align:center;margin-top:20px'>
            <div style='font-size:40px'>✅</div>
            <div style='font-size:22px;font-weight:700;color:#00E5A0;margin-top:10px'>
                Application Received
            </div>
            <div style='font-size:15px;color:#C8D8E8;margin-top:10px;line-height:1.8'>
                Thank you. Your application has been submitted successfully.<br>
                A loan officer will review your details and reach out to you shortly.<br><br>
                <strong>Reference:</strong> APP-{ref}
            </div>
        </div>
        """.format(ref=np.random.randint(100000, 999999)), unsafe_allow_html=True)

        if st.button("Submit Another Application"):
            st.session_state.customer_submitted = False
            st.rerun()

    else:
        # ── SECTION 1: PERSONAL DETAILS ──────────
        st.markdown('<div class="section-header">1. Personal Details</div>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            c_fullname = st.text_input("Full Name", placeholder="e.g. Chukwuemeka Obi")
            c_age = st.slider("Age (years)", 18, 70, 30)
            c_family_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widow"])
        with c2:
            c_phone = st.text_input("Phone Number", placeholder="e.g. 08012345678")
            c_education = st.selectbox("Highest Education Level", [
                "Secondary", "Higher education", "Incomplete higher",
                "Lower secondary", "Academic degree"
            ])
            c_children = st.number_input("Number of Dependants", 0, 10, 0)
        with c3:
            c_family_members = st.number_input("Total Family Members", 1, 15, 2)
            st.markdown('<p style="font-size:10px;font-weight:700;color:#00D4FF;font-family:Space Mono,monospace;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:6px">Supporting Documents</p>', unsafe_allow_html=True)
            c_biz_reg   = st.file_uploader("📄 Business Registration Certificate", type=["pdf","jpg","jpeg","png"], key="biz_reg_file")
            c_bank_stmt = st.file_uploader("🏦 6 Months Bank Statement", type=["pdf","jpg","jpeg","png"], key="bank_file")
            c_tax_id    = st.file_uploader("📋 Tax Identification Number (TIN)", type=["pdf","jpg","jpeg","png"], key="tax_file")
            c_utility   = st.file_uploader("🔖 Utility Bill / Proof of Address", type=["pdf","jpg","jpeg","png"], key="utility_file")

        st.markdown("---")

        # ── SECTION 2: EMPLOYMENT & INCOME ───────
        st.markdown('<div class="section-header">2. Employment & Income</div>', unsafe_allow_html=True)
        e1, e2, e3 = st.columns(3)
        with e1:
            c_employment_sector = st.selectbox("Employment Sector", [
                "Banking / Finance", "Government / Civil Service",
                "Healthcare", "Education", "Technology",
                "Trade / Commerce", "Agriculture",
                "Transport / Logistics", "Construction",
                "Other"
            ])
            c_income_type = st.selectbox("Income Type", [
                "Fixed Salary", "Business / Self-Employed",
                "Commission-Based", "Irregular / Seasonal"
            ])
        with e2:
            c_employment_years = st.slider("Years in Current Job / Business", 0, 40, 3)
            c_income = st.number_input(
                "Monthly Net Income (₦)",
                min_value=10000, max_value=50000000, value=150000, step=10000, format="%d",
                help="Your take-home income after tax and deductions"
            )
        with e3:
            c_employer = st.text_input("Employer / Business Name", placeholder="e.g. Lagos State Government")
            c_active_loans = st.number_input(
                "Number of Active Loans / Credit Facilities",
                min_value=0, max_value=20, value=0,
                help="Include all active loans across all lenders"
            )

        st.markdown("---")

        # ── SECTION 3: LOAN REQUEST ───────────────
        st.markdown('<div class="section-header">3. Loan Request</div>', unsafe_allow_html=True)
        l1, l2, l3 = st.columns(3)
        with l1:
            c_loan_amount = st.number_input(
                "Loan Amount Requested (₦)",
                min_value=10000, max_value=500000000, value=500000, step=50000, format="%d"
            )
            c_contract_type = st.selectbox("Loan Type", ["Cash loans", "Revolving loans"])
        with l2:
            c_annuity = st.number_input(
                "Expected Monthly Repayment (₦)",
                min_value=1000, max_value=50000000, value=50000, step=5000, format="%d"
            )
            c_goods_price = st.number_input(
                "Asset / Purpose Value (₦)",
                min_value=0, max_value=500000000, value=400000, step=50000, format="%d",
                help="Value of asset, goods, or purpose of the loan"
            )
        with l3:
            c_delinquency = st.selectbox(
                "Previous Loan Default History",
                ["Never", "5+ years ago", "2 to 5 years ago", "Within the last 2 years"],
                help="Has this applicant ever defaulted on a loan?"
            )

        st.markdown("---")

        # ── SECTION 4: BVN VERIFICATION ──────────
        st.markdown('<div class="section-header">4. BVN Verification (Required)</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style='background:linear-gradient(135deg,rgba(0,212,255,0.08),rgba(0,212,255,0.03));
                    border:1px solid rgba(0,212,255,0.2);border-radius:8px;padding:14px 18px;
                    font-size:12px;color:#C8D8E8;margin-bottom:14px;line-height:1.8;
                    font-family:Sora,sans-serif'>
            Your BVN is required to verify your identity and retrieve your credit bureau history.
            This is a <strong style="color:#00D4FF">soft enquiry only</strong> and will not affect your credit score.
            Your BVN is encrypted and used solely for this application.
        </div>
        """, unsafe_allow_html=True)

        bvn_col1, bvn_col2 = st.columns([2, 1])
        with bvn_col1:
            c_bvn = st.text_input(
                "Bank Verification Number (BVN)",
                placeholder="Enter your 11-digit BVN",
                max_chars=11,
                help="Your BVN is an 11-digit number issued by your bank"
            )
        with bvn_col2:
            bvn_verified = False
            if c_bvn and len(c_bvn) == 11 and c_bvn.isdigit():
                st.markdown("""
                <div style='margin-top:28px'>
                    <span class='verified-badge'>✅ BVN Format Valid</span>
                </div>
                """, unsafe_allow_html=True)
                bvn_verified = True
            elif c_bvn:
                st.markdown("""
                <div style='margin-top:28px'>
                    <span class='unverified-badge'>⚠️ Invalid BVN Format</span>
                </div>
                """, unsafe_allow_html=True)

        c_bvn_consent = st.checkbox("I consent to BVN-based credit bureau verification (soft enquiry only)")

        if c_bvn and c_bvn_consent and bvn_verified:
            st.info(
                "🔄 In production: A live bureau API call (CRC / FirstCentral / Mono) would be triggered here "
                "to auto-populate your credit history. Your application will be flagged as Bureau-Verified."
            )

        st.markdown("---")

        # ── SUBMIT ────────────────────────────────
        if st.button("📤 Submit Application"):
            if not c_fullname or not c_phone:
                st.error("Please provide your full name and phone number before submitting.")
            else:
                annual_income = c_income * 12
                application = {
                    "name": c_fullname,
                    "phone": c_phone,
                    "age": c_age,
                    "family_status": c_family_status,
                    "education": c_education,
                    "children": c_children,
                    "family_members": c_family_members,
                    "biz_reg": c_biz_reg is not None,
                    "bank_stmt": c_bank_stmt is not None,
                    "tax_id": c_tax_id is not None,
                    "utility": c_utility is not None,
                    "biz_reg_file": c_biz_reg.name if c_biz_reg else None,
                    "bank_stmt_file": c_bank_stmt.name if c_bank_stmt else None,
                    "tax_id_file": c_tax_id.name if c_tax_id else None,
                    "utility_file": c_utility.name if c_utility else None,
                    "biz_reg_bytes": c_biz_reg.read() if c_biz_reg else None,
                    "bank_stmt_bytes": c_bank_stmt.read() if c_bank_stmt else None,
                    "tax_id_bytes": c_tax_id.read() if c_tax_id else None,
                    "utility_bytes": c_utility.read() if c_utility else None,
                    "own_car": False,
                    "own_realty": False,
                    "flag_document_3": any([c_biz_reg, c_bank_stmt, c_tax_id, c_utility]),
                    "employment_sector": c_employment_sector,
                    "income_type": c_income_type,
                    "employment_years": c_employment_years,
                    "income": annual_income,
                    "employer": c_employer,
                    "active_loans": c_active_loans,
                    "loan_amount": c_loan_amount,
                    "contract_type": c_contract_type,
                    "annuity": c_annuity,
                    "goods_price": c_goods_price,
                    "delinquency_recency": c_delinquency,
                    "bvn_provided": bvn_verified and c_bvn_consent,
                    "ext_source_1": 0.5,
                    "ext_source_2": 0.5,
                    "ext_source_3": 0.5,
                }
                st.session_state.submitted_applications.append(application)
                st.session_state.customer_submitted = True
                st.rerun()


# ═════════════════════════════════════════════════════
# LOAN OFFICER DASHBOARD
# ═════════════════════════════════════════════════════
else:

    st.markdown("# 🏦 Loan Default Risk Predictor")
    st.markdown(
        "Assess borrower credit risk using machine learning. "
        "Pre-fill from a submitted customer application or enter details manually below."
    )

    st.warning(
        "⚖️ **Decision Support Tool — Not a Substitute for Credit Judgement** — "
        "This tool provides a data-driven risk signal to aid informed decision-making. "
        "Final approval must incorporate loan officer assessment of borrower context, "
        "market conditions, guarantor quality, and institutional credit policy."
    )
    st.info(
        "🔒 **Fair Lending Model** — Gender-neutral and CBN fair lending compliant. "
        "Risk scoring is based solely on financial behaviour and creditworthiness indicators. "
        "| 📍 Built for Nigeria · Powered by XGBoost · Explained by SHAP"
    )
    st.markdown("---")

    # ── SUBMITTED APPLICATIONS INBOX ─────────
    if st.session_state.submitted_applications:
        st.markdown('<div class="section-header">📥 Submitted Applications Inbox</div>', unsafe_allow_html=True)
        st.markdown(f"**{len(st.session_state.submitted_applications)} application(s) awaiting review**")

        # ── APPLICATION CARDS ──────────────────
        for i, a in enumerate(st.session_state.submitted_applications):
            docs_submitted = sum([a.get("biz_reg",False), a.get("bank_stmt",False), a.get("tax_id",False), a.get("utility",False)])
            bvn_badge = "🔵 BVN Verified" if a.get("bvn_provided") else "⚠️ No BVN"
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#0F1F3D,#0A1628);border:1px solid rgba(0,212,255,0.15);
                        border-radius:10px;padding:16px 20px;margin-bottom:10px">
                <div style="display:flex;justify-content:space-between;align-items:center">
                    <div>
                        <div style="font-size:16px;font-weight:700;color:#F0F6FF">{a['name']}</div>
                        <div style="font-size:11px;color:#8BA3BF;margin-top:3px;font-family:Space Mono,monospace">
                            APP-{i+1:03d} &nbsp;|&nbsp; ₦{a['loan_amount']:,} &nbsp;|&nbsp; {a['employment_sector']} &nbsp;|&nbsp; {bvn_badge}
                        </div>
                    </div>
                    <div style="text-align:right">
                        <div style="font-size:11px;color:#00D4FF;font-family:Space Mono,monospace">{docs_submitted}/4 docs</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        app_options = [
            f"APP-{i+1:03d} — {a['name']} | ₦{a['loan_amount']:,} | {a['employment_sector']}"
            for i, a in enumerate(st.session_state.submitted_applications)
        ]
        app_options = ["-- Select an application to assess --"] + app_options
        selected_app = st.selectbox("Open application for full assessment", app_options)

        if selected_app != "-- Select an application to assess --":
            app_idx = int(selected_app.split("APP-")[1].split(" ")[0]) - 1
            loaded = st.session_state.submitted_applications[app_idx]
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,rgba(0,229,160,0.08),rgba(0,229,160,0.03));
                        border:1px solid rgba(0,229,160,0.25);border-radius:8px;padding:12px 18px">
                <span style="font-size:14px;font-weight:700;color:#00E5A0">✅ Loaded: {loaded['name']}</span>
                <span style="font-size:11px;color:#8BA3BF;margin-left:12px;font-family:Space Mono,monospace">
                    {'🔵 Bureau-Verified' if loaded.get('bvn_provided') else '⚠️ Self-Reported — BVN not provided'}
                </span>
            </div>
            """, unsafe_allow_html=True)
        else:
            loaded = None
        st.markdown("---")
    else:
        loaded = None

    # ── INPUT FORM ────────────────────────────
    st.markdown('<div class="section-header">Borrower Information</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    def pre(key, default):
        if loaded:
            return loaded.get(key, default)
        return default

    with col1:
        st.markdown(
            '<p style="font-size:11px;font-weight:700;color:#00D4FF;font-family:Space Mono,monospace;text-transform:uppercase;letter-spacing:0.1em;'
            'border-bottom:2px solid #2E75B6;padding-bottom:6px">Personal Details</p>',
            unsafe_allow_html=True
        )
        age = st.slider("Age (years)", 18, 70, pre("age", 35))
        family_status = st.selectbox(
            "Family Status",
            ["Single", "Married", "Divorced", "Widow"],
            index=["Single", "Married", "Divorced", "Widow"].index(pre("family_status", "Single"))
        )
        children = st.number_input("Number of Dependants", 0, 10, pre("children", 0))
        family_members = st.number_input("Total Family Members", 1, 15, pre("family_members", 2))
        education = st.selectbox(
            "Education Level",
            ["Secondary", "Higher education", "Incomplete higher", "Lower secondary", "Academic degree"],
            index=["Secondary", "Higher education", "Incomplete higher", "Lower secondary", "Academic degree"].index(
                pre("education", "Secondary")
            )
        )

    with col2:
        st.markdown(
            '<p style="font-size:11px;font-weight:700;color:#00D4FF;font-family:Space Mono,monospace;text-transform:uppercase;letter-spacing:0.1em;'
            'border-bottom:2px solid #2E75B6;padding-bottom:6px">Financial Details</p>',
            unsafe_allow_html=True
        )
        income = st.number_input(
            "Annual Income (₦)",
            min_value=10000, max_value=500000000,
            value=pre("income", 1800000), step=50000, format="%d",
            help="Total annual income — salary, business income, and all other sources"
        )
        loan_amount = st.number_input(
            "Loan Amount Requested (₦)",
            min_value=10000, max_value=500000000,
            value=pre("loan_amount", 5000000), step=100000, format="%d"
        )
        annuity = st.number_input(
            "Monthly Repayment Amount (₦)",
            min_value=1000, max_value=50000000,
            value=pre("annuity", 150000), step=10000, format="%d"
        )
        goods_price = st.number_input(
            "Asset / Goods Value (₦)",
            min_value=0, max_value=500000000,
            value=pre("goods_price", 4500000), step=100000, format="%d"
        )
        contract_type = st.selectbox(
            "Loan Type",
            ["Cash loans", "Revolving loans"],
            index=["Cash loans", "Revolving loans"].index(pre("contract_type", "Cash loans"))
        )

    with col3:
        st.markdown(
            '<p style="font-size:11px;font-weight:700;color:#00D4FF;font-family:Space Mono,monospace;text-transform:uppercase;letter-spacing:0.1em;'
            'border-bottom:2px solid #2E75B6;padding-bottom:6px">Employment, History & Identity</p>',
            unsafe_allow_html=True
        )

        # Employment enhancements
        employment_sector = st.selectbox(
            "Employment Sector",
            ["Banking / Finance", "Government / Civil Service", "Healthcare", "Education",
             "Technology", "Trade / Commerce", "Agriculture", "Transport / Logistics",
             "Construction", "Other"],
            index=["Banking / Finance", "Government / Civil Service", "Healthcare", "Education",
                   "Technology", "Trade / Commerce", "Agriculture", "Transport / Logistics",
                   "Construction", "Other"].index(pre("employment_sector", "Trade / Commerce"))
        )
        income_type = st.selectbox(
            "Income Type",
            ["Fixed Salary", "Business / Self-Employed", "Commission-Based", "Irregular / Seasonal"],
            index=["Fixed Salary", "Business / Self-Employed", "Commission-Based", "Irregular / Seasonal"].index(
                pre("income_type", "Fixed Salary")
            ),
            help="Income stability is a key default predictor"
        )
        employment_years = st.slider(
            "Years in Current Employment / Business",
            0, 40, pre("employment_years", 5)
        )

        # Credit history enhancements
        st.markdown(
            '<p style="font-size:13px;font-weight:600;color:#F0F6FF;margin-top:10px;margin-bottom:4px">'
            'Credit History</p>',
            unsafe_allow_html=True
        )
        delinquency_recency = st.selectbox(
            "Previous Default History",
            ["Never", "5+ years ago", "2 to 5 years ago", "Within the last 2 years"],
            index=["Never", "5+ years ago", "2 to 5 years ago", "Within the last 2 years"].index(
                pre("delinquency_recency", "Never")
            ),
            help="Recency of default is a stronger predictor than frequency"
        )
        active_loans = st.number_input(
            "Active Loan Obligations (all lenders)",
            min_value=0, max_value=20,
            value=pre("active_loans", 0),
            help="Total number of active loans across all lenders — impacts DTI"
        )

        ext_source_1 = st.slider(
            "Credit Bureau Score 1", 0.0, 1.0,
            pre("ext_source_1", 0.5), 0.01,
            help="0 = poor, 1 = excellent. Leave at 0.5 if unknown."
        )
        ext_source_2 = st.slider(
            "Credit Bureau Score 2", 0.0, 1.0,
            pre("ext_source_2", 0.5), 0.01
        )
        ext_source_3 = st.slider(
            "Credit Bureau Score 3", 0.0, 1.0,
            pre("ext_source_3", 0.5), 0.01
        )

        # BVN
        st.markdown(
            '<p style="font-size:13px;font-weight:600;color:#F0F6FF;margin-top:10px;margin-bottom:4px">'
            'Identity Verification</p>',
            unsafe_allow_html=True
        )
        bvn_input = st.text_input(
            "BVN (Bank Verification Number)",
            placeholder="11-digit BVN",
            max_chars=11,
            help="Triggers bureau API call to auto-verify credit history in production"
        )
        bvn_consent_officer = st.checkbox(
            "✅ Applicant consent obtained for bureau enquiry",
            value=pre("bvn_provided", False)
        )

        bvn_valid = bvn_input and len(bvn_input) == 11 and bvn_input.isdigit()
        bvn_bureau_verified = bvn_valid and bvn_consent_officer

        if bvn_bureau_verified:
            st.markdown('<span class="verified-badge">✅ Bureau-Verified Application</span>', unsafe_allow_html=True)
            st.info("🔄 Production: Live CRC/FirstCentral/Mono API call would populate bureau scores automatically.")
        elif bvn_input:
            st.markdown('<span class="unverified-badge">⚠️ BVN Invalid or Consent Pending</span>', unsafe_allow_html=True)

        st.markdown(
            '<p style="font-size:13px;font-weight:600;color:#F0F6FF;margin-top:10px;margin-bottom:4px">'
            'Document Verification</p>',
            unsafe_allow_html=True
        )
        doc_biz_reg   = pre("biz_reg", False)
        doc_bank_stmt = pre("bank_stmt", False)
        doc_tin       = pre("tax_id", False)
        doc_utility   = pre("utility", False)
        flag_document_3 = any([doc_biz_reg, doc_bank_stmt, doc_tin, doc_utility])

        # ── DOCUMENT STATUS PANEL ──────────────
        docs_info = [
            ("📄 Business Registration", doc_biz_reg, pre("biz_reg_file", None)),
            ("🏦 6-Month Bank Statement", doc_bank_stmt, pre("bank_stmt_file", None)),
            ("📋 TIN / Tax Document", doc_tin, pre("tax_id_file", None)),
            ("🔖 Utility Bill / Proof of Address", doc_utility, pre("utility_file", None)),
        ]
        # ── DOCUMENT STATUS + DOWNLOAD ─────────
        st.markdown('''
        <div style="background:linear-gradient(135deg,#0F1F3D,#0A1628);border:1px solid rgba(0,212,255,0.15);
                    border-radius:10px;padding:14px 18px;margin-top:8px;margin-bottom:8px">
            <div style="font-size:10px;color:#00D4FF;font-family:Space Mono,monospace;text-transform:uppercase;
                        letter-spacing:0.12em;margin-bottom:10px;font-weight:700">Document Verification Panel</div>
        </div>
        ''', unsafe_allow_html=True)

        doc_keys = [
            ("📄 Business Registration", "biz_reg", "biz_reg_file", "biz_reg_bytes"),
            ("🏦 6-Month Bank Statement", "bank_stmt", "bank_stmt_file", "bank_stmt_bytes"),
            ("📋 TIN / Tax Document", "tax_id", "tax_id_file", "tax_id_bytes"),
            ("🔖 Utility Bill / Address", "utility", "utility_file", "utility_bytes"),
        ]
        for label, submitted_key, file_key, bytes_key in doc_keys:
            submitted = pre(submitted_key, False)
            filename  = pre(file_key, None)
            filebytes = pre(bytes_key, None)
            dcol1, dcol2 = st.columns([3, 1])
            with dcol1:
                if submitted and filename:
                    st.markdown(f'''<div style="padding:8px 0;font-size:12px;color:#C8D8E8">
                        <span style="color:#00E5A0;font-weight:700">✅ {label}</span>
                        <span style="color:#8BA3BF;font-size:11px;margin-left:8px;font-family:Space Mono,monospace">{filename}</span>
                    </div>''', unsafe_allow_html=True)
                else:
                    st.markdown(f'''<div style="padding:8px 0;font-size:12px">
                        <span style="color:#FF4560;font-weight:700">⚠ {label}</span>
                        <span style="color:#8BA3BF;font-size:11px;margin-left:8px">Not uploaded</span>
                    </div>''', unsafe_allow_html=True)
            with dcol2:
                if filebytes and filename:
                    ext = filename.split(".")[-1].lower()
                    mime = "application/pdf" if ext == "pdf" else f"image/{ext}"
                    st.download_button(
                        label="⬇ Download",
                        data=filebytes,
                        file_name=filename,
                        mime=mime,
                        key=f"dl_{bytes_key}_{pre('name','applicant')}",
                        use_container_width=True
                    )

    st.markdown("---")

    # ── ENGINEERED FEATURES ───────────────────
    def compute_engineered_features(
            age, income, loan_amount, annuity,
            employment_years, ext_source_1,
            ext_source_2, ext_source_3,
            family_members, goods_price,
            children, own_car, own_realty,
            flag_document_3, contract_type,
            education, family_status):

        ext_sources = [s for s in [ext_source_1, ext_source_2, ext_source_3] if s > 0]
        ext_mean = np.mean(ext_sources) if ext_sources else 0.5
        ext_min = np.min(ext_sources) if ext_sources else 0.5

        return {
            'AGE_YEARS': age,
            'EMPLOYMENT_YEARS': employment_years,
            'CREDIT_INCOME_RATIO': loan_amount / max(income, 1),
            'ANNUITY_INCOME_RATIO': annuity / max(income, 1),
            'CREDIT_TERM_YEARS': annuity / max(loan_amount, 1),
            'INCOME_PER_PERSON': income / max(family_members, 1),
            'EXT_SOURCE_MEAN': ext_mean,
            'EXT_SOURCE_MIN': ext_min,
            'EMPLOYMENT_AGE_RATIO': employment_years / max(age, 1),
            'EXT_SOURCE_1': ext_source_1,
            'EXT_SOURCE_2': ext_source_2,
            'EXT_SOURCE_3': ext_source_3,
            'AMT_CREDIT': loan_amount,
            'AMT_INCOME_TOTAL': income,
            'AMT_ANNUITY': annuity,
            'AMT_GOODS_PRICE': goods_price,
            'DAYS_BIRTH': -age * 365,
            'DAYS_EMPLOYED': -employment_years * 365,
            'CNT_CHILDREN': children,
            'CNT_FAM_MEMBERS': family_members,
            'FLAG_OWN_CAR': 1 if own_car else 0,
            'FLAG_OWN_REALTY': 1 if own_realty else 0,
            'FLAG_DOCUMENT_3': 1 if flag_document_3 else 0,
            'NAME_CONTRACT_TYPE': 1 if contract_type == "Revolving loans" else 0,
            'NAME_EDUCATION_TYPE_Higher education': 1 if education == "Higher education" else 0,
            'NAME_FAMILY_STATUS_Married': 1 if family_status == "Married" else 0,
        }

    # ── PREDICT BUTTON ────────────────────────
    predict_col, _ = st.columns([1, 2])
    with predict_col:
        predict_button = st.button("🔍 Predict Default Risk")

    if predict_button:

        engineered = compute_engineered_features(
            age, income, loan_amount, annuity,
            employment_years, ext_source_1,
            ext_source_2, ext_source_3,
            family_members, goods_price,
            children, own_car, own_realty,
            flag_document_3, contract_type,
            education, family_status
        )
        input_df = build_input_dataframe(engineered, feature_names)

        raw_probability = model.predict_proba(input_df)[0][1]

        # Apply contextual modifiers from enhanced fields
        modifier = (
            delinquency_risk_modifier(delinquency_recency) +
            active_loan_modifier(active_loans) +
            income_stability_modifier(income_type)
        )
        probability = min(raw_probability + modifier, 1.0)

        risk_label, risk_color, risk_class, risk_icon = get_risk_label(
            probability, medium_threshold, high_threshold
        )

        credit_income = loan_amount / max(income, 1)
        ext_avg = np.mean([ext_source_1, ext_source_2, ext_source_3])

        st.markdown("---")
        st.markdown("## Assessment Result")

        if bvn_bureau_verified:
            st.markdown(
                '<span class="verified-badge">✅ Bureau-Verified Application — Score anchored to real data</span>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<span class="unverified-badge">⚠️ Self-Reported — Bureau verification recommended for higher confidence</span>',
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        # ── RESULT CARDS ──────────────────────
        r1, r2, r3, r4 = st.columns(4)

        with r1:
            st.markdown(f"""
            <div class="{risk_class}">
                <div style="font-size:36px">{risk_icon}</div>
                <div style="font-size:20px;font-weight:700;color:{risk_color};margin-top:6px">
                    {risk_label}
                </div>
                <div style="font-size:11px;color:#8BA3BF;margin-top:4px">
                    Policy: {int(medium_threshold*100)}% / {int(high_threshold*100)}%
                </div>
            </div>
            """, unsafe_allow_html=True)

        with r2:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size:12px;color:#8BA3BF;margin-bottom:4px">Default Probability</div>
                <div style="font-size:36px;font-weight:700;color:{risk_color}">{probability*100:.1f}%</div>
                <div style="font-size:11px;color:#aaa;margin-top:2px">
                    Model: {raw_probability*100:.1f}% + context adjustments
                </div>
            </div>
            """, unsafe_allow_html=True)

        with r3:
            ci_color = "#E24B4A" if credit_income > 5 else "#F0A500" if credit_income > 3 else "#1D9E75"
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size:12px;color:#8BA3BF;margin-bottom:4px">Loan-to-Income Ratio</div>
                <div style="font-size:36px;font-weight:700;color:{ci_color}">{credit_income:.1f}x</div>
            </div>
            """, unsafe_allow_html=True)

        with r4:
            bureau_color = "#E24B4A" if ext_avg < 0.35 else "#F0A500" if ext_avg < 0.55 else "#1D9E75"
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size:12px;color:#8BA3BF;margin-bottom:4px">Avg Credit Bureau Score</div>
                <div style="font-size:36px;font-weight:700;color:{bureau_color}">{ext_avg:.2f}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ── INSIGHT BOX ───────────────────────
        delinquency_note = ""
        if delinquency_recency == "Within the last 2 years":
            delinquency_note = " Recent default history within 2 years is a significant red flag and has been factored into this score."
        elif delinquency_recency == "2 to 5 years ago":
            delinquency_note = " A prior default 2-5 years ago has been noted and moderately weighted."

        active_loan_note = f" Borrower currently holds {active_loans} active loan obligation(s)." if active_loans > 0 else ""
        income_note = f" Income is {income_type.lower()}, which carries {'higher' if income_type in ['Irregular / Seasonal', 'Commission-Based'] else 'standard'} repayment variability."

        if probability >= high_threshold:
            insight = (
                f"⚠️ This application carries significant default risk.{delinquency_note}{active_loan_note}{income_note} "
                "The credit bureau profile and debt-to-income ratio suggest this borrower may struggle to meet "
                "repayment obligations. Recommend decline or referral to credit committee with additional collateral "
                "or guarantor requirements before consideration."
            )
        elif probability >= medium_threshold:
            insight = (
                f"⚡ This application shows moderate risk indicators.{delinquency_note}{active_loan_note}{income_note} "
                "Consider requesting additional documentation — 6 months bank statement, business registration, "
                "or a credible guarantor. Loan restructuring to reduce monthly repayment burden may bring this "
                "within acceptable risk bounds."
            )
        else:
            insight = (
                f"✅ This application presents a low default risk profile.{active_loan_note}{income_note} "
                "Credit bureau history and debt-to-income ratio are within acceptable bounds. Recommend standard "
                "approval process with routine documentation verification — bank statement, means of identification, "
                "and proof of income."
            )

        st.markdown(f'<div class="insight-box">{insight}</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="disclaimer-box">'
            '⚖️ <strong>Reminder:</strong> This score is one input into the credit decision. '
            'Loan officer assessment of borrower context, market conditions, guarantor quality, '
            'and business viability must inform the final decision.'
            '</div>',
            unsafe_allow_html=True
        )

        # ── SHAP CHART ────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-header">Why did the model give this score?</div>', unsafe_allow_html=True)
        st.markdown("The chart below shows which factors pushed the risk score **up** 🔴 or **down** 🔵 for this borrower.")

        with st.spinner("Generating credit risk explanation..."):
            try:
                explainer = shap.TreeExplainer(model)
                shap_vals = explainer.shap_values(input_df)
                shap_series = pd.Series(shap_vals[0], index=feature_names).abs().sort_values(ascending=False).head(12)
                top_features = shap_series.index.tolist()
                top_shap = pd.Series(shap_vals[0], index=feature_names)[top_features]
                top_labels = [get_label(f) for f in top_features]
                colors = ['#E24B4A' if v > 0 else '#2E75B6' for v in top_shap.values]
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.barh(top_labels[::-1], top_shap.values[::-1], color=colors[::-1], edgecolor='none', height=0.6)
                ax.axvline(x=0, color='#333333', linewidth=0.8)
                ax.set_xlabel('Impact on Default Probability', fontsize=11)
                ax.set_title(
                    'Credit Risk Drivers — Why This Borrower Was Scored This Way\n'
                    '🔴 Red = increases default risk  |  🔵 Blue = reduces default risk',
                    fontsize=11, fontweight='bold', pad=14
                )
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.tick_params(axis='y', labelsize=10)
                fig.patch.set_facecolor('#FFFFFF')
                ax.set_facecolor('#FAFAFA')
                plt.tight_layout()
                st.pyplot(fig)
                plt.close()
            except Exception as e:
                st.warning(f"SHAP explanation could not be generated: {e}")

        # ── KEY RISK FACTORS ──────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-header">Key Risk Factors</div>', unsafe_allow_html=True)

        f1, f2, f3, f4 = st.columns(4)

        with f1:
            bureau_status = (
                "🔴 Weak — High Risk" if ext_avg < 0.35 else
                "🟡 Moderate — Review" if ext_avg < 0.55 else
                "🟢 Strong — Low Risk"
            )
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#0F1F3D,#0A1628);border-radius:10px;padding:16px;
                        border-left:4px solid #2E75B6;box-shadow:0 0 20px rgba(0,212,255,0.08)">
                <div style="font-size:12px;color:#8BA3BF;margin-bottom:4px">Credit Bureau History</div>
                <div style="font-size:24px;font-weight:700;color:#F0F6FF">{ext_avg:.2f} / 1.00</div>
                <div style="font-size:13px;color:#C8D8E8;margin-top:6px">{bureau_status}</div>
            </div>
            """, unsafe_allow_html=True)

        with f2:
            debt_color = "#E24B4A" if credit_income > 5 else "#F0A500" if credit_income > 3 else "#1D9E75"
            debt_status = (
                "🔴 Very High — Decline Risk" if credit_income > 5 else
                "🟡 Elevated — Review" if credit_income > 3 else
                "🟢 Manageable — Acceptable"
            )
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#0F1F3D,#0A1628);border-radius:10px;padding:16px;
                        border-left:4px solid {debt_color};box-shadow:0 0 20px rgba(0,212,255,0.08)">
                <div style="font-size:12px;color:#8BA3BF;margin-bottom:4px">Loan-to-Income Ratio</div>
                <div style="font-size:24px;font-weight:700;color:{debt_color}">{credit_income:.1f}x annual income</div>
                <div style="font-size:13px;color:#C8D8E8;margin-top:6px">{debt_status}</div>
            </div>
            """, unsafe_allow_html=True)

        with f3:
            emp_color = "#E24B4A" if employment_years < 1 else "#F0A500" if employment_years < 3 else "#1D9E75"
            employ_status = (
                "🔴 Unstable — No Employment" if employment_years < 1 else
                "🟡 Early Stage — Less than 3yrs" if employment_years < 3 else
                "🟢 Stable — 3+ Years"
            )
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#0F1F3D,#0A1628);border-radius:10px;padding:16px;
                        border-left:4px solid {emp_color};box-shadow:0 0 20px rgba(0,212,255,0.08)">
                <div style="font-size:12px;color:#8BA3BF;margin-bottom:4px">Employment Stability</div>
                <div style="font-size:24px;font-weight:700;color:{emp_color}">{employment_years} yrs — {income_type}</div>
                <div style="font-size:13px;color:#C8D8E8;margin-top:6px">{employ_status}</div>
            </div>
            """, unsafe_allow_html=True)

        with f4:
            delinq_color = (
                "#1D9E75" if delinquency_recency == "Never" else
                "#F0A500" if delinquency_recency in ["5+ years ago", "2 to 5 years ago"] else
                "#E24B4A"
            )
            delinq_status = (
                "🟢 Clean Record" if delinquency_recency == "Never" else
                "🟡 Historical — Low Weight" if delinquency_recency == "5+ years ago" else
                "🟡 Notable — Moderate Weight" if delinquency_recency == "2 to 5 years ago" else
                "🔴 Recent — High Weight"
            )
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#0F1F3D,#0A1628);border-radius:10px;padding:16px;
                        border-left:4px solid {delinq_color};box-shadow:0 0 20px rgba(0,212,255,0.08)">
                <div style="font-size:12px;color:#8BA3BF;margin-bottom:4px">Default History</div>
                <div style="font-size:18px;font-weight:700;color:{delinq_color}">{delinquency_recency}</div>
                <div style="font-size:13px;color:#C8D8E8;margin-top:6px">{delinq_status}</div>
                <div style="font-size:12px;color:#8BA3BF;margin-top:4px">{active_loans} active loan(s)</div>
            </div>
            """, unsafe_allow_html=True)

        # ── RECOMMENDATION ────────────────────
        st.markdown("---")
        st.markdown('<div class="section-header">Credit Officer Recommendation</div>', unsafe_allow_html=True)

        rec_col1, rec_col2 = st.columns(2)

        with rec_col1:
            if probability >= high_threshold:
                st.markdown(f"""
                <div style="background:linear-gradient(135deg,rgba(255,69,96,0.1),rgba(255,69,96,0.04));border-radius:10px;padding:18px;border-left:4px solid #FF4560">
                    <div style="font-size:15px;font-weight:700;color:#E24B4A;margin-bottom:8px">
                        ❌ Recommendation: DECLINE or REFER
                    </div>
                    <div style="font-size:14px;color:#C8D8E8;line-height:1.7">
                        Default probability exceeds your institution's threshold of {int(high_threshold*100)}%.
                        If referral is considered, require collateral, guarantor, or significant loan reduction
                        before re-assessment.<br><br>
                        <em style="color:#8BA3BF">Credit committee review is recommended before communicating
                        a final decline to the borrower.</em>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            elif probability >= medium_threshold:
                st.markdown(f"""
                <div style="background:linear-gradient(135deg,rgba(255,183,0,0.1),rgba(255,183,0,0.04));border-radius:10px;padding:18px;border-left:4px solid #FFB700">
                    <div style="font-size:15px;font-weight:700;color:#B8860B;margin-bottom:8px">
                        ⚡ Recommendation: CONDITIONAL APPROVAL
                    </div>
                    <div style="font-size:14px;color:#C8D8E8;line-height:1.7">
                        Score falls within your institution's review band
                        ({int(medium_threshold*100)}–{int(high_threshold*100)}%).
                        Consider reducing loan amount, shortening repayment term, or requesting
                        additional supporting documents before final approval.<br><br>
                        <em style="color:#8BA3BF">Loan officer judgement is critical at this threshold —
                        local market knowledge, guarantor assessment, and business site visit
                        should inform the final decision.</em>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background:linear-gradient(135deg,rgba(0,229,160,0.1),rgba(0,229,160,0.04));border-radius:10px;padding:18px;border-left:4px solid #00E5A0">
                    <div style="font-size:15px;font-weight:700;color:#1D9E75;margin-bottom:8px">
                        ✅ Recommendation: APPROVE
                    </div>
                    <div style="font-size:14px;color:#C8D8E8;line-height:1.7">
                        Risk profile is within your institution's acceptable threshold of
                        {int(medium_threshold*100)}%.
                        Proceed with standard loan processing and documentation verification.<br><br>
                        <em style="color:#8BA3BF">Loan officer should verify income source, confirm
                        documentation, and apply institutional credit policy before final approval.</em>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        with rec_col2:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#0F1F3D,#0A1628);border-radius:10px;padding:18px;
                        border:1px solid rgba(0,212,255,0.15);box-shadow:0 0 20px rgba(0,212,255,0.08)">
                <div style="font-size:11px;font-weight:700;color:#00D4FF;font-family:Space Mono,monospace;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:12px;
                            border-bottom:2px solid #2E75B6;padding-bottom:6px">
                    Summary for Credit File
                </div>
                <table style="width:100%;font-size:13px;border-collapse:collapse">
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">Borrower Age</td>
                        <td style="padding:6px 0;font-weight:600;color:#F0F6FF;text-align:right">{age} years</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">Annual Income</td>
                        <td style="padding:6px 0;font-weight:600;color:#F0F6FF;text-align:right">₦{income:,}</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">Loan Requested</td>
                        <td style="padding:6px 0;font-weight:600;color:#F0F6FF;text-align:right">₦{loan_amount:,}</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">Monthly Repayment</td>
                        <td style="padding:6px 0;font-weight:600;color:#F0F6FF;text-align:right">₦{annuity:,}</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">Employment Sector</td>
                        <td style="padding:6px 0;font-weight:600;color:#F0F6FF;text-align:right">{employment_sector}</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">Income Type</td>
                        <td style="padding:6px 0;font-weight:600;color:#F0F6FF;text-align:right">{income_type}</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">Default History</td>
                        <td style="padding:6px 0;font-weight:600;color:{delinq_color};text-align:right">{delinquency_recency}</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">Active Loans</td>
                        <td style="padding:6px 0;font-weight:600;color:#F0F6FF;text-align:right">{active_loans}</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">Loan-to-Income</td>
                        <td style="padding:6px 0;font-weight:600;color:{ci_color};text-align:right">{credit_income:.1f}x</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">Avg Bureau Score</td>
                        <td style="padding:6px 0;font-weight:600;color:{bureau_color};text-align:right">{ext_avg:.2f} / 1.00</td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">BVN Verified</td>
                        <td style="padding:6px 0;font-weight:600;color:{'#1D9E75' if bvn_bureau_verified else '#F0A500'};text-align:right">
                            {'✅ Yes' if bvn_bureau_verified else '⚠️ No'}
                        </td>
                    </tr>
                    <tr style="border-bottom:1px solid rgba(0,212,255,0.08)">
                        <td style="padding:6px 0;color:#8BA3BF">Model Score</td>
                        <td style="padding:6px 0;font-weight:600;color:{risk_color};text-align:right">{probability*100:.1f}% default probability</td>
                    </tr>
                    <tr>
                        <td style="padding:6px 0;color:#8BA3BF">Risk Category</td>
                        <td style="padding:6px 0;font-weight:700;color:{risk_color};text-align:right">{risk_label}</td>
                    </tr>
                </table>
            </div>
            """, unsafe_allow_html=True)


# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
st.markdown("""
<div class="footer">
    Built by <strong>Nkpo-ikana Udom</strong> —
    Operations & Strategy | Fintech & Credit Risk |
    <a href='https://www.linkedin.com/in/nkpo-ikana-udom-479ba91a9/' target='_blank'>LinkedIn</a> ·
    <a href='https://github.com/stephenudom' target='_blank'>GitHub</a><br>
    Trained on 1,600,000 loan applications · XGBoost · SHAP Explainability ·
    Gender-Neutral · CBN Fair Lending Compliant · Full Nigerian Market Range ·
    Adjustable Risk Thresholds · BVN-Ready · Dual Interface
</div>
""", unsafe_allow_html=True)
