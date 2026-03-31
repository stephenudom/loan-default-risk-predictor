<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Loan Application — Joyful Smile Nigeria Limited</title>
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
</head>
<body>

<div class="app-shell">

  <!-- ── SIDEBAR ── -->
  <aside class="sidebar">
    <div class="logo-area">
      <div class="logo-icon">
        <svg viewBox="0 0 24 24"><path d="M12 3C7 3 3 7 3 12s4 9 9 9 9-4 9-9-4-9-9-9zm0 14c-2.8 0-5-2.2-5-5s2.2-5 5-5 5 2.2 5 5-2.2 5-5 5zm-2-6.5l1.5 1.5 3-3"/></svg>
      </div>
      <div class="logo-brand">Joyful Smile<br>Nigeria Limited</div>
      <div class="logo-sub">Financial Services</div>
    </div>

    <p class="sidebar-tagline">Your growth journey begins with a single application. We make it simple.</p>

    <nav class="steps-nav">
      <div class="step-item active" onclick="goTo(1)">
        <div class="step-num">1</div>
        <div>
          <div class="step-title">Personal Details</div>
          <div class="step-label">Identity & contact</div>
        </div>
      </div>
      <div class="step-item" onclick="goTo(2)">
        <div class="step-num">2</div>
        <div>
          <div class="step-title">Employment & Income</div>
          <div class="step-label">Work & earnings</div>
        </div>
      </div>
      <div class="step-item" onclick="goTo(3)">
        <div class="step-num">3</div>
        <div>
          <div class="step-title">Loan Request</div>
          <div class="step-label">Amount & purpose</div>
        </div>
      </div>
      <div class="step-item" onclick="goTo(4)">
        <div class="step-num">4</div>
        <div>
          <div class="step-title">Documents</div>
          <div class="step-label">Supporting files</div>
        </div>
      </div>
      <div class="step-item" onclick="goTo(5)">
        <div class="step-num">5</div>
        <div>
          <div class="step-title">BVN & Review</div>
          <div class="step-label">Verify & submit</div>
        </div>
      </div>
    </nav>

    <div class="sidebar-help">
      <div class="help-line">Need assistance?</div>
      <div class="help-contact">07010057527</div>
      <div class="help-contact" style="font-size:11px;color:rgba(255,255,255,0.3);margin-top:2px">joyfulsmilesnigerialimited@gmail.com</div>
    </div>
  </aside>

  <!-- ── MAIN ── -->
  <div class="main-content">

    <!-- Top bar -->
    <div class="top-bar">
      <div class="top-bar-left">Loan Application &nbsp;/&nbsp; <strong id="top-step-name">Personal Details</strong></div>
      <div class="progress-bar-wrap">
        <div class="progress-bar-fill" id="progress-fill" style="width:20%"></div>
      </div>
      <div class="progress-label" id="progress-label">Step 1 of 5</div>
    </div>

    <!-- Form area -->
    <div class="form-area">

      <!-- ══ STEP 1: PERSONAL DETAILS ══ -->
      <div class="step-content active" id="step-1">
        <div class="section-eyebrow">Step 1 of 5</div>
        <h1 class="section-title">Personal Details</h1>
        <p class="section-desc">Provide your personal information exactly as it appears on your government-issued ID.</p>

        <div class="field-row cols-2">
          <div>
            <label>First Name <span class="req">*</span></label>
            <input type="text" id="first-name" placeholder="e.g. Chukwuemeka">
          </div>
          <div>
            <label>Last Name <span class="req">*</span></label>
            <input type="text" id="last-name" placeholder="e.g. Okonkwo">
          </div>
        </div>

        <div class="field-row cols-2">
          <div>
            <label>Middle Name</label>
            <input type="text" id="middle-name" placeholder="Optional">
          </div>
          <div>
            <label>Date of Birth <span class="req">*</span></label>
            <input type="text" id="dob" placeholder="DD / MM / YYYY">
          </div>
        </div>

        <div class="field-row cols-2">
          <div>
            <label>Phone Number <span class="req">*</span></label>
            <input type="tel" id="phone" placeholder="e.g. 08012345678">
          </div>
          <div>
            <label>Email Address</label>
            <input type="email" id="email" placeholder="e.g. name@email.com">
          </div>
        </div>

        <div class="field-row cols-3">
          <div>
            <label>Marital Status <span class="req">*</span></label>
            <select id="marital">
              <option value="">Select</option>
              <option>Single</option>
              <option>Married</option>
              <option>Divorced</option>
              <option>Widowed</option>
            </select>
          </div>
          <div>
            <label>No. of Dependants</label>
            <input type="number" id="dependants" placeholder="0" min="0" max="20">
          </div>
          <div>
            <label>Total Family Members</label>
            <input type="number" id="family" placeholder="1" min="1">
          </div>
        </div>

        <div class="field-row cols-2">
          <div>
            <label>Highest Education Level <span class="req">*</span></label>
            <select id="education">
              <option value="">Select level</option>
              <option>SSCE / O'Level</option>
              <option>OND / NCE</option>
              <option>HND / B.Sc</option>
              <option>Postgraduate (M.Sc / MBA)</option>
              <option>PhD / Doctorate</option>
              <option>Professional Certification</option>
              <option>No formal education</option>
            </select>
          </div>
          <div>
            <label>Residential State <span class="req">*</span></label>
            <select id="state">
              <option value="">Select state</option>
              <option>Abia</option><option>Adamawa</option><option>Akwa Ibom</option>
              <option>Anambra</option><option>Bauchi</option><option>Bayelsa</option>
              <option>Benue</option><option>Borno</option><option>Cross River</option>
              <option>Delta</option><option>Ebonyi</option><option>Edo</option>
              <option>Ekiti</option><option>Enugu</option><option>FCT — Abuja</option>
              <option>Gombe</option><option>Imo</option><option>Jigawa</option>
              <option>Kaduna</option><option>Kano</option><option>Katsina</option>
              <option>Kebbi</option><option>Kogi</option><option>Kwara</option>
              <option>Lagos</option><option>Nasarawa</option><option>Niger</option>
              <option>Ogun</option><option>Ondo</option><option>Osun</option>
              <option>Oyo</option><option>Plateau</option><option>Rivers</option>
              <option>Sokoto</option><option>Taraba</option><option>Yobe</option>
              <option>Zamfara</option>
            </select>
          </div>
        </div>

        <div class="field-group">
          <label>Residential Address <span class="req">*</span></label>
          <textarea id="address" placeholder="House number, street, town, local government area"></textarea>
        </div>

        <div class="form-nav">
          <span></span>
          <button class="btn btn-primary" onclick="nextStep()">
            Continue
            <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
      </div>

      <!-- ══ STEP 2: EMPLOYMENT & INCOME ══ -->
      <div class="step-content" id="step-2">
        <div class="section-eyebrow">Step 2 of 5</div>
        <h1 class="section-title">Employment & Income</h1>
        <p class="section-desc">Tell us about your work and how you earn. This helps us determine the right loan size for you.</p>

        <div class="field-row cols-2">
          <div>
            <label>Employment Status <span class="req">*</span></label>
            <select id="emp-status" onchange="toggleEmpFields()">
              <option value="">Select</option>
              <option>Employed (Full-time)</option>
              <option>Employed (Part-time)</option>
              <option>Self-Employed / Business Owner</option>
              <option>Civil Servant / Government Employee</option>
              <option>Contractor / Freelancer</option>
              <option>Retired</option>
              <option>Unemployed</option>
            </select>
          </div>
          <div>
            <label>Employment Sector <span class="req">*</span></label>
            <select id="emp-sector">
              <option value="">Select sector</option>
              <option>Banking & Finance</option>
              <option>Government / Civil Service</option>
              <option>Healthcare & Pharmaceuticals</option>
              <option>Education & Training</option>
              <option>Technology & Telecoms</option>
              <option>Trade & Commerce</option>
              <option>Agriculture & Agribusiness</option>
              <option>Transport & Logistics</option>
              <option>Construction & Real Estate</option>
              <option>Oil & Gas</option>
              <option>Manufacturing</option>
              <option>Creative & Media</option>
              <option>Other</option>
            </select>
          </div>
        </div>

        <div class="field-row cols-2" id="employer-fields">
          <div>
            <label>Employer / Business Name <span class="req">*</span></label>
            <input type="text" id="employer" placeholder="e.g. Lagos State Government">
          </div>
          <div>
            <label>Years in Current Role / Business <span class="req">*</span></label>
            <select id="emp-years">
              <option value="">Select</option>
              <option>Less than 6 months</option>
              <option>6 months to 1 year</option>
              <option>1 to 2 years</option>
              <option>2 to 5 years</option>
              <option>5 to 10 years</option>
              <option>Over 10 years</option>
            </select>
          </div>
        </div>

        <div class="field-row cols-2">
          <div>
            <label>Income Type <span class="req">*</span></label>
            <select id="income-type">
              <option value="">Select</option>
              <option>Fixed Monthly Salary</option>
              <option>Business Revenue (Regular)</option>
              <option>Commission-Based</option>
              <option>Irregular / Seasonal</option>
              <option>Pension</option>
              <option>Rental Income</option>
              <option>Multiple Sources</option>
            </select>
          </div>
          <div>
            <label>Pay Frequency <span class="req">*</span></label>
            <select id="pay-freq">
              <option value="">Select</option>
              <option>Monthly</option>
              <option>Bi-weekly</option>
              <option>Weekly</option>
              <option>Daily</option>
              <option>Project-based</option>
            </select>
          </div>
        </div>

        <div class="field-row cols-2">
          <div>
            <label>Monthly Net Income (₦) <span class="req">*</span></label>
            <div class="input-prefix-wrap">
              <span class="input-prefix">₦</span>
              <input type="number" id="monthly-income" placeholder="0.00" min="0">
            </div>
            <div class="input-hint">Take-home income after tax and deductions</div>
          </div>
          <div>
            <label>Other Monthly Income (₦)</label>
            <div class="input-prefix-wrap">
              <span class="input-prefix">₦</span>
              <input type="number" id="other-income" placeholder="0.00" min="0">
            </div>
            <div class="input-hint">Rental, commission, business, etc.</div>
          </div>
        </div>

        <div class="field-row cols-2">
          <div>
            <label>Total Monthly Obligations (₦)</label>
            <div class="input-prefix-wrap">
              <span class="input-prefix">₦</span>
              <input type="number" id="obligations" placeholder="0.00" min="0">
            </div>
            <div class="input-hint">Existing loan repayments, rent, etc.</div>
          </div>
          <div>
            <label>Number of Active Loans</label>
            <input type="number" id="active-loans" placeholder="0" min="0">
            <div class="input-hint">Across all lenders including this application</div>
          </div>
        </div>

        <div class="field-row cols-2">
          <div>
            <label>Previous Loan Default History</label>
            <select id="default-history">
              <option value="Never">Never defaulted</option>
              <option value="5yr">Defaulted — over 5 years ago</option>
              <option value="2-5yr">Defaulted — 2 to 5 years ago</option>
              <option value="recent">Defaulted — within the last 2 years</option>
            </select>
          </div>
          <div>
            <label>Work / Office Phone Number</label>
            <input type="tel" id="work-phone" placeholder="e.g. 0123456789">
          </div>
        </div>

        <div class="form-nav">
          <button class="btn btn-secondary" onclick="prevStep()">
            <svg viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            Back
          </button>
          <button class="btn btn-primary" onclick="nextStep()">
            Continue
            <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
      </div>

      <!-- ══ STEP 3: LOAN REQUEST ══ -->
      <div class="step-content" id="step-3">
        <div class="section-eyebrow">Step 3 of 5</div>
        <h1 class="section-title">Loan Request</h1>
        <p class="section-desc">Tell us how much you need, what it's for, and how you plan to repay.</p>

        <div class="field-row cols-2">
          <div>
            <label>Loan Amount Requested (₦) <span class="req">*</span></label>
            <div class="input-prefix-wrap">
              <span class="input-prefix">₦</span>
              <input type="number" id="loan-amount" placeholder="0.00" min="10000" oninput="updateDSR()">
            </div>
          </div>
          <div>
            <label>Loan Tenure <span class="req">*</span></label>
            <select id="loan-tenure" onchange="updateDSR()">
              <option value="">Select</option>
              <option value="3">3 months</option>
              <option value="6">6 months</option>
              <option value="9">9 months</option>
              <option value="12">12 months</option>
              <option value="18">18 months</option>
              <option value="24">24 months</option>
              <option value="36">36 months</option>
            </select>
          </div>
        </div>

        <div class="field-row cols-2">
          <div>
            <label>Purpose of Loan <span class="req">*</span></label>
            <select id="loan-purpose">
              <option value="">Select purpose</option>
              <option>Working Capital / Business Expansion</option>
              <option>Equipment / Machinery Purchase</option>
              <option>Stock / Inventory Purchase</option>
              <option>School Fees / Education</option>
              <option>Medical / Healthcare</option>
              <option>Home Renovation</option>
              <option>Vehicle Purchase</option>
              <option>Personal / Emergency</option>
              <option>Salary Advance</option>
              <option>Other</option>
            </select>
          </div>
          <div>
            <label>Loan Type <span class="req">*</span></label>
            <select id="loan-type">
              <option>Cash Loan</option>
              <option>Revolving Credit</option>
            </select>
          </div>
        </div>

        <!-- DSR indicator -->
        <div id="dsr-card" style="display:none;background:white;border:1px solid var(--border);border-radius:var(--radius-lg);padding:18px 20px;margin-bottom:24px">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px">
            <div style="font-size:12px;font-weight:600;color:var(--text-muted);letter-spacing:0.06em;text-transform:uppercase">Estimated Repayment Overview</div>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">
            <div style="text-align:center;padding:12px;background:var(--off-white);border-radius:8px">
              <div style="font-size:11px;color:var(--text-muted);margin-bottom:4px">Monthly Repayment</div>
              <div style="font-size:18px;font-weight:600;color:var(--text-primary)" id="dsr-monthly">—</div>
            </div>
            <div style="text-align:center;padding:12px;background:var(--off-white);border-radius:8px">
              <div style="font-size:11px;color:var(--text-muted);margin-bottom:4px">Total Repayable</div>
              <div style="font-size:18px;font-weight:600;color:var(--text-primary)" id="dsr-total">—</div>
            </div>
            <div style="text-align:center;padding:12px;background:var(--off-white);border-radius:8px">
              <div style="font-size:11px;color:var(--text-muted);margin-bottom:4px">Debt-Service Ratio</div>
              <div style="font-size:18px;font-weight:600" id="dsr-ratio">—</div>
            </div>
          </div>
        </div>

        <div class="field-group">
          <label>Brief Description of Loan Purpose</label>
          <textarea id="loan-desc" placeholder="Briefly describe what the funds will be used for and how repayment will be made. e.g. Purchase of 50 bags of rice for resale at Balogun Market..."></textarea>
        </div>

        <div class="field-row cols-2">
          <div>
            <label>Collateral / Asset Value (₦)</label>
            <div class="input-prefix-wrap">
              <span class="input-prefix">₦</span>
              <input type="number" id="collateral" placeholder="0.00" min="0">
            </div>
            <div class="input-hint">Leave blank if unsecured application</div>
          </div>
          <div>
            <label>Guarantor Available?</label>
            <select id="guarantor">
              <option>No guarantor</option>
              <option>Yes — guarantor available</option>
            </select>
          </div>
        </div>

        <div class="form-nav">
          <button class="btn btn-secondary" onclick="prevStep()">
            <svg viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            Back
          </button>
          <button class="btn btn-primary" onclick="nextStep()">
            Continue
            <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
      </div>

      <!-- ══ STEP 4: DOCUMENTS ══ -->
      <div class="step-content" id="step-4">
        <div class="section-eyebrow">Step 4 of 5</div>
        <h1 class="section-title">Supporting Documents</h1>
        <p class="section-desc">Upload clear, legible copies of the documents below. All four are required to process your application.</p>

        <div class="callout callout-info">
          <div class="callout-icon">i</div>
          <div class="callout-body">
            <strong>Accepted formats:</strong> PDF, JPG, PNG, JPEG &nbsp;·&nbsp; <strong>Max file size:</strong> 5MB per document.
            Ensure documents are clear, fully visible, and not expired. Blurred or cropped files will delay processing.
          </div>
        </div>

        <div class="docs-grid">
          <div>
            <label>Business Registration Certificate <span class="req">*</span></label>
            <div class="upload-zone" id="zone-biz">
              <input type="file" accept=".pdf,.jpg,.jpeg,.png" onchange="handleUpload(this,'biz','Business Reg. Certificate')">
              <div class="upload-icon">
                <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              </div>
              <div class="upload-title">Click or drag to upload</div>
              <div class="upload-sub">CAC Certificate of Incorporation or Business Name</div>
              <div style="margin-top:8px">
                <span class="upload-tag">PDF</span>
                <span class="upload-tag">JPG</span>
                <span class="upload-tag">PNG</span>
              </div>
            </div>
            <div id="file-biz"></div>
          </div>

          <div>
            <label>6 Months Bank Statement <span class="req">*</span></label>
            <div class="upload-zone" id="zone-bank">
              <input type="file" accept=".pdf,.jpg,.jpeg,.png" onchange="handleUpload(this,'bank','Bank Statement')">
              <div class="upload-icon">
                <svg viewBox="0 0 24 24"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg>
              </div>
              <div class="upload-title">Click or drag to upload</div>
              <div class="upload-sub">Last 6 consecutive months — stamped by bank</div>
              <div style="margin-top:8px">
                <span class="upload-tag">PDF</span>
                <span class="upload-tag">JPG</span>
                <span class="upload-tag">PNG</span>
              </div>
            </div>
            <div id="file-bank"></div>
          </div>

          <div>
            <label>Tax Identification Number (TIN) <span class="req">*</span></label>
            <div class="upload-zone" id="zone-tin">
              <input type="file" accept=".pdf,.jpg,.jpeg,.png" onchange="handleUpload(this,'tin','TIN Certificate')">
              <div class="upload-icon">
                <svg viewBox="0 0 24 24"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
              </div>
              <div class="upload-title">Click or drag to upload</div>
              <div class="upload-sub">FIRS-issued TIN certificate or JTAX card</div>
              <div style="margin-top:8px">
                <span class="upload-tag">PDF</span>
                <span class="upload-tag">JPG</span>
                <span class="upload-tag">PNG</span>
              </div>
            </div>
            <div id="file-tin"></div>
          </div>

          <div>
            <label>Utility Bill / Proof of Address <span class="req">*</span></label>
            <div class="upload-zone" id="zone-utility">
              <input type="file" accept=".pdf,.jpg,.jpeg,.png" onchange="handleUpload(this,'utility','Utility Bill')">
              <div class="upload-icon">
                <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
              </div>
              <div class="upload-title">Click or drag to upload</div>
              <div class="upload-sub">NEPA/EKEDC bill, LAWMA, or water bill — not older than 3 months</div>
              <div style="margin-top:8px">
                <span class="upload-tag">PDF</span>
                <span class="upload-tag">JPG</span>
                <span class="upload-tag">PNG</span>
              </div>
            </div>
            <div id="file-utility"></div>
          </div>
        </div>

        <div class="divider"><div class="divider-line"></div><div class="divider-label">Optional but recommended</div><div class="divider-line"></div></div>

        <div class="field-row cols-2">
          <div>
            <label>Valid Government ID</label>
            <div class="upload-zone" style="padding:18px 16px">
              <input type="file" accept=".pdf,.jpg,.jpeg,.png" onchange="handleUpload(this,'id','Govt ID')">
              <div style="display:flex;align-items:center;gap:12px">
                <div class="upload-icon" style="margin:0;flex-shrink:0">
                  <svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/></svg>
                </div>
                <div style="text-align:left">
                  <div class="upload-title" style="font-size:13px">NIN / Passport / Driver's Licence</div>
                  <div class="upload-sub">Any valid government-issued photo ID</div>
                </div>
              </div>
            </div>
            <div id="file-id"></div>
          </div>
          <div>
            <label>Passport Photograph</label>
            <div class="upload-zone" style="padding:18px 16px">
              <input type="file" accept=".jpg,.jpeg,.png" onchange="handleUpload(this,'passport','Passport Photo')">
              <div style="display:flex;align-items:center;gap:12px">
                <div class="upload-icon" style="margin:0;flex-shrink:0">
                  <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="10" r="3"/><path d="M7 20.662V19a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v1.662"/></svg>
                </div>
                <div style="text-align:left">
                  <div class="upload-title" style="font-size:13px">Recent passport photograph</div>
                  <div class="upload-sub">White background, taken within 6 months</div>
                </div>
              </div>
            </div>
            <div id="file-passport"></div>
          </div>
        </div>

        <div class="form-nav">
          <button class="btn btn-secondary" onclick="prevStep()">
            <svg viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            Back
          </button>
          <button class="btn btn-primary" onclick="nextStep()">
            Continue
            <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
      </div>

      <!-- ══ STEP 5: BVN & REVIEW ══ -->
      <div class="step-content" id="step-5">
        <div class="section-eyebrow">Step 5 of 5</div>
        <h1 class="section-title">BVN Verification & Review</h1>
        <p class="section-desc">Enter your BVN for identity verification, then review your application before final submission.</p>

        <!-- BVN -->
        <div style="background:white;border:1px solid var(--border);border-radius:var(--radius-xl);padding:28px;margin-bottom:32px;box-shadow:var(--shadow-sm)">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:18px">
            <div style="width:40px;height:40px;background:var(--teal-pale);border-radius:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0">
              <svg style="width:20px;height:20px;stroke:var(--teal);fill:none;stroke-width:1.8" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <div>
              <div style="font-size:14px;font-weight:600;color:var(--text-primary)">Bank Verification Number (BVN)</div>
              <div style="font-size:12px;color:var(--text-muted)">Required for identity verification — soft enquiry only</div>
            </div>
          </div>

          <div class="field-row cols-2">
            <div>
              <label>Your BVN <span class="req">*</span></label>
              <div class="bvn-wrap">
                <input type="text" id="bvn" placeholder="11-digit BVN" maxlength="11" oninput="validateBVN()">
                <span class="bvn-status" id="bvn-status"></span>
              </div>
              <div class="input-hint">Dial *565*0# on your registered phone to retrieve your BVN</div>
            </div>
            <div style="display:flex;align-items:flex-end">
              <div style="background:var(--off-white);border-radius:var(--radius);padding:14px 16px;font-size:13px;color:var(--text-secondary);line-height:1.6;width:100%">
                Your BVN is encrypted in transit. It will only be used for credit bureau verification and will not be stored beyond this application.
              </div>
            </div>
          </div>

          <label class="checkbox-row" style="margin-top:8px">
            <input type="checkbox" id="bvn-consent">
            <div class="checkbox-text">
              I consent to my BVN being used to retrieve my credit bureau data for the purpose of this loan application.
              <small>This is a soft enquiry and will not negatively affect my credit score.</small>
            </div>
          </label>
        </div>

        <!-- Review summary -->
        <div style="font-size:13px;font-weight:600;color:var(--text-muted);letter-spacing:0.08em;text-transform:uppercase;margin-bottom:16px">Application Summary</div>

        <div class="review-block">
          <div class="review-block-header">
            <div class="review-block-title">Personal Information</div>
            <button class="review-edit" onclick="goTo(1)">Edit</button>
          </div>
          <div class="review-block-body">
            <div class="review-row"><div class="review-key">Full Name</div><div class="review-val" id="rv-name">—</div></div>
            <div class="review-row"><div class="review-key">Phone</div><div class="review-val" id="rv-phone">—</div></div>
            <div class="review-row"><div class="review-key">Email</div><div class="review-val" id="rv-email">—</div></div>
            <div class="review-row"><div class="review-key">State</div><div class="review-val" id="rv-state">—</div></div>
          </div>
        </div>

        <div class="review-block">
          <div class="review-block-header">
            <div class="review-block-title">Employment & Income</div>
            <button class="review-edit" onclick="goTo(2)">Edit</button>
          </div>
          <div class="review-block-body">
            <div class="review-row"><div class="review-key">Status</div><div class="review-val" id="rv-emp">—</div></div>
            <div class="review-row"><div class="review-key">Sector</div><div class="review-val" id="rv-sector">—</div></div>
            <div class="review-row"><div class="review-key">Monthly Net Income</div><div class="review-val" id="rv-income">—</div></div>
            <div class="review-row"><div class="review-key">Default History</div><div class="review-val" id="rv-default">—</div></div>
          </div>
        </div>

        <div class="review-block">
          <div class="review-block-header">
            <div class="review-block-title">Loan Request</div>
            <button class="review-edit" onclick="goTo(3)">Edit</button>
          </div>
          <div class="review-block-body">
            <div class="review-row"><div class="review-key">Amount Requested</div><div class="review-val" id="rv-amount">—</div></div>
            <div class="review-row"><div class="review-key">Tenure</div><div class="review-val" id="rv-tenure">—</div></div>
            <div class="review-row"><div class="review-key">Purpose</div><div class="review-val" id="rv-purpose">—</div></div>
            <div class="review-row"><div class="review-key">Monthly Repayment (est.)</div><div class="review-val" id="rv-repay">—</div></div>
          </div>
        </div>

        <div class="review-block">
          <div class="review-block-header">
            <div class="review-block-title">Documents Submitted</div>
            <button class="review-edit" onclick="goTo(4)">Edit</button>
          </div>
          <div class="review-block-body">
            <div class="review-row">
              <div class="review-key">Business Registration</div>
              <div class="review-val" id="rv-biz">—</div>
            </div>
            <div class="review-row">
              <div class="review-key">Bank Statement</div>
              <div class="review-val" id="rv-bank">—</div>
            </div>
            <div class="review-row">
              <div class="review-key">TIN Certificate</div>
              <div class="review-val" id="rv-tin">—</div>
            </div>
            <div class="review-row">
              <div class="review-key">Utility Bill</div>
              <div class="review-val" id="rv-util">—</div>
            </div>
          </div>
        </div>

        <!-- Declaration -->
        <div style="background:white;border:1px solid var(--border);border-radius:var(--radius-xl);padding:24px;margin-top:24px;box-shadow:var(--shadow-sm)">
          <div style="font-size:13px;font-weight:600;color:var(--text-primary);margin-bottom:14px">Declaration</div>
          <label class="checkbox-row">
            <input type="checkbox" id="declare-1">
            <div class="checkbox-text">
              I confirm that all information provided in this application is true, accurate, and complete to the best of my knowledge.
              <small>Providing false information is a criminal offence under Nigerian law.</small>
            </div>
          </label>
          <label class="checkbox-row">
            <input type="checkbox" id="declare-2">
            <div class="checkbox-text">
              I authorise Joyful Smile Nigeria Limited to verify my information through relevant databases, registries, and credit bureaus.
              <small>In line with the Nigeria Data Protection Regulation (NDPR) 2019.</small>
            </div>
          </label>
          <label class="checkbox-row" style="margin-bottom:0">
            <input type="checkbox" id="declare-3">
            <div class="checkbox-text">
              I have read and I agree to the Terms & Conditions and Privacy Policy of Joyful Smile Nigeria Limited.
            </div>
          </label>
        </div>

        <div class="form-nav">
          <button class="btn btn-secondary" onclick="prevStep()">
            <svg viewBox="0 0 24 24"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            Back
          </button>
          <button class="btn btn-primary" onclick="submitApp()" style="padding:0 40px;background:var(--navy)">
            Submit Application
            <svg viewBox="0 0 24 24"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>
          </button>
        </div>
      </div>

    </div><!-- /form-area -->

    <!-- ══ SUCCESS SCREEN ══ -->
    <div class="success-screen" id="success-screen">
      <div class="success-icon">
        <svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
      </div>
      <div style="font-family:'Cormorant Garamond',serif;font-size:36px;font-weight:600;color:var(--navy);margin-bottom:8px">
        Application Submitted
      </div>
      <p style="font-size:15px;color:var(--text-secondary);margin-bottom:4px">Your reference number</p>
      <div class="success-ref" id="ref-number">JSN-000000</div>
      <p class="success-note">
        Your loan application has been received. Our team will review your documents and contact you within <strong>24 to 48 business hours</strong>.
      </p>
      <div class="success-steps">
        <div class="success-step">
          <div class="success-step-num">01 — Received</div>
          <div class="success-step-text">Your application is in our review queue</div>
        </div>
        <div class="success-step">
          <div class="success-step-num">02 — Review</div>
          <div class="success-step-text">Documents and credit check within 24–48 hrs</div>
        </div>
        <div class="success-step">
          <div class="success-step-num">03 — Decision</div>
          <div class="success-step-text">You will be contacted with our decision</div>
        </div>
      </div>
      <div style="font-size:13px;color:var(--text-muted);margin-top:8px">
        Questions? Call <strong style="color:var(--teal)">07010057527</strong> or email <strong style="color:var(--teal)">joyfulsmilesnigerialimited@gmail.com</strong>
      </div>
    </div>

  </div><!-- /main-content -->
</div><!-- /app-shell -->

<script>
let currentStep = 1;
const totalSteps = 5;
const uploadedFiles = {};

const stepNames = ['Personal Details','Employment & Income','Loan Request','Documents','BVN & Review'];
const progressPct = [20,40,60,80,100];

function goTo(n){
  document.getElementById('step-'+currentStep).classList.remove('active');
  document.querySelectorAll('.step-item')[currentStep-1].classList.remove('active');
  if(n > currentStep) document.querySelectorAll('.step-item')[currentStep-1].classList.add('completed');
  currentStep = n;
  document.getElementById('step-'+currentStep).classList.add('active');
  document.querySelectorAll('.step-item')[currentStep-1].classList.remove('completed');
  document.querySelectorAll('.step-item')[currentStep-1].classList.add('active');
  document.getElementById('top-step-name').textContent = stepNames[n-1];
  document.getElementById('progress-fill').style.width = progressPct[n-1]+'%';
  document.getElementById('progress-label').textContent = 'Step '+n+' of '+totalSteps;
  if(n===5) populateReview();
  window.scrollTo({top:0,behavior:'smooth'});
}

function nextStep(){ if(currentStep < totalSteps) goTo(currentStep+1); }
function prevStep(){ if(currentStep > 1) goTo(currentStep-1); }

function validateBVN(){
  const v = document.getElementById('bvn').value;
  const s = document.getElementById('bvn-status');
  if(v.length===11 && /^\d+$/.test(v)){s.textContent='✓ Valid';s.className='bvn-status bvn-ok';}
  else if(v.length>0){s.textContent='11 digits required';s.className='bvn-status bvn-err';}
  else{s.textContent='';s.className='bvn-status';}
}

function handleUpload(input, key, label){
  const file = input.files[0];
  if(!file) return;
  uploadedFiles[key] = {name:file.name, file:file};
  const container = document.getElementById('file-'+key);
  container.innerHTML = `
    <div class="file-uploaded">
      <svg viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5"/></svg>
      <span class="file-uploaded-name">${file.name}</span>
      <button class="file-remove" onclick="removeFile('${key}','${label}')">×</button>
    </div>`;
  document.getElementById('zone-'+key)?.classList.add('uploaded');
}

function removeFile(key){
  delete uploadedFiles[key];
  document.getElementById('file-'+key).innerHTML='';
}

function fmt(n){ return '₦'+Number(n).toLocaleString('en-NG'); }

function updateDSR(){
  const amt = parseFloat(document.getElementById('loan-amount').value)||0;
  const tenure = parseInt(document.getElementById('loan-tenure').value)||0;
  const income = parseFloat(document.getElementById('monthly-income').value)||0;
  const card = document.getElementById('dsr-card');
  if(amt>0 && tenure>0){
    card.style.display='block';
    const monthly = amt/tenure;
    const total = monthly*tenure;
    const dsr = income>0 ? (monthly/income*100) : null;
    document.getElementById('dsr-monthly').textContent = fmt(monthly.toFixed(0));
    document.getElementById('dsr-total').textContent = fmt(total.toFixed(0));
    const ratioEl = document.getElementById('dsr-ratio');
    if(dsr!==null){
      ratioEl.textContent = dsr.toFixed(1)+'%';
      ratioEl.style.color = dsr>50?'#C0392B':dsr>35?'#8B5E00':'#0F7B6C';
    } else {
      ratioEl.textContent='—';ratioEl.style.color='var(--text-primary)';
    }
  } else { card.style.display='none'; }
}

function docBadge(key){
  if(uploadedFiles[key]) return `<span class="review-badge badge-ok">✓ Uploaded</span>`;
  return `<span class="review-badge badge-missing">Not uploaded</span>`;
}

function populateReview(){
  const fn = document.getElementById('first-name').value;
  const ln = document.getElementById('last-name').value;
  document.getElementById('rv-name').textContent = [fn,ln].filter(Boolean).join(' ')||'—';
  document.getElementById('rv-phone').textContent = document.getElementById('phone').value||'—';
  document.getElementById('rv-email').textContent = document.getElementById('email').value||'—';
  document.getElementById('rv-state').textContent = document.getElementById('state').value||'—';
  document.getElementById('rv-emp').textContent = document.getElementById('emp-status').value||'—';
  document.getElementById('rv-sector').textContent = document.getElementById('emp-sector').value||'—';
  const inc = document.getElementById('monthly-income').value;
  document.getElementById('rv-income').textContent = inc ? fmt(inc) : '—';
  document.getElementById('rv-default').textContent = document.getElementById('default-history').value||'—';
  const lamt = document.getElementById('loan-amount').value;
  document.getElementById('rv-amount').textContent = lamt ? fmt(lamt) : '—';
  const ten = document.getElementById('loan-tenure').value;
  document.getElementById('rv-tenure').textContent = ten ? ten+' months' : '—';
  document.getElementById('rv-purpose').textContent = document.getElementById('loan-purpose').value||'—';
  if(lamt && ten){ document.getElementById('rv-repay').textContent = fmt((lamt/ten).toFixed(0))+' / month'; }
  document.getElementById('rv-biz').innerHTML = docBadge('biz');
  document.getElementById('rv-bank').innerHTML = docBadge('bank');
  document.getElementById('rv-tin').innerHTML = docBadge('tin');
  document.getElementById('rv-util').innerHTML = docBadge('utility');
}

function submitApp(){
  const d1=document.getElementById('declare-1').checked;
  const d2=document.getElementById('declare-2').checked;
  const d3=document.getElementById('declare-3').checked;
  const bvnOk=document.getElementById('bvn-status').classList.contains('bvn-ok');
  const consent=document.getElementById('bvn-consent').checked;
  if(!d1||!d2||!d3){alert('Please confirm all three declaration checkboxes before submitting.');return;}
  if(!bvnOk){alert('Please enter a valid 11-digit BVN before submitting.');return;}
  if(!consent){alert('Please provide consent for BVN verification.');return;}
  const ref = 'JSN-'+Math.random().toString().slice(2,8).toUpperCase();
  document.getElementById('ref-number').textContent = ref;
  document.querySelector('.main-content .form-area').style.display='none';
  document.querySelector('.top-bar').style.display='none';
  document.getElementById('success-screen').style.display='flex';
  document.querySelectorAll('.step-item').forEach(s=>s.classList.add('completed'));
}

function toggleEmpFields(){
  const v=document.getElementById('emp-status').value;
  const show=!v.includes('Unemployed')&&!v.includes('Retired');
  document.getElementById('employer-fields').style.opacity=show?'1':'0.4';
}
</script>
</body>
</html>
