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
    font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,
    "Segoe UI",sans-serif;
    background:#0b1020;
    color:#edf2ff;
}

#cosmos{
    max-width:1250px;
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

.badge{
    display:inline-block;
    padding:5px 9px;
    border-radius:999px;
    background:#1b2947;
    color:#b9c5ff;
    font-size:11px;
}

.grid{
    display:grid;
    grid-template-columns:minmax(0,1fr) 360px;
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
    height:560px;
    background:#080d19;
    border-radius:13px;
    display:block;
    touch-action:none;
}

.controls{
    display:flex;
    gap:8px;
    flex-wrap:wrap;
    margin-top:10px;
}

button,
input,
select{
    font:inherit;
}

button{
    border:1px solid #344365;
    background:#18233d;
    color:#eef2ff;
    border-radius:10px;
    padding:9px 12px;
    cursor:pointer;
    min-height:40px;
}

button:hover{
    background:#202e4d;
}

button.active{
    background:#6478e8;
    border-color:#6478e8;
    color:white;
}

button.primary{
    background:#6478e8;
    border-color:#6478e8;
    font-weight:700;
}

button.danger{
    background:#321c27;
    border-color:#633344;
}

input[type=text]{
    width:100%;
    padding:12px;
    border-radius:10px;
    border:1px solid #33436c;
    background:#0b1122;
    color:#fff;
    outline:none;
}

input[type=text]:focus{
    border-color:#8da2ff;
}

select{
    width:100%;
    padding:10px;
    border-radius:9px;
    border:1px solid #33436c;
    background:#0b1122;
    color:#fff;
}

label{
    display:block;
    font-size:12px;
    color:#9da9c7;
    margin-bottom:6px;
}

.section{
    margin-top:16px;
}

.modeBar{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:7px;
}

.modeBar button{
    width:100%;
}

.layerList{
    display:flex;
    flex-direction:column;
    gap:8px;
}

.layerItem{
    border:1px solid #2b3858;
    border-radius:12px;
    padding:10px;
    background:#0e1629;
    cursor:pointer;
}

.layerItem.selected{
    border-color:#7184ee;
    box-shadow:0 0 0 1px #7184ee inset;
}

.layerTop{
    display:flex;
    align-items:center;
    gap:8px;
}

.layerColor{
    width:11px;
    height:11px;
    border-radius:50%;
    flex:none;
}

.layerName{
    flex:1;
    font-size:13px;
    font-weight:700;
}

.layerType{
    font-size:10px;
    color:#7e8baa;
}

.layerActions{
    display:flex;
    align-items:center;
    gap:6px;
    margin-top:8px;
}

.layerActions button{
    min-height:30px;
    padding:5px 8px;
    font-size:11px;
}

.visibility{
    font-size:12px;
    color:#aeb9d5;
}

.layerVolume{
    width:100%;
    accent-color:#8496ff;
}

.small{
    font-size:11px;
    color:#7886a8;
    line-height:1.55;
}

.help{
    font-size:12px;
    color:#8996b7;
    line-height:1.6;
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

.info{
    padding:10px;
    border-radius:10px;
    background:#0d1527;
    border:1px solid #253453;
    font-size:12px;
    color:#aeb9d5;
}

#message{
    min-height:20px;
    margin-top:8px;
    color:#ffb4b4;
    font-size:12px;
}

.musicBox{
    margin-top:16px;
}

.now{
    font-size:13px;
    color:#aeb9d5;
    min-height:22px;
    margin:9px 0;
}

.progress{
    height:7px;
    background:#202b46;
    border-radius:99px;
    overflow:hidden;
}

#bar{
    height:100%;
    width:0;
    background:#8496ff;
}

.layerCount{
    font-size:11px;
    color:#8996b7;
    margin-top:6px;
}

.transformGrid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
}

.transformGrid button{
    width:100%;
}

hr{
    border:0;
    border-top:1px solid #24314e;
    margin:15px 0;
}

@media(max-width:950px){
    .grid{
        grid-template-columns:1fr;
    }

    canvas{
        height:460px;
    }
}

@media(max-width:600px){
    #cosmos{
        padding:10px;
    }

    canvas{
        height:390px;
    }

    .row,
    .row3{
        grid-template-columns:1fr;
    }
}
</style>
</head>

<body>

<div id="cosmos">

    <div class="header">
        <div>
            <div class="logo">Cos<span>mos</span></div>
            <div class="subtitle">
                Graph → Music · 여러 그래프를 겹쳐 하나의 음악으로 번역하는 수학 음악 실험실
            </div>
        </div>

        <div>
            <span class="badge">Cosmos v2.0</span>
        </div>
    </div>


    <div class="grid">

        <!-- ================= GRAPH ================= -->

        <section class="card">

            <h2>① Graph Canvas</h2>

            <div class="graphWrap">
                <canvas id="graph" width="1200" height="650"></canvas>
            </div>

            <div class="controls">

                <button id="zoomIn">＋ 확대</button>
                <button id="zoomOut">－ 축소</button>

                <button id="left">← 이동</button>
                <button id="right">→ 이동</button>
                <button id="up">↑ 이동</button>
                <button id="down">↓ 이동</button>

                <button id="resetView">화면 초기화</button>

            </div>


            <!-- MODE -->

            <div class="section">

                <h2>② 작업 모드</h2>

                <div class="modeBar">

                    <button id="navigateMode" class="active">
                        이동
                    </button>

                    <button id="sketchMode">
                        손그림
                    </button>

                    <button id="editMode">
                        Edit
                    </button>

                </div>

                <div class="help" style="margin-top:8px">

                    <b>이동</b> : 그래프 화면 이동<br>
                    <b>손그림</b> : 선택된 레이어에 직접 곡선 그리기<br>
                    <b>Edit</b> : 선택된 그래프 이동·확대·축소·회전

                </div>

            </div>


            <!-- FUNCTION -->

            <div class="section">

                <h2>③ 선택된 레이어에 함수 입력</h2>

                <input
                    id="expr"
                    type="text"
                    value="sin(x)"
                    autocomplete="off"
                    spellcheck="false"
                >

                <div class="controls">

                    <button id="draw" class="primary">
                        함수 그래프 생성
                    </button>

                    <button id="clearLayer">
                        선택 레이어 지우기
                    </button>

                </div>

                <div id="message"></div>

            </div>


            <!-- EDIT -->

            <div class="section">

                <h2>④ Edit</h2>

                <div class="transformGrid">

                    <button id="scaleUp">
                        🔍 확대
                    </button>

                    <button id="scaleDown">
                        🔎 축소
                    </button>

                    <button id="rotateLeft">
                        ↶ 15°
                    </button>

                    <button id="rotateRight">
                        ↷ 15°
                    </button>

                    <button id="resetTransform">
                        변환 초기화
                    </button>

                    <button id="centerLayer">
                        가운데 정렬
                    </button>

                </div>

                <div class="help" style="margin-top:8px">
                    Edit 모드에서 그래프를 드래그하면 이동합니다.
                    마우스 휠을 움직이면 확대·축소됩니다.
                    회전 버튼으로 그래프를 회전할 수 있습니다.
                </div>

            </div>


            <!-- ANALYSIS -->

            <div class="section">

                <h2>⑤ 그래프 분석</h2>

                <div class="info">
                    <div>정의역 : <span id="domain">—</span></div>
                    <div>최솟값 : <span id="minY">—</span></div>
                    <div>최댓값 : <span id="maxY">—</span></div>
                    <div>평균 높이 : <span id="avgY">—</span></div>
                    <div>레이어 : <span id="selectedLayerInfo">—</span></div>
                </div>

            </div>

        </section>


        <!-- ================= SIDE PANEL ================= -->

        <div>

            <!-- LAYERS -->

            <section class="card">

                <h2>Graph Layers</h2>

                <div class="layerList" id="layerList"></div>

                <div class="controls">

                    <button id="addFunctionLayer" class="primary">
                        ＋ 함수 레이어
                    </button>

                    <button id="addSketchLayer">
                        ＋ 손그림 레이어
                    </button>

                    <button id="deleteLayer" class="danger">
                        선택 레이어 삭제
                    </button>

                </div>

                <div class="layerCount" id="layerCount">
                    0개 레이어
                </div>

                <div class="help" style="margin-top:10px">
                    👁 표시된 레이어만 음악에 포함됩니다.
                    여러 레이어를 동시에 표시하면 각각의 그래프가
                    독립적인 음높이로 동시에 재생됩니다.
                </div>

            </section>


            <!-- MUSIC -->

            <section class="card musicBox">

                <h2>Graph → Music</h2>

                <div class="row">

                    <div>

                        <label>음악 길이</label>

                        <select id="duration">

                            <option value="10">10초</option>
                            <option value="20">20초</option>
                            <option value="30">30초</option>

                            <option value="60">1분</option>
                            <option value="120">2분</option>
                            <option value="180">3분</option>
                            <option value="240">4분</option>
                            <option value="300">5분</option>

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

                    <label>스타일</label>

                    <select id="style">

                        <option value="pop">Pop</option>
                        <option value="kpop">K-pop</option>
                        <option value="jpop">J-pop</option>
                        <option value="lofi">Lo-fi</option>
                        <option value="edm">EDM</option>

                    </select>

                </div>


                <div class="controls">

                    <button id="play" class="primary">
                        ▶ 그래프 전체로 음악 만들기
                    </button>

                    <button id="stop">
                        ■ 정지
                    </button>

                </div>


                <div class="now" id="now">
                    표시된 모든 그래프가 동시에 음악으로 변환됩니다.
                </div>

                <div class="progress">
                    <div id="bar"></div>
                </div>

            </section>


            <!-- PRINCIPLE -->

            <section class="card musicBox">

                <h2>Cosmos 변환 원리</h2>

                <div class="help">

                    <b>각 레이어</b> = 하나의 독립적인 음악 선율<br><br>

                    x축 → 음악의 시간<br>
                    y축 → 음높이<br>
                    그래프 상승 → 높은 음<br>
                    그래프 하강 → 낮은 음<br>
                    그래프의 전체 길이 → 음악 전체 길이<br><br>

                    따라서 여러 그래프를 겹치면
                    여러 개의 독립적인 선율이 동시에 울리면서
                    하나의 음악 구조를 만들 수 있습니다.

                </div>

            </section>

        </div>

    </div>

</div>


<script>

(function(){

"use strict";


/* =========================================================
   기본 설정
========================================================= */

const canvas = document.getElementById("graph");
const ctx = canvas.getContext("2d");

const expr = document.getElementById("expr");
const msg = document.getElementById("message");

let xmin = -10;
let xmax = 10;
let ymin = -6;
let ymax = 6;

let mode = "navigate";

let dragging = false;
let lastX = 0;
let lastY = 0;

let audioCtx = null;

let playing = false;
let raf = null;
let playbackStart = 0;
let playbackDuration = 10;

let audioVoices = [];

let layerIdCounter = 1;


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
   레이어 구조
========================================================= */

let layers = [

    {
        id: 1,
        name: "Graph 1",
        type: "function",
        expression: "sin(x)",
        visible: true,
        volume: 0.14,
        color: layerColors[0],
        points: [],
        transform: {
            tx: 0,
            ty: 0,
            scale: 1,
            rotation: 0
        }
    },

    {
        id: 2,
        name: "Graph 2",
        type: "function",
        expression: "0.5*cos(2*x)",
        visible: true,
        volume: 0.10,
        color: layerColors[1],
        points: [],
        transform: {
            tx: 0,
            ty: 0,
            scale: 1,
            rotation: 0
        }
    }

];

let selectedLayerId = 1;


/* =========================================================
   수식 파서
========================================================= */

const funcs = {

    sin: Math.sin,
    cos: Math.cos,
    tan: Math.tan,

    sqrt: Math.sqrt,
    abs: Math.abs,

    log: Math.log,
    ln: Math.log,

    exp: Math.exp,

    asin: Math.asin,
    acos: Math.acos,
    atan: Math.atan

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

            let j = i + 1;

            while(
                j < s.length &&
                /[0-9.]/.test(s[j])
            ){
                j++;
            }

            const n = Number(s.slice(i,j));

            if(!Number.isFinite(n)){
                throw Error("숫자를 확인하세요.");
            }

            tokens.push({
                t:"num",
                v:n
            });

            i = j;
            continue;
        }


        if(/[A-Za-z_]/.test(s[i])){

            let j = i + 1;

            while(
                j < s.length &&
                /[A-Za-z_]/.test(s[j])
            ){
                j++;
            }

            tokens.push({
                t:"id",
                v:s.slice(i,j).toLowerCase()
            });

            i = j;
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

        throw Error("지원하지 않는 문자가 있습니다: " + s[i]);
    }

    return tokens;
}


function parseExpression(s){

    const ts = tokenize(s);

    let p = 0;


    function primary(){

        const z = ts[p];

        if(!z){
            throw Error("수식이 완성되지 않았습니다.");
        }


        if(z.t === "num"){

            p++;

            return () => z.v;

        }


        if(z.t === "id"){

            p++;

            if(z.v === "x"){
                return x => x;
            }

            if(z.v === "pi"){
                return () => Math.PI;
            }

            if(z.v === "e"){
                return () => Math.E;
            }


            if(funcs[z.v]){

                if(!ts[p] || ts[p].t !== "("){
                    throw Error(z.v + " 뒤에 괄호가 필요합니다.");
                }

                p++;

                const a = addsub();

                if(!ts[p] || ts[p].t !== ")"){
                    throw Error("괄호를 닫아주세요.");
                }

                p++;

                return x => funcs[z.v](a(x));
            }


            throw Error("알 수 없는 함수/변수: " + z.v);
        }


        if(z.t === "("){

            p++;

            const a = addsub();

            if(!ts[p] || ts[p].t !== ")"){
                throw Error("괄호를 닫아주세요.");
            }

            p++;

            return a;
        }


        if(z.t === "+"){

            p++;

            return primary();

        }


        if(z.t === "-"){

            p++;

            const a = primary();

            return x => -a(x);

        }


        throw Error("수식을 확인하세요.");
    }


    function power(){

        let a = primary();

        if(ts[p] && ts[p].t === "^"){

            p++;

            const b = power();

            const aa = a;

            return x => Math.pow(
                aa(x),
                b(x)
            );

        }

        return a;
    }


    function muldiv(){

        let a = power();

        while(
            ts[p] &&
            (
                ts[p].t === "*" ||
                ts[p].t === "/"
            )
        ){

            const op = ts[p++].t;
            const b = power();

            const aa = a;

            if(op === "*"){
                a = x => aa(x) * b(x);
            }else{
                a = x => aa(x) / b(x);
            }

        }

        return a;
    }


    function addsub(){

        let a = muldiv();

        while(
            ts[p] &&
            (
                ts[p].t === "+" ||
                ts[p].t === "-"
            )
        ){

            const op = ts[p++].t;
            const b = muldiv();

            const aa = a;

            if(op === "+"){
                a = x => aa(x) + b(x);
            }else{
                a = x => aa(x) - b(x);
            }

        }

        return a;
    }


    const f = addsub();

    if(p !== ts.length){
        throw Error("수식을 확인하세요.");
    }

    return f;
}


/* =========================================================
   좌표 변환
========================================================= */

function W(){
    return canvas.getBoundingClientRect().width;
}

function H(){
    return canvas.getBoundingClientRect().height;
}

function sx(x){
    return (
        (x - xmin) /
        (xmax - xmin)
    ) * W();
}

function sy(y){
    return (
        H() -
        (y - ymin) /
        (ymax - ymin) *
        H()
    );
}

function invx(px){
    return xmin +
        px / W() *
        (xmax - xmin);
}

function invy(py){
    return ymin +
        (H() - py) /
        H() *
        (ymax - ymin);
}


/* =========================================================
   변환
========================================================= */

function transformPoint(point, transform){

    const cx = point.cx;
    const cy = point.cy;

    const x0 = point.x - cx;
    const y0 = point.y - cy;

    const cos = Math.cos(transform.rotation);
    const sin = Math.sin(transform.rotation);

    const x1 =
        (x0 * cos - y0 * sin) *
        transform.scale;

    const y1 =
        (x0 * sin + y0 * cos) *
        transform.scale;

    return {

        x:
            cx +
            x1 +
            transform.tx,

        y:
            cy +
            y1 +
            transform.ty

    };
}


function transformedPoints(layer){

    if(!layer.points.length){
        return [];
    }

    return layer.points.map(p =>
        transformPoint(
            p,
            layer.transform
        )
    );
}


/* =========================================================
   함수 그래프 생성
========================================================= */

function generateFunctionPoints(expression){

    const f = parseExpression(expression);

    const result = [];

    const N = 1200;

    for(let i=0;i<=N;i++){

        const x =
            xmin +
            (xmax-xmin) *
            i/N;

        let y;

        try{
            y = f(x);
        }catch(e){
            y = NaN;
        }

        if(
            Number.isFinite(y) &&
            Math.abs(y) < 100000
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
   중심 계산
========================================================= */

function getCenter(points){

    if(!points.length){
        return {
            x:0,
            y:0
        };
    }

    let sxv = 0;
    let syv = 0;

    points.forEach(p=>{
        sxv += p.x;
        syv += p.y;
    });

    return {
        x:sxv/points.length,
        y:syv/points.length
    };
}


/* =========================================================
   레이어 선택
========================================================= */

function selectedLayer(){

    return layers.find(
        l => l.id === selectedLayerId
    );

}


/* =========================================================
   레이어 UI
========================================================= */

function renderLayers(){

    const box =
        document.getElementById("layerList");

    box.innerHTML = "";


    layers.forEach(layer=>{

        const item =
            document.createElement("div");

        item.className =
            "layerItem" +
            (
                layer.id === selectedLayerId
                ? " selected"
                : ""
            );


        const top =
            document.createElement("div");

        top.className =
            "layerTop";


        const color =
            document.createElement("span");

        color.className =
            "layerColor";

        color.style.background =
            layer.color;


        const name =
            document.createElement("span");

        name.className =
            "layerName";

        name.textContent =
            layer.name;


        const type =
            document.createElement("span");

        type.className =
            "layerType";

        type.textContent =
            layer.type === "function"
            ? "FUNCTION"
            : "SKETCH";


        top.appendChild(color);
        top.appendChild(name);
        top.appendChild(type);


        const actions =
            document.createElement("div");

        actions.className =
            "layerActions";


        const visibility =
            document.createElement("button");

        visibility.textContent =
            layer.visible
            ? "👁 표시"
            : "○ 숨김";

        visibility.className =
            "visibility";


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


        const volume =
            document.createElement("input");

        volume.type = "range";
        volume.min = "0";
        volume.max = "0.3";
        volume.step = "0.01";
        volume.value = layer.volume;

        volume.className =
            "layerVolume";


        volume.addEventListener(
            "click",
            e=>e.stopPropagation()
        );


        volume.addEventListener(
            "input",
            e=>{
                layer.volume =
                    Number(e.target.value);
            }
        );


        actions.appendChild(
            visibility
        );

        actions.appendChild(
            volume
        );


        item.appendChild(top);
        item.appendChild(actions);


        item.addEventListener(
            "click",
            ()=>{

                selectedLayerId =
                    layer.id;

                expr.value =
                    layer.expression || "";

                renderLayers();
                draw();

            }
        );


        box.appendChild(item);

    });


    document.getElementById(
        "layerCount"
    ).textContent =
        layers.length +
        "개 레이어 · " +
        layers.filter(l=>l.visible).length +
        "개 재생";


    const selected =
        selectedLayer();

    if(selected){

        document.getElementById(
            "selectedLayerInfo"
        ).textContent =
            selected.name +
            " · " +
            (
                selected.type === "function"
                ? "함수"
                : "손그림"
            );

    }

}


/* =========================================================
   함수 그래프 생성 버튼
========================================================= */

document
.getElementById("draw")
.addEventListener("click",()=>{

    const layer =
        selectedLayer();

    if(!layer)return;


    try{

        const points =
            generateFunctionPoints(
                expr.value
            );

        if(points.length < 10){
            throw Error(
                "그래프를 충분히 생성할 수 없습니다."
            );
        }


        const center =
            getCenter(points);


        points.forEach(p=>{

            p.cx = center.x;
            p.cy = center.y;

        });


        layer.type = "function";
        layer.expression =
            expr.value;

        layer.points =
            points;

        layer.transform = {
            tx:0,
            ty:0,
            scale:1,
            rotation:0
        };


        msg.textContent = "";

        renderLayers();
        draw();

    }catch(e){

        msg.textContent =
            e.message;

    }

});


/* =========================================================
   레이어 추가
========================================================= */

function addLayer(type){

    layerIdCounter++;

    const index =
        layers.length %
        layerColors.length;


    const layer = {

        id:layerIdCounter,

        name:
            type === "function"
            ? "Function " + layerIdCounter
            : "Sketch " + layerIdCounter,

        type:type,

        expression:
            type === "function"
            ? "sin(x)"
            : "",

        visible:true,

        volume:
            type === "function"
            ? 0.12
            : 0.10,

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


    if(type === "function"){

        try{

            const points =
                generateFunctionPoints(
                    layer.expression
                );

            const center =
                getCenter(points);

            points.forEach(p=>{
                p.cx=center.x;
                p.cy=center.y;
            });

            layer.points=points;

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
.getElementById("addFunctionLayer")
.addEventListener(
    "click",
    ()=>addLayer("function")
);


document
.getElementById("addSketchLayer")
.addEventListener(
    "click",
    ()=>addLayer("sketch")
);


/* =========================================================
   레이어 삭제
========================================================= */

document
.getElementById("deleteLayer")
.addEventListener(
    "click",
    ()=>{

        if(layers.length <= 1){

            msg.textContent =
                "최소 한 개의 레이어는 필요합니다.";

            return;

        }


        const index =
            layers.findIndex(
                l => l.id === selectedLayerId
            );


        layers =
            layers.filter(
                l => l.id !== selectedLayerId
            );


        selectedLayerId =
            layers[
                Math.max(
                    0,
                    index - 1
                )
            ].id;


        expr.value =
            selectedLayer().expression || "";

        renderLayers();
        draw();

    }
);


/* =========================================================
   손그림
========================================================= */

let sketchPoints = [];

canvas.addEventListener(
    "pointerdown",
    e=>{

        if(mode !== "sketch"){
            return;
        }


        const layer =
            selectedLayer();

        if(!layer){
            return;
        }


        sketchPoints = [];


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

        if(mode !== "sketch"){
            return;
        }

        if(!sketchPoints.length){
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

        if(mode !== "sketch"){
            return;
        }


        if(sketchPoints.length < 5){
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
                simplified.map(p=>({
                    x:p.x,
                    y:p.y
                }))
            );


        layer.type =
            "sketch";

        layer.expression = "";

        layer.points =
            simplified.map(p=>({

                x:p.x,
                y:p.y,

                cx:center.x,
                cy:center.y

            }));


        layer.transform = {

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


function simplifyPoints(points, step){

    const result=[];

    for(
        let i=0;
        i<points.length;
        i+=step
    ){

        result.push({
            x:points[i].x,
            y:points[i].y
        });

    }

    return result;

}


/* =========================================================
   손그림 미리보기
========================================================= */

function drawSketchPreview(){

    draw();

    if(sketchPoints.length < 2){
        return;
    }


    ctx.save();

    ctx.strokeStyle =
        selectedLayer().color;

    ctx.lineWidth=4;

    ctx.beginPath();


    sketchPoints.forEach(
        (p,i)=>{

            const px=sx(p.x);
            const py=sy(p.y);

            if(i===0){
                ctx.moveTo(px,py);
            }else{
                ctx.lineTo(px,py);
            }

        }
    );


    ctx.stroke();

    ctx.restore();

}


/* =========================================================
   Edit 모드
========================================================= */

canvas.addEventListener(
    "pointerdown",
    e=>{

        if(mode !== "edit"){
            return;
        }


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

        if(mode !== "edit"){
            return;
        }

        if(!dragging){
            return;
        }


        const layer =
            selectedLayer();


        if(!layer || !layer.points.length){
            return;
        }


        const dx =
            e.clientX-lastX;

        const dy =
            e.clientY-lastY;


        layer.transform.tx +=
            dx/W() *
            (xmax-xmin);


        layer.transform.ty -=
            dy/H() *
            (ymax-ymin);


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


/* =========================================================
   Edit 휠
========================================================= */

canvas.addEventListener(
    "wheel",
    e=>{

        if(mode !== "edit"){
            return;
        }


        e.preventDefault();


        const layer =
            selectedLayer();


        if(!layer){
            return;
        }


        if(e.shiftKey){

            layer.transform.rotation +=
                e.deltaY < 0
                ? 0.08
                : -0.08;

        }else{

            layer.transform.scale *=
                e.deltaY < 0
                ? 1.08
                : 0.92;

            layer.transform.scale =
                Math.max(
                    0.15,
                    Math.min(
                        5,
                        layer.transform.scale
                    )
                );

        }


        draw();

    },
    {passive:false}
);


/* =========================================================
   Edit 버튼
========================================================= */

document
.getElementById("scaleUp")
.addEventListener(
    "click",
    ()=>{

        const l=selectedLayer();

        if(l){
            l.transform.scale =
                Math.min(
                    5,
                    l.transform.scale*1.12
                );

            draw();
        }

    }
);


document
.getElementById("scaleDown")
.addEventListener(
    "click",
    ()=>{

        const l=selectedLayer();

        if(l){
            l.transform.scale =
                Math.max(
                    0.15,
                    l.transform.scale*0.88
                );

            draw();
        }

    }
);


document
.getElementById("rotateLeft")
.addEventListener(
    "click",
    ()=>{

        const l=selectedLayer();

        if(l){

            l.transform.rotation -=
                Math.PI/12;

            draw();

        }

    }
);


document
.getElementById("rotateRight")
.addEventListener(
    "click",
    ()=>{

        const l=selectedLayer();

        if(l){

            l.transform.rotation +=
                Math.PI/12;

            draw();

        }

    }
);


document
.getElementById("resetTransform")
.addEventListener(
    "click",
    ()=>{

        const l=selectedLayer();

        if(l){

            l.transform={
                tx:0,
                ty:0,
                scale:1,
                rotation:0
            };

            draw();

        }

    }
);


document
.getElementById("centerLayer")
.addEventListener(
    "click",
    ()=>{

        const l=selectedLayer();

        if(l){

            l.transform.tx=0;
            l.transform.ty=0;

            draw();

        }

    }
);


/* =========================================================
   모드 버튼
========================================================= */

function setMode(newMode){

    mode=newMode;

    document
    .getElementById("navigateMode")
    .classList.toggle(
        "active",
        mode==="navigate"
    );

    document
    .getElementById("sketchMode")
    .classList.toggle(
        "active",
        mode==="sketch"
    );

    document
    .getElementById("editMode")
    .classList.toggle(
        "active",
        mode==="edit"
    );

}


document
.getElementById("navigateMode")
.addEventListener(
    "click",
    ()=>setMode("navigate")
);


document
.getElementById("sketchMode")
.addEventListener(
    "click",
    ()=>setMode("sketch")
);


document
.getElementById("editMode")
.addEventListener(
    "click",
    ()=>setMode("edit")
);


/* =========================================================
   레이어 지우기
========================================================= */

document
.getElementById("clearLayer")
.addEventListener(
    "click",
    ()=>{

        const l =
            selectedLayer();

        if(!l)return;


        l.points=[];
        l.expression="";


        expr.value="";


        draw();
        renderLayers();

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
        (xmin+xmax)/2 +
        dx*(xmax-xmin);

    const cy =
        (ymin+ymax)/2 +
        dy*(ymax-ymin);


    const xr =
        (xmax-xmin)*factor;

    const yr =
        (ymax-ymin)*factor;


    xmin=cx-xr/2;
    xmax=cx+xr/2;

    ymin=cy-yr/2;
    ymax=cy+yr/2;


    draw();

}


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


/* =========================================================
   화면 이동 모드 드래그
========================================================= */

canvas.addEventListener(
    "pointerdown",
    e=>{

        if(mode !== "navigate"){
            return;
        }


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

        if(mode !== "navigate"){
            return;
        }

        if(!dragging){
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


/* =========================================================
   확대/축소
========================================================= */

canvas.addEventListener(
    "wheel",
    e=>{

        if(mode !== "navigate"){
            return;
        }


        e.preventDefault();


        const factor =
            e.deltaY < 0
            ? .8
            : 1.25;


        const mx =
            invx(e.offsetX);

        const my =
            invy(e.offsetY);


        xmin =
            mx+(xmin-mx)*factor;

        xmax =
            mx+(xmax-mx)*factor;


        ymin =
            my+(ymin-my)*factor;

        ymax =
            my+(ymax-my)*factor;


        draw();

    },
    {passive:false}
);


/* =========================================================
   그래프 그리기
========================================================= */

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


function fmt(v){

    if(!Number.isFinite(v)){
        return "—";
    }

    if(Math.abs(v)<1e-9){
        return "0";
    }

    if(Math.abs(v)>=100){
        return Math.round(v).toString();
    }

    return Number(
        v.toFixed(2)
    ).toString();

}


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

    ctx.strokeStyle="#18243d";

    ctx.fillStyle="#64718e";

    ctx.font="11px system-ui";


    for(
        let x=Math.ceil(xmin/xs)*xs;
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
        let y=Math.ceil(ymin/ys)*ys;
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


    /* axes */

    ctx.strokeStyle="#596783";

    ctx.lineWidth=1.4;


    if(
        xmin<=0 &&
        xmax>=0
    ){

        const px=sx(0);

        ctx.beginPath();

        ctx.moveTo(px,0);

        ctx.lineTo(px,h);

        ctx.stroke();

    }


    if(
        ymin<=0 &&
        ymax>=0
    ){

        const py=sy(0);

        ctx.beginPath();

        ctx.moveTo(0,py);

        ctx.lineTo(w,py);

        ctx.stroke();

    }


    /* layers */

    layers.forEach(layer=>{

        if(!layer.visible){
            return;
        }


        const points =
            transformedPoints(layer);


        if(points.length < 2){
            return;
        }


        ctx.save();

        ctx.strokeStyle =
            layer.color;

        ctx.lineWidth =
            layer.id === selectedLayerId
            ? 3.5
            : 2.4;

        ctx.lineJoin="round";

        ctx.lineCap="round";


        ctx.beginPath();


        points.forEach(
            (p,i)=>{

                const px=sx(p.x);
                const py=sy(p.y);


                if(
                    px < -100 ||
                    px > w+100 ||
                    py < -100 ||
                    py > h+100
                ){
                    return;
                }


                if(i===0){
                    ctx.moveTo(px,py);
                }else{
                    ctx.lineTo(px,py);
                }

            }
        );


        ctx.stroke();


        /* selected layer center */

        if(
            layer.id ===
            selectedLayerId
        ){

            const center =
                getCenter(points);


            const px=sx(center.x);
            const py=sy(center.y);


            ctx.fillStyle =
                layer.color;

            ctx.globalAlpha=.18;

            ctx.beginPath();

            ctx.arc(
                px,
                py,
                15,
                0,
                Math.PI*2
            );

            ctx.fill();

            ctx.globalAlpha=1;

        }


        ctx.restore();

    });


    /* =====================================================
       여러 레이어 재생 위치
    ===================================================== */

    if(
        playing &&
        playbackStart
    ){

        const elapsed =
            (performance.now() -
             playbackStart)
            / 1000;


        const progress =
            Math.max(
                0,
                Math.min(
                    1,
                    elapsed /
                    playbackDuration
                )
            );


        layers.forEach(layer=>{

            if(
                !layer.visible ||
                layer.points.length < 2
            ){
                return;
            }


            const points =
                transformedPoints(layer);


            const index =
                Math.min(
                    points.length-1,
                    Math.floor(
                        progress *
                        (points.length-1)
                    )
                );


            const p =
                points[index];


            if(!p){
                return;
            }


            const px=sx(p.x);
            const py=sy(p.y);


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

            ctx.fillStyle="#ffffff";

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
       분석
    ===================================================== */

    const l =
        selectedLayer();


    if(
        l &&
        l.points.length
    ){

        const points =
            transformedPoints(l);


        const ys =
            points
            .map(p=>p.y)
            .filter(
                Number.isFinite
            );


        if(ys.length){

            const min =
                Math.min(...ys);

            const max =
                Math.max(...ys);

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
        hi <= lo
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
            norm *
            (scale.length-1)
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
            (m-69)/12
        );

}


/* =========================================================
   스타일
========================================================= */

const styles={

    pop:{
        waveform:"triangle",
        attack:.025,
        release:.12,
        baseGain:1
    },

    kpop:{
        waveform:"sawtooth",
        attack:.015,
        release:.08,
        baseGain:.8
    },

    jpop:{
        waveform:"triangle",
        attack:.02,
        release:.1,
        baseGain:.9
    },

    lofi:{
        waveform:"sine",
        attack:.05,
        release:.2,
        baseGain:.65
    },

    edm:{
        waveform:"square",
        attack:.01,
        release:.06,
        baseGain:.55
    }

};


/* =========================================================
   그래프별 음 데이터
========================================================= */

function prepareLayerAudio(layer){

    const points =
        transformedPoints(layer);


    if(points.length < 2){
        return null;
    }


    const values =
        points
        .map(p=>p.y)
        .filter(
            Number.isFinite
        );


    if(values.length < 2){
        return null;
    }


    const lo =
        Math.min(...values);

    const hi =
        Math.max(...values);


    return {

        points:points,

        lo:lo,

        hi:hi

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
                l.points.length >= 2
        );


    if(!visibleLayers.length){

        msg.textContent =
            "음악으로 변환할 표시된 그래프가 없습니다.";

        return;

    }


    if(!audioCtx){

        audioCtx =
            new (
                window.AudioContext ||
                window.webkitAudioContext
            )();

    }


    if(
        audioCtx.state ===
        "suspended"
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


    audioVoices=[];


    /*
       레이어마다 독립적인 oscillator 생성.
       그래프의 전체 길이를 음악 전체 길이에
       정확히 대응시킨다.
    */

    visibleLayers.forEach(layer=>{

        const data =
            prepareLayerAudio(
                layer
            );


        if(!data){
            return;
        }


        const osc =
            audioCtx.createOscillator();

        const gain =
            audioCtx.createGain();


        osc.type =
            style.waveform;


        const start =
            audioCtx.currentTime +
            .05;


        gain.gain.setValueAtTime(
            0,
            start
        );


        gain.gain.linearRampToValueAtTime(
            layer.volume *
            style.baseGain,
            start +
            style.attack
        );


        osc.connect(gain);

        gain.connect(
            audioCtx.destination
        );


        osc.start(start);


        audioVoices.push({

            layer:layer,

            data:data,

            osc:osc,

            gain:gain,

            lastFreq:0

        });

    });


    if(!audioVoices.length){

        stopMusic();

        msg.textContent =
            "재생할 수 있는 그래프가 없습니다.";

        return;

    }


    document.getElementById(
        "now"
    ).textContent =
        visibleLayers.length +
        "개 그래프 레이어가 동시에 재생됩니다.";


    raf =
        requestAnimationFrame(
            musicTick
        );

}


/* =========================================================
   음악 시간 진행
========================================================= */

function musicTick(){

    if(!playing){
        return;
    }


    const elapsed =
        (performance.now() -
         playbackStart) /
        1000;


    const progress =
        Math.max(
            0,
            Math.min(
                1,
                elapsed /
                playbackDuration
            )
        );


    audioVoices.forEach(voice=>{

        const points =
            voice.data.points;


        const index =
            Math.min(
                points.length-1,
                Math.floor(
                    progress *
                    (points.length-1)
                )
            );


        const p =
            points[index];


        const midi =
            graphMidi(
                p.y,
                voice.data.lo,
                voice.data.hi,
                scales[
                    document.getElementById(
                        "scale"
                    ).value
                ]
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

        }else{

            voice.osc.frequency
                .cancelScheduledValues(
                    now
                );


            voice.osc.frequency
                .linearRampToValueAtTime(
                    freq,
                    now + .055
                );

        }


        voice.lastFreq =
            freq;

    });


    document.getElementById(
        "bar"
    ).style.width =
        (
            progress*100
        ) + "%";


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


    if(progress < 1){

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

                voice.gain
                    .gain
                    .cancelScheduledValues(
                        now
                    );


                voice.gain
                    .gain
                    .setTargetAtTime(
                        0,
                        now,
                        .08
                    );


                voice.osc.stop(
                    now+.35
                );

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

                    voice.gain
                        .gain
                        .cancelScheduledValues(
                            now
                        );


                    voice.gain
                        .gain
                        .setTargetAtTime(
                            0,
                            now,
                            .04
                        );


                    voice.osc.stop(
                        now+.1
                    );

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
   리사이즈
========================================================= */

function resize(){

    const rect =
        canvas.getBoundingClientRect();


    const dpr =
        window.devicePixelRatio || 1;


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

renderLayers();

resize();


/*
   처음부터 두 그래프가 보이도록 생성
*/

try{

    layers.forEach(layer=>{

        if(
            layer.type ===
            "function" &&
            !layer.points.length
        ){

            const points =
                generateFunctionPoints(
                    layer.expression
                );


            const center =
                getCenter(points);


            points.forEach(p=>{

                p.cx=center.x;
                p.cy=center.y;

            });


            layer.points=points;

        }

    });

}catch(e){}


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
        background:#0b1020;
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
    height=1700,
    scrolling=True
)
