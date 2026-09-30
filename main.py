import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cosmos — Graph to Music",
    page_icon="✿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML = r"""
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">


<style>
:root{
    --bg:#f6f7fb;
    --surface:#ffffff;
    --surface-soft:#fbfbfd;
    --text:#17181d;
    --muted:#6f7480;
    --muted-2:#9aa0ab;
    --line:#e6e7ec;
    --line-strong:#d9dbe3;
    --accent:#7a5af8;
    --accent-dark:#6242e5;
    --accent-soft:#f0edff;
    --danger:#b4233c;
    --danger-soft:#fff1f3;
    --success:#167c62;
    --success-soft:#eaf8f3;
    --shadow:0 12px 36px rgba(25, 25, 40, .06);
    --shadow-sm:0 3px 14px rgba(25, 25, 40, .05);
}

*{box-sizing:border-box;}

html{scroll-behavior:smooth;}

body{
    margin:0;
    font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",
        "Noto Sans KR",sans-serif;
    background:var(--bg);
    color:var(--text);
}

button,input,select{font:inherit;}

button{
    border:1px solid var(--line-strong);
    background:#fff;
    color:var(--text);
    border-radius:9px;
    padding:9px 12px;
    min-height:38px;
    cursor:pointer;
    transition:
        background .16s ease,
        border-color .16s ease,
        color .16s ease,
        transform .16s ease,
        box-shadow .16s ease;
}

button:hover{
    background:#f8f8fb;
    border-color:#c9cbd5;
}

button:active{transform:translateY(1px);}

button.active,
button.primary{
    background:var(--accent);
    border-color:var(--accent);
    color:#fff;
    font-weight:700;
    box-shadow:0 5px 14px rgba(122,90,248,.18);
}

button.active:hover,
button.primary:hover{
    background:var(--accent-dark);
    border-color:var(--accent-dark);
}

button.danger{
    background:var(--danger-soft);
    border-color:#f2c7cf;
    color:var(--danger);
}

button.danger:hover{
    background:#ffe7eb;
    border-color:#e9aeb9;
}

button.success{
    background:var(--success-soft);
    border-color:#b9e5d7;
    color:var(--success);
}

button.success:hover{
    background:#def3eb;
}

button:disabled{
    opacity:.45;
    cursor:not-allowed;
}

#cosmos{
    max-width:1380px;
    margin:0 auto;
    padding:30px 30px 60px;
}

/* ---------- brand ---------- */

.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:24px;
    margin-bottom:20px;
}

.brand{
    display:flex;
    align-items:center;
    gap:14px;
    min-width:0;
}

.brandMark{
    width:48px;
    height:48px;
    border:1px solid #ddd7ff;
    background:#fff;
    border-radius:14px;
    display:grid;
    place-items:center;
    box-shadow:var(--shadow-sm);
    flex:none;
}

.brandMark svg{
    width:34px;
    height:34px;
    display:block;
}

.brandText{min-width:0;}

.logo{
    font-size:25px;
    line-height:1;
    font-weight:800;
    letter-spacing:-.8px;
}

.logo span{color:var(--accent);}

.subtitle{
    color:var(--muted);
    font-size:13px;
    margin-top:7px;
    line-height:1.5;
}

.brandMeaning{
    display:flex;
    align-items:center;
    gap:7px;
    margin-top:6px;
    color:#8b8797;
    font-size:10px;
    letter-spacing:.08em;
    text-transform:uppercase;
}

.brandMeaning .dot{
    width:4px;
    height:4px;
    border-radius:50%;
    background:#b7adf7;
}

.badge{
    display:inline-flex;
    align-items:center;
    gap:6px;
    padding:7px 10px;
    border:1px solid var(--line);
    border-radius:999px;
    background:#fff;
    color:#6e687f;
    font-size:10px;
    font-weight:700;
    letter-spacing:.04em;
}

.badge::before{
    content:"";
    width:6px;
    height:6px;
    border-radius:50%;
    background:#72c6aa;
}

/* ---------- navigation ---------- */

.topNav{
    display:flex;
    align-items:center;
    gap:5px;
    padding:5px;
    margin-bottom:18px;
    border:1px solid var(--line);
    background:rgba(255,255,255,.84);
    border-radius:12px;
    box-shadow:var(--shadow-sm);
}

.navItem{
    appearance:none;
    -webkit-appearance:none;
    border:0;
    background:transparent;
    color:#707582;
    text-decoration:none;
    font-size:12px;
    font-weight:700;
    padding:8px 12px;
    min-height:34px;
    border-radius:8px;
    cursor:pointer;
    box-shadow:none;
}

.navItem:hover{
    background:#f3f2f8;
    color:var(--text);
    border-color:transparent;
}

.navItem.active,
.navItem.primaryNav{
    background:var(--accent-soft);
    color:#6548db;
}

.navItem.active:hover,
.navItem.primaryNav:hover{
    background:#e9e5ff;
    color:#573bc7;
}

/* ---------- layout ---------- */

.grid{
    display:grid;
    grid-template-columns:minmax(0,1fr) 390px;
    gap:18px;
    align-items:start;
}

.card{
    background:var(--surface);
    border:1px solid var(--line);
    border-radius:16px;
    padding:18px;
    box-shadow:var(--shadow);
}

.card + .card{margin-top:14px;}

.card h2{
    font-size:14px;
    line-height:1.3;
    margin:0 0 12px;
    letter-spacing:-.2px;
}

.section{
    margin-top:18px;
    padding-top:18px;
    border-top:1px solid #f0f0f3;
}

.section h2{
    font-size:12px;
    color:#555a66;
    margin-bottom:9px;
}

.eyebrow{
    color:var(--accent);
    font-size:10px;
    font-weight:800;
    letter-spacing:.1em;
    text-transform:uppercase;
    margin-bottom:6px;
}

.panelTitle{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:12px;
    margin-bottom:12px;
}

.panelTitle h2{margin:0;}

.panelHint{
    color:var(--muted-2);
    font-size:10px;
}

/* ---------- graph ---------- */

.graphWrap{
    position:relative;
    overflow:hidden;
    border:1px solid var(--line);
    border-radius:12px;
    background:#fcfcfe;
}

canvas{
    width:100%;
    height:590px;
    background:#fcfcfe;
    border-radius:12px;
    display:block;
    touch-action:none;
}

.graphToolbar{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:10px;
    padding:10px 11px;
    border:1px solid var(--line);
    border-top:0;
    border-radius:0 0 12px 12px;
    background:#fff;
}

.graphToolbarLabel{
    color:var(--muted);
    font-size:10px;
}

.controls{
    display:flex;
    gap:7px;
    flex-wrap:wrap;
    margin-top:10px;
}

.graphControls button{
    min-height:34px;
    padding:7px 10px;
    font-size:11px;
}

/* ---------- modes ---------- */

.modeBar{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:6px;
}

.modeBar button{
    width:100%;
    font-size:11px;
    min-height:37px;
}

.help{
    font-size:11px;
    color:#777d89;
    line-height:1.7;
}

.help b{color:#505560;}

.editNotice{
    display:none;
    margin-top:8px;
    padding:10px 11px;
    border-radius:9px;
    background:var(--accent-soft);
    border:1px solid #ddd6ff;
    color:#6047c9;
    font-size:10px;
    line-height:1.55;
}

.editNotice.active{display:block;}

/* ---------- inputs ---------- */

input[type=text],
input[type=search]{
    width:100%;
    padding:10px 11px;
    border-radius:9px;
    border:1px solid var(--line-strong);
    background:#fff;
    color:var(--text);
    outline:none;
    transition:border-color .16s ease,box-shadow .16s ease;
}

input[type=text]:focus,
input[type=search]:focus,
select:focus{
    border-color:#b5a6ff;
    box-shadow:0 0 0 3px rgba(122,90,248,.09);
}

select{
    width:100%;
    padding:10px 11px;
    border-radius:9px;
    border:1px solid var(--line-strong);
    background:#fff;
    color:var(--text);
    outline:none;
}

label{
    display:block;
    font-size:10px;
    font-weight:700;
    color:#777d89;
    margin-bottom:6px;
}

.row{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
}

.row3{
    display:grid;
    grid-template-columns:1fr 1fr 1fr;
    gap:8px;
}

/* ---------- info ---------- */

.info{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:7px;
    padding:9px;
    border-radius:10px;
    background:#fafafd;
    border:1px solid var(--line);
    font-size:11px;
    color:#707682;
    line-height:1.6;
}

.info > div{
    padding:7px 8px;
    border-radius:7px;
    background:#fff;
    border:1px solid #f0f0f3;
}

#message{
    min-height:18px;
    margin-top:7px;
    color:#b4233c;
    font-size:11px;
}

/* ---------- library ---------- */

.libraryList{
    display:flex;
    flex-direction:column;
    gap:6px;
    margin-top:10px;
}

.songItem{
    display:flex;
    align-items:center;
    gap:8px;
    padding:9px;
    border:1px solid var(--line);
    border-radius:9px;
    background:#fff;
}

.songInfo{
    flex:1;
    min-width:0;
}

.songTitle{
    font-size:11px;
    font-weight:700;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.songDate{
    font-size:9px;
    color:#9aa0ab;
    margin-top:3px;
}

.songActions{
    display:flex;
    gap:4px;
    flex:none;
}

.songActions button{
    min-height:27px;
    padding:4px 7px;
    font-size:9px;
}

.libraryMeta{
    font-size:10px;
    color:#8d929d;
    margin-top:7px;
}

/* ---------- layers ---------- */

.layerList{
    display:flex;
    flex-direction:column;
    gap:7px;
}

.layerItem{
    border:1px solid var(--line);
    border-radius:10px;
    padding:9px;
    background:#fff;
    cursor:default;
    transition:border-color .15s ease,box-shadow .15s ease,background .15s ease;
}

.layerItem:hover{background:#fcfcfe;}

.layerItem.selected{
    border-color:#bdb0ff;
    background:#fbfaff;
    box-shadow:0 0 0 2px rgba(122,90,248,.08);
}

.layerTop{
    display:flex;
    align-items:center;
    gap:8px;
    cursor:pointer;
}

.layerColor{
    width:9px;
    height:9px;
    border-radius:50%;
    flex:none;
}

.layerNameInput{
    flex:1;
    min-width:0;
    padding:5px 6px !important;
    min-height:28px;
    font-size:11px;
    font-weight:700;
    border-color:transparent !important;
    background:transparent !important;
    box-shadow:none !important;
}

.layerNameInput:focus{
    border-color:var(--line-strong) !important;
    background:#fff !important;
}

.layerType{
    font-size:8px;
    color:#a0a5ae;
    font-weight:800;
    letter-spacing:.06em;
    flex:none;
}

.layerActions{
    display:flex;
    align-items:center;
    gap:8px;
    margin-top:7px;
}

.layerActions button{
    min-height:28px;
    padding:4px 7px;
    font-size:9px;
}

.visibility{
    font-size:9px;
    color:#777d89;
    flex:none;
}

.volumeBox{
    flex:1;
    min-width:0;
}

.volumeHeader{
    display:flex;
    justify-content:space-between;
    font-size:9px;
    color:#999ea8;
    margin-bottom:3px;
}

.layerVolume{
    width:100%;
    accent-color:var(--accent);
}

/* ---------- music ---------- */

.musicBox{
    margin-top:14px;
}

.musicHero{
    display:flex;
    justify-content:space-between;
    align-items:flex-start;
    gap:12px;
    padding:12px;
    margin-bottom:12px;
    border:1px solid #e5defe;
    border-radius:11px;
    background:linear-gradient(180deg,#fbfaff,#fff);
}

.musicHeroTitle{
    font-size:12px;
    font-weight:800;
    color:#302b3b;
}

.musicHeroText{
    margin-top:3px;
    color:#888391;
    font-size:10px;
    line-height:1.5;
}

.musicMark{
    width:30px;
    height:30px;
    border-radius:9px;
    display:grid;
    place-items:center;
    background:var(--accent-soft);
    color:var(--accent);
    font-size:14px;
    flex:none;
}

.now{
    font-size:11px;
    color:#777d89;
    min-height:20px;
    margin:9px 0;
}

.progress{
    height:6px;
    background:#eeeef3;
    border-radius:99px;
    overflow:hidden;
}

#bar{
    height:100%;
    width:0;
    background:var(--accent);
    transition:width .05s linear;
}

.layerCount{
    font-size:10px;
    color:#8d929d;
    margin-top:6px;
}

/* ---------- principle ---------- */

.notice{
    padding:10px;
    border-radius:9px;
    background:#fafafd;
    border:1px solid var(--line);
    color:#777d89;
    font-size:10px;
    line-height:1.6;
}

hr{
    border:0;
    border-top:1px solid #eeeeF2;
    margin:14px 0;
}

/* ---------- footer ---------- */

.brandFooter{
    margin-top:18px;
    padding:13px 2px 0;
    border-top:1px solid var(--line);
    color:#9a9ea8;
    font-size:10px;
    display:flex;
    justify-content:space-between;
    gap:12px;
}

/* ---------- responsive ---------- */

@media(max-width:950px){
    #cosmos{padding:22px 18px 45px;}
    .grid{grid-template-columns:1fr;}
    canvas{height:500px;}
}

@media(max-width:600px){
    #cosmos{padding:14px 10px 35px;}
    .header{align-items:flex-start;}
    .badge{display:none;}
    .topNav{overflow-x:auto;}
    .navItem{white-space:nowrap;}
    canvas{height:390px;}
    .row,.row3,.info{grid-template-columns:1fr;}
    .brandFooter{flex-direction:column;}
}

/* =========================================================
   COSMOS WORKSPACE — DESMOS-LIKE STRUCTURE
========================================================= */

.workspaceShell{
    background:#fff;
    border:1px solid #dedfe6;
    border-radius:14px;
    box-shadow:0 8px 30px rgba(25,25,40,.07);
    overflow:hidden;
    min-height:760px;
}

.appToolbar{
    height:58px;
    display:flex;
    align-items:center;
    gap:12px;
    padding:0 16px;
    border-bottom:1px solid #e2e3e8;
    background:#fff;
}

.toolbarBrand{
    display:flex;
    align-items:center;
    gap:9px;
    font-weight:800;
    letter-spacing:-.3px;
    margin-right:6px;
}

.toolbarFlower{
    width:30px;
    height:30px;
    border:1px solid #ddd7ff;
    border-radius:8px;
    display:grid;
    place-items:center;
    background:#faf9ff;
}

.toolbarFlower svg{width:22px;height:22px;}

.fileTitle{
    height:34px;
    min-width:190px;
    border:1px solid transparent;
    background:transparent;
    padding:5px 9px;
    font-weight:650;
    color:#34353c;
    border-radius:7px;
}

.fileTitle:hover,
.fileTitle:focus{
    border-color:#d9dbe3;
    background:#fafafd;
    outline:none;
}

.toolbarSpacer{flex:1;}

.toolbarBtn{
    min-height:34px;
    padding:6px 10px;
    font-size:12px;
    border-radius:7px;
}

.toolbarBtn.icon{
    width:34px;
    padding:6px;
    font-size:16px;
}

.workspace{
    display:grid;
    grid-template-columns:310px minmax(0,1fr);
    height:702px;
}

.expressionPane{
    background:#fbfbfc;
    border-right:1px solid #dedfe6;
    display:flex;
    flex-direction:column;
    min-width:0;
    overflow:hidden;
}

.expressionHeader{
    height:58px;
    display:flex;
    align-items:center;
    gap:9px;
    padding:0 12px;
    border-bottom:1px solid #e4e5ea;
}

.expressionHeaderTitle{
    font-size:13px;
    font-weight:800;
    flex:1;
}

.addMenuWrap{position:relative;}

.addMenu{
    position:absolute;
    top:43px;
    left:0;
    z-index:30;
    width:190px;
    padding:6px;
    background:#fff;
    border:1px solid #dddfe6;
    border-radius:10px;
    box-shadow:0 14px 30px rgba(25,25,40,.12);
    display:none;
}

.addMenu.open{display:block;}

.addMenu button{
    width:100%;
    text-align:left;
    border:0;
    background:#fff;
    min-height:34px;
    font-size:11px;
    border-radius:7px;
}

.addMenu button:hover{background:#f4f2ff;}

.expressionScroll{
    flex:1;
    overflow:auto;
    padding:8px;
}

.expressionScroll .layerList{
    display:flex;
    flex-direction:column;
    gap:6px;
}

.expressionFooter{
    border-top:1px solid #e3e4e9;
    padding:9px;
    background:#fff;
}

.expressionFooterRow{
    display:flex;
    gap:6px;
}

.expressionFooter button{
    flex:1;
    min-height:32px;
    font-size:10px;
}

.compactLibrary{
    border-top:1px solid #e3e4e9;
    background:#fff;
}

.compactLibrary summary{
    cursor:pointer;
    padding:11px 12px;
    font-size:11px;
    font-weight:750;
    list-style:none;
}

.compactLibrary summary::-webkit-details-marker{display:none;}

.compactLibrary summary:after{
    content:"＋";
    float:right;
    color:#8b8e99;
}

.compactLibrary[open] summary:after{content:"−";}

.libraryInner{
    padding:0 10px 10px;
}

.libraryInner .controls{display:flex;gap:5px;flex-wrap:wrap;}
.libraryInner .controls button{min-height:30px;padding:5px 7px;font-size:9px;}
.libraryInner .section{padding-top:8px;margin-top:8px;}
.libraryInner input,.libraryInner select{min-height:32px;font-size:10px;}
.libraryInner .libraryList{max-height:100px;overflow:auto;}

.graphWorkspace{
    min-width:0;
    display:flex;
    flex-direction:column;
    background:#fff;
}

.graphTop{
    height:44px;
    display:flex;
    align-items:center;
    padding:0 12px;
    gap:8px;
    border-bottom:1px solid #e4e5ea;
}

.graphTopTitle{
    font-size:11px;
    font-weight:800;
    color:#34353c;
}

.graphTopHint{
    font-size:10px;
    color:#9a9ea8;
    flex:1;
}

.graphCanvasArea{
    position:relative;
    flex:1;
    min-height:0;
    background:#fcfcfe;
}

.graphCanvasArea canvas{
    display:block;
    width:100%;
    height:100%;
    border:0;
    border-radius:0;
}

.canvasSettings{
    position:absolute;
    top:10px;
    right:10px;
    z-index:5;
}

.canvasSettingsBtn{
    width:34px;
    height:34px;
    min-height:34px;
    padding:0;
    border-radius:8px;
    background:rgba(255,255,255,.94);
    box-shadow:0 3px 12px rgba(20,20,30,.08);
}

.settingsPanel{
    position:absolute;
    top:48px;
    right:10px;
    z-index:20;
    width:250px;
    padding:12px;
    border:1px solid #dedfe6;
    border-radius:10px;
    background:#fff;
    box-shadow:0 16px 34px rgba(20,20,30,.13);
    display:none;
}

.settingsPanel.open{display:block;}

.settingsTitle{
    font-size:11px;
    font-weight:800;
    margin-bottom:9px;
}

.settingsGrid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:7px;
}

.settingsGrid label{
    font-size:9px;
    color:#777d89;
}

.settingsGrid input{
    margin-top:3px;
    width:100%;
    min-height:30px;
    padding:5px 7px;
    font-size:10px;
}

.settingsChecks{
    margin-top:9px;
    display:flex;
    gap:12px;
    flex-wrap:wrap;
    font-size:10px;
    color:#626670;
}

.graphBottom{
    min-height:126px;
    border-top:1px solid #e2e3e8;
    padding:10px 12px;
    background:#fff;
}

.bottomGrid{
    display:grid;
    grid-template-columns:minmax(0,1.6fr) minmax(230px,.8fr);
    gap:10px;
}

.functionEditor{
    border:1px solid #e1e2e8;
    border-radius:9px;
    background:#fbfbfc;
    padding:8px;
}

.functionEditor label{
    font-size:9px;
    color:#777d89;
    margin-bottom:4px;
}

.functionEditor input{
    min-height:34px;
    background:#fff;
}

.functionActions{
    display:flex;
    gap:6px;
    margin-top:6px;
}

.functionActions button{
    min-height:30px;
    padding:5px 9px;
    font-size:10px;
}

.analysisStrip{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:5px;
}

.analysisCell{
    border:1px solid #e4e5ea;
    border-radius:8px;
    padding:7px;
    background:#fff;
    min-width:0;
}

.analysisLabel{
    font-size:8px;
    color:#9296a0;
    margin-bottom:3px;
}

.analysisValue{
    font-size:10px;
    font-weight:700;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.workspaceRail{
    position:relative;
    border-left:1px solid #dedfe6;
    background:#fff;
}

.workspaceRailTab{
    position:absolute;
    right:0;
    top:18px;
    z-index:8;
    display:flex;
    flex-direction:column;
    gap:6px;
}

.railBtn{
    width:38px;
    min-height:38px;
    padding:0;
    border-radius:8px 0 0 8px;
    background:#fff;
    box-shadow:0 3px 12px rgba(20,20,30,.07);
    font-size:16px;
}

.railPanel{
    position:absolute;
    top:0;
    right:0;
    width:330px;
    height:100%;
    padding:14px;
    background:#fff;
    border-left:1px solid #dedfe6;
    box-shadow:-12px 0 30px rgba(20,20,30,.08);
    z-index:7;
    overflow:auto;
    display:none;
}

.railPanel.open{display:block;}

.railPanelHeader{
    display:flex;
    align-items:center;
    gap:8px;
    margin-bottom:12px;
}

.railPanelHeader h3{
    margin:0;
    font-size:14px;
    flex:1;
}

.railClose{
    width:30px;
    min-height:30px;
    padding:0;
}

.railPanel .musicBox{
    margin-top:0;
}

.railPanel .card{
    border:0;
    box-shadow:none;
    padding:0;
}

.railPanel .row{
    grid-template-columns:1fr 1fr;
}

.keypad{
    position:absolute;
    right:14px;
    bottom:14px;
    z-index:12;
    width:360px;
    padding:10px;
    border:1px solid #dedfe6;
    border-radius:10px;
    background:#fff;
    box-shadow:0 16px 34px rgba(20,20,30,.13);
    display:none;
}

.keypad.open{display:block;}

.keypadGrid{
    display:grid;
    grid-template-columns:repeat(6,1fr);
    gap:5px;
}

.keypad button{
    min-height:34px;
    padding:5px;
    font-size:10px;
}

.principlePanel{
    font-size:11px;
    line-height:1.7;
    color:#656a75;
}

.principleFormula{
    margin:10px 0;
    padding:12px;
    border:1px solid #e2defc;
    background:#faf9ff;
    border-radius:9px;
    color:#4e3eb1;
    font-weight:750;
}

.workspaceHint{
    padding:7px 10px;
    font-size:9px;
    color:#9296a0;
    border-top:1px solid #e6e7ec;
    background:#fbfbfc;
}

@media(max-width:1050px){
    .workspace{grid-template-columns:270px minmax(0,1fr);}
    .bottomGrid{grid-template-columns:1fr;}
    .analysisStrip{grid-template-columns:repeat(3,1fr);}
}

@media(max-width:760px){
    .workspace{grid-template-columns:1fr;height:auto;}
    .expressionPane{height:360px;border-right:0;border-bottom:1px solid #dedfe6;}
    .graphWorkspace{height:700px;}
    .workspaceRail{position:absolute;inset:58px 0 0 0;pointer-events:none;border:0;}
    .workspaceRailTab,.railPanel{pointer-events:auto;}
    .railPanel{width:min(330px,92vw);}
}
</style>

</head>

<body>

<div id="cosmos">

<div class="header">
    <div class="brand">
        <div class="brandMark" aria-label="Cosmos flower logo">
            <svg viewBox="0 0 48 48" aria-hidden="true">
                <g fill="#8b6cf6">
                    <ellipse cx="24" cy="10.5" rx="5.2" ry="10"/>
                    <ellipse cx="35.5" cy="16" rx="5.2" ry="10" transform="rotate(45 35.5 16)"/>
                    <ellipse cx="37.5" cy="29" rx="5.2" ry="10" transform="rotate(90 37.5 29)"/>
                    <ellipse cx="29.5" cy="37" rx="5.2" ry="10" transform="rotate(135 29.5 37)"/>
                    <ellipse cx="18.5" cy="37" rx="5.2" ry="10" transform="rotate(225 18.5 37)"/>
                    <ellipse cx="10.5" cy="29" rx="5.2" ry="10" transform="rotate(270 10.5 29)"/>
                    <ellipse cx="12.5" cy="16" rx="5.2" ry="10" transform="rotate(315 12.5 16)"/>
                </g>
                <circle cx="24" cy="24" r="5.2" fill="#f5c76a"/>
                <circle cx="24" cy="24" r="2.2" fill="#8b6cf6"/>
            </svg>
        </div>
        <div class="brandText">
            <div class="logo">Cos<span>mos</span></div>
            <div class="subtitle">Graph → Music · 수학적 구조를 시각화하고 소리로 경험하는 그래핑 스튜디오</div>
            <div class="brandMeaning"><span>ORDER</span><span class="dot"></span><span>HARMONY</span><span class="dot"></span><span>EXPRESSION</span></div>
        </div>
    </div>
    <span class="badge">Cosmos v3.2 · Mathematics in Harmony</span>
</div>

<div class="workspaceShell">

    <div class="appToolbar">
        <div class="toolbarBrand">
            <div class="toolbarFlower">
                <svg viewBox="0 0 48 48" aria-hidden="true">
                    <g fill="#8b6cf6">
                        <ellipse cx="24" cy="10.5" rx="5.2" ry="10"/>
                        <ellipse cx="35.5" cy="16" rx="5.2" ry="10" transform="rotate(45 35.5 16)"/>
                        <ellipse cx="37.5" cy="29" rx="5.2" ry="10" transform="rotate(90 37.5 29)"/>
                        <ellipse cx="29.5" cy="37" rx="5.2" ry="10" transform="rotate(135 29.5 37)"/>
                        <ellipse cx="18.5" cy="37" rx="5.2" ry="10" transform="rotate(225 18.5 37)"/>
                        <ellipse cx="10.5" cy="29" rx="5.2" ry="10" transform="rotate(270 10.5 29)"/>
                        <ellipse cx="12.5" cy="16" rx="5.2" ry="10" transform="rotate(315 12.5 16)"/>
                    </g>
                    <circle cx="24" cy="24" r="5.2" fill="#f5c76a"/>
                </svg>
            </div>
            <span>COSMOS</span>
        </div>

        <input id="songName" class="fileTitle" type="text" value="Untitled Cosmos" autocomplete="off" aria-label="현재 곡 이름">

        <button id="newSong" class="toolbarBtn" title="새 작업 공간">새로 만들기</button>
        <button id="saveSong" class="toolbarBtn primary" title="현재 곡 저장">저장</button>
        <div class="toolbarSpacer"></div>
        <button id="musicRailOpen" class="toolbarBtn">♫ Graph → Music</button>
        <button id="principleRailOpen" class="toolbarBtn icon" title="Cosmos 원리">?</button>
    </div>

    <div class="workspace">

        <!-- LEFT: EXPRESSIONS -->
        <aside class="expressionPane">

            <div class="expressionHeader">
                <div class="addMenuWrap">
                    <button id="addMenuToggle" class="toolbarBtn primary" title="항목 추가">＋</button>
                    <div id="addMenu" class="addMenu">
                        <button id="addFunctionLayer">ƒ　함수 그래프</button>
                        <button id="addSketchLayer">✎　손그림 그래프</button>
                    </div>
                </div>
                <div class="expressionHeaderTitle">Expressions</div>
                <button id="deleteLayer" class="toolbarBtn danger" title="선택 항목 삭제">삭제</button>
            </div>

            <div class="expressionScroll">
                <div class="layerList" id="layerList"></div>
            </div>

            <div class="expressionFooter">
                <div id="editNotice" class="editNotice">Edit 모드: 그래프를 직접 선택하고 드래그해 이동·크기 조절·회전합니다.</div>
                <div id="layerCount" style="display:none;"></div>
                <div class="expressionFooterRow">
                    <button id="navigateMode" class="active">이동</button>
                    <button id="sketchMode">손그림</button>
                    <button id="editMode">Edit</button>
                </div>
                <div class="workspaceHint">그래프를 드래그해 이동하고 휠로 확대·축소합니다. Edit에서는 그래프를 직접 잡아 움직입니다.</div>
            </div>

            <details class="compactLibrary">
                <summary>Library</summary>
                <div class="libraryInner">
                    <select id="librarySelect"></select>
                    <div class="controls">
                        <button id="newLibrary" class="primary">＋ Library</button>
                        <button id="renameLibrary">이름 변경</button>
                        <button id="deleteLibrary" class="danger">삭제</button>
                    </div>
                    <div class="section">
                        <label>현재 곡</label>
                        <div class="controls">
                            <button id="saveSongSecondary" class="primary">곡 저장</button>
                        </div>
                    </div>
                    <div class="libraryMeta" id="libraryMeta">0개 곡</div>
                    <div class="libraryList" id="songList"></div>
                </div>
            </details>
        </aside>

        <!-- CENTER: GRAPH -->
        <main class="graphWorkspace">

            <div class="graphTop">
                <span class="graphTopTitle">Graph</span>
                <span class="graphTopHint">수식을 입력하면 그래프가 즉시 캔버스에 표시됩니다.</span>
            </div>

            <div class="graphCanvasArea">
                <canvas id="graph" width="1200" height="650"></canvas>

                <div class="canvasSettings">
                    <button id="settingsToggle" class="canvasSettingsBtn" title="그래프 설정">⚙</button>
                    <div id="settingsPanel" class="settingsPanel">
                        <div class="settingsTitle">Graph Settings</div>
                        <div class="settingsGrid">
                            <div><label>X 최소</label><input id="xminInput" type="number" value="-10" step="1"></div>
                            <div><label>X 최대</label><input id="xmaxInput" type="number" value="10" step="1"></div>
                            <div><label>Y 최소</label><input id="yminInput" type="number" value="-6" step="1"></div>
                            <div><label>Y 최대</label><input id="ymaxInput" type="number" value="6" step="1"></div>
                        </div>
                        <div class="settingsChecks">
                            <label><input id="gridToggle" type="checkbox" checked> 격자</label>
                            <label><input id="axisToggle" type="checkbox" checked> 축</label>
                        </div>
                        <button id="resetView" style="width:100%;margin-top:9px;">기본 화면으로</button>
                    </div>
                </div>

                <div id="keypad" class="keypad">
                    <div class="keypadGrid">
                        <button data-key="x">x</button>
                        <button data-key="y">y</button>
                        <button data-key="(">(</button>
                        <button data-key=")">)</button>
                        <button data-key="^">aᵇ</button>
                        <button data-key="pi">π</button>
                        <button data-key="7">7</button>
                        <button data-key="8">8</button>
                        <button data-key="9">9</button>
                        <button data-key="/">÷</button>
                        <button data-key="sqrt(">√</button>
                        <button data-key="sin(">sin</button>
                        <button data-key="4">4</button>
                        <button data-key="5">5</button>
                        <button data-key="6">6</button>
                        <button data-key="*">×</button>
                        <button data-key="cos(">cos</button>
                        <button data-key="tan(">tan</button>
                        <button data-key="1">1</button>
                        <button data-key="2">2</button>
                        <button data-key="3">3</button>
                        <button data-key="-">−</button>
                        <button data-key="abs(">abs</button>
                        <button data-key="log(">log</button>
                        <button data-key="0">0</button>
                        <button data-key=".">.</button>
                        <button data-key="+">+</button>
                        <button data-key="=">=</button>
                        <button data-key="ln(">ln</button>
                        <button data-key="e">e</button>
                    </div>
                </div>
            </div>

            <div class="graphBottom">
                <div class="bottomGrid">
                    <div class="functionEditor">
                        <label for="expr">선택된 표현식</label>
                        <input id="expr" type="text" value="sin(x)" autocomplete="off" spellcheck="false">
                        <div class="functionActions">
                            <button id="draw" class="primary">그래프 적용</button>
                            <button id="clearLayer">지우기</button>
                            <button id="keypadToggle">⌨ 키패드</button>
                        </div>
                        <div id="message"></div>
                    </div>

                    <div class="analysisStrip">
                        <div class="analysisCell"><div class="analysisLabel">정의역</div><div class="analysisValue" id="domain">—</div></div>
                        <div class="analysisCell"><div class="analysisLabel">최솟값</div><div class="analysisValue" id="minY">—</div></div>
                        <div class="analysisCell"><div class="analysisLabel">최댓값</div><div class="analysisValue" id="maxY">—</div></div>
                        <div class="analysisCell"><div class="analysisLabel">평균</div><div class="analysisValue" id="avgY">—</div></div>
                        <div class="analysisCell"><div class="analysisLabel">선택</div><div class="analysisValue" id="selectedLayerInfo">—</div></div>
                    </div>
                </div>
            </div>

        </main>

        <!-- RIGHT RAIL -->
        <aside class="workspaceRail">

            <div class="workspaceRailTab">
                <button id="musicRailButton" class="railBtn" title="Graph → Music">♫</button>
                <button id="principleRailButton" class="railBtn" title="Cosmos 원리">?</button>
            </div>

            <div id="musicDrawer" class="railPanel">
                <div class="railPanelHeader">
                    <h3>Graph → Music</h3>
                    <button id="musicRailClose" class="railClose">×</button>
                </div>

                <section class="card musicBox" id="music">
                    <div class="musicHero">
                        <div>
                            <div class="musicHeroTitle">Graph → Music</div>
                            <div class="musicHeroText">x축은 시간, y값은 음높이로 변환됩니다. 표시된 그래프는 동시에 하나의 음악으로 구성됩니다.</div>
                        </div>
                        <div class="musicMark">♫</div>
                    </div>

                    <div class="row">
                        <div>
                            <label>음악 길이</label>
                            <select id="duration">
                                <option value="10">10초</option><option value="20">20초</option><option value="30">30초</option>
                                <option value="60">1분</option><option value="120">2분</option><option value="180">3분</option>
                                <option value="240">4분</option><option value="300">5분</option>
                            </select>
                        </div>
                        <div>
                            <label>음계</label>
                            <select id="scale">
                                <option value="major">C Major</option>
                                <option value="minor">A Minor</option>
                                <option value="pentatonic">Pentatonic</option>
                                <option value="chromatic">Chromatic</option>
                            </select>
                        </div>
                    </div>

                    <div class="section">
                        <label>음악 스타일 / 장르</label>
                        <select id="style">
                            <optgroup label="Pop">
                                <option value="pop">Pop</option><option value="kpop">K-pop</option><option value="jpop">J-pop</option>
                                <option value="citypop">City Pop</option><option value="rnb">R&B</option>
                            </optgroup>
                            <optgroup label="Electronic">
                                <option value="edm">EDM</option><option value="house">House</option><option value="techno">Techno</option>
                                <option value="trance">Trance</option><option value="futurebass">Future Bass</option><option value="dnb">Drum & Bass</option>
                                <option value="synthwave">Synthwave</option>
                            </optgroup>
                            <optgroup label="Hip-Hop">
                                <option value="hiphop">Hip-Hop</option><option value="trap">Trap</option><option value="boombap">Boom Bap</option>
                                <option value="phonk">Phonk</option><option value="funk">Funk</option>
                            </optgroup>
                            <optgroup label="Band & Jazz">
                                <option value="rock">Rock</option><option value="jazz">Jazz</option><option value="blues">Blues</option>
                            </optgroup>
                            <optgroup label="Classical & Atmosphere">
                                <option value="classic">Classic</option><option value="ambient">Ambient</option><option value="cinematic">Cinematic</option><option value="lofi">Lo-fi</option>
                            </optgroup>
                        </select>
                    </div>

                    <div class="controls">
                        <button id="play" class="primary">▶ 그래프 전체로 음악 만들기</button>
                        <button id="stop">■ 정지</button>
                        <button id="downloadWav" class="success">↓ WAV 저장</button>
                    </div>
                    <div class="now" id="now">표시된 모든 그래프가 동시에 음악으로 변환됩니다.</div>
                    <div class="progress"><div id="bar"></div></div>
                </section>
            </div>

            <div id="principleDrawer" class="railPanel">
                <div class="railPanelHeader">
                    <h3>Cosmos Principle</h3>
                    <button id="principleRailClose" class="railClose">×</button>
                </div>
                <div id="principle" class="principlePanel">
                    <div class="principleFormula">x축 → 시간　│　y값 → 음높이</div>
                    <b>Graph → Music</b><br>
                    그래프의 전체 구간을 음악의 전체 재생 시간에 대응시킵니다.<br><br>
                    그래프가 상승하면 음높이가 올라가고, 하강하면 음높이가 내려갑니다.<br><br>
                    여러 표현식을 동시에 표시하면 각각의 그래프가 독립적인 선율로 변환되어 하나의 음악으로 합쳐집니다.
                </div>
            </div>

        </aside>

    </div>
</div>

<div class="brandFooter">
    <span>Cosmos · Mathematics in Harmony</span>
    <span>수학적 구조를 발견하고, 시각과 소리의 다른 표현으로 경험합니다.</span>
</div>

</div>
<script>

(function(){

"use strict";


/* 상단 페이지 내비게이션은 작업공간 툴바/레일 구조로 대체되었습니다. */

/* =========================================================
   기본 DOM
========================================================= */

const canvas =
    document.getElementById("graph");

const ctx =
    canvas.getContext("2d");

const expr =
    document.getElementById("expr");

const msg =
    document.getElementById("message");

const editNotice =
    document.getElementById("editNotice");


/* =========================================================
   그래프 화면
========================================================= */

let xmin = -10;
let xmax = 10;

let ymin = -6;
let ymax = 6;


function W(){
    return canvas.getBoundingClientRect().width;
}


function H(){
    return canvas.getBoundingClientRect().height;
}


function sx(x){

    return (
        (x-xmin) /
        (xmax-xmin)
    ) * W();

}


function sy(y){

    return (
        H() -
        (y-ymin) /
        (ymax-ymin) *
        H()
    );

}


function invx(px){

    return xmin +
        px/W() *
        (xmax-xmin);

}


function invy(py){

    return ymin +
        (H()-py)/H() *
        (ymax-ymin);

}


/* =========================================================
   상태
========================================================= */

let mode = "navigate";

let draggingView = false;

let lastX = 0;
let lastY = 0;

let layerIdCounter = 2;

let selectedLayerId = 1;


/* =========================================================
   오디오
========================================================= */

let audioCtx = null;

let playing = false;

let raf = null;

let playbackStart = 0;

let playbackDuration = 10;

let audioVoices = [];


/* =========================================================
   Edit 상태
========================================================= */

let editAction = null;

let editPointerId = null;

let editStartX = 0;

let editStartY = 0;

let editStartTx = 0;

let editStartTy = 0;

let editStartScale = 1;

let editStartDistance = 1;

let editStartRotation = 0;

let editStartAngle = 0;


/* =========================================================
   Library 상태
========================================================= */

const LIBRARY_KEY =
    "cosmos_v31_libraries";

let libraries = [];

let currentLibraryId = "";

let currentSongId = null;


/* =========================================================
   레이어 색상
========================================================= */

const layerColors = [

    "#91a4ff",
    "#ff8fab",
    "#7ee7c4",
    "#ffd166",
    "#c49bff",
    "#67d8ff",
    "#ff9f68",
    "#b8f27c"

];


/* =========================================================
   레이어
========================================================= */

let layers = [

    {

        id:1,

        name:"Graph 1",

        type:"function",

        expression:"sin(x)",

        visible:true,

        volume:0.55,

        color:layerColors[0],

        points:[],

        transform:{

            tx:0,

            ty:0,

            scale:1,

            rotation:0

        }

    },


    {

        id:2,

        name:"Graph 2",

        type:"function",

        expression:"0.5*cos(2*x)",

        visible:true,

        volume:0.40,

        color:layerColors[1],

        points:[],

        transform:{

            tx:0,

            ty:0,

            scale:1,

            rotation:0

        }

    }

];


/* =========================================================
   수식 파서
========================================================= */

const funcs = {

    sin:Math.sin,

    cos:Math.cos,

    tan:Math.tan,

    sqrt:Math.sqrt,

    abs:Math.abs,

    log:Math.log,

    ln:Math.log,

    exp:Math.exp,

    asin:Math.asin,

    acos:Math.acos,

    atan:Math.atan

};


function tokenize(s){

    s = s
        .replace(/π/g,"pi")
        .replace(/√/g,"sqrt");

    const tokens = [];

    let i = 0;

    while(i < s.length){

        if(/\s/.test(s[i])){

            i++;

            continue;

        }


        if(/[0-9.]/.test(s[i])){

            let j = i+1;

            while(
                j < s.length &&
                /[0-9.]/.test(s[j])
            ){
                j++;
            }

            const n =
                Number(
                    s.slice(i,j)
                );

            if(!Number.isFinite(n)){
                throw Error("숫자를 확인하세요.");
            }

            tokens.push({
                t:"num",
                v:n
            });

            i=j;

            continue;

        }


        if(/[A-Za-z_]/.test(s[i])){

            let j=i+1;

            while(
                j<s.length &&
                /[A-Za-z_]/.test(s[j])
            ){
                j++;
            }

            tokens.push({

                t:"id",

                v:
                    s
                    .slice(i,j)
                    .toLowerCase()

            });

            i=j;

            continue;

        }


        if("+-*/^(),".includes(s[i])){

            tokens.push({

                t:s[i],

                v:s[i]

            });

            i++;

            continue;

        }


        throw Error(
            "지원하지 않는 문자가 있습니다: " +
            s[i]
        );

    }

    return tokens;

}


function parseExpression(s){

    const ts =
        tokenize(s);

    let p=0;


    function primary(){

        const z=ts[p];

        if(!z){
            throw Error(
                "수식이 완성되지 않았습니다."
            );
        }


        if(z.t==="num"){

            p++;

            return ()=>z.v;

        }


        if(z.t==="id"){

            p++;


            if(z.v==="x"){
                return x=>x;
            }


            if(z.v==="pi"){
                return ()=>Math.PI;
            }


            if(z.v==="e"){
                return ()=>Math.E;
            }


            if(funcs[z.v]){

                if(
                    !ts[p] ||
                    ts[p].t!=="("
                ){
                    throw Error(
                        z.v +
                        " 뒤에 괄호가 필요합니다."
                    );
                }

                p++;

                const a =
                    addsub();

                if(
                    !ts[p] ||
                    ts[p].t!==")"
                ){
                    throw Error(
                        "괄호를 닫아주세요."
                    );
                }

                p++;

                return x =>
                    funcs[z.v](a(x));

            }


            throw Error(
                "알 수 없는 함수/변수: " +
                z.v
            );

        }


        if(z.t==="("){

            p++;

            const a =
                addsub();

            if(
                !ts[p] ||
                ts[p].t!==")"
            ){
                throw Error(
                    "괄호를 닫아주세요."
                );
            }

            p++;

            return a;

        }


        if(z.t==="+"){

            p++;

            return primary();

        }


        if(z.t==="-"){

            p++;

            const a =
                primary();

            return x=>-a(x);

        }


        throw Error(
            "수식을 확인하세요."
        );

    }


    function power(){

        let a =
            primary();

        if(
            ts[p] &&
            ts[p].t==="^"
        ){

            p++;

            const b =
                power();

            const aa =
                a;

            return x =>
                Math.pow(
                    aa(x),
                    b(x)
                );

        }

        return a;

    }


    function muldiv(){

        let a =
            power();

        while(
            ts[p] &&
            (
                ts[p].t==="*" ||
                ts[p].t==="/"
            )
        ){

            const op =
                ts[p++].t;

            const b =
                power();

            const aa =
                a;

            if(op==="*"){

                a =
                    x =>
                        aa(x) *
                        b(x);

            }else{

                a =
                    x =>
                        aa(x) /
                        b(x);

            }

        }

        return a;

    }


    function addsub(){

        let a =
            muldiv();

        while(
            ts[p] &&
            (
                ts[p].t==="+" ||
                ts[p].t==="-"
            )
        ){

            const op =
                ts[p++].t;

            const b =
                muldiv();

            const aa =
                a;

            if(op==="+"){

                a =
                    x =>
                        aa(x)+b(x);

            }else{

                a =
                    x =>
                        aa(x)-b(x);

            }

        }

        return a;

    }


    const f =
        addsub();

    if(
        p!==ts.length
    ){
        throw Error(
            "수식을 확인하세요."
        );
    }

    return f;

}


/* =========================================================
   중심
========================================================= */

function getCenter(points){

    if(!points.length){

        return {
            x:0,
            y:0
        };

    }


    let ax=0;
    let ay=0;

    points.forEach(p=>{

        ax+=p.x;
        ay+=p.y;

    });


    return {

        x:
            ax/points.length,

        y:
            ay/points.length

    };

}


/* =========================================================
   함수 그래프 생성
========================================================= */

function generateFunctionPoints(expression){

    const f =
        parseExpression(
            expression
        );

    const result=[];

    const N=1200;


    for(
        let i=0;
        i<=N;
        i++
    ){

        const x =
            xmin +
            (xmax-xmin) *
            i/N;

        let y;

        try{

            y=f(x);

        }catch(e){

            y=NaN;

        }


        if(
            Number.isFinite(y) &&
            Math.abs(y)<100000
        ){

            result.push({

                x:x,

                y:y,

                cx:x,

                cy:y

            });

        }

    }


    return result;

}


/* =========================================================
   변환
========================================================= */

function transformPoint(
    point,
    transform
){

    const x0 =
        point.x-point.cx;

    const y0 =
        point.y-point.cy;

    const c =
        Math.cos(
            transform.rotation
        );

    const s =
        Math.sin(
            transform.rotation
        );


    const x1 =
        (
            x0*c -
            y0*s
        ) *
        transform.scale;


    const y1 =
        (
            x0*s +
            y0*c
        ) *
        transform.scale;


    return {

        x:
            point.cx +
            x1 +
            transform.tx,

        y:
            point.cy +
            y1 +
            transform.ty

    };

}


function transformedPoints(layer){

    if(
        !layer ||
        !layer.points ||
        !layer.points.length
    ){
        return [];
    }


    return layer.points.map(
        p =>
            transformPoint(
                p,
                layer.transform
            )
    );

}


/* =========================================================
   선택 레이어
========================================================= */

function selectedLayer(){

    return layers.find(
        l =>
            l.id ===
            selectedLayerId
    ) || null;

}


function selectLayer(id){

    const exists =
        layers.some(
            l => l.id === id
        );

    if(!exists){
        return;
    }

    selectedLayerId=id;

    const l=
        selectedLayer();

    expr.value =
        l.expression || "";

    renderLayers();

    draw();

}


/* =========================================================
   레이어 UI
========================================================= */

function renderLayers(){

    const box =
        document.getElementById(
            "layerList"
        );

    box.innerHTML="";


    layers.forEach(layer=>{

        const item =
            document.createElement(
                "div"
            );

        item.className =
            "layerItem" +
            (
                layer.id===selectedLayerId
                ? " selected"
                : ""
            );


        const top =
            document.createElement(
                "div"
            );

        top.className =
            "layerTop";


        const dot =
            document.createElement(
                "span"
            );

        dot.className =
            "layerColor";

        dot.style.background =
            layer.color;


        const nameInput =
            document.createElement(
                "input"
            );

        nameInput.type="text";

        nameInput.value =
            layer.name;

        nameInput.className =
            "layerNameInput";


        const type =
            document.createElement(
                "span"
            );

        type.className =
            "layerType";

        type.textContent =
            layer.type==="function"
            ? "FUNCTION"
            : "SKETCH";


        top.appendChild(dot);

        top.appendChild(
            nameInput
        );

        top.appendChild(type);


        const actions =
            document.createElement(
                "div"
            );

        actions.className =
            "layerActions";


        const visibility =
            document.createElement(
                "button"
            );

        visibility.className =
            "visibility";

        visibility.textContent =
            layer.visible
            ? "👁 표시"
            : "○ 숨김";


        const volumeBox =
            document.createElement(
                "div"
            );

        volumeBox.className =
            "volumeBox";


        const volumeHeader =
            document.createElement(
                "div"
            );

        volumeHeader.className =
            "volumeHeader";


        const volumeText =
            document.createElement(
                "span"
            );

        volumeText.textContent =
            "음량";


        const volumeValue =
            document.createElement(
                "span"
            );

        volumeValue.textContent =
            Math.round(
                layer.volume*100
            ) + "%";


        volumeHeader.appendChild(
            volumeText
        );

        volumeHeader.appendChild(
            volumeValue
        );


        const volume =
            document.createElement(
                "input"
            );

        volume.type="range";

        volume.min="0";

        volume.max="1";

        volume.step="0.01";

        volume.value =
            layer.volume;

        volume.className =
            "layerVolume";


        volumeBox.appendChild(
            volumeHeader
        );

        volumeBox.appendChild(
            volume
        );


        actions.appendChild(
            visibility
        );

        actions.appendChild(
            volumeBox
        );


        item.appendChild(top);

        item.appendChild(actions);


        /*
           선택은 layerItem 자체에서만 처리.
           내부 입력/버튼은 selection 이벤트가
           부모로 전파되지 않도록 막는다.
        */

        top.addEventListener(
            "click",
            e=>{
                if(
                    e.target === nameInput
                ){
                    return;
                }
                selectLayer(layer.id);
            }
        );


        item.addEventListener(
            "click",
            e=>{
                if(
                    e.target === visibility ||
                    e.target === volume ||
                    actions.contains(e.target)
                ){
                    e.stopPropagation();
                }
            }
        );


        item.addEventListener(
            "pointerdown",
            e=>{
                if(
                    actions.contains(e.target) ||
                    e.target === nameInput
                ){
                    e.stopPropagation();
                }
            }
        );


        nameInput.addEventListener(
            "click",
            e=>{
                e.stopPropagation();
            }
        );


        nameInput.addEventListener(
            "pointerdown",
            e=>{
                e.stopPropagation();
            }
        );


        nameInput.addEventListener(
            "change",
            e=>{

                const newName =
                    e.target.value.trim();

                layer.name =
                    newName ||
                    "Graph " +
                    layer.id;

                e.target.value =
                    layer.name;

                updateSelectedInfo();

            }
        );


        visibility.addEventListener(
            "click",
            e=>{

                e.stopPropagation();

                layer.visible =
                    !layer.visible;

                renderLayers();

                draw();

            }
        );


        visibility.addEventListener(
            "pointerdown",
            e=>{
                e.stopPropagation();
            }
        );


        volume.addEventListener(
            "click",
            e=>{

                e.stopPropagation();

            }
        );


        volume.addEventListener(
            "pointerdown",
            e=>{

                e.stopPropagation();

            }
        );


        volume.addEventListener(
            "input",
            e=>{

                e.stopPropagation();

                layer.volume =
                    Number(
                        e.target.value
                    );

                volumeValue.textContent =
                    Math.round(
                        layer.volume*100
                    ) + "%";

            }
        );


        box.appendChild(item);

    });


    document.getElementById(
        "layerCount"
    ).textContent =
        layers.length +
        "개 레이어 · " +
        layers.filter(
            l=>l.visible
        ).length +
        "개 재생";


    updateSelectedInfo();

}


/* =========================================================
   선택 레이어 정보
========================================================= */

function updateSelectedInfo(){

    const selected =
        selectedLayer();

    const box =
        document.getElementById(
            "selectedLayerInfo"
        );


    if(!selected){

        box.textContent =
            "선택 없음";

        return;

    }


    box.textContent =
        selected.name +
        " · " +
        (
            selected.type ===
            "function"
            ? "함수"
            : "손그림"
        );

}


/* =========================================================
   함수 그래프 생성
========================================================= */

document
.getElementById("draw")
.addEventListener(
    "click",
    ()=>{

        const layer =
            selectedLayer();

        if(!layer){
            return;
        }


        try{

            const points =
                generateFunctionPoints(
                    expr.value.trim()
                );


            if(points.length<10){

                throw Error(
                    "그래프를 충분히 생성할 수 없습니다."
                );

            }


            const center =
                getCenter(points);


            points.forEach(p=>{

                p.cx =
                    center.x;

                p.cy =
                    center.y;

            });


            layer.type =
                "function";

            layer.expression =
                expr.value.trim();

            layer.points =
                points;

            layer.transform={

                tx:0,

                ty:0,

                scale:1,

                rotation:0

            };


            msg.textContent="";

            renderLayers();

            draw();

        }catch(e){

            msg.textContent =
                e.message;

        }

    }
);


/* =========================================================
   레이어 추가
========================================================= */

function addLayer(type){

    layerIdCounter++;


    const index =
        (
            layers.length
        ) %
        layerColors.length;


    const layer={

        id:
            layerIdCounter,

        name:
            type==="function"
            ? "Function " +
                layerIdCounter
            : "Sketch " +
                layerIdCounter,

        type:type,

        expression:
            type==="function"
            ? "sin(x)"
            : "",

        visible:true,

        volume:
            type==="function"
            ? 0.45
            : 0.35,

        color:
            layerColors[index],

        points:[],

        transform:{

            tx:0,

            ty:0,

            scale:1,

            rotation:0

        }

    };


    if(
        type==="function"
    ){

        try{

            const points =
                generateFunctionPoints(
                    layer.expression
                );

            const center =
                getCenter(points);


            points.forEach(p=>{

                p.cx =
                    center.x;

                p.cy =
                    center.y;

            });


            layer.points =
                points;

        }catch(e){}

    }


    layers.push(layer);

    selectedLayerId =
        layer.id;

    expr.value =
        layer.expression;


    renderLayers();

    draw();

}


document
.getElementById(
    "addFunctionLayer"
)
.addEventListener(
    "click",
    ()=>{
        addLayer("function");
    }
);


document
.getElementById(
    "addSketchLayer"
)
.addEventListener(
    "click",
    ()=>{
        addLayer("sketch");
    }
);


/* =========================================================
   레이어 삭제
========================================================= */

document
.getElementById(
    "deleteLayer"
)
.addEventListener(
    "click",
    ()=>{

        if(
            layers.length<=1
        ){

            msg.textContent =
                "최소 한 개의 레이어는 필요합니다.";

            return;

        }


        const index =
            layers.findIndex(
                l =>
                    l.id ===
                    selectedLayerId
            );


        layers =
            layers.filter(
                l =>
                    l.id !==
                    selectedLayerId
            );


        selectedLayerId =
            layers[
                Math.max(
                    0,
                    index-1
                )
            ].id;


        expr.value =
            selectedLayer()
            ?.expression || "";


        renderLayers();

        draw();

    }
);


/* =========================================================
   손그림
========================================================= */

let sketchPoints=[];


canvas.addEventListener(
    "pointerdown",
    e=>{

        if(
            mode !==
            "sketch"
        ){
            return;
        }


        const layer =
            selectedLayer();

        if(!layer){
            return;
        }


        sketchPoints=[];


        const rect =
            canvas.getBoundingClientRect();


        const x =
            invx(
                e.clientX -
                rect.left
            );


        const y =
            invy(
                e.clientY -
                rect.top
            );


        sketchPoints.push({

            x:x,

            y:y

        });


        canvas.setPointerCapture(
            e.pointerId
        );

    }
);


canvas.addEventListener(
    "pointermove",
    e=>{

        if(
            mode !==
            "sketch"
        ){
            return;
        }


        if(
            !sketchPoints.length
        ){
            return;
        }


        const rect =
            canvas.getBoundingClientRect();


        const x =
            invx(
                e.clientX -
                rect.left
            );


        const y =
            invy(
                e.clientY -
                rect.top
            );


        sketchPoints.push({

            x:x,

            y:y

        });


        drawSketchPreview();

    }
);


canvas.addEventListener(
    "pointerup",
    e=>{

        if(
            mode !==
            "sketch"
        ){
            return;
        }


        if(
            sketchPoints.length<5
        ){

            sketchPoints=[];

            draw();

            return;

        }


        const layer =
            selectedLayer();


        if(!layer){
            return;
        }


        const simplified =
            simplifyPoints(
                sketchPoints,
                2
            );


        const center =
            getCenter(
                simplified
            );


        layer.type =
            "sketch";

        layer.expression="";


        layer.points =
            simplified.map(
                p=>({

                    x:p.x,

                    y:p.y,

                    cx:center.x,

                    cy:center.y

                })
            );


        layer.transform={

            tx:0,

            ty:0,

            scale:1,

            rotation:0

        };


        sketchPoints=[];


        renderLayers();

        draw();

    }
);


function simplifyPoints(
    points,
    step
){

    const result=[];


    for(
        let i=0;
        i<points.length;
        i+=step
    ){

        result.push({

            x:
                points[i].x,

            y:
                points[i].y

        });

    }


    return result;

}


/* =========================================================
   손그림 미리보기
========================================================= */

function drawSketchPreview(){

    draw();


    if(
        sketchPoints.length<2
    ){
        return;
    }


    const layer =
        selectedLayer();


    if(!layer){
        return;
    }


    ctx.save();


    ctx.strokeStyle =
        layer.color;

    ctx.lineWidth=4;

    ctx.lineCap="round";

    ctx.lineJoin="round";


    ctx.beginPath();


    sketchPoints.forEach(
        (p,i)=>{

            const px =
                sx(p.x);

            const py =
                sy(p.y);


            if(i===0){

                ctx.moveTo(
                    px,
                    py
                );

            }else{

                ctx.lineTo(
                    px,
                    py
                );

            }

        }
    );


    ctx.stroke();

    ctx.restore();

}


/* =========================================================
   Edit 도구
========================================================= */

function getEditData(layer){

    if(
        !layer ||
        !layer.points.length
    ){
        return null;
    }


    const points =
        transformedPoints(
            layer
        );


    if(
        points.length<2
    ){
        return null;
    }


    const screenPoints =
        points.map(
            p=>({

                x:sx(p.x),

                y:sy(p.y)

            })
        );


    let minX=Infinity;

    let maxX=-Infinity;

    let minY=Infinity;

    let maxY=-Infinity;


    screenPoints.forEach(p=>{

        minX=Math.min(
            minX,
            p.x
        );

        maxX=Math.max(
            maxX,
            p.x
        );

        minY=Math.min(
            minY,
            p.y
        );

        maxY=Math.max(
            maxY,
            p.y
        );

    });


    const center =
        getCenter(points);


    const cx =
        sx(center.x);

    const cy =
        sy(center.y);


    return {

        points:screenPoints,

        minX:minX,

        maxX:maxX,

        minY:minY,

        maxY:maxY,

        centerX:cx,

        centerY:cy

    };

}


function getEditHandles(layer){

    const data =
        getEditData(layer);


    if(!data){
        return null;
    }


    const size=8;


    const corners=[

        {
            type:"scale",
            x:data.minX,
            y:data.minY
        },

        {
            type:"scale",
            x:data.maxX,
            y:data.minY
        },

        {
            type:"scale",
            x:data.minX,
            y:data.maxY
        },

        {
            type:"scale",
            x:data.maxX,
            y:data.maxY
        },

        {
            type:"rotate",
            x:
                (
                    data.minX+
                    data.maxX
                )/2,

            y:
                data.minY-36
        }

    ];


    return {
        corners:corners,
        size:size
    };

}


function distance(
    x1,
    y1,
    x2,
    y2
){

    return Math.hypot(
        x1-x2,
        y1-y2
    );

}


function distanceToSegment(
    px,
    py,
    ax,
    ay,
    bx,
    by
){

    const dx =
        bx-ax;

    const dy =
        by-ay;


    const len2 =
        dx*dx+
        dy*dy;


    if(
        len2===0
    ){

        return distance(
            px,
            py,
            ax,
            ay
        );

    }


    let t =
        (
            (
                px-ax
            )*dx+
            (
                py-ay
            )*dy
        ) /
        len2;


    t =
        Math.max(
            0,
            Math.min(
                1,
                t
            )
        );


    const x =
        ax+t*dx;

    const y =
        ay+t*dy;


    return distance(
        px,
        py,
        x,
        y
    );

}


function pointNearLayer(
    layer,
    px,
    py
){

    const data =
        getEditData(layer);


    if(!data){
        return false;
    }


    for(
        let i=1;
        i<data.points.length;
        i++
    ){

        const a =
            data.points[i-1];

        const b =
            data.points[i];


        if(
            distanceToSegment(
                px,
                py,
                a.x,
                a.y,
                b.x,
                b.y
            ) <= 12
        ){
            return true;
        }

    }


    return false;

}


function pointInsideBox(
    data,
    px,
    py
){

    return (
        px>=data.minX-8 &&
        px<=data.maxX+8 &&
        py>=data.minY-8 &&
        py<=data.maxY+8
    );

}


function nearHandle(
    handle,
    px,
    py,
    radius=14
){

    return (
        distance(
            px,
            py,
            handle.x,
            handle.y
        ) <= radius
    );

}


/* =========================================================
   Edit Pointer Down
========================================================= */

canvas.addEventListener(
    "pointerdown",
    e=>{

        if(
            mode !==
            "edit"
        ){
            return;
        }


        const rect =
            canvas.getBoundingClientRect();


        const px =
            e.clientX -
            rect.left;

        const py =
            e.clientY -
            rect.top;


        const current =
            selectedLayer();


        /*
           1. 선택된 그래프의 핸들을 먼저 검사
        */

        if(current){

            const handles =
                getEditHandles(
                    current
                );


            if(handles){

                const rotateHandle =
                    handles.corners.find(
                        h =>
                            h.type==="rotate"
                    );


                if(
                    rotateHandle &&
                    nearHandle(
                        rotateHandle,
                        px,
                        py,
                        16
                    )
                ){

                    editAction =
                        "rotate";

                    editPointerId =
                        e.pointerId;

                    const data =
                        getEditData(
                            current
                        );


                    editStartX =
                        px;

                    editStartY =
                        py;

                    editStartRotation =
                        current.transform.rotation;

                    editStartAngle =
                        Math.atan2(
                            py-data.centerY,
                            px-data.centerX
                        );


                    canvas.setPointerCapture(
                        e.pointerId
                    );

                    return;

                }


                const scaleHandle =
                    handles.corners.find(
                        h =>
                            h.type==="scale" &&
                            nearHandle(
                                h,
                                px,
                                py,
                                15
                            )
                    );


                if(scaleHandle){

                    editAction =
                        "scale";

                    editPointerId =
                        e.pointerId;

                    const data =
                        getEditData(
                            current
                        );


                    editStartScale =
                        current.transform.scale;

                    editStartDistance =
                        distance(
                            px,
                            py,
                            data.centerX,
                            data.centerY
                        );


                    editStartX=px;

                    editStartY=py;


                    canvas.setPointerCapture(
                        e.pointerId
                    );

                    return;

                }

            }

        }


        /*
           2. 그래프 선을 클릭했는지 검사
           뒤에 그려진 레이어부터 검사
        */

        let hitLayer=null;


        for(
            let i=
                layers.length-1;
            i>=0;
            i--
        ){

            const layer =
                layers[i];


            if(
                !layer.visible ||
                layer.points.length<2
            ){
                continue;
            }


            if(
                pointNearLayer(
                    layer,
                    px,
                    py
                )
            ){

                hitLayer =
                    layer;

                break;

            }

        }


        if(hitLayer){

            selectLayer(
                hitLayer.id
            );


            editAction =
                "move";

            editPointerId =
                e.pointerId;


            editStartX =
                px;

            editStartY =
                py;


            editStartTx =
                hitLayer.transform.tx;

            editStartTy =
                hitLayer.transform.ty;


            canvas.setPointerCapture(
                e.pointerId
            );

            return;

        }


        /*
           3. 선택된 그래프 내부를 클릭해도 이동
        */

        if(current){

            const data =
                getEditData(
                    current
                );


            if(
                data &&
                pointInsideBox(
                    data,
                    px,
                    py
                )
            ){

                editAction =
                    "move";

                editPointerId =
                    e.pointerId;


                editStartX=px;

                editStartY=py;


                editStartTx =
                    current.transform.tx;

                editStartTy =
                    current.transform.ty;


                canvas.setPointerCapture(
                    e.pointerId
                );

            }

        }

    }
);


/* =========================================================
   Edit Pointer Move
========================================================= */

canvas.addEventListener(
    "pointermove",
    e=>{

        if(
            mode !==
            "edit"
        ){
            return;
        }


        const layer =
            selectedLayer();


        if(
            !layer ||
            !editAction
        ){
            return;
        }


        const rect =
            canvas.getBoundingClientRect();


        const px =
            e.clientX -
            rect.left;

        const py =
            e.clientY -
            rect.top;


        if(
            editAction ===
            "move"
        ){

            const dx =
                px -
                editStartX;

            const dy =
                py -
                editStartY;


            layer.transform.tx =
                editStartTx +
                dx/W() *
                (xmax-xmin);


            layer.transform.ty =
                editStartTy -
                dy/H() *
                (ymax-ymin);


        }else if(
            editAction ===
            "scale"
        ){

            const data =
                getEditData(
                    layer
                );


            if(!data){
                return;
            }


            const currentDistance =
                distance(
                    px,
                    py,
                    data.centerX,
                    data.centerY
                );


            if(
                editStartDistance>0
            ){

                layer.transform.scale =
                    editStartScale *
                    (
                        currentDistance /
                        editStartDistance
                    );


                layer.transform.scale =
                    Math.max(
                        0.15,
                        Math.min(
                            5,
                            layer.transform.scale
                        )
                    );

            }


        }else if(
            editAction ===
            "rotate"
        ){

            const data =
                getEditData(
                    layer
                );


            if(!data){
                return;
            }


            const angle =
                Math.atan2(
                    py-data.centerY,
                    px-data.centerX
                );


            const delta =
                angle -
                editStartAngle;


            layer.transform.rotation =
                editStartRotation +
                delta;

        }


        draw();

    }
);


/* =========================================================
   Edit Pointer Up
========================================================= */

function endEdit(){

    editAction=null;

    editPointerId=null;

}


canvas.addEventListener(
    "pointerup",
    endEdit
);


canvas.addEventListener(
    "pointercancel",
    endEdit
);


/* =========================================================
   Edit Hover Cursor
========================================================= */

canvas.addEventListener(
    "pointermove",
    e=>{

        if(
            mode!=="edit"
        ){
            return;
        }


        if(editAction){
            return;
        }


        const rect =
            canvas.getBoundingClientRect();


        const px =
            e.clientX -
            rect.left;

        const py =
            e.clientY -
            rect.top;


        const current =
            selectedLayer();


        if(current){

            const handles =
                getEditHandles(
                    current
                );


            if(handles){

                if(
                    handles.corners.some(
                        h =>
                            nearHandle(
                                h,
                                px,
                                py,
                                15
                            )
                    )
                ){

                    const rotate =
                        handles.corners.find(
                            h =>
                                h.type ===
                                "rotate" &&
                                nearHandle(
                                    h,
                                    px,
                                    py,
                                    15
                                )
                        );


                    canvas.style.cursor =
                        rotate
                        ? "crosshair"
                        : "nwse-resize";

                    return;

                }

            }

        }


        canvas.style.cursor =
            "default";

    }
);


/* =========================================================
   모드
========================================================= */

function setMode(newMode){

    mode =
        newMode;


    document
    .getElementById(
        "navigateMode"
    )
    .classList.toggle(
        "active",
        mode==="navigate"
    );


    document
    .getElementById(
        "sketchMode"
    )
    .classList.toggle(
        "active",
        mode==="sketch"
    );


    document
    .getElementById(
        "editMode"
    )
    .classList.toggle(
        "active",
        mode==="edit"
    );


    editNotice.classList.toggle(
        "active",
        mode==="edit"
    );


    editAction=null;


    if(
        mode!=="edit"
    ){
        canvas.style.cursor =
            "default";
    }


    draw();

}


document
.getElementById(
    "navigateMode"
)
.addEventListener(
    "click",
    ()=>{
        setMode("navigate");
    }
);


document
.getElementById(
    "sketchMode"
)
.addEventListener(
    "click",
    ()=>{
        setMode("sketch");
    }
);


document
.getElementById(
    "editMode"
)
.addEventListener(
    "click",
    ()=>{
        setMode("edit");
    }
);


/* =========================================================
   레이어 지우기
========================================================= */

document
.getElementById(
    "clearLayer"
)
.addEventListener(
    "click",
    ()=>{

        const l =
            selectedLayer();

        if(!l){
            return;
        }


        l.points=[];

        l.expression="";


        expr.value="";


        renderLayers();

        draw();

    }
);


/* =========================================================
   화면 이동
========================================================= */

function changeView(
    factor,
    dx=0,
    dy=0
){

    const cx =
        (
            xmin+xmax
        )/2 +
        dx *
        (
            xmax-xmin
        );


    const cy =
        (
            ymin+ymax
        )/2 +
        dy *
        (
            ymax-ymin
        );


    const xr =
        (
            xmax-xmin
        ) *
        factor;


    const yr =
        (
            ymax-ymin
        ) *
        factor;


    xmin =
        cx-xr/2;

    xmax =
        cx+xr/2;

    ymin =
        cy-yr/2;

    ymax =
        cy+yr/2;


    draw();

}


/* =========================================================
   화면 드래그
========================================================= */

canvas.addEventListener(
    "pointerdown",
    e=>{

        if(
            mode!=="navigate"
        ){
            return;
        }


        draggingView=true;

        lastX=e.clientX;

        lastY=e.clientY;


        canvas.setPointerCapture(
            e.pointerId
        );

    }
);


canvas.addEventListener(
    "pointermove",
    e=>{

        if(
            mode!=="navigate" ||
            !draggingView
        ){
            return;
        }


        const dx =
            e.clientX-lastX;

        const dy =
            e.clientY-lastY;


        const xr =
            xmax-xmin;

        const yr =
            ymax-ymin;


        xmin -=
            dx/W()*xr;

        xmax -=
            dx/W()*xr;


        ymin +=
            dy/H()*yr;

        ymax +=
            dy/H()*yr;


        lastX=
            e.clientX;

        lastY=
            e.clientY;


        draw();

    }
);


canvas.addEventListener(
    "pointerup",
    ()=>{
        draggingView=false;
    }
);


canvas.addEventListener(
    "pointercancel",
    ()=>{
        draggingView=false;
    }
);


/* =========================================================
   휠 확대
========================================================= */

canvas.addEventListener(
    "wheel",
    e=>{

        if(
            mode!=="navigate"
        ){
            return;
        }


        e.preventDefault();


        const factor =
            e.deltaY<0
            ? .8
            : 1.25;


        const mx =
            invx(
                e.offsetX
            );


        const my =
            invy(
                e.offsetY
            );


        xmin =
            mx +
            (
                xmin-mx
            )*factor;


        xmax =
            mx +
            (
                xmax-mx
            )*factor;


        ymin =
            my +
            (
                ymin-my
            )*factor;


        ymax =
            my +
            (
                ymax-my
            )*factor;


        draw();

    },
    {
        passive:false
    }
);


/* =========================================================
   그래프 그리기
========================================================= */

function niceStep(range){

    const raw =
        range/10;


    const p =
        Math.pow(
            10,
            Math.floor(
                Math.log10(raw)
            )
        );


    const n =
        raw/p;


    return (
        n<1.5
        ?1
        :n<3
        ?2
        :n<7
        ?5
        :10
    )*p;

}


function fmt(v){

    if(
        !Number.isFinite(v)
    ){
        return "—";
    }


    if(
        Math.abs(v)<1e-9
    ){
        return "0";
    }


    if(
        Math.abs(v)>=100
    ){
        return Math.round(v)
            .toString();
    }


    return Number(
        v.toFixed(2)
    ).toString();

}


function draw(){

    const w =
        W();

    const h =
        H();


    ctx.clearRect(
        0,
        0,
        w,
        h
    );


    ctx.fillStyle =
        "#fcfcfe";


    ctx.fillRect(
        0,
        0,
        w,
        h
    );


    /* grid */

    const xs =
        niceStep(
            xmax-xmin
        );


    const ys =
        niceStep(
            ymax-ymin
        );


    ctx.lineWidth=1;

    ctx.strokeStyle =
        document.getElementById("gridToggle")?.checked
        ? "#ececf1"
        : "transparent";

    ctx.fillStyle =
        "#9a9ea8";

    ctx.font =
        "11px system-ui";


    for(
        let x =
            Math.ceil(
                xmin/xs
            )*xs;
        x<=xmax;
        x+=xs
    ){

        const px =
            sx(x);


        ctx.beginPath();

        ctx.moveTo(
            px,
            0
        );

        ctx.lineTo(
            px,
            h
        );

        ctx.stroke();


        if(
            Math.abs(x)>1e-9
        ){

            ctx.fillText(
                fmt(x),
                px+4,
                h-7
            );

        }

    }


    for(
        let y =
            Math.ceil(
                ymin/ys
            )*ys;
        y<=ymax;
        y+=ys
    ){

        const py =
            sy(y);


        ctx.beginPath();

        ctx.moveTo(
            0,
            py
        );

        ctx.lineTo(
            w,
            py
        );

        ctx.stroke();


        if(
            Math.abs(y)>1e-9
        ){

            ctx.fillText(
                fmt(y),
                6,
                py-4
            );

        }

    }


    /* axes */

    ctx.strokeStyle =
        document.getElementById("axisToggle")?.checked
        ? "#c8cad2"
        : "transparent";

    ctx.lineWidth =
        1.4;


    if(
        xmin<=0 &&
        xmax>=0
    ){

        const px =
            sx(0);


        ctx.beginPath();

        ctx.moveTo(
            px,
            0
        );

        ctx.lineTo(
            px,
            h
        );

        ctx.stroke();

    }


    if(
        ymin<=0 &&
        ymax>=0
    ){

        const py =
            sy(0);


        ctx.beginPath();

        ctx.moveTo(
            0,
            py
        );

        ctx.lineTo(
            w,
            py
        );

        ctx.stroke();

    }


    /* layers */

    layers.forEach(layer=>{

        if(
            !layer.visible
        ){
            return;
        }


        const points =
            transformedPoints(
                layer
            );


        if(
            points.length<2
        ){
            return;
        }


        ctx.save();


        ctx.strokeStyle =
            layer.color;


        ctx.lineWidth =
            layer.id===
            selectedLayerId
            ? 3.5
            : 2.4;


        ctx.lineJoin =
            "round";

        ctx.lineCap =
            "round";


        ctx.beginPath();


        let hasStarted=false;


        points.forEach(
            p=>{

                const px =
                    sx(p.x);

                const py =
                    sy(p.y);


                if(
                    px<-100 ||
                    px>w+100 ||
                    py<-100 ||
                    py>h+100
                ){
                    return;
                }


                if(!hasStarted){

                    ctx.moveTo(
                        px,
                        py
                    );

                    hasStarted=true;

                }else{

                    ctx.lineTo(
                        px,
                        py
                    );

                }

            }
        );


        ctx.stroke();


        ctx.restore();

    });


    /* =====================================================
       재생 위치
    ===================================================== */

    if(
        playing &&
        playbackStart
    ){

        const elapsed =
            (
                performance.now() -
                playbackStart
            )/1000;


        const progress =
            Math.max(
                0,
                Math.min(
                    1,
                    elapsed/
                    playbackDuration
                )
            );


        layers.forEach(layer=>{

            if(
                !layer.visible ||
                layer.points.length<2
            ){
                return;
            }


            const points =
                transformedPoints(
                    layer
                );


            const index =
                Math.min(
                    points.length-1,
                    Math.floor(
                        progress *
                        (
                            points.length-1
                        )
                    )
                );


            const p =
                points[index];


            if(!p){
                return;
            }


            const px =
                sx(p.x);

            const py =
                sy(p.y);


            ctx.save();


            ctx.beginPath();

            ctx.arc(
                px,
                py,
                12,
                0,
                Math.PI*2
            );

            ctx.fillStyle =
                layer.color;

            ctx.globalAlpha=.18;

            ctx.fill();

            ctx.globalAlpha=1;


            ctx.beginPath();

            ctx.arc(
                px,
                py,
                6,
                0,
                Math.PI*2
            );

            ctx.fillStyle =
                "#ffffff";

            ctx.fill();


            ctx.beginPath();

            ctx.arc(
                px,
                py,
                4,
                0,
                Math.PI*2
            );

            ctx.fillStyle =
                layer.color;

            ctx.fill();


            ctx.restore();

        });

    }


    /* =====================================================
       Edit 선택 박스
    ===================================================== */

    if(
        mode==="edit"
    ){

        const selected =
            selectedLayer();


        if(
            selected &&
            selected.visible &&
            selected.points.length>=2
        ){

            const data =
                getEditData(
                    selected
                );


            if(data){

                ctx.save();


                ctx.strokeStyle =
                    "#b7a9ff";

                ctx.lineWidth=1.5;

                ctx.setLineDash([
                    6,
                    5
                ]);


                ctx.strokeRect(
                    data.minX-5,
                    data.minY-5,
                    data.maxX-data.minX+10,
                    data.maxY-data.minY+10
                );


                ctx.setLineDash([]);


                /*
                   회전 연결선
                */

                ctx.beginPath();

                ctx.moveTo(
                    (
                        data.minX+
                        data.maxX
                    )/2,
                    data.minY-5
                );

                ctx.lineTo(
                    (
                        data.minX+
                        data.maxX
                    )/2,
                    data.minY-36
                );

                ctx.stroke();


                const handles =
                    getEditHandles(
                        selected
                    );


                handles.corners.forEach(
                    h=>{

                        ctx.beginPath();

                        ctx.arc(
                            h.x,
                            h.y,
                            h.type==="rotate"
                            ? 7
                            : 6,
                            0,
                            Math.PI*2
                        );

                        ctx.fillStyle =
                            h.type==="rotate"
                            ? "#7a5af8"
                            : "#ffffff";

                        ctx.fill();

                        ctx.strokeStyle =
                            "#9c8bf0";

                        ctx.stroke();

                    }
                );


                ctx.restore();

            }

        }

    }


    /* =====================================================
       분석
    ===================================================== */

    const l =
        selectedLayer();


    if(
        l &&
        l.points.length
    ){

        const points =
            transformedPoints(
                l
            );


        const ys =
            points
            .map(
                p=>p.y
            )
            .filter(
                Number.isFinite
            );


        if(ys.length){

            const min =
                Math.min(
                    ...ys
                );


            const max =
                Math.max(
                    ...ys
                );


            const avg =
                ys.reduce(
                    (a,b)=>a+b,
                    0
                ) /
                ys.length;


            document.getElementById(
                "domain"
            ).textContent =
                fmt(xmin) +
                " ≤ x ≤ " +
                fmt(xmax);


            document.getElementById(
                "minY"
            ).textContent =
                fmt(min);


            document.getElementById(
                "maxY"
            ).textContent =
                fmt(max);


            document.getElementById(
                "avgY"
            ).textContent =
                fmt(avg);

        }

    }

}


/* =========================================================
   음계
========================================================= */

const scales={

    major:[
        0,2,4,5,7,9,11,
        12,14,16,17,19,21,23,24
    ],

    minor:[
        0,2,3,5,7,8,10,
        12,14,15,17,19,20,22,24
    ],

    pentatonic:[
        0,2,4,7,9,
        12,14,16,19,21,24
    ],

    chromatic:[
        0,1,2,3,4,5,
        6,7,8,9,10,11,
        12,13,14,15,16,17,
        18,19,20,21,22,23,24
    ]

};


/* =========================================================
   스타일
========================================================= */

const styles={

    pop:{
        waveform:"triangle",
        attack:.025,
        release:.15,
        baseGain:1,
        subGain:.02
    },

    kpop:{
        waveform:"sawtooth",
        attack:.012,
        release:.10,
        baseGain:.78,
        subGain:.04
    },

    jpop:{
        waveform:"triangle",
        attack:.018,
        release:.12,
        baseGain:.9,
        subGain:.03
    },

    citypop:{
        waveform:"triangle",
        attack:.035,
        release:.18,
        baseGain:.85,
        subGain:.04
    },

    rnb:{
        waveform:"sine",
        attack:.04,
        release:.22,
        baseGain:.9,
        subGain:.06
    },

    edm:{
        waveform:"square",
        attack:.008,
        release:.07,
        baseGain:.55,
        subGain:.12
    },

    house:{
        waveform:"sawtooth",
        attack:.012,
        release:.11,
        baseGain:.62,
        subGain:.12
    },

    techno:{
        waveform:"square",
        attack:.006,
        release:.08,
        baseGain:.58,
        subGain:.13
    },

    trance:{
        waveform:"sawtooth",
        attack:.02,
        release:.15,
        baseGain:.68,
        subGain:.08
    },

    futurebass:{
        waveform:"sawtooth",
        attack:.03,
        release:.24,
        baseGain:.72,
        subGain:.12
    },

    dnb:{
        waveform:"square",
        attack:.006,
        release:.07,
        baseGain:.60,
        subGain:.15
    },

    synthwave:{
        waveform:"sawtooth",
        attack:.035,
        release:.20,
        baseGain:.72,
        subGain:.10
    },

    hiphop:{
        waveform:"triangle",
        attack:.02,
        release:.13,
        baseGain:.83,
        subGain:.07
    },

    trap:{
        waveform:"sawtooth",
        attack:.008,
        release:.11,
        baseGain:.68,
        subGain:.13
    },

    boombap:{
        waveform:"triangle",
        attack:.018,
        release:.16,
        baseGain:.78,
        subGain:.07
    },

    phonk:{
        waveform:"sawtooth",
        attack:.006,
        release:.13,
        baseGain:.72,
        subGain:.18
    },

    funk:{
        waveform:"square",
        attack:.009,
        release:.09,
        baseGain:.82,
        subGain:.06
    },

    rock:{
        waveform:"sawtooth",
        attack:.014,
        release:.12,
        baseGain:.72,
        subGain:.10
    },

    jazz:{
        waveform:"triangle",
        attack:.045,
        release:.24,
        baseGain:.78,
        subGain:.04
    },

    blues:{
        waveform:"sine",
        attack:.04,
        release:.23,
        baseGain:.80,
        subGain:.05
    },

    classic:{
        waveform:"sine",
        attack:.08,
        release:.42,
        baseGain:.72,
        subGain:.025
    },

    ambient:{
        waveform:"sine",
        attack:.22,
        release:.55,
        baseGain:.52,
        subGain:.04
    },

    cinematic:{
        waveform:"triangle",
        attack:.12,
        release:.48,
        baseGain:.62,
        subGain:.07
    },

    lofi:{
        waveform:"sine",
        attack:.055,
        release:.22,
        baseGain:.62,
        subGain:.07
    }

};


/* =========================================================
   y → MIDI
========================================================= */

function graphMidi(
    y,
    lo,
    hi,
    scale
){

    if(
        !Number.isFinite(y) ||
        !Number.isFinite(lo) ||
        !Number.isFinite(hi) ||
        hi<=lo
    ){
        return 60;
    }


    const norm =
        Math.max(
            0,
            Math.min(
                1,
                (y-lo)/(hi-lo)
            )
        );


    const index =
        Math.round(
            norm*
            (
                scale.length-1
            )
        );


    return 48 +
        scale[
            Math.max(
                0,
                Math.min(
                    scale.length-1,
                    index
                )
            )
        ];

}


function midiFreq(m){

    return 440 *
        Math.pow(
            2,
            (
                m-69
            )/12
        );

}


/* =========================================================
   그래프 음 데이터
========================================================= */

function prepareLayerAudio(layer){

    const points =
        transformedPoints(
            layer
        );


    if(
        points.length<2
    ){
        return null;
    }


    const values =
        points
        .map(
            p=>p.y
        )
        .filter(
            Number.isFinite
        );


    if(
        values.length<2
    ){
        return null;
    }


    return {

        points:points,

        lo:
            Math.min(
                ...values
            ),

        hi:
            Math.max(
                ...values
            )

    };

}


/* =========================================================
   라이브 음성 생성
========================================================= */

function createLiveVoice(
    layer,
    data,
    style,
    start
){

    const osc =
        audioCtx.createOscillator();


    const gain =
        audioCtx.createGain();


    osc.type =
        style.waveform;


    gain.gain.setValueAtTime(
        0,
        start
    );


    gain.gain.linearRampToValueAtTime(
        layer.volume *
        style.baseGain,
        start+
        style.attack
    );


    osc.connect(gain);


    gain.connect(
        audioCtx.destination
    );


    osc.start(start);


    let subOsc=null;

    let subGain=null;


    if(
        style.subGain>0
    ){

        subOsc =
            audioCtx
            .createOscillator();


        subGain =
            audioCtx
            .createGain();


        subOsc.type =
            style.waveform;


        subGain.gain.setValueAtTime(
            0,
            start
        );


        subGain.gain.linearRampToValueAtTime(
            layer.volume *
            style.subGain,
            start+
            style.attack
        );


        subOsc.connect(
            subGain
        );


        subGain.connect(
            audioCtx.destination
        );


        subOsc.start(start);

    }


    return {

        layer:layer,

        data:data,

        osc:osc,

        gain:gain,

        subOsc:subOsc,

        subGain:subGain,

        lastFreq:0

    };

}


/* =========================================================
   음악 재생
========================================================= */

async function playMusic(){

    stopMusic();


    const visibleLayers =
        layers.filter(
            l =>
                l.visible &&
                l.points.length>=2
        );


    if(
        !visibleLayers.length
    ){

        msg.textContent =
            "음악으로 변환할 표시된 그래프가 없습니다.";

        return;

    }


    if(!audioCtx){

        audioCtx =
            new(
                window.AudioContext ||
                window.webkitAudioContext
            )();

    }


    if(
        audioCtx.state==="suspended"
    ){

        await audioCtx.resume();

    }


    const duration =
        Number(
            document.getElementById(
                "duration"
            ).value
        );


    const scale =
        scales[
            document.getElementById(
                "scale"
            ).value
        ];


    const style =
        styles[
            document.getElementById(
                "style"
            ).value
        ];


    playbackDuration =
        duration;


    playbackStart =
        performance.now();


    playing=true;


    const start =
        audioCtx.currentTime+
        .05;


    audioVoices=[];


    visibleLayers.forEach(
        layer=>{

            const data =
                prepareLayerAudio(
                    layer
                );


            if(!data){
                return;
            }


            const voice =
                createLiveVoice(
                    layer,
                    data,
                    style,
                    start
                );


            audioVoices.push(
                voice
            );

        }
    );


    if(
        !audioVoices.length
    ){

        stopMusic();

        msg.textContent =
            "재생할 수 있는 그래프가 없습니다.";

        return;

    }


    document.getElementById(
        "now"
    ).textContent =
        audioVoices.length +
        "개 그래프 레이어가 동시에 재생됩니다.";


    raf =
        requestAnimationFrame(
            musicTick
        );

}


/* =========================================================
   음악 Tick
========================================================= */

function musicTick(){

    if(!playing){
        return;
    }


    const elapsed =
        (
            performance.now() -
            playbackStart
        )/1000;


    const progress =
        Math.max(
            0,
            Math.min(
                1,
                elapsed/
                playbackDuration
            )
        );


    audioVoices.forEach(
        voice=>{

            const points =
                voice.data.points;


            const index =
                Math.min(
                    points.length-1,
                    Math.floor(
                        progress*
                        (
                            points.length-1
                        )
                    )
                );


            const p =
                points[index];


            if(!p){
                return;
            }


            const scale =
                scales[
                    document.getElementById(
                        "scale"
                    ).value
                ];


            const midi =
                graphMidi(
                    p.y,
                    voice.data.lo,
                    voice.data.hi,
                    scale
                );


            const freq =
                Math.max(
                    45,
                    Math.min(
                        1800,
                        midiFreq(midi)
                    )
                );


            const now =
                audioCtx.currentTime;


            if(
                !voice.lastFreq
            ){

                voice.osc.frequency
                    .setValueAtTime(
                        freq,
                        now
                    );


                if(
                    voice.subOsc
                ){

                    voice.subOsc
                        .frequency
                        .setValueAtTime(
                            freq/2,
                            now
                        );

                }

            }else{

                voice.osc.frequency
                    .cancelScheduledValues(
                        now
                    );


                voice.osc.frequency
                    .linearRampToValueAtTime(
                        freq,
                        now+.055
                    );


                if(
                    voice.subOsc
                ){

                    voice.subOsc.frequency
                        .cancelScheduledValues(
                            now
                        );


                    voice.subOsc.frequency
                        .linearRampToValueAtTime(
                            freq/2,
                            now+.055
                        );

                }

            }


            voice.lastFreq =
                freq;

        }
    );


    document.getElementById(
        "bar"
    ).style.width =
        (
            progress*100
        )+"%";


    document.getElementById(
        "now"
    ).textContent =
        "재생 중 · " +
        Math.round(
            progress*100
        ) +
        "% · " +
        audioVoices.length +
        "개 그래프 동시 재생";


    draw();


    if(
        progress<1
    ){

        raf =
            requestAnimationFrame(
                musicTick
            );

    }else{

        finishMusic();

    }

}


/* =========================================================
   음악 종료
========================================================= */

function finishMusic(){

    playing=false;


    const now =
        audioCtx
        ? audioCtx.currentTime
        : 0;


    audioVoices.forEach(
        voice=>{

            try{

                voice.gain.gain
                    .cancelScheduledValues(
                        now
                    );


                voice.gain.gain
                    .linearRampToValueAtTime(
                        0,
                        now+.12
                    );


                voice.osc.stop(
                    now+.2
                );


                if(
                    voice.subGain &&
                    voice.subOsc
                ){

                    voice.subGain.gain
                        .cancelScheduledValues(
                            now
                        );


                    voice.subGain.gain
                        .linearRampToValueAtTime(
                            0,
                            now+.12
                        );


                    voice.subOsc.stop(
                        now+.2
                    );

                }

            }catch(e){}

        }
    );


    audioVoices=[];

    playbackStart=0;


    document.getElementById(
        "bar"
    ).style.width="100%";


    document.getElementById(
        "now"
    ).textContent =
        "재생 완료";


    draw();

}


/* =========================================================
   정지
========================================================= */

function stopMusic(){

    playing=false;


    if(raf){

        cancelAnimationFrame(
            raf
        );

    }


    raf=null;


    if(audioCtx){

        const now =
            audioCtx.currentTime;


        audioVoices.forEach(
            voice=>{

                try{

                    voice.gain.gain
                        .cancelScheduledValues(
                            now
                        );


                    voice.gain.gain
                        .setTargetAtTime(
                            0,
                            now,
                            .03
                        );


                    voice.osc.stop(
                        now+.1
                    );


                    if(
                        voice.subGain &&
                        voice.subOsc
                    ){

                        voice.subGain.gain
                            .cancelScheduledValues(
                                now
                            );


                        voice.subGain.gain
                            .setTargetAtTime(
                                0,
                                now,
                                .03
                            );


                        voice.subOsc.stop(
                            now+.1
                        );

                    }

                }catch(e){}

            }
        );

    }


    audioVoices=[];

    playbackStart=0;


    document.getElementById(
        "bar"
    ).style.width="0%";


    document.getElementById(
        "now"
    ).textContent =
        "정지됨";


    draw();

}


document
.getElementById("play")
.addEventListener(
    "click",
    playMusic
);


document
.getElementById("stop")
.addEventListener(
    "click",
    stopMusic
);


/* =========================================================
   WAV 파일 생성
========================================================= */

function safeFilename(name){

    return (
        name
        .replace(
            /[<>:"/\\|?*]+/g,
            "_"
        )
        .trim() ||
        "Cosmos Song"
    );

}


function createWavBlob(
    audioBuffer
){

    const numChannels =
        1;

    const sampleRate =
        audioBuffer.sampleRate;

    const samples =
        audioBuffer.getChannelData(0);


    const bytesPerSample=2;

    const dataSize =
        samples.length *
        bytesPerSample;


    const buffer =
        new ArrayBuffer(
            44+dataSize
        );


    const view =
        new DataView(buffer);


    function writeString(
        offset,
        string
    ){

        for(
            let i=0;
            i<string.length;
            i++
        ){

            view.setUint8(
                offset+i,
                string.charCodeAt(i)
            );

        }

    }


    writeString(
        0,
        "RIFF"
    );


    view.setUint32(
        4,
        36+dataSize,
        true
    );


    writeString(
        8,
        "WAVE"
    );


    writeString(
        12,
        "fmt "
    );


    view.setUint32(
        16,
        16,
        true
    );


    view.setUint16(
        20,
        1,
        true
    );


    view.setUint16(
        22,
        numChannels,
        true
    );


    view.setUint32(
        24,
        sampleRate,
        true
    );


    view.setUint32(
        28,
        sampleRate *
        numChannels *
        bytesPerSample,
        true
    );


    view.setUint16(
        32,
        numChannels *
        bytesPerSample,
        true
    );


    view.setUint16(
        34,
        16,
        true
    );


    writeString(
        36,
        "data"
    );


    view.setUint32(
        40,
        dataSize,
        true
    );


    let offset=44;


    for(
        let i=0;
        i<samples.length;
        i++
    ){

        const s =
            Math.max(
                -1,
                Math.min(
                    1,
                    samples[i]
                )
            );


        const value =
            s<0
            ? s*0x8000
            : s*0x7fff;


        view.setInt16(
            offset,
            value,
            true
        );


        offset+=2;

    }


    return new Blob(
        [buffer],
        {
            type:"audio/wav"
        }
    );

}


/* =========================================================
   WAV 오프라인 렌더링
========================================================= */

async function downloadWav(){

    const visibleLayers =
        layers.filter(
            l =>
                l.visible &&
                l.points.length>=2
        );


    if(
        !visibleLayers.length
    ){

        msg.textContent =
            "저장할 수 있는 표시된 그래프가 없습니다.";

        return;

    }


    stopMusic();


    const duration =
        Number(
            document.getElementById(
                "duration"
            ).value
        );


    const scale =
        scales[
            document.getElementById(
                "scale"
            ).value
        ];


    const style =
        styles[
            document.getElementById(
                "style"
            ).value
        ];


    const sampleRate =
        44100;


    const totalSamples =
        Math.floor(
            duration*
            sampleRate
        );


    msg.textContent =
        "WAV 파일을 만드는 중입니다. 잠시만 기다려 주세요...";


    document.getElementById(
        "now"
    ).textContent =
        "오디오 렌더링 중 · " +
        duration +
        "초";


    const offline =
        new OfflineAudioContext(
            1,
            totalSamples,
            sampleRate
        );


    /*
       마스터 컴프레서로 레이어가
       동시에 울릴 때 지나치게 튀는 것을 줄임
    */

    const compressor =
        offline.createDynamicsCompressor();


    compressor.threshold.value =
        -18;

    compressor.knee.value =
        12;

    compressor.ratio.value =
        5;

    compressor.attack.value =
        .003;

    compressor.release.value =
        .15;


    compressor.connect(
        offline.destination
    );


    visibleLayers.forEach(
        layer=>{

            const data =
                prepareLayerAudio(
                    layer
                );


            if(!data){
                return;
            }


            const osc =
                offline.createOscillator();


            const gain =
                offline.createGain();


            osc.type =
                style.waveform;


            const points =
                data.points;


            const initialMidi =
                graphMidi(
                    points[0].y,
                    data.lo,
                    data.hi,
                    scale
                );


            const initialFreq =
                midiFreq(
                    initialMidi
                );


            osc.frequency.setValueAtTime(
                initialFreq,
                0
            );


            for(
                let i=1;
                i<points.length;
                i++
            ){

                const progress =
                    i/
                    (
                        points.length-1
                    );


                const t =
                    progress*
                    duration;


                const midi =
                    graphMidi(
                        points[i].y,
                        data.lo,
                        data.hi,
                        scale
                    );


                const freq =
                    Math.max(
                        45,
                        Math.min(
                            1800,
                            midiFreq(midi)
                        )
                    );


                osc.frequency
                    .linearRampToValueAtTime(
                        freq,
                        t
                    );

            }


            const level =
                layer.volume *
                style.baseGain;


            gain.gain.setValueAtTime(
                0,
                0
            );


            gain.gain
                .linearRampToValueAtTime(
                    level,
                    Math.min(
                        style.attack,
                        duration/4
                    )
                );


            gain.gain
                .linearRampToValueAtTime(
                    level,
                    Math.max(
                        style.attack,
                        duration-.12
                    )
                );


            gain.gain
                .linearRampToValueAtTime(
                    0,
                    duration
                );


            osc.connect(gain);

            gain.connect(compressor);

            osc.start(0);

            osc.stop(duration);


            /*
               서브 옥타브
            */

            if(style.subGain>0){

                const sub =
                    offline
                    .createOscillator();


                const subGain =
                    offline
                    .createGain();


                sub.type =
                    style.waveform;


                sub.frequency.setValueAtTime(
                    initialFreq/2,
                    0
                );


                for(
                    let i=1;
                    i<points.length;
                    i++
                ){

                    const progress =
                        i/
                        (
                            points.length-1
                        );


                    const t =
                        progress*
                        duration;


                    const midi =
                        graphMidi(
                            points[i].y,
                            data.lo,
                            data.hi,
                            scale
                        );


                    const freq =
                        Math.max(
                            30,
                            Math.min(
                                900,
                                midiFreq(midi)/2
                            )
                        );


                    sub.frequency
                        .linearRampToValueAtTime(
                            freq,
                            t
                        );

                }


                subGain.gain.setValueAtTime(
                    0,
                    0
                );


                subGain.gain
                    .linearRampToValueAtTime(
                        layer.volume *
                        style.subGain,
                        Math.min(
                            style.attack,
                            duration/4
                        )
                    );


                subGain.gain
                    .linearRampToValueAtTime(
                        layer.volume *
                        style.subGain,
                        Math.max(
                            style.attack,
                            duration-.12
                        )
                    );


                subGain.gain
                    .linearRampToValueAtTime(
                        0,
                        duration
                    );


                sub.connect(
                    subGain
                );


                subGain.connect(
                    compressor
                );


                sub.start(0);

                sub.stop(duration);

            }

        }
    );


    try{

        const rendered =
            await offline.startRendering();


        const blob =
            createWavBlob(
                rendered
            );


        const url =
            URL.createObjectURL(
                blob
            );


        const a =
            document.createElement(
                "a"
            );


        const filename =
            safeFilename(
                document.getElementById(
                    "songName"
                ).value
            );


        a.href=url;

        a.download =
            filename +
            ".wav";


        document.body.appendChild(
            a
        );


        a.click();

        a.remove();


        setTimeout(
            ()=>{
                URL.revokeObjectURL(
                    url
                );
            },
            5000
        );


        msg.textContent =
            "WAV 파일을 저장했습니다.";


        document.getElementById(
            "now"
        ).textContent =
            "WAV 저장 완료";

    }catch(error){

        console.error(error);

        msg.textContent =
            "WAV 생성 중 오류가 발생했습니다.";

    }

}


document
.getElementById(
    "downloadWav"
)
.addEventListener(
    "click",
    downloadWav
);


/* =========================================================
   Library
========================================================= */

function createId(
    prefix
){

    return (
        prefix+
        Date.now()+
        "_" +
        Math.random()
        .toString(36)
        .slice(2,8)
    );

}


function defaultLibraries(){

    return [

        {

            id:
                createId(
                    "lib_"
                ),

            name:
                "My Library",

            songs:[]

        }

    ];

}


function loadLibraries(){

    try{

        const raw =
            localStorage.getItem(
                LIBRARY_KEY
            );


        if(!raw){

            return defaultLibraries();

        }


        const parsed =
            JSON.parse(raw);


        if(
            !Array.isArray(parsed) ||
            !parsed.length
        ){

            return defaultLibraries();

        }


        return parsed;

    }catch(e){

        return defaultLibraries();

    }

}


function saveLibraries(){

    try{

        localStorage.setItem(
            LIBRARY_KEY,
            JSON.stringify(
                libraries
            )
        );

    }catch(e){

        msg.textContent =
            "Library 저장 공간을 사용할 수 없습니다.";

    }

}


function currentLibrary(){

    return libraries.find(
        l =>
            l.id===
            currentLibraryId
    ) || null;

}


/* =========================================================
   Library UI
========================================================= */

function renderLibrarySelect(){

    const select =
        document.getElementById(
            "librarySelect"
        );


    select.innerHTML="";


    libraries.forEach(
        lib=>{

            const option =
                document.createElement(
                    "option"
                );

            option.value =
                lib.id;

            option.textContent =
                lib.name;

            if(
                lib.id===
                currentLibraryId
            ){

                option.selected=true;

            }

            select.appendChild(
                option
            );

        }
    );

}


function renderSongList(){

    const box =
        document.getElementById(
            "songList"
        );


    box.innerHTML="";


    const lib =
        currentLibrary();


    if(!lib){

        return;

    }


    document.getElementById(
        "libraryMeta"
    ).textContent =
        lib.songs.length +
        "개 곡";


    if(
        !lib.songs.length
    ){

        const empty =
            document.createElement(
                "div"
            );

        empty.className =
            "notice";

        empty.textContent =
            "아직 저장된 곡이 없습니다. 현재 곡 이름을 입력하고 '곡 저장'을 눌러주세요.";

        box.appendChild(
            empty
        );

        return;

    }


    lib.songs
        .slice()
        .reverse()
        .forEach(
            song=>{

                const item =
                    document.createElement(
                        "div"
                    );

                item.className =
                    "songItem";


                const info =
                    document.createElement(
                        "div"
                    );

                info.className =
                    "songInfo";


                const title =
                    document.createElement(
                        "div"
                    );

                title.className =
                    "songTitle";

                title.textContent =
                    song.name;


                const date =
                    document.createElement(
                        "div"
                    );

                date.className =
                    "songDate";

                date.textContent =
                    new Date(
                        song.savedAt
                    )
                    .toLocaleString(
                        "ko-KR"
                    );


                info.appendChild(
                    title
                );

                info.appendChild(
                    date
                );


                const actions =
                    document.createElement(
                        "div"
                    );

                actions.className =
                    "songActions";


                const loadBtn =
                    document.createElement(
                        "button"
                    );

                loadBtn.textContent =
                    "불러오기";


                const deleteBtn =
                    document.createElement(
                        "button"
                    );

                deleteBtn.textContent =
                    "삭제";

                deleteBtn.className =
                    "danger";


                actions.appendChild(
                    loadBtn
                );

                actions.appendChild(
                    deleteBtn
                );


                item.appendChild(
                    info
                );

                item.appendChild(
                    actions
                );


                loadBtn.addEventListener(
                    "click",
                    e=>{

                        e.stopPropagation();

                        loadSong(
                            song.id
                        );

                    }
                );


                deleteBtn.addEventListener(
                    "click",
                    e=>{

                        e.stopPropagation();

                        deleteSong(
                            song.id
                        );

                    }
                );


                box.appendChild(
                    item
                );

            }
        );

}


/* =========================================================
   곡 직렬화
========================================================= */

function serializeLayers(){

    return layers.map(
        layer=>({

            id:
                layer.id,

            name:
                layer.name,

            type:
                layer.type,

            expression:
                layer.expression,

            visible:
                layer.visible,

            volume:
                layer.volume,

            color:
                layer.color,

            /*
               함수는 expression으로
               다시 생성할 수 있으므로 points를
               저장하지 않아도 됨.
            */

            points:
                layer.type==="sketch"
                ? layer.points
                : [],

            transform:{
                tx:
                    layer.transform.tx,

                ty:
                    layer.transform.ty,

                scale:
                    layer.transform.scale,

                rotation:
                    layer.transform.rotation
            }

        })
    );

}


/* =========================================================
   곡 불러오기용 레이어 복원
========================================================= */

function restoreLayers(
    savedLayers
){

    layers =
        savedLayers.map(
            layer=>({

                id:
                    layer.id,

                name:
                    layer.name ||
                    "Graph " +
                    layer.id,

                type:
                    layer.type ||
                    "function",

                expression:
                    layer.expression ||
                    "",

                visible:
                    layer.visible !==
                    false,

                volume:
                    Number.isFinite(
                        layer.volume
                    )
                    ? layer.volume
                    : .4,

                color:
                    layer.color ||
                    layerColors[
                        (
                            layer.id-1
                        ) %
                        layerColors.length
                    ],

                points:
                    layer.type==="sketch"
                    ? (
                        layer.points ||
                        []
                    )
                    : [],

                transform:{
                    tx:
                        layer.transform
                        ?.tx || 0,

                    ty:
                        layer.transform
                        ?.ty || 0,

                    scale:
                        layer.transform
                        ?.scale || 1,

                    rotation:
                        layer.transform
                        ?.rotation || 0
                }

            })
        );


    /*
       함수 레이어 points 재생성
    */

    layers.forEach(
        layer=>{

            if(
                layer.type==="function"
            ){

                try{

                    const points =
                        generateFunctionPoints(
                            layer.expression
                        );


                    const center =
                        getCenter(
                            points
                        );


                    points.forEach(
                        p=>{

                            p.cx =
                                center.x;

                            p.cy =
                                center.y;

                        }
                    );


                    layer.points =
                        points;

                }catch(e){

                    layer.points=[];

                }

            }else{

                const center =
                    getCenter(
                        layer.points
                    );


                layer.points =
                    layer.points.map(
                        p=>({

                            x:p.x,

                            y:p.y,

                            cx:
                                p.cx ??
                                center.x,

                            cy:
                                p.cy ??
                                center.y

                        })
                    );

            }

        }
    );


    layerIdCounter =
        Math.max(
            ...layers.map(
                l=>l.id
            ),
            1
        );

}


/* =========================================================
   현재 상태 직렬화
========================================================= */

function buildSongSnapshot(){

    return {

        id:
            currentSongId ||
            createId(
                "song_"
            ),

        name:
            document.getElementById(
                "songName"
            ).value.trim()
            ||
            "Untitled Cosmos",

        savedAt:
            Date.now(),

        duration:
            document.getElementById(
                "duration"
            ).value,

        scale:
            document.getElementById(
                "scale"
            ).value,

        style:
            document.getElementById(
                "style"
            ).value,

        view:{

            xmin:xmin,

            xmax:xmax,

            ymin:ymin,

            ymax:ymax

        },

        layers:
            serializeLayers()

    };

}


/* =========================================================
   곡 저장
========================================================= */

function saveSong(){

    const lib =
        currentLibrary();


    if(!lib){

        return;

    }


    const name =
        document.getElementById(
            "songName"
        ).value.trim()
        ||
        "Untitled Cosmos";


    document.getElementById(
        "songName"
    ).value =
        name;


    const snapshot =
        buildSongSnapshot();


    let index =
        lib.songs.findIndex(
            s =>
                s.id===
                currentSongId
        );


    if(index>=0){

        snapshot.id =
            currentSongId;

        lib.songs[index] =
            snapshot;

    }else{

        currentSongId =
            snapshot.id;

        lib.songs.push(
            snapshot
        );

    }


    saveLibraries();

    renderSongList();


    msg.textContent =
        "'" +
        name +
        "' 곡을 '" +
        lib.name +
        "'에 저장했습니다.";

}


document
.getElementById(
    "saveSong"
)
.addEventListener(
    "click",
    saveSong
);


/* =========================================================
   곡 불러오기
========================================================= */

function loadSong(songId){

    const lib =
        currentLibrary();


    if(!lib){
        return;
    }


    const song =
        lib.songs.find(
            s =>
                s.id===
                songId
        );


    if(!song){
        return;
    }


    stopMusic();


    currentSongId =
        song.id;


    document.getElementById(
        "songName"
    ).value =
        song.name;


    document.getElementById(
        "duration"
    ).value =
        song.duration ||
        "30";


    document.getElementById(
        "scale"
    ).value =
        song.scale ||
        "major";


    document.getElementById(
        "style"
    ).value =
        song.style ||
        "pop";


    if(song.view){

        xmin =
            Number.isFinite(
                song.view.xmin
            )
            ? song.view.xmin
            : -10;

        xmax =
            Number.isFinite(
                song.view.xmax
            )
            ? song.view.xmax
            : 10;

        ymin =
            Number.isFinite(
                song.view.ymin
            )
            ? song.view.ymin
            : -6;

        ymax =
            Number.isFinite(
                song.view.ymax
            )
            ? song.view.ymax
            : 6;

    }


    restoreLayers(
        song.layers
    );


    selectedLayerId =
        layers.length
        ? layers[0].id
        : null;


    expr.value =
        selectedLayer()
        ?.expression || "";


    renderLayers();

    draw();


    msg.textContent =
        "'" +
        song.name +
        "' 곡을 불러왔습니다.";

}


/* =========================================================
   곡 삭제
========================================================= */

function deleteSong(songId){

    const lib =
        currentLibrary();


    if(!lib){
        return;
    }


    const song =
        lib.songs.find(
            s =>
                s.id===
                songId
        );


    if(!song){
        return;
    }


    if(
        !confirm(
            "'" +
            song.name +
            "' 곡을 삭제할까요?"
        )
    ){
        return;
    }


    lib.songs =
        lib.songs.filter(
            s =>
                s.id!==
                songId
        );


    if(
        currentSongId===
        songId
    ){

        currentSongId=null;

    }


    saveLibraries();

    renderSongList();


    msg.textContent =
        "곡을 삭제했습니다.";

}


/* =========================================================
   새 곡
========================================================= */

function createFreshWorkspace(){

    stopMusic();


    xmin=-10;

    xmax=10;

    ymin=-6;

    ymax=6;


    layerIdCounter=2;

    selectedLayerId=1;


    layers=[

        {

            id:1,

            name:"Graph 1",

            type:"function",

            expression:"sin(x)",

            visible:true,

            volume:.55,

            color:layerColors[0],

            points:[],

            transform:{
                tx:0,
                ty:0,
                scale:1,
                rotation:0
            }

        },

        {

            id:2,

            name:"Graph 2",

            type:"function",

            expression:"0.5*cos(2*x)",

            visible:true,

            volume:.40,

            color:layerColors[1],

            points:[],

            transform:{
                tx:0,
                ty:0,
                scale:1,
                rotation:0
            }

        }

    ];


    layers.forEach(
        layer=>{

            const points =
                generateFunctionPoints(
                    layer.expression
                );


            const center =
                getCenter(
                    points
                );


            points.forEach(
                p=>{

                    p.cx =
                        center.x;

                    p.cy =
                        center.y;

                }
            );


            layer.points =
                points;

        }
    );


    document.getElementById(
        "songName"
    ).value =
        "Untitled Cosmos";


    document.getElementById(
        "duration"
    ).value =
        "30";


    document.getElementById(
        "scale"
    ).value =
        "major";


    document.getElementById(
        "style"
    ).value =
        "pop";


    expr.value =
        "sin(x)";


    currentSongId=null;


    renderLayers();

    draw();

}


document
.getElementById(
    "newSong"
)
.addEventListener(
    "click",
    ()=>{

        createFreshWorkspace();

        msg.textContent =
            "새 곡 작업 공간을 만들었습니다.";

    }
);


/* =========================================================
   새 Library
========================================================= */

document
.getElementById(
    "newLibrary"
)
.addEventListener(
    "click",
    ()=>{

        const name =
            prompt(
                "새 Library 이름을 입력하세요."
            );


        if(!name){
            return;
        }


        const library={

            id:
                createId(
                    "lib_"
                ),

            name:
                name.trim(),

            songs:[]

        };


        libraries.push(
            library
        );


        currentLibraryId =
            library.id;


        currentSongId=null;


        saveLibraries();

        renderLibrarySelect();

        renderSongList();


        msg.textContent =
            "'" +
            library.name +
            "' Library를 만들었습니다.";

    }
);


/* =========================================================
   Library 이름 변경
========================================================= */

document
.getElementById(
    "renameLibrary"
)
.addEventListener(
    "click",
    ()=>{

        const lib =
            currentLibrary();


        if(!lib){
            return;
        }


        const name =
            prompt(
                "새 Library 이름",
                lib.name
            );


        if(!name){
            return;
        }


        lib.name =
            name.trim();


        saveLibraries();

        renderLibrarySelect();

        renderSongList();


        msg.textContent =
            "Library 이름을 변경했습니다.";

    }
);


/* =========================================================
   Library 삭제
========================================================= */

document
.getElementById(
    "deleteLibrary"
)
.addEventListener(
    "click",
    ()=>{

        if(
            libraries.length<=1
        ){

            msg.textContent =
                "최소 한 개의 Library는 필요합니다.";

            return;

        }


        const lib =
            currentLibrary();


        if(!lib){
            return;
        }


        if(
            !confirm(
                "'" +
                lib.name +
                "' Library와 안의 저장된 곡들을 모두 삭제할까요?"
            )
        ){
            return;
        }


        libraries =
            libraries.filter(
                l =>
                    l.id!==
                    currentLibraryId
            );


        currentLibraryId =
            libraries[0].id;

        currentSongId=null;


        saveLibraries();

        renderLibrarySelect();

        renderSongList();


        msg.textContent =
            "Library를 삭제했습니다.";

    }
);


/* =========================================================
   Library 변경
========================================================= */

document
.getElementById(
    "librarySelect"
)
.addEventListener(
    "change",
    e=>{

        currentLibraryId =
            e.target.value;

        currentSongId=null;

        renderSongList();


        msg.textContent =
            "'" +
            currentLibrary()
            ?.name +
            "' Library를 선택했습니다.";

    }
);



/* =========================================================
   WORKSPACE UI
========================================================= */

const addMenuToggle =
    document.getElementById("addMenuToggle");

const addMenu =
    document.getElementById("addMenu");

addMenuToggle.addEventListener(
    "click",
    e=>{
        e.stopPropagation();
        addMenu.classList.toggle("open");
    }
);

document.addEventListener(
    "click",
    e=>{
        if(
            !e.target.closest(".addMenuWrap")
        ){
            addMenu.classList.remove("open");
        }
    }
);

document
.querySelectorAll("#addMenu button")
.forEach(
    button=>{
        button.addEventListener(
            "click",
            ()=>{
                addMenu.classList.remove("open");
            }
        );
    }
);


/* ---------- rail ---------- */

function toggleRail(
    id,
    open
){
    document
    .querySelectorAll(".railPanel")
    .forEach(
        panel=>{
            panel.classList.toggle(
                "open",
                panel.id===id
                    ? open
                    : false
            );
        }
    );
}

document
.getElementById("musicRailOpen")
.addEventListener(
    "click",
    ()=>toggleRail("musicDrawer",true)
);

document
.getElementById("musicRailButton")
.addEventListener(
    "click",
    ()=>toggleRail("musicDrawer",true)
);

document
.getElementById("musicRailClose")
.addEventListener(
    "click",
    ()=>toggleRail("musicDrawer",false)
);

document
.getElementById("principleRailOpen")
.addEventListener(
    "click",
    ()=>toggleRail("principleDrawer",true)
);

document
.getElementById("principleRailButton")
.addEventListener(
    "click",
    ()=>toggleRail("principleDrawer",true)
);

document
.getElementById("principleRailClose")
.addEventListener(
    "click",
    ()=>toggleRail("principleDrawer",false)
);


/* ---------- secondary save ---------- */

document
.getElementById("saveSongSecondary")
.addEventListener(
    "click",
    ()=>{
        document
        .getElementById("saveSong")
        .click();
    }
);


/* ---------- graph settings ---------- */

const settingsToggle =
    document.getElementById("settingsToggle");

const settingsPanel =
    document.getElementById("settingsPanel");

settingsToggle.addEventListener(
    "click",
    e=>{
        e.stopPropagation();
        settingsPanel.classList.toggle("open");
    }
);

document.addEventListener(
    "click",
    e=>{
        if(
            !e.target.closest(".canvasSettings")
        ){
            settingsPanel.classList.remove("open");
        }
    }
);

function syncViewInputs(){
    document.getElementById("xminInput").value = fmt(xmin);
    document.getElementById("xmaxInput").value = fmt(xmax);
    document.getElementById("yminInput").value = fmt(ymin);
    document.getElementById("ymaxInput").value = fmt(ymax);
}

function applyViewInputs(){
    const a = Number(document.getElementById("xminInput").value);
    const b = Number(document.getElementById("xmaxInput").value);
    const c = Number(document.getElementById("yminInput").value);
    const d = Number(document.getElementById("ymaxInput").value);

    if(
        !Number.isFinite(a) ||
        !Number.isFinite(b) ||
        !Number.isFinite(c) ||
        !Number.isFinite(d) ||
        a>=b ||
        c>=d
    ){
        msg.textContent = "축 범위를 올바르게 입력하세요.";
        return;
    }

    xmin=a;
    xmax=b;
    ymin=c;
    ymax=d;
    draw();
}

["xminInput","xmaxInput","yminInput","ymaxInput"]
.forEach(
    id=>{
        document
        .getElementById(id)
        .addEventListener(
            "change",
            applyViewInputs
        );
    }
);

document
.getElementById("resetView")
.addEventListener(
    "click",
    ()=>{
        xmin=-10;
        xmax=10;
        ymin=-6;
        ymax=6;
        syncViewInputs();
        draw();
    }
);

document
.getElementById("gridToggle")
.addEventListener(
    "change",
    draw
);

document
.getElementById("axisToggle")
.addEventListener(
    "change",
    draw
);


/* ---------- keypad ---------- */

document
.getElementById("keypadToggle")
.addEventListener(
    "click",
    ()=>{
        document
        .getElementById("keypad")
        .classList.toggle("open");
    }
);

document
.querySelectorAll("#keypad [data-key]")
.forEach(
    button=>{
        button.addEventListener(
            "click",
            ()=>{
                const key=button.dataset.key;
                const start=expr.selectionStart ?? expr.value.length;
                const end=expr.selectionEnd ?? expr.value.length;

                expr.value =
                    expr.value.slice(0,start) +
                    key +
                    expr.value.slice(end);

                expr.focus();

                const pos=start+key.length;
                expr.setSelectionRange(pos,pos);
            }
        );
    }
);


/* ---------- initial workspace values ---------- */

syncViewInputs();

/* =========================================================
   리사이즈
========================================================= */

function resize(){

    const rect =
        canvas.getBoundingClientRect();


    const dpr =
        window.devicePixelRatio ||
        1;


    canvas.width =
        Math.max(
            600,
            Math.floor(
                rect.width*dpr
            )
        );


    canvas.height =
        Math.max(
            400,
            Math.floor(
                rect.height*dpr
            )
        );


    ctx.setTransform(
        dpr,
        0,
        0,
        dpr,
        0,
        0
    );


    draw();

}


window.addEventListener(
    "resize",
    resize
);


/* =========================================================
   초기화
========================================================= */

libraries =
    loadLibraries();


currentLibraryId =
    libraries[0].id;


createFreshWorkspace();


renderLibrarySelect();

renderSongList();


resize();

renderLayers();

draw();


})();

</script>

</body>
</html>
"""

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background:#f6f7fb;
    }

    [data-testid="stHeader"] {
        background:transparent;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(
    HTML,
    height=2300,
    scrolling=True
)
