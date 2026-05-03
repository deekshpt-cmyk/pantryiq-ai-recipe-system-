import streamlit as st

st.set_page_config(
    page_title="Mise 🌿 — AI Kitchen Intelligence",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════
# SESSION STATE
# ══════════════════════════════════════════════════════════════════
if "page" not in st.session_state:
    st.session_state.page = "home"

# ══════════════════════════════════════════════════════════════════
# GLOBAL CSS
# ══════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&family=Playfair+Display:wght@600&display=swap');

/* ── Reset Streamlit chrome ── */
            .nav-logo {
    padding-left: 16px;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    max-width: 100% !important;
}
section[data-testid="stSidebar"] { display: none !important; }
div[data-testid="stDecoration"] { display: none !important; }

/* ── Root tokens ── */
:root {
    --sage:        #6aa67a;
    --sage-mid:    #8bbf99;
    --sage-light:  #b8d9c2;
    --sage-pale:   #e6f3eb;
    --sage-ghost:  #f2f8f4;
    --cream:       #f8faf7;
    --white:       #ffffff;
    --text-dark:   #1c271e;
    --text-mid:    #4a5e4c;
    --text-soft:   #8aa08c;
    --border:      #cfe4d6;
}

/* ══════════════════════════════
   BASE BACKGROUND
══════════════════════════════ */
html, body {
    background: linear-gradient(135deg, #f8faf7 0%, #eef5ef 50%, #e8f3ec 100%) !important;
    font-family: 'DM Sans', sans-serif !important;
    color: var(--text-dark) !important;
}
.stApp {
    background: linear-gradient(135deg, #f8faf7 0%, #eef5ef 50%, #e8f3ec 100%) !important;
    font-family: 'DM Sans', sans-serif !important;
    color: var(--text-dark) !important;
    position: relative !important;
    min-height: 100vh;
}
.stApp::before {
    content: "";
    position: fixed;
    top: -60px; left: -60px;
    width: 420px; height: 420px;
    background: radial-gradient(circle at 30% 30%, #6aa67a33, #b8d9c244 40%, transparent 70%);
    filter: blur(48px);
    z-index: 0;
    pointer-events: none;
    animation: blobFloat 20s ease-in-out infinite;
}
.stApp::after {
    content: "";
    position: fixed;
    bottom: -80px; right: -80px;
    width: 520px; height: 520px;
    background: radial-gradient(circle at 65% 65%, #6aa67a22, #a8d4b622 45%, transparent 70%);
    filter: blur(60px);
    z-index: 0;
    pointer-events: none;
    animation: blobFloat 26s ease-in-out infinite reverse;
}
.main, .block-container {
    position: relative !important;
    z-index: 1 !important;
}
div[data-testid="stVerticalBlock"] > div { gap: 0 !important; }

/* ── Background layers ── */
.bg-mesh {
    position: fixed; inset: 0;
    pointer-events: none; z-index: 0;
    background:
        radial-gradient(ellipse 60% 50% at 15% 20%, #b8d9c228, transparent),
        radial-gradient(ellipse 45% 55% at 85% 75%, #8bbf9920, transparent),
        radial-gradient(ellipse 35% 40% at 60% 10%, #cfe4d618, transparent),
        radial-gradient(ellipse 50% 35% at 30% 88%, #a8d4b615, transparent);
}
.bg-grid {
    position: fixed; inset: 0;
    pointer-events: none; z-index: 0;
    background-image: radial-gradient(circle, #6aa67a18 1px, transparent 1px);
    background-size: 36px 36px;
    opacity: .55;
}
.bg-blob {
    position: fixed; pointer-events: none; z-index: 0;
    border-radius: 50%; filter: blur(72px);
}
.blob-1 { width:560px; height:560px; top:-180px; left:-200px;
           background: radial-gradient(circle, #b8d9c240, #6aa67a18 55%, transparent);
           opacity:.7; animation: blobFloat 22s ease-in-out infinite; }
.blob-2 { width:440px; height:440px; bottom:20px; right:-140px;
           background: radial-gradient(circle, #8bbf9938, #cfe4d620 55%, transparent);
           opacity:.65; animation: blobFloat 28s ease-in-out infinite reverse; }
.blob-3 { width:300px; height:300px; top:38%; left:66%;
           background: radial-gradient(circle, #a8d4b630, transparent);
           opacity:.55; animation: blobFloat 19s ease-in-out 5s infinite; }
.blob-4 { width:220px; height:220px; top:62%; left:14%;
           background: radial-gradient(circle, #cfe4d635, transparent);
           opacity:.5; animation: blobFloat 24s ease-in-out 10s infinite reverse; }
@keyframes blobFloat {
    0%,100% { transform: translateY(0) scale(1) rotate(0deg); }
    33%      { transform: translateY(-22px) scale(1.05) rotate(2deg); }
    66%      { transform: translateY(-10px) scale(.97) rotate(-1deg); }
}
.deco-corner { position:fixed; pointer-events:none; z-index:0; opacity:.07; }
.deco-tl { top:0; left:0; width:340px; height:340px;
            animation: leafFloat 30s ease-in-out infinite; }
.deco-br { bottom:0; right:0; width:420px; height:420px;
            animation: leafFloat 36s ease-in-out 8s infinite reverse; }
.deco-tr { top:60px; right:0; width:240px; height:240px;
            opacity:.05; animation: leafFloat 26s ease-in-out 4s infinite; }
.leaf { position:fixed; pointer-events:none; z-index:0;
        opacity:.09; font-size:2rem;
        animation: leafFloat 22s ease-in-out infinite; filter: blur(.4px); }
@keyframes leafFloat {
    0%,100% { transform: translateY(0) rotate(-5deg); }
    50%      { transform: translateY(-24px) rotate(9deg); }
}

/* ══════════════════════════════
   NAVBAR WRAPPER
══════════════════════════════ */
.navbar-wrap {
    position: sticky; top: 0; z-index: 500;
    /* full-width strip with very light tint behind the centered pill */
    background: transparent;
    padding: 14px 24px;
}
/* Centered white container */
.navbar-inner {
    display: flex; align-items: center; justify-content: space-between;
    max-width: 1100px; margin: 0 auto;
    padding: 14px 40px;
    background: rgba(255, 255, 255, 0.72);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid #e6efe8;
    border-radius: 20px;
    box-shadow: 0 4px 24px rgba(106,166,122,.08);
}
/* Playfair Display logo */
.nav-logo {
    font-family: 'Playfair Display', serif;
    font-size: 28px; font-weight: 600;
    color: var(--text-dark); letter-spacing: 0.5px;
    white-space: nowrap; line-height: 1;
}
.nav-logo span { color: var(--sage); }

/* ── Nav buttons styled as text links ── */
/* Target ALL button variants inside the nav column */
div[data-testid="stHorizontalBlock"] button,
div[data-testid="column"] button {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 4px 0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: .88rem !important;
    font-weight: 400 !important;
    color: var(--text-mid) !important;
    cursor: pointer !important;
    letter-spacing: .15px !important;
    transition: color .2s !important;
    min-height: unset !important;
    height: auto !important;
    line-height: 1.4 !important;
}
div[data-testid="stHorizontalBlock"] button:hover,
div[data-testid="column"] button:hover {
    color: var(--sage) !important;
    background: transparent !important;
    border: none !important;
}
div[data-testid="stHorizontalBlock"] button:focus,
div[data-testid="column"] button:focus {
    outline: none !important;
    box-shadow: none !important;
}
/* Active nav button */
button.nav-active {
    color: var(--sage) !important;
    font-weight: 500 !important;
    border-bottom: 2px solid var(--sage) !important;
    border-radius: 0 !important;
    padding-bottom: 2px !important;
}
/* Streamlit injects p tags inside buttons */
div[data-testid="column"] button p {
    font-size: .88rem !important;
    font-weight: inherit !important;
    color: inherit !important;
    margin: 0 !important;
}

/* ══════════════════════════════
   HERO
══════════════════════════════ */
.hero-section {
    display: flex; flex-direction: column; align-items: center;
    text-align: center; padding: 72px 24px 36px;
    position: relative; z-index: 1;
}
.badge {
    display: inline-flex; align-items: center; gap: 7px;
    background: var(--sage-pale); border: 1px solid var(--border);
    border-radius: 99px; padding: 6px 20px;
    font-size: .76rem; font-weight: 500;
    color: var(--text-mid); letter-spacing: .5px;
    margin-bottom: 30px; animation: fadeDown .55s ease both;
}
.hero-heading {
    font-family: 'Lora', serif;
    font-size: clamp(2.2rem, 4.5vw, 3.6rem);
    font-weight: 600; line-height: 1.2; color: var(--text-dark);
    max-width: 680px; margin: 0 auto 22px;
    animation: fadeDown .65s ease .1s both;
}
.hero-heading em { color: var(--sage); font-style: italic; }
.hero-sub {
    font-size: 1.05rem; line-height: 1.75;
    color: var(--text-mid); font-weight: 300;
    max-width: 440px; margin: 0 auto;
    animation: fadeDown .7s ease .2s both;
}
@keyframes fadeDown {
    from { opacity:0; transform:translateY(-18px); }
    to   { opacity:1; transform:translateY(0); }
}

/* ══════════════════════════════
   UPLOAD CARD
══════════════════════════════ */
.upload-section {
    display: flex; flex-direction: column; align-items: center;
    padding: 8px 24px 0; position: relative; z-index: 1;
    animation: fadeUp .75s ease .3s both;
}
@keyframes fadeUp {
    from { opacity:0; transform:translateY(24px); }
    to   { opacity:1; transform:translateY(0); }
}
.upload-card {
    width: 100%; max-width: 580px;
    background: var(--sage-ghost);
    border: 2.5px dashed var(--sage-light);
    border-radius: 36px; padding: 46px 44px 32px;
    text-align: center;
    box-shadow: 0 8px 36px rgba(106,166,122,.14);
    transition: box-shadow .3s, border-color .3s;
}
.upload-card:hover {
    box-shadow: 0 16px 52px rgba(106,166,122,.22);
    border-color: var(--sage);
}
.upload-icon { font-size: 3rem; margin-bottom: 14px;
               filter: drop-shadow(0 4px 10px rgba(106,166,122,.3)); }
.upload-title {
    font-family: 'Lora', serif;
    font-size: 1.5rem; font-weight: 600;
    color: var(--text-dark); margin-bottom: 6px;
}
.upload-sub  { font-size:.9rem; color:var(--text-soft); margin-bottom:4px; }
.upload-types{ font-size:.74rem; color:var(--text-soft);
               letter-spacing:.25px; margin-bottom:28px; }
div[data-testid="stFileUploader"] { background: transparent !important; }
div[data-testid="stFileUploader"] > label { display:none !important; }
div[data-testid="stFileUploadDropzone"] {
    background: var(--white) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 20px !important;
    padding: 18px 20px !important;
    transition: border-color .25s;
}
div[data-testid="stFileUploadDropzone"]:hover { border-color: var(--sage) !important; }
div[data-testid="stFileUploadDropzone"] span {
    color: var(--text-soft) !important;
    font-size: .85rem !important;
    font-family: 'DM Sans', sans-serif !important;
}
button[data-testid="baseButton-secondary"] {
    background: var(--sage) !important;
    color: white !important;
    border: none !important;
    border-radius: 99px !important;
    padding: 9px 24px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: .84rem !important;
    font-weight: 500 !important;
}
button[data-testid="baseButton-secondary"]:hover { background: #4d8a5e !important; }

/* ══════════════════════════════
   HELPER TEXT
══════════════════════════════ */
.helper-text {
    text-align: center; font-size:.84rem; color:var(--text-soft);
    padding: 20px 24px 100px;
    position: relative; z-index:1;
    animation: fadeUp .75s ease .5s both; letter-spacing:.1px;
}

/* ══════════════════════════════
   PREVIEW
══════════════════════════════ */
.preview-outer {
    display:flex; justify-content:center;
    padding:0 24px 20px; position:relative; z-index:1;
}
.preview-card {
    width:100%; max-width:580px;
    background:var(--white); border:1px solid var(--border);
    border-radius:28px; padding:22px;
    box-shadow: 0 8px 32px rgba(106,166,122,.12);
}
.preview-label {
    font-size:.72rem; text-transform:uppercase;
    letter-spacing:.6px; color:var(--text-soft);
    font-weight:500; margin-bottom:12px;
}
.preview-ok { margin-top:12px; font-size:.82rem; color:var(--sage); font-weight:500; }

/* ══════════════════════════════
   RECIPES PAGE
══════════════════════════════ */
.page-section {
    display: flex; flex-direction: column; align-items: center;
    text-align: center; padding: 72px 24px 40px;
    position: relative; z-index: 1;
}
.page-title {
    font-family: 'Lora', serif;
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 600; color: var(--text-dark);
    margin-bottom: 16px; animation: fadeDown .6s ease both;
}
.page-sub {
    font-size: 1rem; color: var(--text-soft);
    font-weight: 300; max-width: 440px;
    animation: fadeDown .7s ease .1s both;
}
.recipe-grid {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 20px; max-width: 900px; width: 100%;
    margin-top: 48px; animation: fadeUp .8s ease .2s both;
}
.recipe-card {
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 24px; padding: 28px 24px;
    text-align: left;
    box-shadow: 0 4px 20px rgba(106,166,122,.10);
    transition: transform .25s, box-shadow .25s;
}
.recipe-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 36px rgba(106,166,122,.18);
}
.recipe-emoji { font-size: 2.2rem; margin-bottom: 12px; }
.recipe-name {
    font-family: 'Lora', serif; font-size: 1.05rem;
    font-weight: 600; color: var(--text-dark); margin-bottom: 6px;
}
.recipe-desc { font-size: .8rem; color: var(--text-soft); line-height: 1.55; }
.recipe-tag {
    display: inline-block; margin-top: 14px;
    background: var(--sage-pale); color: var(--sage);
    border-radius: 99px; padding: 3px 12px;
    font-size: .7rem; font-weight: 500; letter-spacing: .3px;
}
.empty-state {
    margin-top: 40px;
    background: var(--white);
    border: 2px dashed var(--border);
    border-radius: 28px; padding: 48px 40px;
    max-width: 480px; width: 100%;
    animation: fadeUp .7s ease .2s both;
}
.empty-icon { font-size: 3rem; margin-bottom: 16px; }
.empty-title {
    font-family: 'Lora', serif; font-size: 1.3rem;
    font-weight: 600; color: var(--text-dark); margin-bottom: 8px;
}
.empty-desc { font-size: .88rem; color: var(--text-soft); line-height: 1.65; }

/* ══════════════════════════════
   SHOPPING LIST PAGE
══════════════════════════════ */
.shopping-wrap {
    display: flex; flex-direction: column; align-items: center;
    padding: 72px 24px 100px;
    position: relative; z-index: 1;
}
.shopping-card {
    width: 100%; max-width: 620px;
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: 32px; padding: 36px 36px 32px;
    box-shadow: 0 8px 36px rgba(106,166,122,.13);
    animation: fadeUp .7s ease both;
}
.shopping-header {
    display: flex; align-items: center; gap: 12px;
    margin-bottom: 28px;
}
.shopping-header-icon { font-size: 1.9rem; }
.shopping-header-text { font-family: 'Lora', serif; font-size: 1.4rem;
                         font-weight: 600; color: var(--text-dark); }
.shopping-item {
    display: flex; align-items: center; gap: 14px;
    padding: 13px 0;
    border-bottom: 1px solid var(--sage-ghost);
}
.shopping-item:last-child { border-bottom: none; }
.item-check {
    width: 22px; height: 22px; border-radius: 50%;
    border: 2px solid var(--sage-light);
    flex-shrink: 0; display: flex; align-items: center; justify-content: center;
    font-size: .75rem; color: var(--sage);
    transition: background .2s;
}
.item-check.done { background: var(--sage); border-color: var(--sage); color: white; }
.item-text { font-size: .9rem; color: var(--text-mid); flex: 1; }
.item-text.done { text-decoration: line-through; color: var(--text-soft); }
.item-cat {
    font-size: .68rem; color: var(--text-soft);
    background: var(--sage-ghost);
    border-radius: 99px; padding: 2px 10px;
    letter-spacing: .3px;
}
.shopping-empty {
    text-align: center; padding: 20px 0;
    color: var(--text-soft); font-size: .88rem;
}
/* Streamlit text_input in shopping list */
div[data-testid="stTextInput"] input {
    border: 1.5px solid var(--border) !important;
    border-radius: 99px !important;
    padding: 10px 20px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: .88rem !important;
    background: var(--sage-ghost) !important;
    color: var(--text-dark) !important;
    transition: border-color .2s !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: var(--sage) !important;
    outline: none !important;
    box-shadow: 0 0 0 3px rgba(106,166,122,.12) !important;
}

/* ══════════════════════════════
   FLOATING CHAT WIDGET
══════════════════════════════ */
.chat-widget {
    position: fixed; bottom: 98px; right: 26px;
    width: 300px; z-index: 1000;
    background: var(--white);
    border-radius: 28px; border: 1px solid var(--border);
    box-shadow: 0 20px 60px rgba(0,0,0,.13), 0 4px 16px rgba(106,166,122,.15);
    overflow: hidden; animation: widgetIn .5s ease both;
}
@keyframes widgetIn {
    from { opacity:0; transform:translateY(32px) scale(.96); }
    to   { opacity:1; transform:translateY(0) scale(1); }
}
.chat-head {
    background: linear-gradient(135deg, var(--sage) 0%, #4d8a5e 100%);
    padding: 14px 16px; display: flex; align-items: center; gap: 11px;
}
.chat-avatar {
    width:38px; height:38px; border-radius:50%;
    background:rgba(255,255,255,.22);
    display:flex; align-items:center; justify-content:center;
    font-size:1.15rem; flex-shrink:0;
}
.chat-name { font-weight:600; font-size:.92rem; color:#fff; line-height:1.2;
             font-family:'DM Sans',sans-serif; }
.chat-status { display:flex; align-items:center; gap:5px;
               font-size:.68rem; color:rgba(255,255,255,.82); }
.dot { width:7px; height:7px; border-radius:50%; background:#a8f4bc;
       box-shadow:0 0 7px #a8f4bc; }
.chat-body { padding:16px 14px 14px; }
.bubble {
    background:var(--sage-ghost); border-radius:4px 18px 18px 18px;
    padding:11px 14px; font-size:.81rem; line-height:1.6;
    color:var(--text-mid); margin-bottom:14px; font-family:'DM Sans',sans-serif;
}
.chat-input {
    display:flex; align-items:center; gap:8px;
    background:var(--sage-ghost); border-radius:99px;
    padding:9px 9px 9px 16px; border:1px solid var(--border);
}
.chat-placeholder { flex:1; font-size:.8rem; color:var(--text-soft);
                    font-family:'DM Sans',sans-serif; }
.send-btn {
    width:30px; height:30px; border-radius:50%; background:var(--sage);
    display:flex; align-items:center; justify-content:center;
    color:white; font-size:.78rem; flex-shrink:0; cursor:pointer; border:none;
    transition:background .2s;
}
.send-btn:hover { background:#4d8a5e; }

/* ══════════════════════════════
   FAB
══════════════════════════════ */
.fab {
    position:fixed; bottom:26px; right:26px;
    width:58px; height:58px; border-radius:50%;
    background:linear-gradient(135deg, var(--sage) 0%, #4d8a5e 100%);
    box-shadow:0 8px 28px rgba(106,166,122,.50);
    display:flex; align-items:center; justify-content:center;
    font-size:1.45rem; z-index:1001; cursor:pointer; border:none;
    transition:transform .2s, box-shadow .2s;
}
.fab:hover { transform:scale(1.1) rotate(-5deg);
             box-shadow:0 14px 38px rgba(106,166,122,.6); }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# BACKGROUND DECORATIONS (rendered once, always visible)
# ══════════════════════════════════════════════════════════════════
st.markdown("""
<div class="bg-grid"></div>
<div class="bg-mesh"></div>
<div class="bg-blob blob-1"></div>
<div class="bg-blob blob-2"></div>
<div class="bg-blob blob-3"></div>
<div class="bg-blob blob-4"></div>
<svg class="deco-corner deco-tl" viewBox="0 0 340 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="60"  cy="80"  rx="55" ry="90" fill="#6aa67a" transform="rotate(-30 60 80)"/>
  <ellipse cx="130" cy="50"  rx="40" ry="75" fill="#4d8a5e" transform="rotate(-15 130 50)"/>
  <ellipse cx="30"  cy="160" rx="35" ry="65" fill="#8bbf99" transform="rotate(-45 30 160)"/>
  <ellipse cx="170" cy="90"  rx="30" ry="58" fill="#6aa67a" transform="rotate(-5 170 90)"/>
  <ellipse cx="90"  cy="30"  rx="20" ry="42" fill="#4d8a5e" transform="rotate(-55 90 30)"/>
  <path d="M60 80 Q80 120 100 160"  stroke="#4d8a5e" stroke-width="3"   stroke-linecap="round" fill="none" opacity=".5"/>
  <path d="M130 50 Q140 90 150 130" stroke="#4d8a5e" stroke-width="2.5" stroke-linecap="round" fill="none" opacity=".4"/>
</svg>
<svg class="deco-corner deco-br" viewBox="0 0 420 420" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="340" cy="360" rx="70" ry="110" fill="#6aa67a" transform="rotate(30 340 360)"/>
  <ellipse cx="280" cy="390" rx="50" ry="85"  fill="#8bbf99" transform="rotate(15 280 390)"/>
  <ellipse cx="390" cy="290" rx="42" ry="72"  fill="#4d8a5e" transform="rotate(50 390 290)"/>
  <ellipse cx="230" cy="370" rx="30" ry="55"  fill="#6aa67a" transform="rotate(5 230 370)"/>
  <circle cx="360" cy="240" r="22" fill="#cfe4d6"/>
  <circle cx="310" cy="310" r="16" fill="#b8d9c2"/>
  <path d="M340 360 Q310 320 280 280" stroke="#4d8a5e" stroke-width="3" stroke-linecap="round" fill="none" opacity=".4"/>
</svg>
<svg class="deco-corner deco-tr" viewBox="0 0 240 240" fill="none" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="200" cy="40"  rx="35" ry="60" fill="#8bbf99" transform="rotate(25 200 40)"/>
  <ellipse cx="230" cy="100" rx="28" ry="50" fill="#6aa67a" transform="rotate(40 230 100)"/>
  <ellipse cx="170" cy="20"  rx="22" ry="40" fill="#4d8a5e" transform="rotate(10 170 20)"/>
</svg>
<div class="leaf" style="top:12%;left:3%;animation-delay:-3s;">🌿</div>
<div class="leaf" style="top:55%;left:93%;animation-delay:-9s;font-size:1.5rem;">🍃</div>
<div class="leaf" style="top:80%;left:7%;animation-delay:-15s;font-size:1.2rem;">🌱</div>
<div class="leaf" style="top:28%;left:91%;animation-delay:-1s;font-size:1.8rem;">🌿</div>
<div class="leaf" style="top:70%;left:50%;animation-delay:-20s;font-size:1rem;opacity:.05;">🍀</div>
<div class="leaf" style="top:42%;left:2%;animation-delay:-7s;font-size:1.1rem;">🌾</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# NAVBAR  (sticky, uses st.columns + st.button for navigation)
# ══════════════════════════════════════════════════════════════════
with st.container():
    st.markdown('<div class="navbar-wrap"><div class="navbar-inner">', unsafe_allow_html=True)

    logo_col, spacer, nav_home, nav_recipes, nav_shopping = st.columns([2.2, 6.5, 1, 1, 1.4])
    with logo_col:
        st.markdown('<div class="nav-logo">Mise <span>🌿</span></div>', unsafe_allow_html=True)

    with nav_home:
        home_style = "nav-active" if st.session_state.page == "home" else ""
        if st.button("Home", key="btn_home"):
            st.session_state.page = "home"
            st.rerun()
        if home_style:
            st.markdown(f"""<style>
                div[data-testid="column"]:nth-of-type(3) button {{
                    color: var(--sage) !important; font-weight: 500 !important;
                    border-bottom: 2px solid var(--sage) !important;
                    border-radius: 0 !important; padding-bottom: 3px !important;
                }}
            </style>""", unsafe_allow_html=True)

    with nav_recipes:
        recipes_style = "nav-active" if st.session_state.page == "recipes" else ""
        if st.button("Recipes", key="btn_recipes"):
            st.session_state.page = "recipes"
            st.rerun()
        if recipes_style:
            st.markdown(f"""<style>
                div[data-testid="column"]:nth-of-type(4) button {{
                    color: var(--sage) !important; font-weight: 500 !important;
                    border-bottom: 2px solid var(--sage) !important;
                    border-radius: 0 !important; padding-bottom: 3px !important;
                }}
            </style>""", unsafe_allow_html=True)

    with nav_shopping:
        shopping_style = "nav-active" if st.session_state.page == "shopping" else ""
        if st.button("Shopping List", key="btn_shopping"):
            st.session_state.page = "shopping"
            st.rerun()
        if shopping_style:
            st.markdown(f"""<style>
                div[data-testid="column"]:nth-of-type(5) button {{
                    color: var(--sage) !important; font-weight: 500 !important;
                    border-bottom: 2px solid var(--sage) !important;
                    border-radius: 0 !important; padding-bottom: 3px !important;
                }}
            </style>""", unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# PAGE FUNCTIONS
# ══════════════════════════════════════════════════════════════════

def show_home():
    # ── Hero ──────────────────────────────────────────────────────
    with st.container():
        st.markdown("""
        <section class="hero-section">
          <div class="badge">✨ AI-powered kitchen intelligence</div>
          <h1 class="hero-heading">
            Cook smarter with <em>what you have</em> 👨‍🍳✨
          </h1>
          <p class="hero-sub">
            Snap your fridge, discover recipes, skip the grocery run.<br>
            Your fridge already has the answer.
          </p>
        </section>
        """, unsafe_allow_html=True)

    # ── Upload card ───────────────────────────────────────────────
    with st.container():
        st.markdown("""
        <div class="upload-section">
          <div class="upload-card">
            <div class="upload-icon">📷</div>
            <div class="upload-title">Upload your fridge</div>
            <div class="upload-sub">Drag &amp; drop or click to browse</div>
            <div class="upload-types">JPG · PNG · WEBP &nbsp;up to 10 MB</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        _, mid, _ = st.columns([1, 2, 1])
        with mid:
            uploaded = st.file_uploader(
                label="fridge_upload",
                type=["jpg", "jpeg", "png", "webp"],
                accept_multiple_files=True,
                label_visibility="collapsed",
            )

    # ── Preview ───────────────────────────────────────────────────
    if uploaded:
        st.markdown('<div class="preview-outer"><div class="preview-card">', unsafe_allow_html=True)
        st.markdown('<div class="preview-label">📸 Uploaded image</div>', unsafe_allow_html=True)
        _, img_col, _ = st.columns([1, 2, 1])
        with img_col:
            for file in uploaded:
                st.image(file,width="stretch")
        st.markdown(
            '<div class="preview-ok">✅ &nbsp;Image received — analysing ingredients…</div>',
            unsafe_allow_html=True,
        )
        st.markdown('</div></div>', unsafe_allow_html=True)

    # ── Helper text ───────────────────────────────────────────────
    with st.container():
        st.markdown("""
        <p class="helper-text">
          🌿 We'll detect ingredients and suggest recipes instantly — no account needed.
        </p>
        """, unsafe_allow_html=True)


def show_recipes():
    st.markdown("""
    <div class="page-section">
      <h1 class="page-title">Recipes 🍳</h1>
      <p class="page-sub">Upload a fridge photo on the Home page and your personalised recipes will appear here.</p>
      <div class="recipe-grid">

        <div class="recipe-card">
          <div class="recipe-emoji">🥗</div>
          <div class="recipe-name">Spring Veggie Salad</div>
          <div class="recipe-desc">Fresh greens, cherry tomatoes, cucumber and a lemon-herb vinaigrette. Ready in 10 minutes.</div>
          <span class="recipe-tag">Quick · 10 min</span>
        </div>

        <div class="recipe-card">
          <div class="recipe-emoji">🍜</div>
          <div class="recipe-name">Ginger Miso Noodles</div>
          <div class="recipe-desc">Silky ramen noodles in a warming miso broth with soft-boiled egg and crispy tofu.</div>
          <span class="recipe-tag">Comfort · 25 min</span>
        </div>

        <div class="recipe-card">
          <div class="recipe-emoji">🥘</div>
          <div class="recipe-name">Smoky Chickpea Stew</div>
          <div class="recipe-desc">Hearty chickpeas simmered with smoked paprika, tomatoes and spinach. One-pot wonder.</div>
          <span class="recipe-tag">Vegan · 30 min</span>
        </div>

        <div class="recipe-card">
          <div class="recipe-emoji">🍳</div>
          <div class="recipe-name">Herb Frittata</div>
          <div class="recipe-desc">Fluffy oven-baked eggs with fresh herbs, feta and roasted cherry tomatoes.</div>
          <span class="recipe-tag">Veggie · 20 min</span>
        </div>

        <div class="recipe-card">
          <div class="recipe-emoji">🌮</div>
          <div class="recipe-name">Black Bean Tacos</div>
          <div class="recipe-desc">Spiced black beans, avocado crema, pickled onions in warm corn tortillas.</div>
          <span class="recipe-tag">Plant-based · 15 min</span>
        </div>

        <div class="recipe-card">
          <div class="recipe-emoji">🥙</div>
          <div class="recipe-name">Roasted Veggie Wrap</div>
          <div class="recipe-desc">Charred peppers, hummus and rocket in a toasted wholegrain wrap with tahini drizzle.</div>
          <span class="recipe-tag">Healthy · 20 min</span>
        </div>

      </div>
    </div>
    """, unsafe_allow_html=True)


def show_shopping():
    # Session state for the list
    if "shopping_items" not in st.session_state:
        st.session_state.shopping_items = [
            {"text": "Olive oil",      "category": "Pantry",  "done": False},
            {"text": "Cherry tomatoes","category": "Produce", "done": False},
            {"text": "Feta cheese",    "category": "Dairy",   "done": True},
            {"text": "Chickpeas (tin)","category": "Pantry",  "done": False},
            {"text": "Fresh spinach",  "category": "Produce", "done": False},
        ]

    st.markdown('<div class="shopping-wrap">', unsafe_allow_html=True)

    # ── Title ─────────────────────────────────────────────────────
    st.markdown("""
    <div style="text-align:center;padding-bottom:32px;position:relative;z-index:1;">
      <h1 class="page-title">Shopping List 🛒</h1>
      <p class="page-sub">Add ingredients you need and tick them off as you shop.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Input row ─────────────────────────────────────────────────
    _, input_col, btn_col, _ = st.columns([1, 3.5, 1, 1])
    with input_col:
        new_item = st.text_input(
            label="new_item",
            placeholder="  Add an ingredient…",
            label_visibility="collapsed",
            key="shopping_input",
        )
    with btn_col:
        add_clicked = st.button("＋ Add", key="add_item_btn", use_container_width=True)
        st.markdown("""<style>
            div[data-testid="column"]:nth-of-type(3) button {
                background: var(--sage) !important;
                color: white !important;
                border-radius: 99px !important;
                border: none !important;
                font-size:.86rem !important;
                font-weight:500 !important;
                padding: 9px 0 !important;
            }
            div[data-testid="column"]:nth-of-type(3) button:hover {
                background: #4d8a5e !important;
                color: white !important;
            }
        </style>""", unsafe_allow_html=True)

    if add_clicked and new_item.strip():
        st.session_state.shopping_items.append(
            {"text": new_item.strip(), "category": "General", "done": False}
        )
        st.rerun()

    # ── List card ─────────────────────────────────────────────────
    _, card_col, _ = st.columns([1, 4, 1])
    with card_col:
        st.markdown('<div class="shopping-card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="shopping-header">
          <span class="shopping-header-icon">🛒</span>
          <span class="shopping-header-text">Your List</span>
        </div>
        """, unsafe_allow_html=True)

        if not st.session_state.shopping_items:
            st.markdown("""
            <div class="shopping-empty">
              Your list is empty — add ingredients above 🌿
            </div>
            """, unsafe_allow_html=True)
        else:
            for i, item in enumerate(st.session_state.shopping_items):
                check_icon = "✓" if item["done"] else ""
                check_cls  = "item-check done" if item["done"] else "item-check"
                text_cls   = "item-text done"  if item["done"] else "item-text"
                col_chk, col_txt, col_del = st.columns([0.5, 6, 0.8])

                with col_chk:
                    if st.button(check_icon or "○", key=f"chk_{i}"):
                        st.session_state.shopping_items[i]["done"] = not item["done"]
                        st.rerun()
                    st.markdown(f"""<style>
                        /* per-item check button */
                    </style>""", unsafe_allow_html=True)

                with col_txt:
                    st.markdown(
                        f'<div style="display:flex;align-items:center;gap:10px;padding:6px 0;">'
                        f'<span class="{text_cls}">{item["text"]}</span>'
                        f'<span class="item-cat">{item["category"]}</span>'
                        f'</div>',
                        unsafe_allow_html=True,
                    )

                with col_del:
                    if st.button("✕", key=f"del_{i}"):
                        st.session_state.shopping_items.pop(i)
                        st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)  # shopping-card

    # ── Summary ───────────────────────────────────────────────────
    total  = len(st.session_state.shopping_items)
    done_n = sum(1 for x in st.session_state.shopping_items if x["done"])
    if total:
        st.markdown(
            f'<p style="text-align:center;font-size:.8rem;color:var(--text-soft);'
            f'margin-top:16px;position:relative;z-index:1;">'
            f'✅ {done_n} of {total} items ticked off</p>',
            unsafe_allow_html=True,
        )

    st.markdown('</div>', unsafe_allow_html=True)  # shopping-wrap


# ══════════════════════════════════════════════════════════════════
# ROUTER
# ══════════════════════════════════════════════════════════════════
if st.session_state.page == "home":
    show_home()
elif st.session_state.page == "recipes":
    show_recipes()
elif st.session_state.page == "shopping":
    show_shopping()

# ══════════════════════════════════════════════════════════════════
# FLOATING CHAT WIDGET + FAB (always visible)
# ══════════════════════════════════════════════════════════════════
st.markdown("""
<div class="chat-widget">
  <div class="chat-head">
    <div class="chat-avatar">👩‍🍳</div>
    <div>
      <div class="chat-name">Mise 👩‍🍳</div>
      <div class="chat-status"><span class="dot"></span> Online</div>
    </div>
  </div>
  <div class="chat-body">
    <div class="bubble">
      Hi! I'm Mise 👋 Ask me anything about recipes or ingredients!
    </div>
    <div class="chat-input">
      <span class="chat-placeholder">Type a message…</span>
      <button class="send-btn">➤</button>
    </div>
  </div>
</div>
<button class="fab">🌿</button>
""", unsafe_allow_html=True)
