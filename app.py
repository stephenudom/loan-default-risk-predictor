import streamlit as st
import numpy as np
import io
import os
import random

st.set_page_config(
    page_title="Joyful Smile Nigeria Limited — Loan Portal",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box}
:root{
  --navy:#0B1F3A;--navy-mid:#122540;--navy-light:#1A3457;
  --teal:#009B8D;--teal-light:#00B8A8;--teal-pale:#E6F7F6;--teal-dark:#007A6E;
  --white:#FFFFFF;--off-white:#F8FAFB;
  --text-primary:#0B1F3A;--text-secondary:#4A6480;--text-muted:#7A94AC;
  --border:#D4E1ED;--border-focus:#009B8D;
  --error:#C0392B;--error-bg:#FDF2F1;
  --success:#0F7B6C;--success-bg:#E6F7F4;
  --amber:#B8860B;--amber-bg:#FFF8E6;
  --radius:8px;--radius-lg:12px;--radius-xl:16px;
}

/* ── HIDE STREAMLIT CHROME ── */
#MainMenu,footer,header{visibility:hidden}
.block-container{padding:0!important;max-width:100%!important}
section[data-testid="stSidebar"]{display:none!important}
[data-testid="stAppViewContainer"]{background:var(--off-white)!important}

/* ── BODY ── */
body,html,[class*="css"]{font-family:'DM Sans',sans-serif!important;color:var(--text-primary)!important}

/* ── MODE GATE ── */
.gate-wrap{
  min-height:100vh;background:var(--navy);
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  padding:40px 20px;
}
.gate-brand{font-family:'Cormorant Garamond',serif;font-size:44px;font-weight:600;color:#fff;margin-bottom:4px;letter-spacing:-0.01em}
.gate-brand span{color:#00B8A8}
.gate-tagline{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:18px;color:rgba(255,255,255,0.4);margin-bottom:10px}
.gate-rc{font-size:11px;color:rgba(255,255,255,0.22);letter-spacing:0.1em;text-transform:uppercase;margin-bottom:52px}
.gate-cards{display:flex;gap:20px;flex-wrap:wrap;justify-content:center}
.gate-card{
  width:276px;background:rgba(255,255,255,0.04);
  border:1px solid rgba(0,155,141,0.22);border-radius:var(--radius-xl);
  padding:34px 30px;text-align:left;
}
.gate-card-icon{width:46px;height:46px;background:rgba(0,155,141,0.14);border-radius:11px;display:flex;align-items:center;justify-content:center;margin-bottom:18px}
.gate-card-title{font-size:18px;font-weight:600;color:#fff;margin-bottom:6px}
.gate-card-desc{font-size:12px;color:rgba(255,255,255,0.4);line-height:1.7;margin-bottom:18px}
.gate-card-arrow{font-size:11px;color:#00B8A8;font-weight:600;letter-spacing:0.06em;text-transform:uppercase}

/* ── SIDEBAR ── */
.jsn-sidebar{
  width:280px;flex-shrink:0;background:var(--navy);
  height:100vh;position:sticky;top:0;
  display:flex;flex-direction:column;padding:32px 26px;
  overflow:hidden;
}
.brand-name{font-family:'Cormorant Garamond',serif;font-size:19px;font-weight:600;color:#fff;line-height:1.25}
.brand-name span{color:#00B8A8}
.brand-tagline{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:12px;color:rgba(255,255,255,0.32);margin-top:3px}
.brand-rc{font-size:10px;color:rgba(255,255,255,0.18);letter-spacing:0.1em;text-transform:uppercase;margin-top:2px}
.mode-badge{
  display:inline-flex;align-items:center;gap:6px;
  background:rgba(0,155,141,0.14);border:1px solid rgba(0,155,141,0.28);
  border-radius:20px;padding:5px 11px;
  font-size:10px;font-weight:600;color:#00B8A8;
  letter-spacing:0.06em;text-transform:uppercase;margin:18px 0;
}
.sb-div{height:1px;background:rgba(255,255,255,0.07);margin:0 0 16px}
.step-item{display:flex;align-items:flex-start;gap:11px;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.04)}
.step-item:last-child{border-bottom:none}
.step-num{
  width:27px;height:27px;flex-shrink:0;border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-size:11px;font-weight:600;
  border:1.5px solid rgba(255,255,255,0.16);color:rgba(255,255,255,0.3);
  margin-top:1px;transition:all 0.2s;
}
.step-num.active{background:var(--teal);border-color:var(--teal);color:#fff}
.step-num.done{background:rgba(0,155,141,0.18);border-color:var(--teal);color:#00B8A8}
.step-title{font-size:13px;color:rgba(255,255,255,0.4);font-weight:500;margin-bottom:1px}
.step-title.active{color:#fff}
.step-title.done{color:rgba(255,255,255,0.55)}
.step-lbl{font-size:10px;color:rgba(255,255,255,0.22);line-height:1.3}
.step-lbl.active{color:rgba(255,255,255,0.48)}
.sb-footer{margin-top:auto;padding-top:18px;border-top:1px solid rgba(255,255,255,0.07)}
.sb-flabel{font-size:10px;color:rgba(255,255,255,0.26);letter-spacing:0.08em;text-transform:uppercase;margin-bottom:5px}
.sb-contact{font-size:12px;color:#00B8A8;font-weight:500;line-height:1.8}
.sb-address{font-size:10px;color:rgba(255,255,255,0.2);line-height:1.6;margin-top:4px}

/* ── TOP BAR ── */
.top-bar{background:#fff;border-bottom:1px solid var(--border);padding:13px 40px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:10}
.tb-left{font-size:12px;color:var(--text-muted)}
.tb-left strong{color:var(--text-primary)}
.prog-wrap{flex:1;max-width:220px;background:var(--border);border-radius:4px;height:3px;margin:0 18px;overflow:hidden}
.prog-fill{height:100%;background:var(--teal);border-radius:4px;transition:width 0.3s}
.tb-right{font-size:11px;color:var(--text-muted);font-weight:500}

/* ── SECTION HEADERS ── */
.eyebrow{font-size:10px;letter-spacing:0.14em;text-transform:uppercase;color:var(--teal);font-weight:600;margin-bottom:6px}
.sec-h1{font-family:'Cormorant Garamond',serif;font-size:28px;font-weight:600;color:var(--navy);line-height:1.2;margin-bottom:7px}
.sec-desc{font-size:13px;color:var(--text-secondary);margin-bottom:28px;line-height:1.6;max-width:500px}

/* ── FORM AREA ── */
.form-area{flex:1;padding:40px 40px 80px;max-width:800px}

/* ── LABELS ── */
.fl{font-size:11px!important;font-weight:600!important;color:var(--text-secondary)!important;letter-spacing:0.05em!important;text-transform:uppercase!important}

/* ── STREAMLIT INPUT OVERRIDES ── */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stSelectbox"] select{
  border:1.5px solid var(--border)!important;
  border-radius:var(--radius)!important;
  font-family:'DM Sans',sans-serif!important;
  font-size:14px!important;
  color:var(--text-primary)!important;
  background:#fff!important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stNumberInput"] input:focus{
  border-color:var(--teal)!important;
  box-shadow:0 0 0 3px rgba(0,155,141,0.1)!important;
}
.stSelectbox [data-baseweb="select"] > div{
  border:1.5px solid var(--border)!important;
  border-radius:var(--radius)!important;
  background:#fff!important;
}

/* ── REVIEW BLOCKS ── */
.rv-block{background:#fff;border:1px solid var(--border);border-radius:var(--radius-xl);margin-bottom:16px;overflow:hidden}
.rv-hd{padding:13px 20px;background:var(--off-white);border-bottom:1px solid var(--border);font-size:12px;font-weight:600;color:var(--text-primary)}
.rv-bd{padding:12px 20px}
.rv-row{display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid rgba(212,225,237,0.35);gap:14px;font-size:12px}
.rv-row:last-child{border-bottom:none}
.rv-key{color:var(--text-muted);flex:1}
.rv-val{font-weight:500;color:var(--text-primary);text-align:right}
.bdg{display:inline-flex;padding:2px 9px;border-radius:20px;font-size:10px;font-weight:700;letter-spacing:0.04em}
.bdg-ok{background:var(--success-bg);color:var(--success)}
.bdg-miss{background:var(--error-bg);color:var(--error)}
.bdg-info{background:var(--teal-pale);color:var(--teal-dark)}
.bdg-warn{background:var(--amber-bg);color:var(--amber)}

/* ── CALLOUT ── */
.callout{display:flex;gap:11px;padding:13px 15px;border-radius:var(--radius-lg);margin-bottom:20px}
.callout-info{background:#EEF6FF;border:1px solid #B5D4F4}
.callout-warn{background:var(--amber-bg);border:1px solid #FAD97A}
.callout-icon{width:18px;height:18px;flex-shrink:0;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:700;margin-top:1px}
.callout-info .callout-icon{background:#B5D4F4;color:#0C447C}
.callout-warn .callout-icon{background:#FAD97A;color:#633806}
.callout-body{font-size:12px;line-height:1.6;color:var(--text-primary)}

/* ── VALIDATION ERROR ── */
.val-error{background:var(--error-bg);border:1px solid rgba(192,57,43,0.25);border-radius:var(--radius);padding:11px 15px;font-size:13px;color:var(--error);margin-bottom:16px;font-weight:500}
.val-error ul{margin:6px 0 0 18px;padding:0}
.val-error ul li{margin-bottom:3px;font-size:12px}

/* ── FILE UPLOAD ── */
[data-testid="stFileUploader"]{
  border:2px dashed var(--border)!important;
  border-radius:var(--radius-lg)!important;
  background:#fff!important;
  padding:8px!important;
}
.file-ok{display:flex;align-items:center;gap:8px;padding:8px 12px;background:var(--success-bg);border:1px solid rgba(15,123,108,0.18);border-radius:var(--radius);margin-top:4px;font-size:12px;color:var(--success);font-weight:500}

/* ── DSR CARD ── */
.dsr-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius-lg);padding:15px 17px;margin-bottom:20px}
.dsr-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:9px}
.dsr-cell{text-align:center;padding:10px;background:var(--off-white);border-radius:var(--radius)}
.dsr-lbl{font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:3px}
.dsr-val{font-size:16px;font-weight:600;color:var(--text-primary)}

/* ── SUCCESS ── */
.success-wrap{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:70px 40px;min-height:70vh}
.success-circle{width:70px;height:70px;background:var(--success-bg);border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 22px}
.success-h{font-family:'Cormorant Garamond',serif;font-size:32px;font-weight:600;color:var(--navy);margin-bottom:6px}
.success-ref{display:inline-block;font-family:monospace;font-size:18px;font-weight:700;color:var(--teal);background:var(--teal-pale);border:1px solid rgba(0,155,141,0.2);border-radius:7px;padding:7px 22px;margin:16px 0;letter-spacing:0.1em}
.success-note{font-size:13px;color:var(--text-secondary);max-width:400px;line-height:1.7;margin:0 auto}
.success-steps{display:flex;gap:12px;margin:24px 0;justify-content:center;flex-wrap:wrap}
.ss-step{background:#fff;border:1px solid var(--border);border-radius:var(--radius-lg);padding:13px 16px;text-align:left;width:164px}
.ss-n{font-size:10px;font-weight:700;color:var(--teal);letter-spacing:0.08em;text-transform:uppercase;margin-bottom:4px}
.ss-t{font-size:12px;color:var(--text-primary);line-height:1.4}

/* ── OFFICER TOPBAR ── */
.o-topbar{background:var(--navy);padding:13px 36px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(0,155,141,0.18)}
.o-brand{font-family:'Cormorant Garamond',serif;font-size:16px;font-weight:600;color:#fff}
.o-brand span{color:#00B8A8}
.o-badge{background:rgba(0,155,141,0.14);border:1px solid rgba(0,155,141,0.28);border-radius:20px;padding:4px 11px;font-size:10px;font-weight:600;color:#00B8A8;letter-spacing:0.06em;text-transform:uppercase}

/* ── OFFICER APP CARD ── */
.app-card{background:#fff;border:1px solid var(--border);border-radius:var(--radius-lg);padding:16px 20px;margin-bottom:10px;display:flex;align-items:center;gap:14px;cursor:pointer;transition:border-color 0.15s}
.app-card:hover{border-color:var(--teal)}
.app-avatar{width:42px;height:42px;background:var(--navy);border-radius:11px;display:flex;align-items:center;justify-content:center;font-family:'Cormorant Garamond',serif;font-size:16px;font-weight:600;color:#00B8A8;flex-shrink:0}
.app-name{font-size:15px;font-weight:600;color:var(--text-primary);margin-bottom:3px}
.app-meta{font-size:11px;color:var(--text-muted)}
.app-amount{font-size:14px;font-weight:600;color:var(--navy)}
.app-time{font-size:10px;color:var(--text-muted);margin-top:2px}

/* ── DETAIL PANEL ── */
.dp-header{background:var(--navy);padding:20px 26px;border-radius:var(--radius-xl) var(--radius-xl) 0 0;display:flex;align-items:flex-start;justify-content:space-between}
.dp-name{font-family:'Cormorant Garamond',serif;font-size:22px;font-weight:600;color:#fff}
.dp-ref{font-size:10px;color:rgba(255,255,255,0.35);margin-top:2px;font-family:monospace;letter-spacing:0.08em}
.dp-sec{font-size:10px;font-weight:600;color:var(--text-muted);letter-spacing:0.1em;text-transform:uppercase;margin:18px 0 10px}
.dp-sec:first-child{margin-top:0}
.dp-grid{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-bottom:4px}
.dp-field{background:var(--off-white);border-radius:var(--radius);padding:11px 13px}
.dp-flbl{font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:3px}
.dp-fval{font-size:13px;font-weight:500;color:var(--text-primary)}
.dp-field.full{grid-column:1/-1}
.doc-row{display:flex;align-items:center;justify-content:space-between;padding:10px 12px;background:var(--off-white);border-radius:var(--radius);margin-bottom:7px}
.doc-name{font-size:13px;font-weight:500;color:var(--text-primary)}
.doc-file{font-size:11px;color:var(--text-muted);margin-top:1px}

/* ── LOGIN ── */
.login-wrap{display:flex;align-items:center;justify-content:center;min-height:100vh;background:var(--off-white)}
.login-card{width:380px;background:#fff;border:1px solid var(--border);border-radius:var(--radius-xl);padding:38px 34px}
.login-brand{font-family:'Cormorant Garamond',serif;font-size:21px;font-weight:600;color:var(--navy);margin-bottom:3px}
.login-brand span{color:var(--teal)}
.login-bar{height:3px;background:linear-gradient(90deg,var(--teal),var(--navy));border-radius:2px;margin:18px 0 24px}

/* ── DIVIDER ── */
.divider{display:flex;align-items:center;gap:10px;margin:22px 0}
.div-line{flex:1;height:1px;background:var(--border)}
.div-lbl{font-size:11px;color:var(--text-muted);white-space:nowrap;font-weight:500}

/* ── STBUTTON OVERRIDES ── */
.stButton>button{
  font-family:'DM Sans',sans-serif!important;
  font-weight:600!important;font-size:14px!important;
  border-radius:var(--radius)!important;
  height:46px!important;padding:0 24px!important;
  transition:all 0.15s!important;
}
.btn-primary-style>button{background:var(--teal)!important;color:#fff!important;border:none!important}
.btn-primary-style>button:hover{background:var(--teal-light)!important}
.btn-navy-style>button{background:var(--navy)!important;color:#fff!important;border:none!important}
.btn-outline-style>button{background:#fff!important;color:var(--text-primary)!important;border:1.5px solid var(--border)!important}
.btn-approve-style>button{background:var(--success-bg)!important;color:var(--success)!important;border:1px solid rgba(15,123,108,0.25)!important}
.btn-approve-style>button:hover{background:var(--success)!important;color:#fff!important}
.btn-decline-style>button{background:var(--error-bg)!important;color:var(--error)!important;border:1px solid rgba(192,57,43,0.2)!important}
.btn-decline-style>button:hover{background:var(--error)!important;color:#fff!important}
.btn-review-style>button{background:var(--amber-bg)!important;color:var(--amber)!important;border:1px solid rgba(184,134,11,0.2)!important}

/* ── CHECKBOX ── */
.stCheckbox label{font-family:'DM Sans',sans-serif!important;font-size:13px!important;color:var(--text-primary)!important}
[data-testid="stCheckbox"]{border:1.5px solid var(--border);border-radius:var(--radius);padding:11px 14px;background:#fff;margin-bottom:8px}

/* ── HR ── */
hr{border-color:var(--border)!important;margin:20px 0!important}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# SESSION STATE INIT
# ─────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "mode": "gate",          # gate | applicant | officer_login | officer
        "app_step": 1,
        "submitted": False,
        "app_ref": "",
        "applications": [],
        "selected_app": -1,
        "officer_view": "inbox",
        # Step 1
        "a_fname": "OduduAbasi", "a_lname": "Nkpo-Ikana", "a_mname": "",
        "a_dob": "", "a_phone": "", "a_email": "", "a_marital": "",
        "a_deps": 0, "a_fam": 1, "a_edu": "", "a_state": "", "a_address": "",
        # Step 2
        "a_empstat": "", "a_sector": "", "a_employer": "", "a_empyrs": "",
        "a_inctype": "", "a_payfreq": "", "a_income": 0, "a_otherinc": 0,
        "a_oblig": 0, "a_actloans": 0, "a_default": "Never defaulted",
        "a_workphone": "",
        # Step 3
        "a_lamount": 0, "a_tenure": "", "a_purpose": "", "a_ltype": "Cash Loan",
        "a_ldesc": "", "a_collateral": 0, "a_guarantor": "No guarantor",
        # Step 4 - files stored as dicts
        "a_files": {},
        # Step 5
        "a_bvn": "", "a_bvnconsent": False,
        "a_d1": False, "a_d2": False, "a_d3": False,
        # Officer decisions
        "officer_decisions": {},
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ─────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────
def fmtN(n):
    try:
        return "₦{:,.0f}".format(float(n))
    except Exception:
        return "—"

def doc_badge(has):
    if has:
        return '<span class="bdg bdg-ok">✓ Uploaded</span>'
    return '<span class="bdg bdg-miss">Not Uploaded</span>'

def status_badge(s):
    colors = {"Pending": "bdg-info", "Approved": "bdg-ok", "Declined": "bdg-miss", "Under Review": "bdg-warn"}
    cls = colors.get(s, "bdg-info")
    return f'<span class="bdg {cls}">{s}</span>'

def sidebar_html(step, mode_label):
    steps = [
        ("Personal Details", "Identity & contact"),
        ("Employment & Income", "Work & earnings"),
        ("Loan Request", "Amount & purpose"),
        ("Documents", "Supporting files"),
        ("BVN & Review", "Verify & submit"),
    ]
    items = ""
    for i, (title, label) in enumerate(steps, 1):
        num_cls = "active" if i == step else ("done" if i < step else "")
        t_cls = "active" if i == step else ("done" if i < step else "")
        l_cls = "active" if i == step else ""
        items += f"""
        <div class="step-item">
          <div class="step-num {num_cls}">{i}</div>
          <div>
            <div class="step-title {t_cls}">{title}</div>
            <div class="step-lbl {l_cls}">{label}</div>
          </div>
        </div>"""
    return f"""
    <div class="jsn-sidebar">
      <div class="brand-name">Joyful<span>Smiles</span></div>
      <div class="brand-tagline">Confidence reassured...</div>
      <div class="brand-rc">RC No. 8967399</div>
      <div class="mode-badge">{mode_label}</div>
      <div class="sb-div"></div>
      <div>{items}</div>
      <div class="sb-footer">
        <div class="sb-flabel">Need assistance?</div>
        <div class="sb-contact">07010057527 · 08136021246</div>
        <div class="sb-address">5, Shosanya Close, Aboru,<br>Iyana Ipaja, Lagos State</div>
      </div>
    </div>"""

def topbar_html(step_name, step_num, pct):
    return f"""
    <div class="top-bar">
      <div class="tb-left">Loan Application &nbsp;/&nbsp; <strong>{step_name}</strong></div>
      <div class="prog-wrap"><div class="prog-fill" style="width:{pct}%"></div></div>
      <div class="tb-right">Step {step_num} of 5</div>
    </div>"""


# ─────────────────────────────────────────────────────────────
# VALIDATION
# ─────────────────────────────────────────────────────────────
def validate_step1():
    errors = []
    if not st.session_state.a_fname.strip():
        errors.append("First Name is required")
    if not st.session_state.a_lname.strip():
        errors.append("Last Name is required")
    if not st.session_state.a_dob.strip():
        errors.append("Date of Birth is required")
    if not st.session_state.a_phone.strip():
        errors.append("Phone Number is required")
    if not st.session_state.a_marital or st.session_state.a_marital == "Select":
        errors.append("Marital Status is required")
    if not st.session_state.a_edu or st.session_state.a_edu == "Select":
        errors.append("Education Level is required")
    if not st.session_state.a_state or st.session_state.a_state == "Select state":
        errors.append("Residential State is required")
    if not st.session_state.a_address.strip():
        errors.append("Residential Address is required")
    return errors

def validate_step2():
    errors = []
    if not st.session_state.a_empstat or st.session_state.a_empstat == "Select":
        errors.append("Employment Status is required")
    if not st.session_state.a_sector or st.session_state.a_sector == "Select sector":
        errors.append("Employment Sector is required")
    if not st.session_state.a_empyrs or st.session_state.a_empyrs == "Select":
        errors.append("Years in Current Role is required")
    if not st.session_state.a_inctype or st.session_state.a_inctype == "Select":
        errors.append("Income Type is required")
    if not st.session_state.a_payfreq or st.session_state.a_payfreq == "Select":
        errors.append("Pay Frequency is required")
    if not st.session_state.a_income or st.session_state.a_income <= 0:
        errors.append("Monthly Net Income must be greater than zero")
    return errors

def validate_step3():
    errors = []
    if not st.session_state.a_lamount or st.session_state.a_lamount < 10000:
        errors.append("Loan Amount must be at least ₦10,000")
    if not st.session_state.a_tenure or st.session_state.a_tenure == "Select":
        errors.append("Loan Tenure is required")
    if not st.session_state.a_purpose or st.session_state.a_purpose == "Select purpose":
        errors.append("Purpose of Loan is required")
    return errors

def validate_step4():
    errors = []
    files = st.session_state.a_files
    if "biz" not in files:
        errors.append("Business Registration Certificate is required")
    if "bank" not in files:
        errors.append("6 Months Bank Statement is required")
    if "tin" not in files:
        errors.append("TIN Certificate is required")
    if "util" not in files:
        errors.append("Utility Bill / Proof of Address is required")
    return errors

def validate_step5():
    errors = []
    bvn = st.session_state.a_bvn.strip()
    if not bvn or not bvn.isdigit() or len(bvn) != 11:
        errors.append("A valid 11-digit BVN is required")
    if not st.session_state.a_bvnconsent:
        errors.append("BVN bureau verification consent is required")
    if not st.session_state.a_d1:
        errors.append("Please confirm Declaration 1 (information accuracy)")
    if not st.session_state.a_d2:
        errors.append("Please confirm Declaration 2 (authorisation to verify)")
    if not st.session_state.a_d3:
        errors.append("Please confirm Declaration 3 (Terms & Conditions)")
    return errors

def show_errors(errors):
    if errors:
        items = "".join(f"<li>{e}</li>" for e in errors)
        st.markdown(
            f'<div class="val-error">⚠ Please complete the following before continuing:<ul>{items}</ul></div>',
            unsafe_allow_html=True
        )
        return True
    return False


# ─────────────────────────────────────────────────────────────
# MODE: GATE
# ─────────────────────────────────────────────────────────────
if st.session_state.mode == "gate":
    st.markdown("""
    <div class="gate-wrap">
      <div class="gate-brand">Joyful<span>Smiles</span></div>
      <div class="gate-tagline">Confidence reassured...</div>
      <div class="gate-rc">RC No. 8967399 &nbsp;·&nbsp; 5, Shosanya Close, Aboru, Iyana Ipaja, Lagos State</div>
      <div class="gate-cards">
        <div class="gate-card">
          <div class="gate-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#00B8A8" stroke-width="1.8">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>
            </svg>
          </div>
          <div class="gate-card-title">Loan Applicant</div>
          <div class="gate-card-desc">Apply for a business or personal loan. Complete the guided 5-step form and submit your documents securely.</div>
          <div class="gate-card-arrow">▶ Apply Now</div>
        </div>
        <div class="gate-card" style="margin-left:4px">
          <div class="gate-card-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#00B8A8" stroke-width="1.8">
              <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>
            </svg>
          </div>
          <div class="gate-card-title">Loan Officer</div>
          <div class="gate-card-desc">Review submitted applications, download documents, and make credit decisions from the officer dashboard.</div>
          <div class="gate-card-arrow">▶ Officer Login</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns([2, 1, 0.5, 1, 2])
    with col2:
        if st.button("Apply for a Loan", use_container_width=True):
            st.session_state.mode = "applicant"
            st.rerun()
    with col4:
        if st.button("Officer Login", use_container_width=True):
            st.session_state.mode = "officer_login"
            st.rerun()


# ─────────────────────────────────────────────────────────────
# MODE: OFFICER LOGIN
# ─────────────────────────────────────────────────────────────
elif st.session_state.mode == "officer_login":
    st.markdown('<div class="login-wrap">', unsafe_allow_html=True)
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.markdown("""
        <div class="login-card">
          <div class="login-brand">Joyful<span>Smiles</span> Officer Portal</div>
          <div style="font-size:12px;color:var(--text-muted);margin-top:3px">Loan Officer Access — RC No. 8967399</div>
          <div class="login-bar"></div>
        </div>
        """, unsafe_allow_html=True)

        email = st.text_input("Officer ID / Email", placeholder="officer@joyfulsmiles.com", value="admin@joyfulsmiles.com")
        password = st.text_input("Password", type="password", placeholder="Enter password", value="password123")

        c1, c2 = st.columns(2)
        with c1:
            if st.button("← Back to Home", use_container_width=True):
                st.session_state.mode = "gate"
                st.rerun()
        with c2:
            if st.button("Sign In →", use_container_width=True):
                if email and password:
                    st.session_state.mode = "officer"
                    st.rerun()
                else:
                    st.error("Please enter your credentials.")
    st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# MODE: APPLICANT
# ─────────────────────────────────────────────────────────────
elif st.session_state.mode == "applicant":

    step = st.session_state.app_step
    step_names = ["Personal Details", "Employment & Income", "Loan Request", "Documents", "BVN & Review"]
    step_pct = [20, 40, 60, 80, 100]

    # Layout
    sidebar_col, main_col = st.columns([0.34, 1])

    with sidebar_col:
        st.markdown(sidebar_html(step, "Loan Application"), unsafe_allow_html=True)
        if st.button("← Home", key="app_home"):
            st.session_state.mode = "gate"
            st.rerun()

    with main_col:

        if st.session_state.submitted:
            # SUCCESS SCREEN
            st.markdown(f"""
            <div class="success-wrap">
              <div class="success-circle">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#0F7B6C" stroke-width="2.2"><path d="M20 6L9 17l-5-5"/></svg>
              </div>
              <div class="success-h">Application Submitted</div>
              <div style="font-size:13px;color:var(--text-muted);margin-bottom:4px">Your reference number</div>
              <div class="success-ref">{st.session_state.app_ref}</div>
              <p class="success-note">Your application has been received. Our team will review your documents and contact you within <strong>24 to 48 business hours</strong>.</p>
              <div class="success-steps">
                <div class="ss-step"><div class="ss-n">01 — Received</div><div class="ss-t">Application is in our review queue</div></div>
                <div class="ss-step"><div class="ss-n">02 — Review</div><div class="ss-t">Documents and credit check within 24–48 hrs</div></div>
                <div class="ss-step"><div class="ss-n">03 — Decision</div><div class="ss-t">You will be contacted with our decision</div></div>
              </div>
              <div style="font-size:12px;color:var(--text-muted);margin-top:8px">
                Questions? Call <strong style="color:var(--teal)">07010057527 / 08136021246</strong>
              </div>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown(topbar_html(step_names[step-1], step, step_pct[step-1]), unsafe_allow_html=True)
            st.markdown('<div style="padding:36px 40px 60px;max-width:800px">', unsafe_allow_html=True)

            # ── STEP 1 ──────────────────────────────────────────
            if step == 1:
                st.markdown('<div class="eyebrow">Step 1 of 5</div>', unsafe_allow_html=True)
                st.markdown('<div class="sec-h1">Personal Details</div>', unsafe_allow_html=True)
                st.markdown('<p class="sec-desc">Provide your personal information exactly as it appears on your government-issued ID.</p>', unsafe_allow_html=True)

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">First Name *</div>', unsafe_allow_html=True)
                    st.text_input("First Name", key="a_fname", label_visibility="collapsed", placeholder="e.g. OduduAbasi")
                with c2:
                    st.markdown('<div class="fl">Last Name *</div>', unsafe_allow_html=True)
                    st.text_input("Last Name", key="a_lname", label_visibility="collapsed", placeholder="e.g. Nkpo-Ikana")

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Middle Name</div>', unsafe_allow_html=True)
                    st.text_input("Middle Name", key="a_mname", label_visibility="collapsed", placeholder="Optional")
                with c2:
                    st.markdown('<div class="fl">Date of Birth *</div>', unsafe_allow_html=True)
                    st.text_input("DOB", key="a_dob", label_visibility="collapsed", placeholder="DD / MM / YYYY")

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Phone Number *</div>', unsafe_allow_html=True)
                    st.text_input("Phone", key="a_phone", label_visibility="collapsed", placeholder="e.g. 08012345678")
                with c2:
                    st.markdown('<div class="fl">Email Address</div>', unsafe_allow_html=True)
                    st.text_input("Email", key="a_email", label_visibility="collapsed", placeholder="e.g. name@email.com")

                c1, c2, c3 = st.columns(3)
                with c1:
                    st.markdown('<div class="fl">Marital Status *</div>', unsafe_allow_html=True)
                    st.selectbox("Marital", ["Select", "Single", "Married", "Divorced", "Widowed"], key="a_marital", label_visibility="collapsed")
                with c2:
                    st.markdown('<div class="fl">No. of Dependants</div>', unsafe_allow_html=True)
                    st.number_input("Deps", key="a_deps", min_value=0, max_value=20, label_visibility="collapsed")
                with c3:
                    st.markdown('<div class="fl">Total Family Members</div>', unsafe_allow_html=True)
                    st.number_input("Fam", key="a_fam", min_value=1, max_value=20, label_visibility="collapsed")

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Highest Education Level *</div>', unsafe_allow_html=True)
                    st.selectbox("Edu", ["Select", "SSCE / O'Level", "OND / NCE", "HND / B.Sc", "Postgraduate (M.Sc / MBA)", "PhD / Doctorate", "Professional Certification", "No formal education"], key="a_edu", label_visibility="collapsed")
                with c2:
                    st.markdown('<div class="fl">Residential State *</div>', unsafe_allow_html=True)
                    states = ["Select state", "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "FCT — Abuja", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"]
                    st.selectbox("State", states, key="a_state", label_visibility="collapsed")

                st.markdown('<div class="fl">Residential Address *</div>', unsafe_allow_html=True)
                st.text_area("Address", key="a_address", label_visibility="collapsed", placeholder="House number, street, town, local government area", height=80)

                st.markdown("---")
                _, btn_col = st.columns([3, 1])
                with btn_col:
                    if st.button("Continue →", use_container_width=True, key="s1_next"):
                        errors = validate_step1()
                        if not show_errors(errors):
                            st.session_state.app_step = 2
                            st.rerun()

            # ── STEP 2 ──────────────────────────────────────────
            elif step == 2:
                st.markdown('<div class="eyebrow">Step 2 of 5</div>', unsafe_allow_html=True)
                st.markdown('<div class="sec-h1">Employment & Income</div>', unsafe_allow_html=True)
                st.markdown('<p class="sec-desc">Tell us about your work and how you earn. This helps us determine the right facility for you.</p>', unsafe_allow_html=True)

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Employment Status *</div>', unsafe_allow_html=True)
                    st.selectbox("EmpStat", ["Select", "Employed (Full-time)", "Employed (Part-time)", "Self-Employed / Business Owner", "Civil Servant / Government Employee", "Contractor / Freelancer", "Retired", "Unemployed"], key="a_empstat", label_visibility="collapsed")
                with c2:
                    st.markdown('<div class="fl">Employment Sector *</div>', unsafe_allow_html=True)
                    st.selectbox("Sector", ["Select sector", "Banking & Finance", "Government / Civil Service", "Healthcare & Pharmaceuticals", "Education & Training", "Technology & Telecoms", "Trade & Commerce", "Agriculture & Agribusiness", "Transport & Logistics", "Construction & Real Estate", "Oil & Gas", "Manufacturing", "Creative & Media", "Other"], key="a_sector", label_visibility="collapsed")

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Employer / Business Name *</div>', unsafe_allow_html=True)
                    st.text_input("Employer", key="a_employer", label_visibility="collapsed", placeholder="e.g. Lagos State Government")
                with c2:
                    st.markdown('<div class="fl">Years in Current Role *</div>', unsafe_allow_html=True)
                    st.selectbox("EmpYrs", ["Select", "Less than 6 months", "6 months to 1 year", "1 to 2 years", "2 to 5 years", "5 to 10 years", "Over 10 years"], key="a_empyrs", label_visibility="collapsed")

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Income Type *</div>', unsafe_allow_html=True)
                    st.selectbox("IncType", ["Select", "Fixed Monthly Salary", "Business Revenue (Regular)", "Commission-Based", "Irregular / Seasonal", "Pension", "Rental Income", "Multiple Sources"], key="a_inctype", label_visibility="collapsed")
                with c2:
                    st.markdown('<div class="fl">Pay Frequency *</div>', unsafe_allow_html=True)
                    st.selectbox("PayFreq", ["Select", "Monthly", "Bi-weekly", "Weekly", "Daily", "Project-based"], key="a_payfreq", label_visibility="collapsed")

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Monthly Net Income (₦) *</div>', unsafe_allow_html=True)
                    st.number_input("Income", key="a_income", min_value=0, step=1000, format="%d", label_visibility="collapsed")
                    st.markdown('<div style="font-size:11px;color:var(--text-muted);margin-top:-12px;margin-bottom:12px">Take-home income after tax and deductions</div>', unsafe_allow_html=True)
                with c2:
                    st.markdown('<div class="fl">Other Monthly Income (₦)</div>', unsafe_allow_html=True)
                    st.number_input("OtherInc", key="a_otherinc", min_value=0, step=1000, format="%d", label_visibility="collapsed")
                    st.markdown('<div style="font-size:11px;color:var(--text-muted);margin-top:-12px;margin-bottom:12px">Rental, commission, allowances, etc.</div>', unsafe_allow_html=True)

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Total Monthly Obligations (₦)</div>', unsafe_allow_html=True)
                    st.number_input("Oblig", key="a_oblig", min_value=0, step=1000, format="%d", label_visibility="collapsed")
                    st.markdown('<div style="font-size:11px;color:var(--text-muted);margin-top:-12px;margin-bottom:12px">Existing loan repayments, rent, etc.</div>', unsafe_allow_html=True)
                with c2:
                    st.markdown('<div class="fl">Number of Active Loans</div>', unsafe_allow_html=True)
                    st.number_input("ActLoans", key="a_actloans", min_value=0, max_value=50, label_visibility="collapsed")

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Previous Loan Default History</div>', unsafe_allow_html=True)
                    st.selectbox("Default", ["Never defaulted", "Defaulted — over 5 years ago", "Defaulted — 2 to 5 years ago", "Defaulted — within last 2 years"], key="a_default", label_visibility="collapsed")
                with c2:
                    st.markdown('<div class="fl">Work / Office Phone</div>', unsafe_allow_html=True)
                    st.text_input("WorkPhone", key="a_workphone", label_visibility="collapsed", placeholder="e.g. 0123456789")

                st.markdown("---")
                nav_l, nav_r = st.columns(2)
                with nav_l:
                    if st.button("← Back", use_container_width=True, key="s2_back"):
                        st.session_state.app_step = 1
                        st.rerun()
                with nav_r:
                    if st.button("Continue →", use_container_width=True, key="s2_next"):
                        errors = validate_step2()
                        if not show_errors(errors):
                            st.session_state.app_step = 3
                            st.rerun()

            # ── STEP 3 ──────────────────────────────────────────
            elif step == 3:
                st.markdown('<div class="eyebrow">Step 3 of 5</div>', unsafe_allow_html=True)
                st.markdown('<div class="sec-h1">Loan Request</div>', unsafe_allow_html=True)
                st.markdown('<p class="sec-desc">Tell us how much you need, what it is for, and how you plan to repay.</p>', unsafe_allow_html=True)

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Loan Amount Requested (₦) *</div>', unsafe_allow_html=True)
                    st.number_input("LAmount", key="a_lamount", min_value=0, step=10000, format="%d", label_visibility="collapsed")
                with c2:
                    st.markdown('<div class="fl">Loan Tenure *</div>', unsafe_allow_html=True)
                    st.selectbox("Tenure", ["Select", "3 months", "6 months", "9 months", "12 months", "18 months", "24 months", "36 months"], key="a_tenure", label_visibility="collapsed")

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Purpose of Loan *</div>', unsafe_allow_html=True)
                    st.selectbox("Purpose", ["Select purpose", "Working Capital / Business Expansion", "Equipment / Machinery Purchase", "Stock / Inventory Purchase", "School Fees / Education", "Medical / Healthcare", "Home Renovation", "Vehicle Purchase", "Personal / Emergency", "Salary Advance", "Other"], key="a_purpose", label_visibility="collapsed")
                with c2:
                    st.markdown('<div class="fl">Loan Type *</div>', unsafe_allow_html=True)
                    st.selectbox("LType", ["Cash Loan", "Revolving Credit"], key="a_ltype", label_visibility="collapsed")

                # DSR Calculator
                amt = st.session_state.a_lamount or 0
                tenure_str = st.session_state.a_tenure or ""
                tenure_map = {"3 months": 3, "6 months": 6, "9 months": 9, "12 months": 12, "18 months": 18, "24 months": 24, "36 months": 36}
                ten = tenure_map.get(tenure_str, 0)
                inc = st.session_state.a_income or 0
                if amt > 0 and ten > 0:
                    monthly = amt / ten
                    dsr = (monthly / inc * 100) if inc > 0 else None
                    dsr_color = "var(--error)" if (dsr or 0) > 50 else "var(--amber)" if (dsr or 0) > 35 else "var(--success)"
                    dsr_str = f'<span style="color:{dsr_color}">{dsr:.1f}%</span>' if dsr else "—"
                    st.markdown(f"""
                    <div class="dsr-card">
                      <div style="font-size:10px;font-weight:600;color:var(--text-muted);letter-spacing:0.08em;text-transform:uppercase">Estimated Repayment Overview</div>
                      <div class="dsr-grid">
                        <div class="dsr-cell"><div class="dsr-lbl">Monthly Repayment</div><div class="dsr-val">{fmtN(monthly)}</div></div>
                        <div class="dsr-cell"><div class="dsr-lbl">Total Repayable</div><div class="dsr-val">{fmtN(amt)}</div></div>
                        <div class="dsr-cell"><div class="dsr-lbl">Debt-Service Ratio</div><div class="dsr-val">{dsr_str}</div></div>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown('<div class="fl">Brief Description of Loan Purpose</div>', unsafe_allow_html=True)
                st.text_area("LDesc", key="a_ldesc", label_visibility="collapsed", placeholder="Describe what the funds will be used for and how repayment will be made...", height=80)

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Collateral / Asset Value (₦)</div>', unsafe_allow_html=True)
                    st.number_input("Collateral", key="a_collateral", min_value=0, step=5000, format="%d", label_visibility="collapsed")
                    st.markdown('<div style="font-size:11px;color:var(--text-muted);margin-top:-12px">Leave blank if unsecured</div>', unsafe_allow_html=True)
                with c2:
                    st.markdown('<div class="fl">Guarantor Available?</div>', unsafe_allow_html=True)
                    st.selectbox("Guarantor", ["No guarantor", "Yes — guarantor available"], key="a_guarantor", label_visibility="collapsed")

                st.markdown("---")
                nav_l, nav_r = st.columns(2)
                with nav_l:
                    if st.button("← Back", use_container_width=True, key="s3_back"):
                        st.session_state.app_step = 2
                        st.rerun()
                with nav_r:
                    if st.button("Continue →", use_container_width=True, key="s3_next"):
                        errors = validate_step3()
                        if not show_errors(errors):
                            st.session_state.app_step = 4
                            st.rerun()

            # ── STEP 4 ──────────────────────────────────────────
            elif step == 4:
                st.markdown('<div class="eyebrow">Step 4 of 5</div>', unsafe_allow_html=True)
                st.markdown('<div class="sec-h1">Supporting Documents</div>', unsafe_allow_html=True)
                st.markdown('<p class="sec-desc">Upload clear, legible copies. All four required documents must be submitted.</p>', unsafe_allow_html=True)

                st.markdown("""
                <div class="callout callout-info">
                  <div class="callout-icon">i</div>
                  <div class="callout-body"><strong>Accepted formats:</strong> PDF, JPG, PNG &nbsp;·&nbsp; <strong>Max size:</strong> 5MB per file. All four documents below are required.</div>
                </div>
                """, unsafe_allow_html=True)

                files = st.session_state.a_files
                doc_defs = [
                    ("biz",     "Business Registration Certificate *",  "CAC Certificate or Business Name"),
                    ("bank",    "6 Months Bank Statement *",            "Last 6 months — stamped by bank"),
                    ("tin",     "Tax Identification Number (TIN) *",    "FIRS-issued TIN certificate or JTAX card"),
                    ("util",    "Utility Bill / Proof of Address *",    "NEPA/EKEDC or water bill — not older than 3 months"),
                ]

                c1, c2 = st.columns(2)
                cols = [c1, c2, c1, c2]
                for idx, (key, label, hint) in enumerate(doc_defs):
                    with cols[idx]:
                        st.markdown(f'<div class="fl">{label}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="font-size:11px;color:var(--text-muted);margin-bottom:6px">{hint}</div>', unsafe_allow_html=True)
                        uploaded = st.file_uploader(
                            label,
                            type=["pdf", "jpg", "jpeg", "png"],
                            key=f"file_{key}",
                            label_visibility="collapsed"
                        )
                        if uploaded:
                            files[key] = {"name": uploaded.name, "bytes": uploaded.getvalue(), "size": uploaded.size}
                            st.session_state.a_files = files
                            st.markdown(f'<div class="file-ok">✓ &nbsp;{uploaded.name}</div>', unsafe_allow_html=True)
                        elif key in files:
                            st.markdown(f'<div class="file-ok">✓ &nbsp;{files[key]["name"]}</div>', unsafe_allow_html=True)

                st.markdown("""
                <div class="divider"><div class="div-line"></div><div class="div-lbl">Optional but recommended</div><div class="div-line"></div></div>
                """, unsafe_allow_html=True)

                c1, c2 = st.columns(2)
                opt_defs = [
                    ("id",       "Valid Government ID",     "NIN / Passport / Driver's Licence"),
                    ("passport", "Passport Photograph",     "White background, within 6 months"),
                ]
                opt_cols = [c1, c2]
                for idx, (key, label, hint) in enumerate(opt_defs):
                    with opt_cols[idx]:
                        st.markdown(f'<div class="fl">{label}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="font-size:11px;color:var(--text-muted);margin-bottom:6px">{hint}</div>', unsafe_allow_html=True)
                        uploaded = st.file_uploader(label, type=["pdf","jpg","jpeg","png"], key=f"file_{key}", label_visibility="collapsed")
                        if uploaded:
                            files[key] = {"name": uploaded.name, "bytes": uploaded.getvalue(), "size": uploaded.size}
                            st.session_state.a_files = files
                            st.markdown(f'<div class="file-ok">✓ &nbsp;{uploaded.name}</div>', unsafe_allow_html=True)
                        elif key in files:
                            st.markdown(f'<div class="file-ok">✓ &nbsp;{files[key]["name"]}</div>', unsafe_allow_html=True)

                st.markdown("---")
                nav_l, nav_r = st.columns(2)
                with nav_l:
                    if st.button("← Back", use_container_width=True, key="s4_back"):
                        st.session_state.app_step = 3
                        st.rerun()
                with nav_r:
                    if st.button("Continue →", use_container_width=True, key="s4_next"):
                        errors = validate_step4()
                        if not show_errors(errors):
                            st.session_state.app_step = 5
                            st.rerun()

            # ── STEP 5 ──────────────────────────────────────────
            elif step == 5:
                st.markdown('<div class="eyebrow">Step 5 of 5</div>', unsafe_allow_html=True)
                st.markdown('<div class="sec-h1">BVN Verification & Review</div>', unsafe_allow_html=True)
                st.markdown('<p class="sec-desc">Enter your BVN for identity verification, then review and submit your application.</p>', unsafe_allow_html=True)

                # BVN Section
                st.markdown("""
                <div style="background:#fff;border:1px solid var(--border);border-radius:var(--radius-xl);padding:22px 24px;margin-bottom:24px">
                  <div style="font-size:14px;font-weight:600;color:var(--text-primary);margin-bottom:4px">Bank Verification Number (BVN)</div>
                  <div style="font-size:12px;color:var(--text-muted);margin-bottom:16px">Required — soft enquiry only, will not affect your credit score</div>
                """, unsafe_allow_html=True)

                c1, c2 = st.columns(2)
                with c1:
                    st.markdown('<div class="fl">Your BVN *</div>', unsafe_allow_html=True)
                    st.text_input("BVN", key="a_bvn", label_visibility="collapsed", placeholder="11-digit BVN", max_chars=11)
                    bvn = st.session_state.a_bvn.strip()
                    if bvn:
                        if bvn.isdigit() and len(bvn) == 11:
                            st.markdown('<div style="color:var(--success);font-size:12px;font-weight:600;margin-top:-10px;margin-bottom:8px">✓ Valid BVN format</div>', unsafe_allow_html=True)
                        else:
                            st.markdown('<div style="color:var(--error);font-size:12px;font-weight:600;margin-top:-10px;margin-bottom:8px">⚠ Must be exactly 11 digits</div>', unsafe_allow_html=True)
                    st.markdown('<div style="font-size:11px;color:var(--text-muted)">Dial *565*0# to retrieve your BVN</div>', unsafe_allow_html=True)
                with c2:
                    st.markdown('<div style="background:var(--off-white);border-radius:var(--radius);padding:13px 15px;font-size:12px;color:var(--text-secondary);line-height:1.6;height:80px">Your BVN is encrypted in transit and used solely for credit bureau verification for this application.</div>', unsafe_allow_html=True)

                st.checkbox("I consent to my BVN being used to retrieve my credit bureau data for this loan application. (Soft enquiry only — will not negatively affect my credit score.)", key="a_bvnconsent")
                st.markdown('</div>', unsafe_allow_html=True)

                # Review
                s = st.session_state
                tenure_map = {"3 months": 3, "6 months": 6, "9 months": 9, "12 months": 12, "18 months": 18, "24 months": 24, "36 months": 36}
                ten = tenure_map.get(s.a_tenure, 0)
                repay_est = fmtN(s.a_lamount / ten) + "/mo" if s.a_lamount and ten else "—"

                st.markdown('<div style="font-size:11px;font-weight:600;color:var(--text-muted);letter-spacing:0.08em;text-transform:uppercase;margin-bottom:12px">Application Summary</div>', unsafe_allow_html=True)

                st.markdown(f"""
                <div class="rv-block">
                  <div class="rv-hd">Personal Information</div>
                  <div class="rv-bd">
                    <div class="rv-row"><div class="rv-key">Full Name</div><div class="rv-val">{(s.a_fname+' '+s.a_lname).strip() or '—'}</div></div>
                    <div class="rv-row"><div class="rv-key">Phone</div><div class="rv-val">{s.a_phone or '—'}</div></div>
                    <div class="rv-row"><div class="rv-key">Email</div><div class="rv-val">{s.a_email or '—'}</div></div>
                    <div class="rv-row"><div class="rv-key">State</div><div class="rv-val">{s.a_state or '—'}</div></div>
                  </div>
                </div>
                <div class="rv-block">
                  <div class="rv-hd">Employment & Income</div>
                  <div class="rv-bd">
                    <div class="rv-row"><div class="rv-key">Status</div><div class="rv-val">{s.a_empstat or '—'}</div></div>
                    <div class="rv-row"><div class="rv-key">Sector</div><div class="rv-val">{s.a_sector or '—'}</div></div>
                    <div class="rv-row"><div class="rv-key">Monthly Net Income</div><div class="rv-val">{fmtN(s.a_income) if s.a_income else '—'}</div></div>
                    <div class="rv-row"><div class="rv-key">Default History</div><div class="rv-val">{s.a_default or '—'}</div></div>
                  </div>
                </div>
                <div class="rv-block">
                  <div class="rv-hd">Loan Request</div>
                  <div class="rv-bd">
                    <div class="rv-row"><div class="rv-key">Amount Requested</div><div class="rv-val">{fmtN(s.a_lamount) if s.a_lamount else '—'}</div></div>
                    <div class="rv-row"><div class="rv-key">Tenure</div><div class="rv-val">{s.a_tenure or '—'}</div></div>
                    <div class="rv-row"><div class="rv-key">Purpose</div><div class="rv-val">{s.a_purpose or '—'}</div></div>
                    <div class="rv-row"><div class="rv-key">Monthly Repayment (est.)</div><div class="rv-val">{repay_est}</div></div>
                  </div>
                </div>
                <div class="rv-block">
                  <div class="rv-hd">Documents Submitted</div>
                  <div class="rv-bd">
                    <div class="rv-row"><div class="rv-key">Business Registration</div><div class="rv-val">{doc_badge('biz' in s.a_files)}</div></div>
                    <div class="rv-row"><div class="rv-key">Bank Statement</div><div class="rv-val">{doc_badge('bank' in s.a_files)}</div></div>
                    <div class="rv-row"><div class="rv-key">TIN Certificate</div><div class="rv-val">{doc_badge('tin' in s.a_files)}</div></div>
                    <div class="rv-row"><div class="rv-key">Utility Bill</div><div class="rv-val">{doc_badge('util' in s.a_files)}</div></div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

                # Declaration
                st.markdown('<div style="background:#fff;border:1px solid var(--border);border-radius:var(--radius-xl);padding:20px 22px;margin-top:16px"><div style="font-size:12px;font-weight:600;color:var(--text-primary);margin-bottom:12px">Declaration</div>', unsafe_allow_html=True)
                st.checkbox("I confirm all information provided is true, accurate, and complete. (Providing false information is a criminal offence under Nigerian law.)", key="a_d1")
                st.checkbox("I authorise Joyful Smile Nigeria Limited to verify my information through relevant databases, registries, and credit bureaus. (NDPR 2019 compliant.)", key="a_d2")
                st.checkbox("I have read and agree to the Terms & Conditions and Privacy Policy of Joyful Smile Nigeria Limited.", key="a_d3")
                st.markdown('</div>', unsafe_allow_html=True)

                st.markdown("---")
                nav_l, nav_r = st.columns(2)
                with nav_l:
                    if st.button("← Back", use_container_width=True, key="s5_back"):
                        st.session_state.app_step = 4
                        st.rerun()
                with nav_r:
                    if st.button("Submit Application →", use_container_width=True, key="s5_submit"):
                        errors = validate_step5()
                        if not show_errors(errors):
                            ref = "JSN-" + str(random.randint(100000, 999999))
                            s = st.session_state
                            app_record = {
                                "ref": ref,
                                "fname": s.a_fname, "lname": s.a_lname, "mname": s.a_mname,
                                "dob": s.a_dob, "phone": s.a_phone, "email": s.a_email,
                                "marital": s.a_marital, "deps": s.a_deps, "fam": s.a_fam,
                                "edu": s.a_edu, "state": s.a_state, "address": s.a_address,
                                "empstat": s.a_empstat, "sector": s.a_sector, "employer": s.a_employer,
                                "empyrs": s.a_empyrs, "inctype": s.a_inctype, "payfreq": s.a_payfreq,
                                "income": s.a_income, "otherinc": s.a_otherinc, "oblig": s.a_oblig,
                                "actloans": s.a_actloans, "default": s.a_default,
                                "lamount": s.a_lamount, "tenure": s.a_tenure, "purpose": s.a_purpose,
                                "ltype": s.a_ltype, "ldesc": s.a_ldesc, "collateral": s.a_collateral,
                                "guarantor": s.a_guarantor, "bvn": s.a_bvn,
                                "bvnconsent": s.a_bvnconsent, "files": dict(s.a_files),
                                "status": "Pending",
                                "timestamp": "Just now",
                            }
                            st.session_state.applications.append(app_record)
                            st.session_state.app_ref = ref
                            st.session_state.submitted = True
                            st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────
# MODE: OFFICER DASHBOARD
# ─────────────────────────────────────────────────────────────
elif st.session_state.mode == "officer":

    apps = st.session_state.applications

    # Top bar
    st.markdown("""
    <div class="o-topbar">
      <div class="o-brand">Joyful<span>Smiles</span> <span style="font-size:12px;color:rgba(255,255,255,0.28);font-family:'DM Sans',sans-serif;font-weight:400;margin-left:6px">Nigeria Limited</span></div>
      <div style="display:flex;align-items:center;gap:12px">
        <div class="o-badge">Loan Officer Dashboard</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Topbar buttons
    tb1, tb2, tb3, tb4, tb_space = st.columns([1, 1, 1, 1, 4])
    with tb1:
        if st.button("📥 Inbox", use_container_width=True):
            st.session_state.officer_view = "inbox"
            st.session_state.selected_app = -1
            st.rerun()
    with tb2:
        if st.button("✅ Approved", use_container_width=True):
            st.session_state.officer_view = "approved"
            st.session_state.selected_app = -1
            st.rerun()
    with tb3:
        if st.button("❌ Declined", use_container_width=True):
            st.session_state.officer_view = "declined"
            st.session_state.selected_app = -1
            st.rerun()
    with tb4:
        if st.button("← Sign Out", use_container_width=True):
            st.session_state.mode = "gate"
            st.rerun()

    st.markdown("---")

    view = st.session_state.officer_view
    filter_status = {"inbox": "Pending", "approved": "Approved", "declined": "Declined"}.get(view, "Pending")
    view_apps = [a for a in apps if a["status"] == filter_status] if view != "inbox" else apps

    col_list, col_detail = st.columns([1, 1.6])

    with col_list:
        view_labels = {"inbox": "Applications Inbox", "approved": "Approved", "declined": "Declined"}
        st.markdown(f'<div style="font-family:\'Cormorant Garamond\',serif;font-size:22px;font-weight:600;color:var(--navy);margin-bottom:4px">{view_labels.get(view,"Inbox")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="font-size:12px;color:var(--text-muted);margin-bottom:16px">{len(view_apps)} application{"s" if len(view_apps)!=1 else ""}</div>', unsafe_allow_html=True)

        if not view_apps:
            st.markdown('<div style="text-align:center;padding:40px 20px;color:var(--text-muted);font-size:13px">No applications here yet.</div>', unsafe_allow_html=True)
        else:
            for i, a in enumerate(apps):
                if view != "inbox" and a["status"] != filter_status:
                    continue
                real_idx = apps.index(a)
                initials = (a["fname"][0] if a["fname"] else "?") + (a["lname"][0] if a["lname"] else "?")
                is_sel = st.session_state.selected_app == real_idx
                border_style = "border-color:var(--teal);background:var(--teal-pale)" if is_sel else ""
                sbdg = status_badge(a["status"])
                st.markdown(f"""
                <div class="app-card" style="{border_style}">
                  <div class="app-avatar">{initials}</div>
                  <div style="flex:1;min-width:0">
                    <div class="app-name">{a["fname"]} {a["lname"]}</div>
                    <div class="app-meta">{a["ref"]} · {a.get("sector","—")}</div>
                    <div style="margin-top:4px">{sbdg}</div>
                  </div>
                  <div style="text-align:right;flex-shrink:0">
                    <div class="app-amount">{fmtN(a["lamount"]) if a["lamount"] else "—"}</div>
                    <div class="app-time">{a.get("timestamp","")}</div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Open — {a['fname']} {a['lname']}", key=f"sel_{real_idx}", use_container_width=True):
                    st.session_state.selected_app = real_idx
                    st.rerun()

    with col_detail:
        idx = st.session_state.selected_app
        if idx < 0 or idx >= len(apps):
            st.markdown('<div style="display:flex;align-items:center;justify-content:center;min-height:300px;color:var(--text-muted);font-size:13px">Select an application from the list to view details.</div>', unsafe_allow_html=True)
        else:
            a = apps[idx]
            tenure_map2 = {"3 months": 3, "6 months": 6, "9 months": 9, "12 months": 12, "18 months": 18, "24 months": 24, "36 months": 36}
            ten2 = tenure_map2.get(a.get("tenure", ""), 0)
            repay2 = fmtN(a["lamount"] / ten2) + "/mo" if a.get("lamount") and ten2 else "—"

            sbdg = status_badge(a["status"])
            st.markdown(f"""
            <div style="background:#fff;border:1px solid var(--border);border-radius:var(--radius-xl);overflow:hidden;margin-bottom:16px">
              <div class="dp-header">
                <div>
                  <div class="dp-name">{a["fname"]} {a["lname"]}</div>
                  <div class="dp-ref">{a["ref"]} · {a.get("timestamp","")}</div>
                </div>
                <div>{sbdg}</div>
              </div>
              <div style="padding:20px 24px">
                <div class="dp-sec">Personal Information</div>
                <div class="dp-grid">
                  <div class="dp-field"><div class="dp-flbl">Full Name</div><div class="dp-fval">{a["fname"]} {a.get("mname","")} {a["lname"]}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Phone</div><div class="dp-fval">{a.get("phone","—")}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Email</div><div class="dp-fval">{a.get("email","—")}</div></div>
                  <div class="dp-field"><div class="dp-flbl">State</div><div class="dp-fval">{a.get("state","—")}</div></div>
                  <div class="dp-field full"><div class="dp-flbl">Address</div><div class="dp-fval">{a.get("address","—")}</div></div>
                </div>
                <div class="dp-sec">Employment & Income</div>
                <div class="dp-grid">
                  <div class="dp-field"><div class="dp-flbl">Status</div><div class="dp-fval">{a.get("empstat","—")}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Sector</div><div class="dp-fval">{a.get("sector","—")}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Employer</div><div class="dp-fval">{a.get("employer","—")}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Years in Role</div><div class="dp-fval">{a.get("empyrs","—")}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Monthly Net Income</div><div class="dp-fval">{fmtN(a["income"]) if a.get("income") else "—"}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Monthly Obligations</div><div class="dp-fval">{fmtN(a["oblig"]) if a.get("oblig") else "—"}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Active Loans</div><div class="dp-fval">{a.get("actloans","0")}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Default History</div><div class="dp-fval">{a.get("default","—")}</div></div>
                </div>
                <div class="dp-sec">Loan Request</div>
                <div class="dp-grid">
                  <div class="dp-field"><div class="dp-flbl">Amount Requested</div><div class="dp-fval">{fmtN(a["lamount"]) if a.get("lamount") else "—"}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Tenure</div><div class="dp-fval">{a.get("tenure","—")}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Purpose</div><div class="dp-fval">{a.get("purpose","—")}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Est. Monthly Repayment</div><div class="dp-fval">{repay2}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Loan Type</div><div class="dp-fval">{a.get("ltype","—")}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Guarantor</div><div class="dp-fval">{a.get("guarantor","—")}</div></div>
                  <div class="dp-field full"><div class="dp-flbl">Description</div><div class="dp-fval">{a.get("ldesc","—")}</div></div>
                </div>
                <div class="dp-sec">BVN & Verification</div>
                <div class="dp-grid">
                  <div class="dp-field"><div class="dp-flbl">BVN Status</div><div class="dp-fval">{('<span class="bdg bdg-ok">✓ Valid Format</span>') if (a.get("bvn","") and len(a["bvn"])==11) else ('<span class="bdg bdg-miss">Not Provided</span>')}</div></div>
                  <div class="dp-field"><div class="dp-flbl">Bureau Consent</div><div class="dp-fval">{('<span class="bdg bdg-ok">Consent Given</span>') if a.get("bvnconsent") else ('<span class="bdg bdg-miss">No Consent</span>')}</div></div>
                </div>
                <div class="dp-sec">Documents</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            # Document download rows
            files = a.get("files", {})
            doc_labels = {
                "biz": "Business Registration Certificate",
                "bank": "6 Months Bank Statement",
                "tin": "TIN Certificate",
                "util": "Utility Bill / Proof of Address",
                "id": "Government ID",
                "passport": "Passport Photograph",
            }
            for dk, dlabel in doc_labels.items():
                f = files.get(dk)
                status_html = '<span class="bdg bdg-ok">✓ Uploaded</span>' if f else '<span class="bdg bdg-miss">Not Uploaded</span>'
                fname_txt = f["name"] if f else "—"
                st.markdown(f"""
                <div class="doc-row">
                  <div>
                    <div class="doc-name">{dlabel}</div>
                    <div class="doc-file">{fname_txt}</div>
                  </div>
                  <div style="display:flex;align-items:center;gap:10px">{status_html}</div>
                </div>
                """, unsafe_allow_html=True)
                if f and f.get("bytes"):
                    ext = f["name"].split(".")[-1].lower()
                    mime = "application/pdf" if ext == "pdf" else f"image/{ext}"
                    st.download_button(
                        label=f"⬇ Download {dlabel}",
                        data=bytes(f["bytes"]),
                        file_name=f["name"],
                        mime=mime,
                        key=f"dl_{dk}_{idx}",
                        use_container_width=True
                    )

            # Officer notes
            st.markdown("---")
            st.markdown('<div class="fl">Officer Assessment Notes</div>', unsafe_allow_html=True)
            notes_key = f"notes_{idx}"
            if notes_key not in st.session_state:
                st.session_state[notes_key] = a.get("officer_notes", "")
            st.text_area("Notes", key=notes_key, label_visibility="collapsed", height=80, placeholder="Add your assessment notes here...")

            # Decision buttons
            st.markdown('<div style="font-size:12px;font-weight:600;color:var(--text-primary);margin-bottom:10px;margin-top:8px">Credit Decision</div>', unsafe_allow_html=True)
            d1, d2, d3 = st.columns(3)
            with d1:
                if st.button("✅ Approve", use_container_width=True, key=f"approve_{idx}"):
                    apps[idx]["status"] = "Approved"
                    apps[idx]["officer_notes"] = st.session_state.get(notes_key, "")
                    st.session_state.applications = apps
                    st.success(f"Application {a['ref']} approved.")
                    st.rerun()
            with d2:
                if st.button("⚡ Request Info", use_container_width=True, key=f"review_{idx}"):
                    apps[idx]["status"] = "Under Review"
                    apps[idx]["officer_notes"] = st.session_state.get(notes_key, "")
                    st.session_state.applications = apps
                    st.warning(f"Application {a['ref']} marked for further review.")
                    st.rerun()
            with d3:
                if st.button("❌ Decline", use_container_width=True, key=f"decline_{idx}"):
                    apps[idx]["status"] = "Declined"
                    apps[idx]["officer_notes"] = st.session_state.get(notes_key, "")
                    st.session_state.applications = apps
                    st.error(f"Application {a['ref']} declined.")
                    st.rerun()
