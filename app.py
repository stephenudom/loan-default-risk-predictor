import streamlit as st
import numpy as np
import os
import io
import re

# Optional PDF rendering dependency
try:
  import fitz  # PyMuPDF
except Exception:
  fitz = None

st.set_page_config(page_title="Loan Application — Joyful Smile Nigeria Limited",
                   layout="wide", page_icon="🏦")

# ---------------------------
# Inject exact fonts + CSS from provided HTML
# ---------------------------
st.markdown("""
<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&family=Libre+Baskerville:ital@1&display=swap" rel="stylesheet">

<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}

:root{
  --navy:#0B1F3A;
  --navy-mid:#122540;
  --navy-light:#1A3457;
  --teal:#009B8D;
  --teal-light:#00B8A8;
  --teal-pale:#E6F7F6;
  --gold:#C8A44A;
  --gold-light:#E2C070;
  --white:#FFFFFF;
  --off-white:#F8FAFB;
  --text-primary:#0B1F3A;
  --text-secondary:#4A6480;
  --text-muted:#7A94AC;
  --border:#D4E1ED;
  --border-focus:#009B8D;
  --error:#C0392B;
  --error-bg:#FDF2F1;
  --success:#0F7B6C;
  --success-bg:#E6F7F4;
  --shadow-sm:0 1px 4px rgba(11,31,58,0.08);
  --shadow-md:0 4px 16px rgba(11,31,58,0.10);
  --shadow-lg:0 8px 32px rgba(11,31,58,0.12);
  --radius:8px;
  --radius-lg:12px;
  --radius-xl:16px;
}

body{
  font-family:'DM Sans',sans-serif;
  font-size:15px;
  line-height:1.6;
  background:var(--off-white);
  color:var(--text-primary);
  min-height:100vh;
}

/* ── LAYOUT ── */
.app-shell{display:flex;min-height:100vh}

.sidebar{
  width:320px;
  flex-shrink:0;
  background:var(--navy);
  position:sticky;
  top:0;
  height:100vh;
  display:flex;
  flex-direction:column;
  padding:40px 32px;
  overflow:hidden;
}

.sidebar::before{
  content:'';
  position:absolute;
  top:-80px;right:-80px;
  width:260px;height:260px;
  border-radius:50%;
  border:1px solid rgba(0,155,141,0.15);
  pointer-events:none;
}
.sidebar::after{
  content:'';
  position:absolute;
  bottom:-60px;left:-60px;
  width:200px;height:200px;
  border-radius:50%;
  border:1px solid rgba(200,164,74,0.12);
  pointer-events:none;
}

.logo-area{margin-bottom:40px}
.logo-icon{
  width:52px;height:52px;
  background:var(--teal);
  border-radius:14px;
  display:flex;align-items:center;justify-content:center;
  margin-bottom:14px;
}
.logo-icon svg{width:28px;height:28px;fill:white}
.logo-brand{
  font-family:'Cormorant Garamond',serif;
  font-size:22px;font-weight:600;
  color:var(--white);
  line-height:1.2;
}
.logo-sub{
  font-size:11px;color:rgba(255,255,255,0.45);
  letter-spacing:0.12em;text-transform:uppercase;
  margin-top:3px;font-weight:500;
}

.sidebar-tagline{
  font-family:'Cormorant Garamond',serif;
  font-style:italic;
  font-size:17px;
  color:rgba(255,255,255,0.55);
  line-height:1.6;
  margin-bottom:40px;
  padding-bottom:32px;
  border-bottom:1px solid rgba(255,255,255,0.08);
}

/* Steps nav */
.steps-nav{flex:1}
.step-item{
  display:flex;align-items:flex-start;gap:14px;
  padding:12px 0;cursor:pointer;
}
.step-item:not(:last-child){
  border-bottom:1px solid rgba(255,255,255,0.05);
}
.step-num{
  width:30px;height:30px;flex-shrink:0;
  border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-size:12px;font-weight:600;
  border:1.5px solid rgba(255,255,255,0.2);
  color:rgba(255,255,255,0.4);
  transition:all 0.2s;
  margin-top:1px;
}
.step-item.active .step-num{
  background:var(--teal);border-color:var(--teal);
  color:white;
  box-shadow:0 0 0 4px rgba(0,155,141,0.2);
}
.step-item.completed .step-num{
  background:rgba(0,155,141,0.2);border-color:var(--teal);
  color:var(--teal-light);
}
.step-label{font-size:13px;color:rgba(255,255,255,0.35);font-weight:400;line-height:1.3}
.step-title{font-size:14px;color:rgba(255,255,255,0.5);font-weight:500;margin-bottom:2px}
.step-item.active .step-title{color:white}
.step-item.active .step-label{color:rgba(255,255,255,0.55)}
.step-item.completed .step-title{color:rgba(255,255,255,0.6)}

.sidebar-help{
  margin-top:auto;padding-top:24px;
  border-top:1px solid rgba(255,255,255,0.08);
}
.help-line{font-size:12px;color:rgba(255,255,255,0.35);margin-bottom:4px}
.help-contact{
  font-size:13px;color:var(--teal-light);font-weight:500;
}

/* ── MAIN CONTENT ── */
.main-content{
  flex:1;
  display:flex;
  flex-direction:column;
  min-height:100vh;
}

.top-bar{
  background:white;
  border-bottom:1px solid var(--border);
  padding:16px 48px;
  display:flex;align-items:center;justify-content:space-between;
}
.top-bar-left{font-size:13px;color:var(--text-muted)}
.top-bar-left strong{color:var(--text-primary)}
.progress-bar-wrap{
  flex:1;max-width:260px;
  background:var(--border);border-radius:4px;height:4px;
  margin:0 24px;overflow:hidden;
}
.progress-bar-fill{
  height:100%;background:var(--teal);border-radius:4px;
  transition:width 0.4s ease;
}
.progress-label{font-size:12px;color:var(--text-muted)}

.form-area{
  flex:1;
  padding:48px 48px 80px;
  max-width:860px;
}

/* ── SECTION HEADERS ── */
.section-eyebrow{
  font-size:11px;letter-spacing:0.14em;text-transform:uppercase;
  color:var(--teal);font-weight:600;margin-bottom:8px;
}
.section-title{
  font-family:'Cormorant Garamond',serif;
  font-size:32px;font-weight:600;
  color:var(--navy);line-height:1.2;margin-bottom:8px;
}
.section-desc{
  font-size:14px;color:var(--text-secondary);
  margin-bottom:36px;line-height:1.6;
  max-width:540px;
}

/* ── FORM ELEMENTS ── */
.field-group{margin-bottom:24px}
.field-row{display:grid;gap:20px;margin-bottom:24px}
.field-row.cols-2{grid-template-columns:1fr 1fr}
.field-row.cols-3{grid-template-columns:1fr 1fr 1fr}

label{
  display:block;
  font-size:12px;font-weight:600;
  color:var(--text-secondary);
  letter-spacing:0.04em;text-transform:uppercase;
  margin-bottom:7px;
}
label .req{color:var(--teal);margin-left:2px}

input[type=text],input[type=tel],input[type=email],input[type=number],select,textarea{
  width:100%;
  height:46px;
  padding:0 14px;
  background:white;
  border:1.5px solid var(--border);
  border-radius:var(--radius);
  font-family:'DM Sans',sans-serif;
  font-size:14px;
  color:var(--text-primary);
  outline:none;
  transition:border-color 0.15s,box-shadow 0.15s;
  appearance:none;-webkit-appearance:none;
}
textarea{height:100px;padding:12px 14px;resize:vertical;line-height:1.5}
select{
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%237A94AC' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 14px center;
  padding-right:38px;cursor:pointer;
}
input:focus,select:focus,textarea:focus{
  border-color:var(--border-focus);
  box-shadow:0 0 0 3px rgba(0,155,141,0.12);
}
input::placeholder,textarea::placeholder{color:var(--text-muted);font-size:13px}

.input-hint{font-size:12px;color:var(--text-muted);margin-top:5px;line-height:1.4}
.input-prefix-wrap{position:relative}
.input-prefix{
  position:absolute;left:14px;top:50%;transform:translateY(-50%);
  font-size:14px;color:var(--text-muted);font-weight:600;pointer-events:none;
}
.input-prefix-wrap input{padding-left:32px}

/* BVN special */
.bvn-wrap{position:relative}
.bvn-status{
  position:absolute;right:14px;top:50%;transform:translateY(-50%);
  font-size:12px;font-weight:600;
}
.bvn-ok{color:var(--success)}
.bvn-err{color:var(--error)}

/* ── RADIO CARDS ── */
.radio-cards{display:grid;gap:12px}
.radio-cards.cols-2{grid-template-columns:1fr 1fr}
.radio-cards.cols-3{grid-template-columns:1fr 1fr 1fr}
.radio-card{
  position:relative;cursor:pointer;
}
.radio-card input{position:absolute;opacity:0;pointer-events:none}
.radio-card-inner{
  padding:16px 18px;
  border:1.5px solid var(--border);
  border-radius:var(--radius-lg);
  background:white;
  transition:all 0.15s;
}
.radio-card input:checked + .radio-card-inner{
  border-color:var(--teal);
  background:var(--teal-pale);
  box-shadow:0 0 0 3px rgba(0,155,141,0.10);
}
.radio-card-title{font-size:14px;font-weight:600;color:var(--text-primary);margin-bottom:2px}
.radio-card-desc{font-size:12px;color:var(--text-muted);line-height:1.4}
.radio-card input:checked + .radio-card-inner .radio-card-title{color:var(--teal)}

/* ── CHECKBOXES ── */
.checkbox-row{
  display:flex;align-items:flex-start;gap:12px;
  padding:14px 16px;
  border:1.5px solid var(--border);
  border-radius:var(--radius);
  background:white;
  cursor:pointer;margin-bottom:10px;
  transition:border-color 0.15s;
}
.checkbox-row:hover{border-color:var(--teal)}
.checkbox-row input[type=checkbox]{
  width:18px;height:18px;flex-shrink:0;
  margin-top:1px;accent-color:var(--teal);cursor:pointer;
}
.checkbox-text{font-size:13px;color:var(--text-primary);line-height:1.5}
.checkbox-text small{display:block;color:var(--text-muted);font-size:12px;margin-top:1px}

/* ── FILE UPLOAD ── */
.upload-zone{
  border:2px dashed var(--border);
  border-radius:var(--radius-lg);
  background:white;
  padding:28px 24px;
  text-align:center;
  cursor:pointer;
  transition:all 0.2s;
  position:relative;
}
.upload-zone:hover,.upload-zone.drag-over{
  border-color:var(--teal);
  background:var(--teal-pale);
}
.upload-zone input[type=file]{
  position:absolute;inset:0;opacity:0;cursor:pointer;width:100%;height:100%;
}
.upload-icon{
  width:40px;height:40px;
  background:var(--teal-pale);
  border-radius:10px;
  display:flex;align-items:center;justify-content:center;
  margin:0 auto 12px;
}
.upload-icon svg{width:20px;height:20px;stroke:var(--teal);fill:none;stroke-width:1.8}
.upload-title{font-size:14px;font-weight:600;color:var(--text-primary);margin-bottom:3px}
.upload-sub{font-size:12px;color:var(--text-muted)}
.upload-tag{
  display:inline-block;
  background:var(--teal-pale);
  color:var(--teal);
  border:1px solid rgba(0,155,141,0.2);
  border-radius:4px;
  font-size:11px;font-weight:600;
  padding:2px 7px;margin:2px;letter-spacing:0.04em;
  text-transform:uppercase;
}
.file-uploaded{
  display:flex;align-items:center;gap:10px;
  padding:10px 14px;
  background:var(--success-bg);
  border:1px solid rgba(15,123,108,0.2);
  border-radius:var(--radius);
  margin-top:8px;
}
.file-uploaded svg{width:16px;height:16px;flex-shrink:0;stroke:var(--success);fill:none;stroke-width:2}
.file-uploaded-name{font-size:13px;color:var(--success);font-weight:500;flex:1}
.file-remove{
  background:none;border:none;cursor:pointer;
  color:var(--text-muted);font-size:16px;line-height:1;
  padding:0 4px;
}

.docs-grid{display:grid;grid-template-columns:1fr 1fr;gap:20px}

/* ── INFO CALLOUT ── */
.callout{
  display:flex;gap:14px;
  padding:16px 18px;
  border-radius:var(--radius-lg);
  margin-bottom:28px;
}
.callout-info{background:#EEF6FF;border:1px solid #B5D4F4}
.callout-warn{background:#FFF8E6;border:1px solid #FAD97A}
.callout-icon{
  width:20px;height:20px;flex-shrink:0;margin-top:1px;
  border-radius:50%;display:flex;align-items:center;justify-content:center;
  font-size:12px;font-weight:700;
}
.callout-info .callout-icon{background:#B5D4F4;color:#0C447C}
.callout-warn .callout-icon{background:#FAD97A;color:#633806}
.callout-body{font-size:13px;line-height:1.6;color:var(--text-primary)}
.callout-body strong{font-weight:600}

/* ── REVIEW SECTION ── */
.review-block{
  background:white;
  border:1px solid var(--border);
  border-radius:var(--radius-xl);
  margin-bottom:20px;
  overflow:hidden;
  box-shadow:var(--shadow-sm);
}
.review-block-header{
  padding:16px 24px;
  background:var(--off-white);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;
}
.review-block-title{font-size:13px;font-weight:600;color:var(--text-primary);letter-spacing:0.02em}
.review-edit{
  font-size:12px;color:var(--teal);font-weight:500;
  cursor:pointer;background:none;border:none;
}
.review-block-body{padding:16px 24px}
.review-row{
  display:flex;justify-content:space-between;align-items:baseline;
  padding:8px 0;border-bottom:1px solid rgba(212,225,237,0.5);
  gap:20px;
}
.review-row:last-child{border-bottom:none}
.review-key{font-size:13px;color:var(--text-muted);flex:1}
.review-val{font-size:13px;font-weight:500;color:var(--text-primary);text-align:right}
.review-badge{
  display:inline-flex;align-items:center;gap:5px;
  padding:3px 10px;border-radius:20px;
  font-size:11px;font-weight:600;letter-spacing:0.04em;
}
.badge-ok{background:var(--success-bg);color:var(--success)}
.badge-warn{background:#FFF8E6;color:#854F0B}
.badge-missing{background:#FDF2F1;color:var(--error)}

/* ── NAV BUTTONS ── */
.form-nav{
  display:flex;align-items:center;justify-content:space-between;
  margin-top:40px;padding-top:28px;
  border-top:1px solid var(--border);
}
.btn{
  display:inline-flex;align-items:center;gap:8px;
  padding:0 28px;height:48px;
  border-radius:var(--radius);
  font-family:'DM Sans',sans-serif;
  font-size:14px;font-weight:600;
  cursor:pointer;border:none;
  transition:all 0.15s;
  text-decoration:none;
}
.btn-primary{
  background:var(--teal);color:white;
  box-shadow:0 2px 8px rgba(0,155,141,0.28);
}
.btn-primary:hover{background:var(--teal-light);box-shadow:0 4px 16px rgba(0,155,141,0.35)}
.btn-secondary{
  background:white;color:var(--text-primary);
  border:1.5px solid var(--border);
}
.btn-secondary:hover{background:var(--off-white);border-color:var(--text-muted)}
.btn svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2}
.btn-ghost{
  background:none;border:none;color:var(--text-muted);
  font-family:'DM Sans',sans-serif;font-size:14px;cursor:pointer;
}

/* ── SUCCESS SCREEN ── */
.success-screen{
  display:none;flex-direction:column;align-items:center;
  justify-content:center;text-align:center;
  padding:80px 48px;flex:1;
}
.success-icon{
  width:80px;height:80px;
  background:var(--success-bg);
  border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  margin:0 auto 28px;
}
.success-icon svg{width:36px;height:36px;stroke:var(--success);fill:none;stroke-width:2}
.success-ref{
  display:inline-block;
  font-family:monospace;font-size:20px;font-weight:700;
  color:var(--teal);
  background:var(--teal-pale);
  border:1px solid rgba(0,155,141,0.2);
  border-radius:8px;padding:8px 24px;
  margin:20px 0;letter-spacing:0.1em;
}
.success-note{
  font-size:14px;color:var(--text-secondary);
  max-width:420px;line-height:1.7;margin:0 auto;
}
.success-steps{
  display:flex;gap:16px;margin:32px 0;
  justify-content:center;flex-wrap:wrap;
}
.success-step{
  background:white;border:1px solid var(--border);
  border-radius:var(--radius-lg);padding:16px 20px;
  text-align:left;width:180px;
}
.success-step-num{
  font-size:11px;font-weight:700;color:var(--teal);
  letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px;
}
.success-step-text{font-size:13px;color:var(--text-primary);line-height:1.4}

/* ── STEP VISIBILITY ── */
.step-content{display:none}
.step-content.active{display:block}

/* ── DIVIDER ── */
.divider{
  display:flex;align-items:center;gap:12px;margin:32px 0;
}
.divider-line{flex:1;height:1px;background:var(--border)}
.divider-label{font-size:12px;color:var(--text-muted);white-space:nowrap;font-weight:500}

/* ── RESPONSIVE ── */
@media(max-width:900px){
  .sidebar{display:none}
  .form-area{padding:32px 24px 60px}
  .top-bar{padding:14px 24px}
  .field-row.cols-3{grid-template-columns:1fr 1fr}
  .docs-grid{grid-template-columns:1fr}
}
@media(max-width:600px){
  .field-row.cols-2,.field-row.cols-3{grid-template-columns:1fr}
  .radio-cards.cols-3{grid-template-columns:1fr}
  .docs-grid{grid-template-columns:1fr}
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Helper functions & session state
# ---------------------------

def init_state():
    if "step" not in st.session_state:
        st.session_state.step = 1
    if "uploaded" not in st.session_state:
        st.session_state.uploaded = {}
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    defaults = {
        "first_name": "", "last_name": "", "middle_name": "", "dob": "",
        "phone": "", "email": "", "marital": "", "dependants": 0, "family": 1,
        "education": "", "state": "", "address": "",
        "emp_status": "", "emp_sector": "", "employer": "", "emp_years": "",
        "income_type": "", "pay_freq": "", "monthly_income": 0, "other_income": 0,
        "obligations": 0, "active_loans": 0, "default_history": "Never",
        "loan_amount": 0, "loan_tenure": "", "loan_purpose": "", "loan_type": "Cash Loan",
        "collateral": 0, "guarantor": "No guarantor",
        "bvn": "", "bvn_consent": False,
        "declare1": False, "declare2": False, "declare3": False
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def find_letterhead_path():
  """Try to locate the 'Joyful Smiles Letterhead.pdf' file in likely locations.

  Returns the absolute path or None if not found.
  """
  base_dir = os.path.dirname(os.path.abspath(__file__))
  candidates = [
    os.path.join(base_dir, 'Joyful Smiles Letterhead.pdf'),
    os.path.join(base_dir, '..', 'Joyful Smile', 'Joyful Smiles Letterhead.pdf'),
    os.path.join(os.path.expanduser('~'), 'Desktop', 'Joyful Smile', 'Joyful Smiles Letterhead.pdf'),
    os.path.join(os.path.expanduser('~'), 'Desktop', 'Joyful Smiles Letterhead.pdf'),
  ]
  for p in candidates:
    if os.path.exists(p):
      return os.path.abspath(p)
  # last resort: search one level up for matching file name
  root = os.path.dirname(base_dir)
  for folder in (base_dir, root):
    try:
      for fname in os.listdir(folder):
        if 'letterhead' in fname.lower() and fname.lower().endswith('.pdf'):
          return os.path.join(folder, fname)
    except Exception:
      continue
  return None


def load_letterhead_image_and_contacts():
  """Return (image_bytes_or_None, contacts_dict)

  contacts_dict may contain keys: company, phone, email, address
  """
  path = find_letterhead_path()
  contacts = {"company": "Joyful Smile Nigeria Limited", "phone": "07010057527", "email": "joyfulsmilesnigerialimited@gmail.com", "address": None, "pdf_path": None}
  if not path or not fitz:
    # Either not found or PyMuPDF unavailable — return defaults and no image
    if path:
      contacts['pdf_path'] = path
    return None, contacts

  try:
    doc = fitz.open(path)
    page = doc.load_page(0)
    # render as PNG
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
    img_bytes = pix.tobytes('png')
    text = page.get_text('text')
    contacts['pdf_path'] = path

    # extract email
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}', text)
    if emails:
      contacts['email'] = emails[0]

    # extract phone (Nigerian formats)
    phones = re.findall(r'(?:\+234|0)\d{10}', text)
    if phones:
      contacts['phone'] = phones[0]

    # try to get a company line or address — heuristic: first 6 non-empty lines
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    if lines:
      # prefer a line containing 'Joyful' or 'Joyful Smile'
      for ln in lines[:8]:
        if 'joyful' in ln.lower():
          contacts['company'] = ln
          break
      # attempt to build an address snippet from remaining lines
      addr_lines = []
      for ln in lines[:10]:
        if any(tok in ln.lower() for tok in ('street', 'road', 'lagos', 'nigeria', 'office', 'suite', 'plot', 'p.o', 'p.o.')):
          addr_lines.append(ln)
      if addr_lines:
        contacts['address'] = ' | '.join(addr_lines)

    return img_bytes, contacts
  except Exception:
    return None, contacts


def next_step():
    st.session_state.step = min(5, st.session_state.step + 1)

def prev_step():
    st.session_state.step = max(1, st.session_state.step - 1)

def set_step(n):
    st.session_state.step = int(n)

def fmt_naira(n):
    try:
        return "₦{:,.0f}".format(float(n))
    except Exception:
        return "—"

def validate_bvn(v: str):
    return v and v.isdigit() and len(v) == 11

init_state()

# ---------------------------
# Step names (shared)
# ---------------------------
step_names = ["Personal Details", "Employment & Income", "Loan Request", "Documents", "BVN & Review"]

# ---------------------------
# Layout: sidebar + main
# ---------------------------
cols = st.columns([0.32, 1.0])
with cols[0]:
  st.markdown('<div class="sidebar">', unsafe_allow_html=True)
  # Load contact details from letterhead PDF if available, but do not render the PDF image here
  # (PDF-to-image rendering caused layout issues). We will always show the in-app SVG logo instead.
  _ , contacts = load_letterhead_image_and_contacts()
  # Always use the embedded SVG logo to ensure consistent layout
  st.markdown('<div class="logo-icon"><svg viewBox="0 0 24 24"><path d="M12 3C7 3 3 7 3 12s4 9 9 9 9-4 9-9-4-9-9-9zm0 14c-2.8 0-5-2.2-5-5s2.2-5 5-5 5 2.2 5 5-2.2 5-5 5zm-2-6.5l1.5 1.5 3-3"/></svg></div>', unsafe_allow_html=True)

  # Company name and subtitle from contacts (fallbacks provided)
  st.markdown(f"<div class=\"logo-brand\">{contacts.get('company','Joyful Smile Nigeria Limited')}</div>", unsafe_allow_html=True)
  st.markdown(f"<div class=\"logo-sub\">Financial Services</div>", unsafe_allow_html=True)
  # Tagline (if address available, show shortened address)
  tagline = contacts.get('address') or 'Your growth journey begins with a single application. We make it simple.'
  st.markdown(f"<div class=\"sidebar-tagline\">{tagline}</div>", unsafe_allow_html=True)

  for i, name in enumerate(step_names, start=1):
      if st.button(f"{i}. {name}", key=f"step_btn_{i}"):
          set_step(i)

  st.markdown('---')
  st.markdown('<div class="help-line">Need assistance?</div>', unsafe_allow_html=True)
  phone = contacts.get('phone', '07010057527')
  email = contacts.get('email', 'joyfulsmilesnigerialimited@gmail.com')
  st.markdown(f'<div class="help-contact">{phone}</div>', unsafe_allow_html=True)
  st.markdown(f'<div style="font-size:11px;color:rgba(255,255,255,0.3);margin-top:6px">{email}</div>', unsafe_allow_html=True)
  # If the letterhead PDF was discovered, offer it for download
  if contacts.get('pdf_path') and os.path.exists(contacts['pdf_path']):
    try:
      with open(contacts['pdf_path'], 'rb') as _f:
        pdf_bytes = _f.read()
      st.download_button(label='Download Letterhead (PDF)', data=pdf_bytes, file_name=os.path.basename(contacts['pdf_path']), mime='application/pdf')
    except Exception:
      pass
  st.markdown('</div>', unsafe_allow_html=True)

with cols[1]:
    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    progress_map = {1:20,2:40,3:60,4:80,5:100}
    st.markdown(f'<div class="top-bar"><div class="top-bar-left">Loan Application &nbsp;/&nbsp; <strong id="top-step-name">{step_names[st.session_state.step-1]}</strong></div><div class="progress-bar-wrap"><div class="progress-bar-fill" style="width:{progress_map[st.session_state.step]}%"></div></div><div class="progress-label">Step {st.session_state.step} of 5</div></div>', unsafe_allow_html=True)

    # Step 1
    if st.session_state.step == 1 and not st.session_state.submitted:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-eyebrow">Step 1 of 5</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Personal Details</div>', unsafe_allow_html=True)
        st.text_input("First Name", key="first_name", placeholder="e.g. Chukwuemeka")
        st.text_input("Last Name", key="last_name", placeholder="e.g. Okonkwo")
        st.text_input("Middle Name (optional)", key="middle_name")
        st.text_input("Date of Birth (DD / MM / YYYY)", key="dob", placeholder="DD / MM / YYYY")
        st.text_input("Phone Number", key="phone", placeholder="e.g. 08012345678")
        st.text_input("Email Address", key="email", placeholder="e.g. name@email.com")
        st.selectbox("Marital Status", ["", "Single", "Married", "Divorced", "Widowed"], key="marital")
        st.number_input("No. of Dependants", min_value=0, max_value=20, key="dependants")
        st.number_input("Total Family Members", min_value=1, max_value=20, key="family", value=st.session_state.family)
        st.selectbox("Highest Education Level", ["", "SSCE / O'Level", "OND / NCE", "HND / B.Sc", "Postgraduate (M.Sc / MBA)", "PhD / Doctorate", "Professional Certification", "No formal education"], key="education")
        st.selectbox("Residential State", [""] + ["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno","Cross River","Delta","Ebonyi","Edo","Ekiti","Enugu","FCT — Abuja","Gombe","Imo","Jigawa","Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nasarawa","Niger","Ogun","Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara"], key="state")
        st.text_area("Residential Address", key="address", placeholder="House number, street, town, LGA")
        if st.button("Continue ➜"):
            next_step()

    # Step 2
    if st.session_state.step == 2 and not st.session_state.submitted:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-eyebrow">Step 2 of 5</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Employment & Income</div>', unsafe_allow_html=True)
        st.selectbox("Employment Status", ["", "Employed (Full-time)", "Employed (Part-time)", "Self-Employed / Business Owner", "Civil Servant / Government Employee", "Contractor / Freelancer", "Retired", "Unemployed"], key="emp_status")
        st.selectbox("Employment Sector", ["", "Banking & Finance", "Government / Civil Service", "Healthcare & Pharmaceuticals", "Education & Training", "Technology & Telecoms", "Trade & Commerce", "Agriculture & Agribusiness", "Transport & Logistics", "Construction & Real Estate", "Oil & Gas", "Manufacturing", "Creative & Media", "Other"], key="emp_sector")
        st.text_input("Employer / Business Name", key="employer", placeholder="e.g. Lagos State Government")
        st.selectbox("Years in Current Role / Business", ["", "Less than 6 months", "6 months to 1 year", "1 to 2 years", "2 to 5 years", "5 to 10 years", "Over 10 years"], key="emp_years")
        st.selectbox("Income Type", ["", "Fixed Monthly Salary", "Business Revenue (Regular)", "Commission-Based", "Irregular / Seasonal", "Pension", "Rental Income", "Multiple Sources"], key="income_type")
        st.selectbox("Pay Frequency", ["", "Monthly", "Bi-weekly", "Weekly", "Daily", "Project-based"], key="pay_freq")
        st.number_input("Monthly Net Income (₦)", min_value=0, step=1000, key="monthly_income", format="%d")
        st.number_input("Other Monthly Income (₦)", min_value=0, step=1000, key="other_income", format="%d")
        st.number_input("Total Monthly Obligations (₦)", min_value=0, step=1000, key="obligations", format="%d")
        st.number_input("Number of Active Loans", min_value=0, max_value=50, key="active_loans")
        st.selectbox("Previous Loan Default History", ["Never", "5+ years ago", "2 to 5 years ago", "Within the last 2 years"], key="default_history")
        st.text_input("Work / Office Phone Number", key="work_phone", placeholder="e.g. 0123456789")
        c1, c2 = st.columns([1,1])
        with c1:
            if st.button("← Back"):
                prev_step()
        with c2:
            if st.button("Continue ➜", key="to3"):
                next_step()

    # Step 3
    if st.session_state.step == 3 and not st.session_state.submitted:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-eyebrow">Step 3 of 5</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Loan Request</div>', unsafe_allow_html=True)
        st.number_input("Loan Amount Requested (₦)", min_value=10000, step=10000, key="loan_amount", format="%d")
        st.selectbox("Loan Tenure (months)", ["", "3", "6", "9", "12", "18", "24", "36"], key="loan_tenure")
        st.selectbox("Purpose of Loan", ["", "Working Capital / Business Expansion", "Equipment / Machinery Purchase", "Stock / Inventory Purchase", "School Fees / Education", "Medical / Healthcare", "Home Renovation", "Vehicle Purchase", "Personal / Emergency", "Salary Advance", "Other"], key="loan_purpose")
        st.selectbox("Loan Type", ["Cash Loan", "Revolving Credit"], key="loan_type")
        loan_amt = st.session_state.loan_amount or 0
        tenure = int(st.session_state.loan_tenure) if st.session_state.loan_tenure and st.session_state.loan_tenure.isdigit() else 0
        income_monthly = st.session_state.monthly_income or 0
        if loan_amt > 0 and tenure > 0:
            monthly = loan_amt / tenure
            total = monthly * tenure
            dsr = (monthly / income_monthly * 100) if income_monthly > 0 else None
            st.markdown(f"""
                <div class="card">
                  <div style="display:flex;gap:12px;">
                    <div style="flex:1;text-align:center">
                      <div class="small-muted">Monthly Repayment</div>
                      <div style="font-weight:700">{fmt_naira(monthly)}</div>
                    </div>
                    <div style="flex:1;text-align:center">
                      <div class="small-muted">Total Repayable</div>
                      <div style="font-weight:700">{fmt_naira(total)}</div>
                    </div>
                    <div style="flex:1;text-align:center">
                      <div class="small-muted">Debt-Service Ratio</div>
                      <div style="font-weight:700">{(f'{dsr:.1f}%' if dsr is not None else '—')}</div>
                    </div>
                  </div>
                </div>
            """, unsafe_allow_html=True)
        st.text_area("Brief Description of Loan Purpose", key="loan_desc")
        st.number_input("Collateral / Asset Value (₦)", min_value=0, step=1000, key="collateral", format="%d")
        st.selectbox("Guarantor Available?", ["No guarantor", "Yes — guarantor available"], key="guarantor")
        c1, c2 = st.columns([1,1])
        with c1:
            if st.button("← Back", key="b3"):
                prev_step()
        with c2:
            if st.button("Continue ➜", key="to4"):
                next_step()

    # Step 4
    if st.session_state.step == 4 and not st.session_state.submitted:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-eyebrow">Step 4 of 5</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Supporting Documents</div>', unsafe_allow_html=True)
        st.markdown('<div class="small-muted">Upload clear, legible copies. Accepted: PDF, JPG, PNG. Max 5MB each.</div>', unsafe_allow_html=True)
        cols_docs = st.columns(2)
        with cols_docs[0]:
            biz = st.file_uploader("Business Registration Certificate (CAC)", type=["pdf","jpg","jpeg","png"], key="biz_reg_file")
            if biz:
                st.session_state.uploaded['biz'] = {"name": biz.name, "data": biz.getvalue()}
                st.markdown(f"<div class=\"file-uploaded\">{biz.name} <span style=\"color:var(--teal)\">Uploaded</span></div>", unsafe_allow_html=True)
            bank = st.file_uploader("6 Months Bank Statement", type=["pdf","jpg","jpeg","png"], key="bank_stmt_file")
            if bank:
                st.session_state.uploaded['bank'] = {"name": bank.name, "data": bank.getvalue()}
                st.markdown(f"<div class=\"file-uploaded\">{bank.name} <span style=\"color:var(--teal)\">Uploaded</span></div>", unsafe_allow_html=True)
        with cols_docs[1]:
            tin = st.file_uploader("Tax Identification Number (TIN)", type=["pdf","jpg","jpeg","png"], key="tin_file")
            if tin:
                st.session_state.uploaded['tin'] = {"name": tin.name, "data": tin.getvalue()}
                st.markdown(f"<div class=\"file-uploaded\">{tin.name} <span style=\"color:var(--teal)\">Uploaded</span></div>", unsafe_allow_html=True)
            utility = st.file_uploader("Utility Bill / Proof of Address", type=["pdf","jpg","jpeg","png"], key="utility_file")
            if utility:
                st.session_state.uploaded['utility'] = {"name": utility.name, "data": utility.getvalue()}
                st.markdown(f"<div class=\"file-uploaded\">{utility.name} <span style=\"color:var(--teal)\">Uploaded</span></div>", unsafe_allow_html=True)
        st.markdown('<div class="small-muted">Optional but recommended</div>', unsafe_allow_html=True)
        opt_cols = st.columns(2)
        with opt_cols[0]:
            gov_id = st.file_uploader("Valid Government ID (NIN / Passport / Driver's Licence)", type=["pdf","jpg","jpeg","png"], key="id_file")
            if gov_id:
                st.session_state.uploaded['id'] = {"name": gov_id.name, "data": gov_id.getvalue()}
                st.markdown(f"<div class=\"file-uploaded\">{gov_id.name} <span style=\"color:var(--teal)\">Uploaded</span></div>", unsafe_allow_html=True)
        with opt_cols[1]:
            passport = st.file_uploader("Passport Photograph (jpg/png)", type=["jpg","jpeg","png"], key="passport_file")
            if passport:
                st.session_state.uploaded['passport'] = {"name": passport.name, "data": passport.getvalue()}
                st.markdown(f"<div class=\"file-uploaded\">{passport.name} <span style=\"color:var(--teal)\">Uploaded</span></div>", unsafe_allow_html=True)
        c1, c2 = st.columns([1,1])
        with c1:
            if st.button("← Back", key="b4"):
                prev_step()
        with c2:
            if st.button("Continue ➜", key="to5"):
                next_step()

    # Step 5
    if st.session_state.step == 5 and not st.session_state.submitted:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-eyebrow">Step 5 of 5</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-title">BVN Verification & Review</div>', unsafe_allow_html=True)
        st.text_input("Your BVN (11 digits)", key="bvn")
        checked = validate_bvn(st.session_state.bvn)
        if checked:
            st.markdown('<div style="padding:10px;background:rgba(0,184,168,0.06);border-radius:8px;color:var(--teal);font-weight:700">✓ BVN Format Valid</div>', unsafe_allow_html=True)
        elif st.session_state.bvn:
            st.markdown('<div style="padding:10px;background:rgba(240,64,96,0.04);border-radius:8px;color:#C0392B;font-weight:700">⚠️ Invalid BVN</div>', unsafe_allow_html=True)
        st.checkbox("I consent to BVN-based credit bureau verification (soft enquiry only)", key="bvn_consent")

        st.markdown('<div class="small-muted" style="margin-bottom:8px">Application Summary</div>', unsafe_allow_html=True)
        def doc_badge(k):
            if st.session_state.uploaded.get(k):
                return '<span class="review-badge badge-ok">✓ Uploaded</span>'
            return '<span class="review-badge badge-missing">Not uploaded</span>'

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div style="font-weight:700">Personal Information</div>', unsafe_allow_html=True)
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Full Name</div><div class=\"review-val\">{(st.session_state.first_name + ' ' + st.session_state.last_name).strip() or '—'}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Phone</div><div class=\"review-val\">{st.session_state.phone or '—'}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Email</div><div class=\"review-val\">{st.session_state.email or '—'}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">State</div><div class=\"review-val\">{st.session_state.state or '—'}</div></div>")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div style="font-weight:700">Employment & Income</div>', unsafe_allow_html=True)
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Status</div><div class=\"review-val\">{st.session_state.emp_status or '—'}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Sector</div><div class=\"review-val\">{st.session_state.emp_sector or '—'}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Monthly Net Income</div><div class=\"review-val\">{fmt_naira(st.session_state.monthly_income) if st.session_state.monthly_income else '—'}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Default History</div><div class=\"review-val\">{st.session_state.default_history or '—'}</div></div>")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div style="font-weight:700">Loan Request</div>', unsafe_allow_html=True)
        repay_est = "—"
        if st.session_state.loan_amount and st.session_state.loan_tenure and st.session_state.loan_tenure.isdigit():
            repay_est = fmt_naira(st.session_state.loan_amount / int(st.session_state.loan_tenure))
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Amount Requested</div><div class=\"review-val\">{fmt_naira(st.session_state.loan_amount) if st.session_state.loan_amount else '—'}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Tenure</div><div class=\"review-val\">{(st.session_state.loan_tenure + ' months') if st.session_state.loan_tenure else '—'}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Purpose</div><div class=\"review-val\">{st.session_state.loan_purpose or '—'}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Monthly Repayment (est.)</div><div class=\"review-val\">{repay_est}</div></div>")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div style="font-weight:700">Documents Submitted</div>', unsafe_allow_html=True)
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Business Registration</div><div class=\"review-val\">{doc_badge('biz')}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Bank Statement</div><div class=\"review-val\">{doc_badge('bank')}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">TIN Certificate</div><div class=\"review-val\">{doc_badge('tin')}</div></div>")
        st.markdown(f"<div class=\"review-row\"><div class=\"review-key\">Utility Bill</div><div class=\"review-val\">{doc_badge('utility')}</div></div>")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div style="font-weight:700">Declaration</div>', unsafe_allow_html=True)
        st.checkbox("I confirm information provided is true and complete.", key="declare1")
        st.checkbox("I authorise Joyful Smile Nigeria Limited to verify my information (NDPR compliant).", key="declare2")
        st.checkbox("I have read and agree to Terms & Conditions and Privacy Policy.", key="declare3")
        st.markdown('</div>', unsafe_allow_html=True)

        c1, c2 = st.columns([1,1])
        with c1:
            if st.button("← Back", key="b5"):
                prev_step()
        with c2:
            if st.button("Submit Application", key="submit_app"):
                if not (st.session_state.declare1 and st.session_state.declare2 and st.session_state.declare3):
                    st.error("Please confirm all declaration checkboxes before submitting.")
                elif not validate_bvn(st.session_state.bvn):
                    st.error("Please enter a valid 11-digit BVN before submitting.")
                elif not st.session_state.bvn_consent:
                    st.error("Please provide consent for BVN verification.")
                else:
                    st.session_state.submitted = True
                    st.session_state.ref = "JSN-" + str(np.random.randint(100000, 999999))
                    st.experimental_rerun()

    # Success
    if st.session_state.submitted:
        st.markdown('<div class="success-screen" style="display:flex">', unsafe_allow_html=True)
        st.markdown('<div class="success-icon"><svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg></div>', unsafe_allow_html=True)
        st.markdown(f'<div style="font-family:\'Cormorant Garamond\', serif; font-size:36px;font-weight:600;color:var(--navy);margin-bottom:8px">Application Submitted</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="success-ref">{st.session_state.ref}</div>', unsafe_allow_html=True)
        st.markdown('<p class="success-note">Your loan application has been received. Our team will review your documents and contact you within <strong>24 to 48 business hours</strong>.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
