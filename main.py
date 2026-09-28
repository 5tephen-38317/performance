import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Cosmos — Graph to Music",
    page_icon="∿",
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
*{box-sizing:border-box}
body{
  margin:0;
  font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  background:#0b1020;
  color:#edf2ff;
}
#cosmos{max-width:1200px;margin:0 auto;padding:24px}
.header{display:flex;justify-content:space-between;align-items:end;gap:20px;margin-bottom:18px}
.logo{font-size:34px;font-weight:800;letter-spacing:-1px}
.logo span{color:#8da2ff}
.subtitle{color:#9da9c7;font-size:14px;margin-top:5px}
.status{font-size:12px;color:#9da9c7}
.grid{display:grid;grid-template-columns:1fr;gap:16px}
.lowerGrid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.card{
  background:#121a2e;
  border:1px solid #263354;
  border-radius:18px;
  padding:16px;
  box-shadow:0 8px 30px rgba(0,0,0,.18);
}
.card h2{font-size:16px;margin:0 0 12px}
.graphWrap{position:relative}
canvas{width:100%;height:480px;background:#080d19;border-radius:13px;display:block}
.controls{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
input,select,button{
  font:inherit;
}
#expr{
  width:100%;
  padding:13px 14px;
  border-radius:11px;
  border:1px solid #33436c;
  background:#0b1122;
  color:#fff;
  font-size:17px;
  outline:none;
}
#expr:focus{border-color:#8da2ff;box-shadow:0 0 0 3px rgba(141,162,255,.12)}
button{
  border:1px solid #344365;
  background:#18233d;
  color:#eef2ff;
  border-radius:10px;
  padding:10px 13px;
  cursor:pointer;
  min-height:42px;
}
button:hover{background:#202e4d}
.primary{background:#6478e8;border-color:#6478e8;font-weight:700}
.primary:hover{background:#7184ee}
.danger{background:#2a1820}
.keypad{display:grid;grid-template-columns:repeat(5,1fr);gap:7px;margin-top:10px}
.keypad button{min-height:40px;padding:7px}
.keypad .backspace{background:#2a2338;border-color:#4b4168;font-weight:700}
.keypad .backspace:hover{background:#382d4e}
.section{margin-top:16px}
.row{display:grid;grid-template-columns:1fr 1fr;gap:9px}
label{display:block;font-size:12px;color:#9da9c7;margin-bottom:6px}
select{
 width:100%;padding:10px;border-radius:9px;border:1px solid #33436c;
 background:#0b1122;color:#fff;
}
.feature{
 display:flex;justify-content:space-between;gap:10px;padding:10px 0;
 border-bottom:1px solid #222e4b;font-size:13px;
}
.feature:last-child{border-bottom:0}
.value{font-weight:700;color:#b8c4ff}
.help{font-size:12px;color:#8996b7;line-height:1.55;margin-top:10px}
.badge{display:inline-block;padding:5px 8px;border-radius:999px;background:#1b2947;color:#b9c5ff;font-size:11px}
#message{min-height:20px;margin-top:9px;color:#ffb4b4;font-size:12px}
.musicBox{margin-top:16px}
.now{font-size:13px;color:#aeb9d5;min-height:20px;margin-bottom:9px}
.progress{height:7px;background:#202b46;border-radius:99px;overflow:hidden}
#bar{height:100%;width:0;background:#8496ff;transition:width .05s linear}
.small{font-size:11px;color:#7886a8}
@media(max-width:850px){
 .lowerGrid{grid-template-columns:1fr}
 canvas{height:390px}
 .header{align-items:start;flex-direction:column}
}
</style>
</head>
<body>
<div id="cosmos">
  <div class="header">
    <div>
      <div class="logo">Cos<span>mos</span></div>
      <div class="subtitle">Graph → Music · 그래프를 소리로 번역하는 수학 음악 실험실</div>
    </div>
    <div class="status"><span class="badge">Cosmos v1.2</span></div>
  </div>

  <div class="grid">
    <section class="card">
      <h2>① 함수 그래프</h2>
      <div class="graphWrap">
        <canvas id="graph" width="1200" height="600"></canvas>
      </div>

      <div class="controls">
        <button id="zoomIn">＋ 확대</button>
        <button id="zoomOut">－ 축소</button>
        <button id="left">← 이동</button>
        <button id="right">→ 이동</button>
        <button id="up">↑ 이동</button>
        <button id="down">↓ 이동</button>
      </div>

      <div class="section">
        <h2>② 함수 입력</h2>
        <input id="expr" value="sin(x)" autocomplete="off" spellcheck="false"
               aria-label="함수 입력">
        <div class="controls">
          <button class="primary" id="draw">그래프 그리기</button>
          <button id="resetView">화면 초기화</button>
          <button id="clear">지우기</button>
        </div>
        <div class="keypad" id="keypad">
          <button data-v="x">x</button><button data-v="(">(</button><button data-v=")">)</button>
          <button data-v="+">+</button><button data-v="-">−</button>
          <button data-v="7">7</button><button data-v="8">8</button><button data-v="9">9</button>
          <button data-v="*">×</button><button data-v="/">÷</button>
          <button data-v="4">4</button><button data-v="5">5</button><button data-v="6">6</button>
          <button data-v="^">^</button><button data-v=".">.</button>
          <button data-v="1">1</button><button data-v="2">2</button><button data-v="3">3</button>
          <button data-v="pi">π</button><button data-v="0">0</button>
          <button data-v="sin(">sin(</button><button data-v="cos(">cos(</button>
          <button data-v="tan(">tan(</button><button data-v="sqrt(">√(</button><button data-v="abs(">abs(</button>
          <button class="backspace" id="backspace" title="커서 앞의 한 글자 삭제">⌫ 지우기</button>
        </div>
        <div id="message"></div>
      </div>

      <div class="help">
        그래프 영역에서 마우스 휠로 확대/축소할 수 있고, 드래그로 화면을 이동할 수 있습니다.
        음악 재생 중에는 <b>그래프의 왼쪽 끝에서 오른쪽 끝까지 점이 이동</b>하며 현재 재생되는 음을 표시합니다.
        함수는 키보드로 직접 입력하거나 아래 수학 키패드로 입력할 수 있습니다.
      </div>
    </section>

    <div class="lowerGrid">
      <section class="card">
        <h2>③ 그래프 분석</h2>
        <div class="feature"><span>정의역</span><span class="value" id="domain">−10 ≤ x ≤ 10</span></div>
        <div class="feature"><span>최솟값</span><span class="value" id="minY">—</span></div>
        <div class="feature"><span>최댓값</span><span class="value" id="maxY">—</span></div>
        <div class="feature"><span>평균 높이</span><span class="value" id="avgY">—</span></div>
        <div class="feature"><span>변화 방향</span><span class="value" id="trend">—</span></div>
      </section>

      <section class="card musicBox">
        <h2>④ Graph → Music</h2>
        <div class="row">
          <div>
            <label>음계</label>
            <select id="scale">
              <option value="major">C Major</option>
              <option value="minor">A Minor</option>
              <option value="pentatonic">Pentatonic</option>
              <option value="chromatic">Chromatic</option>
            </select>
          </div>
          <div>
            <label>템포</label>
            <select id="tempo">
              <option value="80">80 BPM</option>
              <option value="100" selected>100 BPM</option>
              <option value="120">120 BPM</option>
              <option value="150">150 BPM</option>
            </select>
          </div>
        </div>

        <div class="controls">
          <button class="primary" id="play">▶ 그래프로 음악 만들기</button>
          <button id="stop">■ 정지</button>
        </div>

        <div class="now" id="now">그래프의 높이가 음높이로 변환됩니다.</div>
        <div class="progress"><div id="bar"></div></div>

        <div class="help">
          <b>변환 원리</b><br>
          x축 → 시간의 흐름<br>
          y값 → 음높이<br>
          그래프의 기울기 → 음의 진행 방향<br>
          그래프의 변화량 → 음정 변화의 크기
        </div>
      </section>
    </div>
  </div>

  <section class="card musicBox">
    <h2>Cosmos의 핵심</h2>
    <div class="help">
      같은 수식이라도 그래프의 형태가 달라지면 다른 음악이 만들어집니다.
      즉, 수학적 함수를 단순히 계산하는 것이 아니라
      <b>그래프의 구조를 음악적 데이터로 변환</b>합니다.
    </div>
  </section>
<script>
(function(){
"use strict";

const root=document.getElementById("cosmos");
const canvas=document.getElementById("graph");
const ctx=canvas.getContext("2d");
const expr=document.getElementById("expr");
const msg=document.getElementById("message");

let xmin=-10,xmax=10,ymin=-6,ymax=6;
let dragging=false,lastX=0,lastY=0;
let samples=[];
let audioCtx=null, activeOsc=[];
let playing=false, raf=null;
let playbackPoint=null;

const funcs={
 sin:Math.sin, cos:Math.cos, tan:Math.tan,
 sqrt:Math.sqrt, abs:Math.abs, log:Math.log,
 exp:Math.exp, asin:Math.asin, acos:Math.acos, atan:Math.atan
};

// ---- 안전한 수식 파서: 외부 eval 없이 함수식을 해석 ----
function tokenize(s){
  s=s.replace(/π/g,"pi").replace(/√/g,"sqrt");
  const tokens=[]; let i=0;
  while(i<s.length){
    if(/\s/.test(s[i])){i++;continue}
    if(/[0-9.]/.test(s[i])){
      let j=i+1;
      while(j<s.length && /[0-9.]/.test(s[j]))j++;
      const n=Number(s.slice(i,j));
      if(!Number.isFinite(n)) throw Error("숫자를 확인하세요.");
      tokens.push({t:"num",v:n}); i=j; continue;
    }
    if(/[A-Za-z_]/.test(s[i])){
      let j=i+1;
      while(j<s.length && /[A-Za-z_]/.test(s[j]))j++;
      tokens.push({t:"id",v:s.slice(i,j).toLowerCase()}); i=j; continue;
    }
    if("+-*/^(),".includes(s[i])){tokens.push({t:s[i],v:s[i]});i++;continue}
    throw Error("지원하지 않는 문자가 있습니다: "+s[i]);
  }
  return tokens;
}
function parseExpression(s){
  const ts=tokenize(s); let p=0;
  function primary(){
    const z=ts[p];
    if(!z) throw Error("수식이 완성되지 않았습니다.");
    if(z.t==="num"){p++;return ()=>z.v}
    if(z.t==="id"){
      p++;
      if(z.v==="x") return x=>x;
      if(z.v==="pi") return ()=>Math.PI;
      if(z.v==="e") return ()=>Math.E;
      if(funcs[z.v]){
        if(!ts[p] || ts[p].t!=="(") throw Error(z.v+" 뒤에 괄호가 필요합니다.");
        p++; const a=addsub();
        if(!ts[p] || ts[p].t!==")") throw Error("괄호를 닫아주세요.");
        p++;
        return x=>funcs[z.v](a(x));
      }
      throw Error("알 수 없는 함수/변수: "+z.v);
    }
    if(z.t==="("){
      p++; const a=addsub();
      if(!ts[p] || ts[p].t!==")") throw Error("괄호를 닫아주세요.");
      p++; return a;
    }
    if(z.t==="+"){p++;return primary()}
    if(z.t==="-"){p++;const a=primary();return x=>-a(x)}
    throw Error("수식을 확인하세요.");
  }
  function power(){
    let a=primary();
    if(ts[p] && ts[p].t==="^"){p++;const b=power();const aa=a;return x=>Math.pow(aa(x),b(x))}
    return a;
  }
  function muldiv(){
    let a=power();
    while(ts[p] && (ts[p].t==="*"||ts[p].t==="/")){
      const op=ts[p++].t,b=power(),aa=a;
      a=op==="*"?x=>aa(x)*b(x):x=>aa(x)/b(x);
    }
    return a;
  }
  function addsub(){
    let a=muldiv();
    while(ts[p] && (ts[p].t==="+"||ts[p].t==="-")){
      const op=ts[p++].t,b=muldiv(),aa=a;
      a=op==="+"?x=>aa(x)+b(x):x=>aa(x)-b(x);
    }
    return a;
  }
  const f=addsub();
  if(p!==ts.length) throw Error("수식을 확인하세요.");
  return f;
}

function resize(){
  const r=canvas.getBoundingClientRect();
  const d=window.devicePixelRatio||1;
  canvas.width=Math.max(500,Math.floor(r.width*d));
  canvas.height=Math.max(350,Math.floor(r.height*d));
  ctx.setTransform(d,0,0,d,0,0);
  draw();
}
function W(){return canvas.getBoundingClientRect().width}
function H(){return canvas.getBoundingClientRect().height}
function sx(x){return (x-xmin)/(xmax-xmin)*W()}
function sy(y){return H()-(y-ymin)/(ymax-ymin)*H()}
function invx(px){return xmin+px/W()*(xmax-xmin)}
function invy(py){return ymin+(H()-py)/H()*(ymax-ymin)}

function niceStep(range){
  const raw=range/10, p=Math.pow(10,Math.floor(Math.log10(raw))), n=raw/p;
  return (n<1.5?1:n<3?2:n<7?5:10)*p;
}
function draw(){
  const w=W(),h=H();
  ctx.clearRect(0,0,w,h);
  ctx.fillStyle="#080d19";ctx.fillRect(0,0,w,h);

  const xs=niceStep(xmax-xmin), ys=niceStep(ymax-ymin);
  ctx.lineWidth=1;ctx.strokeStyle="#18243d";ctx.fillStyle="#64718e";ctx.font="11px system-ui";
  for(let x=Math.ceil(xmin/xs)*xs;x<=xmax;x+=xs){
    const px=sx(x);ctx.beginPath();ctx.moveTo(px,0);ctx.lineTo(px,h);ctx.stroke();
    if(Math.abs(x)>1e-9)ctx.fillText(fmt(x),px+4,h-7);
  }
  for(let y=Math.ceil(ymin/ys)*ys;y<=ymax;y+=ys){
    const py=sy(y);ctx.beginPath();ctx.moveTo(0,py);ctx.lineTo(w,py);ctx.stroke();
    if(Math.abs(y)>1e-9)ctx.fillText(fmt(y),6,py-4);
  }
  ctx.strokeStyle="#596783";ctx.lineWidth=1.4;
  const originX = (xmin<=0&&xmax>=0) ? sx(0) : null;
  const originY = (ymin<=0&&ymax>=0) ? sy(0) : null;
  if(originX!==null){ctx.beginPath();ctx.moveTo(originX,0);ctx.lineTo(originX,h);ctx.stroke()}
  if(originY!==null){ctx.beginPath();ctx.moveTo(0,originY);ctx.lineTo(w,originY);ctx.stroke()}
  // 원점 표시
  if(originX!==null && originY!==null){
    ctx.save();
    ctx.fillStyle="#ffffff";
    ctx.beginPath();ctx.arc(originX,originY,4,0,Math.PI*2);ctx.fill();
    ctx.fillStyle="#aeb9d5";
    ctx.font="bold 12px system-ui";
    ctx.fillText("O (0, 0)", originX+8, originY-9);
    ctx.restore();
  }

  let f;
  try{f=parseExpression(expr.value)}catch(e){msg.textContent=e.message;return}
  msg.textContent="";
  samples=[];
  let lastValid=null;
  const N=Math.min(1800,Math.max(700,Math.floor(w*1.5)));
  ctx.beginPath();
  let started=false;
  let min=Infinity,max=-Infinity,sum=0,count=0;
  for(let i=0;i<=N;i++){
    const x=xmin+(xmax-xmin)*i/N;
    let y;
    try{y=f(x)}catch(e){y=NaN}
    const valid=Number.isFinite(y)&&Math.abs(y)<1e8;
    samples.push({x,y});
    if(valid){min=Math.min(min,y);max=Math.max(max,y);sum+=y;count++}
    if(!valid||Math.abs(y)>Math.max(1e4,(ymax-ymin)*100)){
      started=false;lastValid=null;continue;
    }
    const px=sx(x),py=sy(y);
    if(!started|| (lastValid!==null && Math.abs(py-lastValid)>h*2)){
      ctx.moveTo(px,py);started=true;
    }else ctx.lineTo(px,py);
    lastValid=py;
  }
  ctx.strokeStyle="#91a4ff";ctx.lineWidth=3;ctx.lineJoin="round";ctx.stroke();

  // 음악 재생 위치: 화면의 왼쪽 끝에서 오른쪽 끝까지 이동하는 점
  if(playbackPoint && Number.isFinite(playbackPoint.x) && Number.isFinite(playbackPoint.y)){
    const px=sx(playbackPoint.x), py=sy(playbackPoint.y);
    if(px>=-12 && px<=w+12 && py>=-12 && py<=h+12){
      ctx.save();
      ctx.beginPath();
      ctx.arc(px,py,12,0,Math.PI*2);
      ctx.fillStyle="rgba(255,207,92,.18)";
      ctx.fill();
      ctx.beginPath();
      ctx.arc(px,py,7,0,Math.PI*2);
      ctx.fillStyle="#ffffff";
      ctx.fill();
      ctx.beginPath();
      ctx.arc(px,py,4,0,Math.PI*2);
      ctx.fillStyle="#ffcf5c";
      ctx.fill();
      ctx.restore();
    }
  }

  document.getElementById("domain").textContent=fmt(xmin)+" ≤ x ≤ "+fmt(xmax);
  document.getElementById("minY").textContent=count?fmt(min):"—";
  document.getElementById("maxY").textContent=count?fmt(max):"—";
  document.getElementById("avgY").textContent=count?fmt(sum/count):"—";

  if(count){
    let left=0,right=0,n=0;
    for(let i=1;i<samples.length;i++){
      if(Number.isFinite(samples[i-1].y)&&Number.isFinite(samples[i].y)){
        const d=samples[i].y-samples[i-1].y;
        if(d>0)right++; else if(d<0)left++; n++;
      }
    }
    document.getElementById("trend").textContent=
      n?(right>left*1.25?"주로 증가":left>right*1.25?"주로 감소":"상승·하강 반복"):"—";
  }
}
function fmt(v){
  if(!Number.isFinite(v))return "—";
  if(Math.abs(v)<1e-9)return "0";
  return Math.abs(v)>=100?Math.round(v).toString():Number(v.toFixed(2)).toString();
}

function changeView(factor,dx=0,dy=0){
  const cx=(xmin+xmax)/2+(dx*(xmax-xmin));
  const cy=(ymin+ymax)/2+(dy*(ymax-ymin));
  const xr=(xmax-xmin)*factor,yr=(ymax-ymin)*factor;
  xmin=cx-xr/2;xmax=cx+xr/2;ymin=cy-yr/2;ymax=cy+yr/2;draw();
}

document.getElementById("draw").addEventListener("click",draw);
expr.addEventListener("keydown",e=>{if(e.key==="Enter")draw()});
document.getElementById("resetView").addEventListener("click",()=>{
 xmin=-10;xmax=10;ymin=-6;ymax=6;draw();
});
document.getElementById("clear").addEventListener("click",()=>{expr.value="";draw()});
document.getElementById("zoomIn").addEventListener("click",()=>changeView(.75));
document.getElementById("zoomOut").addEventListener("click",()=>changeView(1.35));
document.getElementById("left").addEventListener("click",()=>changeView(1,-.12,0));
document.getElementById("right").addEventListener("click",()=>changeView(1,.12,0));
document.getElementById("up").addEventListener("click",()=>changeView(1,0,.12));
document.getElementById("down").addEventListener("click",()=>changeView(1,0,-.12));

document.querySelectorAll("#keypad button[data-v]").forEach(b=>{
 b.addEventListener("click",()=>{
   const v=b.dataset.v;
   const start=expr.selectionStart??expr.value.length;
   const end=expr.selectionEnd??expr.value.length;
   expr.value=expr.value.slice(0,start)+v+expr.value.slice(end);
   expr.focus();
   const pos=start+v.length;expr.setSelectionRange(pos,pos);draw();
 });
});

document.getElementById("backspace").addEventListener("click",()=>{
  const start=expr.selectionStart??expr.value.length;
  const end=expr.selectionEnd??expr.value.length;
  if(start!==end){
    expr.value=expr.value.slice(0,start)+expr.value.slice(end);
    expr.setSelectionRange(start,start);
  }else if(start>0){
    expr.value=expr.value.slice(0,start-1)+expr.value.slice(start);
    expr.setSelectionRange(start-1,start-1);
  }
  expr.focus();
  draw();
});

canvas.addEventListener("wheel",e=>{
 e.preventDefault();
 const factor=e.deltaY<0?.8:1.25;
 const mx=invx(e.offsetX),my=invy(e.offsetY);
 xmin=mx+(xmin-mx)*factor;xmax=mx+(xmax-mx)*factor;
 ymin=my+(ymin-my)*factor;ymax=my+(ymax-my)*factor;draw();
},{passive:false});
canvas.addEventListener("pointerdown",e=>{
 dragging=true;lastX=e.clientX;lastY=e.clientY;canvas.setPointerCapture(e.pointerId);
});
canvas.addEventListener("pointermove",e=>{
 if(!dragging)return;
 const dx=e.clientX-lastX,dy=e.clientY-lastY;
 const xr=xmax-xmin,yr=ymax-ymin;
 xmin-=dx/W()*xr;xmax-=dx/W()*xr;
 ymin+=dy/H()*yr;ymax+=dy/H()*yr;
 lastX=e.clientX;lastY=e.clientY;draw();
});
canvas.addEventListener("pointerup",()=>dragging=false);
canvas.addEventListener("pointercancel",()=>dragging=false);

// ---- 음악 ----
const scales={
 major:[0,2,4,5,7,9,11,12,14,16,17,19,21,23,24],
 minor:[0,2,3,5,7,8,10,12,14,15,17,19,20,22,24],
 pentatonic:[0,2,4,7,9,12,14,16,19,21,24],
 chromatic:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
};

function makeNotes(){
  // 현재 화면에 실제로 보이는 그래프 부분만 음악 재생에 사용
  // y가 화면 위/아래로 벗어난 구간은 점과 소리 모두 재생에서 제외
  const valid=samples.filter(p=>
    Number.isFinite(p.x)&&Number.isFinite(p.y)&&
    p.x>=xmin&&p.x<=xmax&&p.y>=ymin&&p.y<=ymax
  );
  if(valid.length<10)throw Error("음악으로 변환할 수 있는 그래프가 없습니다.");
  const vals=valid.map(p=>p.y);
  let lo=Math.min(...vals),hi=Math.max(...vals);
  if(Math.abs(hi-lo)<1e-8){lo-=1;hi+=1}
  const scale=scales[document.getElementById("scale").value];
  return {valid,lo,hi,scale};
}
function midiFreq(m){return 440*Math.pow(2,(m-69)/12)}
function graphMidi(y,lo,hi,scale){
  const norm=Math.max(0,Math.min(1,(y-lo)/(hi-lo)));
  const idx=Math.round(norm*(scale.length-1));
  return 48+scale[idx];
}

async function playMusic(){
  stopMusic();
  let data;
  try{data=makeNotes()}catch(e){msg.textContent=e.message;return}
  if(!audioCtx)audioCtx=new (window.AudioContext||window.webkitAudioContext)();
  if(audioCtx.state==="suspended")await audioCtx.resume();

  playing=true;
  const bpm=Number(document.getElementById("tempo").value);
  // 현재 화면에 보이는 그래프 구간만 왼쪽 → 오른쪽으로 재생
  const total=8*(100/bpm);
  const start=audioCtx.currentTime+0.05;
  const osc=audioCtx.createOscillator();
  const gain=audioCtx.createGain();
  osc.type="sine";
  gain.gain.setValueAtTime(0,start);
  gain.gain.linearRampToValueAtTime(0.13,start+0.12);
  osc.connect(gain);gain.connect(audioCtx.destination);
  osc.start(start);
  activeOsc=[osc];

  const started=performance.now();
  let lastFreq=0;
  function tick(now){
    if(!playing)return;
    const pct=Math.min(1,Math.max(0,(now-started)/1000/total));
    const targetIndex=Math.min(data.valid.length-1,Math.max(0,Math.round(pct*(data.valid.length-1))));
    const candidate=data.valid[targetIndex];
    const y=Number.isFinite(candidate.y)?candidate.y:0;
    const midi=graphMidi(y,data.lo,data.hi,data.scale);
    const freq=midiFreq(midi);
    if(Math.abs(freq-lastFreq)>0.1){
      const audioNow=audioCtx.currentTime;
      osc.frequency.cancelScheduledValues(audioNow);
      osc.frequency.setTargetAtTime(freq,audioNow,0.025);
      lastFreq=freq;
    }

    // 점은 실제 그래프 곡선을 따라 왼쪽 → 오른쪽으로 이동
    playbackPoint={x:candidate.x,y:candidate.y};
    document.getElementById("now").textContent=
      "♪ MIDI "+midi+" · 그래프 y = "+fmt(candidate.y);
    draw();
    document.getElementById("bar").style.width=(pct*100)+"%";

    if(pct<1){
      raf=requestAnimationFrame(tick);
    }else{
      const audioNow=audioCtx.currentTime;
      gain.gain.cancelScheduledValues(audioNow);
      gain.gain.setTargetAtTime(0,audioNow,0.08);
      try{osc.stop(audioNow+0.3)}catch(e){}
      playing=false;
      playbackPoint=null;
      draw();
      document.getElementById("now").textContent="재생 완료";
      document.getElementById("bar").style.width="0%";
      activeOsc=[];
    }
  }
  raf=requestAnimationFrame(tick);
}
function stopMusic(){
  playing=false;
  if(raf)cancelAnimationFrame(raf);
  raf=null;
  activeOsc.forEach(o=>{try{o.stop()}catch(e){}});
  activeOsc=[];
  playbackPoint=null;
  draw();
  document.getElementById("bar").style.width="0%";
  document.getElementById("now").textContent="정지됨";
}
document.getElementById("play").addEventListener("click",playMusic);
document.getElementById("stop").addEventListener("click",stopMusic);

window.addEventListener("resize",resize);
resize();
})();
</script>
</body>
</html>
"""

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {background:#0b1020;}
    [data-testid="stHeader"] {background:transparent;}
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(HTML, height=1120, scrolling=True)
