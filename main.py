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
*{
  box-sizing:border-box;
}

body{
  margin:0;
  font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  background:#0b1020;
  color:#edf2ff;
}

#cosmos{
  max-width:1200px;
  margin:0 auto;
  padding:24px;
}

.header{
  display:flex;
  justify-content:space-between;
  align-items:end;
  gap:20px;
  margin-bottom:18px;
}

.logo{
  font-size:34px;
  font-weight:800;
  letter-spacing:-1px;
}

.logo span{
  color:#8da2ff;
}

.subtitle{
  color:#9da9c7;
  font-size:14px;
  margin-top:5px;
}

.status{
  font-size:12px;
  color:#9da9c7;
}

.grid{
  display:grid;
  grid-template-columns:1fr;
  gap:16px;
}

.lowerGrid{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:16px;
}

.card{
  background:#121a2e;
  border:1px solid #263354;
  border-radius:18px;
  padding:16px;
  box-shadow:0 8px 30px rgba(0,0,0,.18);
}

.card h2{
  font-size:16px;
  margin:0 0 12px;
}

.graphWrap{
  position:relative;
}

canvas{
  width:100%;
  height:480px;
  background:#080d19;
  border-radius:13px;
  display:block;
}

.controls{
  display:flex;
  gap:8px;
  flex-wrap:wrap;
  margin-top:12px;
}

input,
select,
button{
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

#expr:focus{
  border-color:#8da2ff;
  box-shadow:0 0 0 3px rgba(141,162,255,.12);
}

button{
  border:1px solid #344365;
  background:#18233d;
  color:#eef2ff;
  border-radius:10px;
  padding:10px 13px;
  cursor:pointer;
  min-height:42px;
}

button:hover{
  background:#202e4d;
}

.primary{
  background:#6478e8;
  border-color:#6478e8;
  font-weight:700;
}

.primary:hover{
  background:#7184ee;
}

.keypad{
  display:grid;
  grid-template-columns:repeat(5,1fr);
  gap:7px;
  margin-top:10px;
}

.keypad button{
  min-height:40px;
  padding:7px;
}

.keypad .backspace{
  background:#2a2338;
  border-color:#4b4168;
  font-weight:700;
}

.section{
  margin-top:16px;
}

.row{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:9px;
}

.three{
  grid-template-columns:1fr 1fr 1fr;
}

label{
  display:block;
  font-size:12px;
  color:#9da9c7;
  margin-bottom:6px;
}

select{
  width:100%;
  padding:10px;
  border-radius:9px;
  border:1px solid #33436c;
  background:#0b1122;
  color:#fff;
}

.feature{
  display:flex;
  justify-content:space-between;
  gap:10px;
  padding:10px 0;
  border-bottom:1px solid #222e4b;
  font-size:13px;
}

.feature:last-child{
  border-bottom:0;
}

.value{
  font-weight:700;
  color:#b8c4ff;
}

.help{
  font-size:12px;
  color:#8996b7;
  line-height:1.55;
  margin-top:10px;
}

.badge{
  display:inline-block;
  padding:5px 8px;
  border-radius:999px;
  background:#1b2947;
  color:#b9c5ff;
  font-size:11px;
}

#message{
  min-height:20px;
  margin-top:9px;
  color:#ffb4b4;
  font-size:12px;
}

.musicBox{
  margin-top:16px;
}

.now{
  font-size:13px;
  color:#aeb9d5;
  min-height:20px;
  margin-bottom:9px;
}

.progress{
  height:8px;
  background:#202b46;
  border-radius:99px;
  overflow:hidden;
}

#bar{
  height:100%;
  width:0;
  background:#8496ff;
  transition:width .05s linear;
}

.layerBox{
  margin-top:14px;
  padding:12px;
  border:1px solid #293756;
  border-radius:12px;
  background:#0d1425;
}

.layerTitle{
  font-size:12px;
  color:#9da9c7;
  margin-bottom:9px;
}

.layers{
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:7px;
}

.layerItem{
  display:flex;
  align-items:center;
  gap:7px;
  font-size:12px;
  color:#cbd4ec;
}

.layerItem input{
  accent-color:#8294ff;
}

.styleInfo{
  margin-top:8px;
  padding:9px;
  border-radius:9px;
  background:#17213a;
  color:#aeb9d5;
  font-size:11px;
  line-height:1.5;
}

@media(max-width:850px){

  .lowerGrid{
    grid-template-columns:1fr;
  }

  canvas{
    height:390px;
  }

  .header{
    align-items:start;
    flex-direction:column;
  }

  .three{
    grid-template-columns:1fr;
  }

  .layers{
    grid-template-columns:1fr;
  }
}
</style>
</head>

<body>

<div id="cosmos">

  <div class="header">

    <div>
      <div class="logo">
        Cos<span>mos</span>
      </div>

      <div class="subtitle">
        Graph → Music · 그래프를 소리로 번역하는 수학 음악 실험실
      </div>
    </div>

    <div class="status">
      <span class="badge">Cosmos v2.0</span>
    </div>

  </div>


  <div class="grid">

    <!-- 그래프 -->
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

        <input
          id="expr"
          value="sin(x)"
          autocomplete="off"
          spellcheck="false"
          aria-label="함수 입력"
        >


        <div class="controls">

          <button class="primary" id="draw">
            그래프 그리기
          </button>

          <button id="resetView">
            화면 초기화
          </button>

          <button id="clear">
            지우기
          </button>

        </div>


        <div class="keypad" id="keypad">

          <button data-v="x">x</button>
          <button data-v="(">(</button>
          <button data-v=")">)</button>
          <button data-v="+">+</button>
          <button data-v="-">−</button>

          <button data-v="7">7</button>
          <button data-v="8">8</button>
          <button data-v="9">9</button>
          <button data-v="*">×</button>
          <button data-v="/">÷</button>

          <button data-v="4">4</button>
          <button data-v="5">5</button>
          <button data-v="6">6</button>
          <button data-v="^">^</button>
          <button data-v=".">.</button>

          <button data-v="1">1</button>
          <button data-v="2">2</button>
          <button data-v="3">3</button>
          <button data-v="pi">π</button>
          <button data-v="0">0</button>

          <button data-v="sin(">sin(</button>
          <button data-v="cos(">cos(</button>
          <button data-v="tan(">tan(</button>
          <button data-v="sqrt(">√(</button>
          <button data-v="abs(">abs(</button>

          <button
            class="backspace"
            id="backspace"
          >
            ⌫ 지우기
          </button>

        </div>

        <div id="message"></div>

      </div>


      <div class="help">

        그래프 영역에서 마우스 휠로 확대/축소할 수 있고,
        드래그로 화면을 이동할 수 있습니다.

        음악 재생 중에는
        <b>그래프의 시작점에서 끝점까지</b>
        재생 위치가 이동합니다.

      </div>

    </section>


    <div class="lowerGrid">

      <!-- 그래프 분석 -->
      <section class="card">

        <h2>③ 그래프 분석</h2>

        <div class="feature">
          <span>정의역</span>
          <span class="value" id="domain">
            −10 ≤ x ≤ 10
          </span>
        </div>

        <div class="feature">
          <span>최솟값</span>
          <span class="value" id="minY">—</span>
        </div>

        <div class="feature">
          <span>최댓값</span>
          <span class="value" id="maxY">—</span>
        </div>

        <div class="feature">
          <span>평균 높이</span>
          <span class="value" id="avgY">—</span>
        </div>

        <div class="feature">
          <span>변화 방향</span>
          <span class="value" id="trend">—</span>
        </div>

      </section>


      <!-- 음악 -->
      <section class="card musicBox">

        <h2>④ Graph → Music</h2>


        <div class="row three">

          <div>

            <label>음계</label>

            <select id="scale">

              <option value="major">
                C Major
              </option>

              <option value="minor">
                A Minor
              </option>

              <option value="pentatonic">
                Pentatonic
              </option>

              <option value="chromatic">
                Chromatic
              </option>

            </select>

          </div>


          <div>

            <label>음악 길이</label>

            <select id="duration">

              <option value="10">
                10초
              </option>

              <option value="20">
                20초
              </option>

              <option value="30">
                30초
              </option>

              <option value="60">
                1분
              </option>

              <option value="120">
                2분
              </option>

              <option value="180">
                3분
              </option>

              <option value="240">
                4분
              </option>

              <option value="300">
                5분
              </option>

            </select>

          </div>


          <div>

            <label>음악 스타일</label>

            <select id="style">

              <option value="lofi">
                Lo-fi
              </option>

              <option value="edm">
                EDM
              </option>

              <option value="jpop">
                J-pop inspired
              </option>

              <option value="kpop">
                K-pop inspired
              </option>

            </select>

          </div>

        </div>


        <div class="styleInfo" id="styleInfo">
          부드러운 코드와 잔잔한 드럼을 사용합니다.
        </div>


        <div class="layerBox">

          <div class="layerTitle">
            음악 레이어
          </div>

          <div class="layers">

            <label class="layerItem">
              <input
                type="checkbox"
                id="layerMelody"
                checked
              >
              그래프 멜로디
            </label>

            <label class="layerItem">
              <input
                type="checkbox"
                id="layerDrum"
                checked
              >
              드럼
            </label>

            <label class="layerItem">
              <input
                type="checkbox"
                id="layerBass"
                checked
              >
              베이스
            </label>

            <label class="layerItem">
              <input
                type="checkbox"
                id="layerChord"
                checked
              >
              코드
            </label>

            <label class="layerItem">
              <input
                type="checkbox"
                id="layerArp"
              >
              아르페지오
            </label>

            <label class="layerItem">
              <input
                type="checkbox"
                id="layerPad"
              >
              패드
            </label>

            <label class="layerItem">
              <input
                type="checkbox"
                id="layerPerc"
              >
              퍼커션
            </label>

            <label class="layerItem">
              <input
                type="checkbox"
                id="layerTexture"
              >
              텍스처
            </label>

          </div>

        </div>


        <div class="controls">

          <button
            class="primary"
            id="play"
          >
            ▶ 그래프로 음악 만들기
          </button>

          <button id="stop">
            ■ 정지
          </button>

        </div>


        <div class="now" id="now">
          그래프의 y값이 음높이로 변환됩니다.
        </div>

        <div class="progress">
          <div id="bar"></div>
        </div>


        <div class="help">

          <b>변환 원리</b><br>

          x축 → 음악의 시간<br>
          y값 → 음높이<br>
          그래프의 상승 → pitch 상승<br>
          그래프의 하강 → pitch 하강<br>
          그래프 전체 → 음악 전체

        </div>

      </section>

    </div>

  </div>


  <section class="card musicBox">

    <h2>Cosmos의 핵심</h2>

    <div class="help">

      같은 수식이라도 그래프의 형태가 달라지면
      다른 음악적 흐름이 만들어집니다.

      <br><br>

      <b>
        그래프의 x축을 음악의 시간,
        y축을 음높이로 대응시켜
        함수의 전체 구조를 하나의 선율로 변환합니다.
      </b>

    </div>

  </section>


<script>

(function(){

"use strict";


/* =========================================
   기본 요소
========================================= */

const canvas=document.getElementById("graph");
const ctx=canvas.getContext("2d");

const expr=document.getElementById("expr");
const msg=document.getElementById("message");


/* =========================================
   그래프 상태
========================================= */

let xmin=-10;
let xmax=10;

let ymin=-6;
let ymax=6;

let dragging=false;
let lastX=0;
let lastY=0;

let samples=[];


/* =========================================
   오디오 상태
========================================= */

let audioCtx=null;

let activeNodes=[];

let playing=false;

let raf=null;

let playbackPoint=null;

let playbackStart=0;

let playbackDuration=10;


/* =========================================
   함수 목록
========================================= */

const funcs={

  sin:Math.sin,
  cos:Math.cos,
  tan:Math.tan,

  sqrt:Math.sqrt,
  abs:Math.abs,

  log:Math.log,
  exp:Math.exp,

  asin:Math.asin,
  acos:Math.acos,
  atan:Math.atan

};


/* =========================================
   수식 토큰화
========================================= */

function tokenize(s){

  s=s
    .replace(/π/g,"pi")
    .replace(/√/g,"sqrt");

  const tokens=[];

  let i=0;

  while(i<s.length){

    if(/\s/.test(s[i])){
      i++;
      continue;
    }


    if(/[0-9.]/.test(s[i])){

      let j=i+1;

      while(
        j<s.length &&
        /[0-9.]/.test(s[j])
      ){
        j++;
      }

      const n=Number(
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
        v:s.slice(i,j).toLowerCase()
      });

      i++;
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
      "지원하지 않는 문자가 있습니다: "+s[i]
    );
  }

  return tokens;
}


/* =========================================
   수식 파서
========================================= */

function parseExpression(s){

  const ts=tokenize(s);

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
            z.v+" 뒤에 괄호가 필요합니다."
          );
        }

        p++;

        const a=addsub();


        if(
          !ts[p] ||
          ts[p].t!==")"
        ){
          throw Error(
            "괄호를 닫아주세요."
          );
        }

        p++;


        return x=>funcs[z.v](a(x));
      }


      throw Error(
        "알 수 없는 함수/변수: "+z.v
      );
    }


    if(z.t==="("){

      p++;

      const a=addsub();


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

      const a=primary();

      return x=>-a(x);
    }


    throw Error(
      "수식을 확인하세요."
    );
  }


  function power(){

    let a=primary();


    if(
      ts[p] &&
      ts[p].t==="^"
    ){

      p++;

      const b=power();

      const aa=a;

      return x=>
        Math.pow(
          aa(x),
          b(x)
        );
    }


    return a;
  }


  function muldiv(){

    let a=power();


    while(
      ts[p] &&
      (
        ts[p].t==="*" ||
        ts[p].t==="/"
      )
    ){

      const op=ts[p++].t;

      const b=power();

      const aa=a;


      a=
        op==="*"
        ? x=>aa(x)*b(x)
        : x=>aa(x)/b(x);
    }


    return a;
  }


  function addsub(){

    let a=muldiv();


    while(
      ts[p] &&
      (
        ts[p].t==="+" ||
        ts[p].t==="-"
      )
    ){

      const op=ts[p++].t;

      const b=muldiv();

      const aa=a;


      a=
        op==="+"
        ? x=>aa(x)+b(x)
        : x=>aa(x)-b(x);
    }


    return a;
  }


  const f=addsub();


  if(p!==ts.length){

    throw Error(
      "수식을 확인하세요."
    );
  }


  return f;
}


/* =========================================
   그래프 좌표
========================================= */

function resize(){

  const r=
    canvas.getBoundingClientRect();

  const d=
    window.devicePixelRatio || 1;

  canvas.width=
    Math.max(
      500,
      Math.floor(r.width*d)
    );

  canvas.height=
    Math.max(
      350,
      Math.floor(r.height*d)
    );

  ctx.setTransform(
    d,0,0,d,0,0
  );

  draw();
}


function W(){
  return canvas.getBoundingClientRect().width;
}


function H(){
  return canvas.getBoundingClientRect().height;
}


function sx(x){

  return (
    (x-xmin)/
    (xmax-xmin)
  )*W();
}


function sy(y){

  return H()-
    (
      (y-ymin)/
      (ymax-ymin)
    )*H();
}


function invx(px){

  return xmin+
    px/W()*
    (xmax-xmin);
}


function invy(py){

  return ymin+
    (H()-py)/H()*
    (ymax-ymin);
}


/* =========================================
   눈금
========================================= */

function niceStep(range){

  const raw=range/10;

  const p=
    Math.pow(
      10,
      Math.floor(
        Math.log10(raw)
      )
    );

  const n=raw/p;


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


/* =========================================
   그래프 그리기
========================================= */

function draw(){

  const w=W();
  const h=H();


  ctx.clearRect(
    0,
    0,
    w,
    h
  );


  ctx.fillStyle="#080d19";

  ctx.fillRect(
    0,
    0,
    w,
    h
  );


  const xs=
    niceStep(xmax-xmin);

  const ys=
    niceStep(ymax-ymin);


  ctx.lineWidth=1;

  ctx.strokeStyle="#18243d";

  ctx.fillStyle="#64718e";

  ctx.font="11px system-ui";


  for(
    let x=
      Math.ceil(xmin/xs)*xs;

    x<=xmax;

    x+=xs
  ){

    const px=sx(x);

    ctx.beginPath();

    ctx.moveTo(px,0);

    ctx.lineTo(px,h);

    ctx.stroke();


    if(Math.abs(x)>1e-9){

      ctx.fillText(
        fmt(x),
        px+4,
        h-7
      );
    }
  }


  for(
    let y=
      Math.ceil(ymin/ys)*ys;

    y<=ymax;

    y+=ys
  ){

    const py=sy(y);

    ctx.beginPath();

    ctx.moveTo(0,py);

    ctx.lineTo(w,py);

    ctx.stroke();


    if(Math.abs(y)>1e-9){

      ctx.fillText(
        fmt(y),
        6,
        py-4
      );
    }
  }


  ctx.strokeStyle="#596783";

  ctx.lineWidth=1.4;


  const originX=
    xmin<=0 &&
    xmax>=0
    ? sx(0)
    : null;


  const originY=
    ymin<=0 &&
    ymax>=0
    ? sy(0)
    : null;


  if(originX!==null){

    ctx.beginPath();

    ctx.moveTo(
      originX,
      0
    );

    ctx.lineTo(
      originX,
      h
    );

    ctx.stroke();
  }


  if(originY!==null){

    ctx.beginPath();

    ctx.moveTo(
      0,
      originY
    );

    ctx.lineTo(
      w,
      originY
    );

    ctx.stroke();
  }


  if(
    originX!==null &&
    originY!==null
  ){

    ctx.save();

    ctx.fillStyle="#ffffff";

    ctx.beginPath();

    ctx.arc(
      originX,
      originY,
      4,
      0,
      Math.PI*2
    );

    ctx.fill();

    ctx.fillStyle="#aeb9d5";

    ctx.font=
      "bold 12px system-ui";

    ctx.fillText(
      "O (0, 0)",
      originX+8,
      originY-9
    );

    ctx.restore();
  }


  let f;


  try{

    f=parseExpression(
      expr.value
    );

  }catch(e){

    msg.textContent=e.message;

    return;
  }


  msg.textContent="";

  samples=[];


  let lastValid=null;

  const N=
    Math.min(
      1800,
      Math.max(
        700,
        Math.floor(w*1.5)
      )
    );


  ctx.beginPath();

  let started=false;

  let min=Infinity;
  let max=-Infinity;
  let sum=0;
  let count=0;


  for(
    let i=0;
    i<=N;
    i++
  ){

    const x=
      xmin+
      (xmax-xmin)*i/N;


    let y;

    try{
      y=f(x);
    }catch(e){
      y=NaN;
    }


    const valid=
      Number.isFinite(y) &&
      Math.abs(y)<1e8;


    samples.push({
      x,
      y
    });


    if(valid){

      min=
        Math.min(
          min,
          y
        );

      max=
        Math.max(
          max,
          y
        );

      sum+=y;

      count++;
    }


    if(
      !valid ||
      Math.abs(y)>
      Math.max(
        1e4,
        (ymax-ymin)*100
      )
    ){

      started=false;

      lastValid=null;

      continue;
    }


    const px=sx(x);
    const py=sy(y);


    if(
      !started ||
      (
        lastValid!==null &&
        Math.abs(py-lastValid)>h*2
      )
    ){

      ctx.moveTo(
        px,
        py
      );

      started=true;

    }else{

      ctx.lineTo(
        px,
        py
      );
    }


    lastValid=py;
  }


  ctx.strokeStyle="#91a4ff";

  ctx.lineWidth=3;

  ctx.lineJoin="round";

  ctx.stroke();


  /* 음악 재생 위치 */

  if(
    playbackPoint &&
    Number.isFinite(playbackPoint.x) &&
    Number.isFinite(playbackPoint.y)
  ){

    const px=sx(
      playbackPoint.x
    );

    const py=sy(
      playbackPoint.y
    );


    if(
      px>=-12 &&
      px<=w+12 &&
      py>=-12 &&
      py<=h+12
    ){

      ctx.save();


      ctx.beginPath();

      ctx.arc(
        px,
        py,
        15,
        0,
        Math.PI*2
      );

      ctx.fillStyle=
        "rgba(255,207,92,.18)";

      ctx.fill();


      ctx.beginPath();

      ctx.arc(
        px,
        py,
        8,
        0,
        Math.PI*2
      );

      ctx.fillStyle="#ffffff";

      ctx.fill();


      ctx.beginPath();

      ctx.arc(
        px,
        py,
        5,
        0,
        Math.PI*2
      );

      ctx.fillStyle="#ffcf5c";

      ctx.fill();


      ctx.restore();
    }
  }


  document.getElementById(
    "domain"
  ).textContent=
    fmt(xmin)+
    " ≤ x ≤ "+
    fmt(xmax);


  document.getElementById(
    "minY"
  ).textContent=
    count
    ? fmt(min)
    : "—";


  document.getElementById(
    "maxY"
  ).textContent=
    count
    ? fmt(max)
    : "—";


  document.getElementById(
    "avgY"
  ).textContent=
    count
    ? fmt(sum/count)
    : "—";


  if(count){

    let left=0;
    let right=0;
    let n=0;


    for(
      let i=1;
      i<samples.length;
      i++
    ){

      if(
        Number.isFinite(
          samples[i-1].y
        ) &&
        Number.isFinite(
          samples[i].y
        )
      ){

        const d=
          samples[i].y-
          samples[i-1].y;


        if(d>0)
          right++;

        else if(d<0)
          left++;

        n++;
      }
    }


    document.getElementById(
      "trend"
    ).textContent=
      n
      ? (
        right>left*1.25
        ? "주로 증가"
        : left>right*1.25
        ? "주로 감소"
        : "상승·하강 반복"
      )
      : "—";
  }
}


/* =========================================
   숫자 표시
========================================= */

function fmt(v){

  if(!Number.isFinite(v))
    return "—";


  if(Math.abs(v)<1e-9)
    return "0";


  if(Math.abs(v)>=100)
    return Math.round(v).toString();


  return Number(
    v.toFixed(2)
  ).toString();
}


/* =========================================
   화면 이동 / 확대
========================================= */

function changeView(
  factor,
  dx=0,
  dy=0
){

  const cx=
    (xmin+xmax)/2+
    (dx*(xmax-xmin));


  const cy=
    (ymin+ymax)/2+
    (dy*(ymax-ymin));


  const xr=
    (xmax-xmin)*factor;

  const yr=
    (ymax-ymin)*factor;


  xmin=cx-xr/2;
  xmax=cx+xr/2;

  ymin=cy-yr/2;
  ymax=cy+yr/2;


  draw();
}


/* =========================================
   버튼
========================================= */

document
  .getElementById("draw")
  .addEventListener(
    "click",
    draw
  );


expr.addEventListener(
  "keydown",
  e=>{
    if(e.key==="Enter")
      draw();
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

      draw();
    }
  );


document
  .getElementById("clear")
  .addEventListener(
    "click",
    ()=>{
      expr.value="";
      draw();
    }
  );


document
  .getElementById("zoomIn")
  .addEventListener(
    "click",
    ()=>changeView(.75)
  );


document
  .getElementById("zoomOut")
  .addEventListener(
    "click",
    ()=>changeView(1.35)
  );


document
  .getElementById("left")
  .addEventListener(
    "click",
    ()=>changeView(1,-.12,0)
  );


document
  .getElementById("right")
  .addEventListener(
    "click",
    ()=>changeView(1,.12,0)
  );


document
  .getElementById("up")
  .addEventListener(
    "click",
    ()=>changeView(1,0,.12)
  );


document
  .getElementById("down")
  .addEventListener(
    "click",
    ()=>changeView(1,0,-.12)
  );


/* =========================================
   수식 키패드
========================================= */

document
  .querySelectorAll(
    "#keypad button[data-v]"
  )
  .forEach(
    b=>{

      b.addEventListener(
        "click",
        ()=>{

          const v=
            b.dataset.v;


          const start=
            expr.selectionStart ??
            expr.value.length;


          const end=
            expr.selectionEnd ??
            expr.value.length;


          expr.value=
            expr.value.slice(
              0,
              start
            )+
            v+
            expr.value.slice(
              end
            );


          expr.focus();


          const pos=
            start+v.length;


          expr.setSelectionRange(
            pos,
            pos
          );


          draw();
        }
      );
    }
  );


document
  .getElementById("backspace")
  .addEventListener(
    "click",
    ()=>{

      const start=
        expr.selectionStart ??
        expr.value.length;


      const end=
        expr.selectionEnd ??
        expr.value.length;


      if(start!==end){

        expr.value=
          expr.value.slice(
            0,
            start
          )+
          expr.value.slice(
            end
          );


        expr.setSelectionRange(
          start,
          start
        );

      }else if(start>0){

        expr.value=
          expr.value.slice(
            0,
            start-1
          )+
          expr.value.slice(
            start
          );


        expr.setSelectionRange(
          start-1,
          start-1
        );
      }


      expr.focus();

      draw();
    }
  );


/* =========================================
   그래프 마우스 조작
========================================= */

canvas.addEventListener(
  "wheel",
  e=>{

    e.preventDefault();


    const factor=
      e.deltaY<0
      ? .8
      : 1.25;


    const mx=
      invx(e.offsetX);

    const my=
      invy(e.offsetY);


    xmin=
      mx+
      (xmin-mx)*factor;


    xmax=
      mx+
      (xmax-mx)*factor;


    ymin=
      my+
      (ymin-my)*factor;


    ymax=
      my+
      (ymax-my)*factor;


    draw();

  },
  {
    passive:false
  }
);


canvas.addEventListener(
  "pointerdown",
  e=>{

    dragging=true;

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

    if(!dragging)
      return;


    const dx=
      e.clientX-lastX;

    const dy=
      e.clientY-lastY;


    const xr=
      xmax-xmin;

    const yr=
      ymax-ymin;


    xmin-=
      dx/W()*xr;

    xmax-=
      dx/W()*xr;


    ymin+=
      dy/H()*yr;

    ymax+=
      dy/H()*yr;


    lastX=e.clientX;
    lastY=e.clientY;


    draw();
  }
);


canvas.addEventListener(
  "pointerup",
  ()=>{
    dragging=false;
  }
);


canvas.addEventListener(
  "pointercancel",
  ()=>{
    dragging=false;
  }
);


/* =========================================
   음계
========================================= */

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


/* =========================================
   스타일 설명
========================================= */

const styleInfo={

  lofi:
    "부드러운 코드와 잔잔한 드럼을 사용합니다.",

  edm:
    "강한 킥과 반복적인 저음으로 에너지 있는 구조를 만듭니다.",

  jpop:
    "밝은 코드와 빠른 아르페지오 느낌을 사용합니다.",

  kpop:
    "명확한 저음과 박자감 있는 반주를 사용합니다."

};


document
  .getElementById("style")
  .addEventListener(
    "change",
    ()=>{
      document.getElementById(
        "styleInfo"
      ).textContent=
        styleInfo[
          document.getElementById(
            "style"
          ).value
        ];
    }
  );


/* =========================================
   그래프 → 음악 데이터
========================================= */

function makeMusicPoints(){

  const valid=
    samples.filter(
      p=>
        Number.isFinite(p.x) &&
        Number.isFinite(p.y)
    );


  if(valid.length<10){

    throw Error(
      "음악으로 변환할 수 있는 그래프가 없습니다."
    );
  }


  /*
    그래프 전체를 음악 전체에 대응시키기 위해
    일정 개수의 점으로 다시 샘플링한다.
  */

  const count=
    Math.min(
      320,
      Math.max(
        120,
        Math.floor(
          valid.length*0.32
        )
      )
    );


  const points=[];


  for(
    let i=0;
    i<count;
    i++
  ){

    const ratio=
      count===1
      ? 0
      : i/(count-1);


    const index=
      Math.round(
        ratio*
        (valid.length-1)
      );


    points.push(
      valid[index]
    );
  }


  const vals=
    points.map(
      p=>p.y
    );


  let lo=
    Math.min(...vals);

  let hi=
    Math.max(...vals);


  if(
    Math.abs(hi-lo)<1e-8
  ){

    lo-=1;
    hi+=1;
  }


  return {
    points,
    lo,
    hi
  };
}


/* =========================================
   y값 → 연속적인 주파수
========================================= */

function graphYToFrequency(
  y,
  lo,
  hi
){

  const norm=
    Math.max(
      0,
      Math.min(
        1,
        (y-lo)/(hi-lo)
      )
    );


  /*
    그래프 높이를 MIDI 48~84 정도로 변환한다.
    여기서는 음계를 억지로 선택하지 않고
    그래프의 높이에 따라 연속적인 주파수를 만든다.
  */

  const midi=
    48+
    norm*36;


  return {
    midi,
    frequency:
      440*
      Math.pow(
        2,
        (midi-69)/12
      )
  };
}


/* =========================================
   오디오 노드 관리
========================================= */

function rememberNode(node){

  activeNodes.push(node);

}


function stopAllNodes(){

  activeNodes.forEach(
    node=>{
      try{
        node.stop();
      }catch(e){}

      try{
        node.disconnect();
      }catch(e){}
    }
  );


  activeNodes=[];
}


/* =========================================
   그래프 멜로디 생성
========================================= */

function createGraphMelody(
  data,
  start,
  duration
){

  const osc=
    audioCtx.createOscillator();

  const gain=
    audioCtx.createGain();


  osc.type="sine";


  const points=
    data.points;


  const segment=
    duration/
    points.length;


  const first=
    graphYToFrequency(
      points[0].y,
      data.lo,
      data.hi
    );


  osc.frequency.setValueAtTime(
    first.frequency,
    start
  );


  gain.gain.setValueAtTime(
    0,
    start
  );


  gain.gain.linearRampToValueAtTime(
    0.16,
    start+0.08
  );


  /*
    그래프의 모든 점을
    곡 전체 시간에 배치한다.

    따라서 10초든 5분이든
    그래프 전체가 정확히 한 번 지나간다.
  */

  for(
    let i=0;
    i<points.length;
    i++
  ){

    const current=
      graphYToFrequency(
        points[i].y,
        data.lo,
        data.hi
      );


    const next=
      graphYToFrequency(
        points[
          Math.min(
            points.length-1,
            i+1
          )
        ].y,
        data.lo,
        data.hi
      );


    const time=
      start+
      i*segment;


    osc.frequency.linearRampToValueAtTime(
      current.frequency,
      time
    );


    osc.frequency.linearRampToValueAtTime(
      next.frequency,
      Math.min(
        start+duration,
        time+segment
      )
    );
  }


  gain.gain.setValueAtTime(
    0.16,
    start+duration-0.15
  );


  gain.gain.linearRampToValueAtTime(
    0,
    start+duration
  );


  osc.connect(gain);

  gain.connect(
    audioCtx.destination
  );


  osc.start(start);

  osc.stop(
    start+duration+0.05
  );


  rememberNode(osc);

  return {
    osc,
    gain
  };
}


/* =========================================
   간단한 음 생성 함수
========================================= */

function note(
  frequency,
  start,
  duration,
  volume,
  type="sine"
){

  const osc=
    audioCtx.createOscillator();

  const gain=
    audioCtx.createGain();


  osc.type=type;

  osc.frequency.setValueAtTime(
    frequency,
    start
  );


  gain.gain.setValueAtTime(
    0,
    start
  );


  gain.gain.linearRampToValueAtTime(
    volume,
    start+0.015
  );


  gain.gain.exponentialRampToValueAtTime(
    0.001,
    start+duration
  );


  osc.connect(gain);

  gain.connect(
    audioCtx.destination
  );


  osc.start(start);

  osc.stop(
    start+duration+0.02
  );


  rememberNode(osc);
}


/* =========================================
   드럼
========================================= */

function createDrums(
  start,
  duration,
  style
){

  let interval;


  if(style==="edm")
    interval=0.45;

  else if(style==="kpop")
    interval=0.5;

  else if(style==="jpop")
    interval=0.4;

  else
    interval=0.65;


  for(
    let t=0;
    t<duration;
    t+=interval
  ){

    const time=
      start+t;


    const osc=
      audioCtx.createOscillator();

    const gain=
      audioCtx.createGain();


    osc.type="sine";

    osc.frequency.setValueAtTime(
      100,
      time
    );


    gain.gain.setValueAtTime(
      0.18,
      time
    );


    gain.gain.exponentialRampToValueAtTime(
      0.001,
      time+0.12
    );


    osc.connect(gain);

    gain.connect(
      audioCtx.destination
    );


    osc.start(time);

    osc.stop(
      time+0.13
    );


    rememberNode(osc);
  }
}


/* =========================================
   베이스
========================================= */

function createBass(
  data,
  start,
  duration
){

  const count=32;

  const segment=
    duration/count;


  for(
    let i=0;
    i<count;
    i++
  ){

    const index=
      Math.floor(
        i/count*
        (data.points.length-1)
      );


    const y=
      data.points[index].y;


    const p=
      graphYToFrequency(
        y,
        data.lo,
        data.hi
      );


    const freq=
      p.frequency/4;


    note(
      freq,
      start+i*segment,
      segment*0.8,
      0.08,
      "triangle"
    );
  }
}


/* =========================================
   코드
========================================= */

function createChords(
  start,
  duration,
  style
){

  const chordRoots=[
    130.81,
    146.83,
    164.81,
    174.61
  ];


  const interval=
    style==="edm"
    ? 2
    : 4;


  for(
    let t=0;
    t<duration;
    t+=interval
  ){

    const root=
      chordRoots[
        Math.floor(
          t/interval
        )%
        chordRoots.length
      ];


    note(
      root,
      start+t,
      interval*0.9,
      0.035,
      "sine"
    );


    note(
      root*1.25,
      start+t,
      interval*0.9,
      0.025,
      "sine"
    );


    note(
      root*1.5,
      start+t,
      interval*0.9,
      0.02,
      "sine"
    );
  }
}


/* =========================================
   아르페지오
========================================= */

function createArpeggio(
  data,
  start,
  duration
){

  const segment=0.22;

  const count=
    Math.floor(
      duration/segment
    );


  for(
    let i=0;
    i<count;
    i++
  ){

    const ratio=
      i/Math.max(
        1,
        count-1
      );


    const index=
      Math.floor(
        ratio*
        (data.points.length-1)
      );


    const p=
      graphYToFrequency(
        data.points[index].y,
        data.lo,
        data.hi
      );


    note(
      p.frequency*2,
      start+i*segment,
      segment*0.75,
      0.025,
      "sine"
    );
  }
}


/* =========================================
   패드
========================================= */

function createPad(
  start,
  duration
){

  const frequencies=[
    130.81,
    164.81,
    196.00
  ];


  frequencies.forEach(
    frequency=>{

      const osc=
        audioCtx.createOscillator();

      const gain=
        audioCtx.createGain();


      osc.type="sine";

      osc.frequency.value=
        frequency;


      gain.gain.setValueAtTime(
        0,
        start
      );


      gain.gain.linearRampToValueAtTime(
        0.025,
        start+1
      );


      gain.gain.setValueAtTime(
        0.025,
        start+duration-1
      );


      gain.gain.linearRampToValueAtTime(
        0,
        start+duration
      );


      osc.connect(gain);

      gain.connect(
        audioCtx.destination
      );


      osc.start(start);

      osc.stop(
        start+duration
      );


      rememberNode(osc);
    }
  );
}


/* =========================================
   퍼커션
========================================= */

function createPercussion(
  start,
  duration
){

  for(
    let t=0;
    t<duration;
    t+=1.5
  ){

    note(
      800,
      start+t,
      0.05,
      0.018,
      "square"
    );
  }
}


/* =========================================
   텍스처
========================================= */

function createTexture(
  start,
  duration
){

  const osc=
    audioCtx.createOscillator();

  const gain=
    audioCtx.createGain();


  osc.type="sawtooth";

  osc.frequency.value=
    55;


  gain.gain.setValueAtTime(
    0.01,
    start
  );


  gain.gain.linearRampToValueAtTime(
    0.025,
    start+duration/2
  );


  gain.gain.linearRampToValueAtTime(
    0,
    start+duration
  );


  osc.connect(gain);

  gain.connect(
    audioCtx.destination
  );


  osc.start(start);

  osc.stop(
    start+duration
  );


  rememberNode(osc);
}


/* =========================================
   음악 재생
========================================= */

async function playMusic(){

  stopMusic();


  let data;


  try{

    data=
      makeMusicPoints();

  }catch(e){

    msg.textContent=
      e.message;

    return;
  }


  if(!audioCtx){

    audioCtx=
      new (
        window.AudioContext ||
        window.webkitAudioContext
      )();
  }


  if(
    audioCtx.state==="suspended"
  ){

    await audioCtx.resume();
  }


  const duration=
    Number(
      document.getElementById(
        "duration"
      ).value
    );


  const style=
    document.getElementById(
      "style"
    ).value;


  playbackDuration=
    duration;


  const start=
    audioCtx.currentTime+
    0.08;


  playing=true;

  playbackStart=
    performance.now();


  /*
    선택한 레이어에 따라
    서로 다른 소리를 쌓는다.
  */


  if(
    document.getElementById(
      "layerMelody"
    ).checked
  ){

    createGraphMelody(
      data,
      start,
      duration
    );
  }


  if(
    document.getElementById(
      "layerDrum"
    ).checked
  ){

    createDrums(
      start,
      duration,
      style
    );
  }


  if(
    document.getElementById(
      "layerBass"
    ).checked
  ){

    createBass(
      data,
      start,
      duration
    );
  }


  if(
    document.getElementById(
      "layerChord"
    ).checked
  ){

    createChords(
      start,
      duration,
      style
    );
  }


  if(
    document.getElementById(
      "layerArp"
    ).checked
  ){

    createArpeggio(
      data,
      start,
      duration
    );
  }


  if(
    document.getElementById(
      "layerPad"
    ).checked
  ){

    createPad(
      start,
      duration
    );
  }


  if(
    document.getElementById(
      "layerPerc"
    ).checked
  ){

    createPercussion(
      start,
      duration
    );
  }


  if(
    document.getElementById(
      "layerTexture"
    ).checked
  ){

    createTexture(
      start,
      duration
    );
  }


  function tick(){

    if(!playing)
      return;


    const elapsed=
      performance.now()-
      playbackStart;


    const pct=
      Math.max(
        0,
        Math.min(
          1,
          elapsed/
          1000/
          duration
        )
      );


    /*
      음악의 진행률을
      그래프의 진행률과
      정확히 동일하게 사용한다.
    */

    const index=
      Math.min(
        data.points.length-1,
        Math.floor(
          pct*
          (data.points.length-1)
        )
      );


    playbackPoint=
      data.points[index];


    const pitch=
      graphYToFrequency(
        playbackPoint.y,
        data.lo,
        data.hi
      );


    document.getElementById(
      "now"
    ).textContent=
      "♪ 그래프 진행 "+
      Math.round(pct*100)+
      "% · y = "+
      fmt(playbackPoint.y)+
      " · MIDI "+
      pitch.midi.toFixed(1);


    document.getElementById(
      "bar"
    ).style.width=
      (pct*100)+"%";


    draw();


    if(pct<1){

      raf=
        requestAnimationFrame(
          tick
        );

    }else{

      playing=false;

      playbackPoint=null;

      draw();


      document.getElementById(
        "now"
      ).textContent=
        "재생 완료 · 그래프 전체가 음악으로 변환되었습니다.";


      document.getElementById(
        "bar"
      ).style.width="100%";


      raf=null;
    }
  }


  raf=
    requestAnimationFrame(
      tick
    );
}


/* =========================================
   음악 정지
========================================= */

function stopMusic(){

  playing=false;


  if(raf)
    cancelAnimationFrame(
      raf
    );


  raf=null;


  stopAllNodes();


  playbackPoint=null;


  draw();


  document.getElementById(
    "bar"
  ).style.width="0%";


  document.getElementById(
    "now"
  ).textContent=
    "정지됨";
}


/* =========================================
   음악 버튼
========================================= */

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


/* =========================================
   시작
========================================= */

window.addEventListener(
  "resize",
  resize
);


resize();

})();
</script>

</body>
</html>
"""


st.markdown(
    """
    <style>

    [data-testid="stAppViewContainer"]{
        background:#0b1020;
    }

    [data-testid="stHeader"]{
        background:transparent;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


components.html(
    HTML,
    height=1350,
    scrolling=True
)
