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

<title>Cosmos — Graph to Music</title>

<style>
* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
    background:
        radial-gradient(circle at 15% 10%, rgba(86, 112, 255, 0.13), transparent 30%),
        radial-gradient(circle at 85% 20%, rgba(177, 91, 255, 0.10), transparent 28%),
        #070912;
    color: #f5f7ff;
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        "Noto Sans KR",
        sans-serif;
}

body {
    min-height: 100vh;
}

button,
input,
select {
    font: inherit;
}

button {
    cursor: pointer;
}

.cosmos {
    width: 100%;
    max-width: 1450px;
    margin: 0 auto;
    padding: 30px 28px 70px;
}

/* ---------- HEADER ---------- */

.header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    margin-bottom: 24px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 14px;
}

.logo {
    width: 48px;
    height: 48px;
    border-radius: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    background:
        linear-gradient(145deg, rgba(114, 131, 255, 0.32), rgba(150, 71, 255, 0.12));
    border: 1px solid rgba(155, 165, 255, 0.25);
    font-size: 27px;
    box-shadow: 0 0 30px rgba(101, 105, 255, 0.12);
}

.title {
    font-size: 28px;
    font-weight: 800;
    letter-spacing: -1px;
}

.subtitle {
    margin-top: 3px;
    color: #8990a9;
    font-size: 13px;
}

.header-badge {
    color: #aeb6d5;
    border: 1px solid rgba(145, 154, 190, 0.22);
    padding: 8px 13px;
    border-radius: 999px;
    font-size: 12px;
    background: rgba(255,255,255,0.025);
}

/* ---------- CARD ---------- */

.card {
    background:
        linear-gradient(145deg, rgba(20, 24, 39, 0.94), rgba(10, 13, 24, 0.97));
    border: 1px solid rgba(145, 154, 190, 0.16);
    border-radius: 20px;
    box-shadow: 0 18px 60px rgba(0,0,0,0.25);
    overflow: hidden;
}

.card-header {
    padding: 19px 21px 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.card-title {
    font-size: 16px;
    font-weight: 750;
}

.card-description {
    color: #737b96;
    font-size: 12px;
    margin-top: 3px;
}

/* ---------- GRAPH ---------- */

.graph-card {
    padding-bottom: 17px;
}

.canvas-wrap {
    position: relative;
    margin: 0 18px;
    height: min(58vh, 600px);
    min-height: 420px;
    border-radius: 16px;
    overflow: hidden;
    background:
        radial-gradient(circle at 50% 50%, rgba(72, 83, 144, 0.07), transparent 55%),
        #080b15;
    border: 1px solid rgba(135, 145, 183, 0.14);
}

#graphCanvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
}

.canvas-help {
    position: absolute;
    top: 14px;
    left: 15px;
    z-index: 3;
    color: #6f7793;
    font-size: 11px;
    background: rgba(4,6,13,0.65);
    border: 1px solid rgba(130,140,180,0.12);
    border-radius: 8px;
    padding: 7px 9px;
    pointer-events: none;
}

.canvas-status {
    position: absolute;
    right: 15px;
    top: 14px;
    z-index: 3;
    color: #8d96b8;
    font-size: 11px;
    background: rgba(4,6,13,0.65);
    border: 1px solid rgba(130,140,180,0.12);
    border-radius: 8px;
    padding: 7px 9px;
    pointer-events: none;
}

#playPoint {
    position: absolute;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #ffffff;
    border: 3px solid #7e8cff;
    box-shadow:
        0 0 0 5px rgba(111, 124, 255, 0.15),
        0 0 24px rgba(120, 133, 255, 0.85);
    transform: translate(-50%, -50%);
    display: none;
    pointer-events: none;
    z-index: 4;
}

.graph-controls {
    padding: 17px 18px 0;
    display: grid;
    grid-template-columns: 1fr auto auto auto auto;
    gap: 9px;
}

.input {
    width: 100%;
    border: 1px solid rgba(142, 151, 184, 0.18);
    background: #0b0e19;
    color: #f5f7ff;
    border-radius: 11px;
    padding: 12px 14px;
    outline: none;
}

.input:focus {
    border-color: rgba(128, 139, 255, 0.65);
    box-shadow: 0 0 0 3px rgba(108, 122, 255, 0.08);
}

.btn {
    border: 1px solid rgba(145, 154, 190, 0.18);
    background: #111525;
    color: #e8ebf8;
    border-radius: 11px;
    padding: 10px 14px;
    transition: 0.15s ease;
    white-space: nowrap;
}

.btn:hover {
    background: #171c31;
    border-color: rgba(145, 155, 255, 0.38);
}

.btn.primary {
    background: linear-gradient(135deg, #5667e8, #7655cf);
    border-color: transparent;
    color: white;
    box-shadow: 0 8px 24px rgba(84, 98, 229, 0.18);
}

.btn.primary:hover {
    filter: brightness(1.08);
}

.btn.danger {
    color: #ff9caa;
}

.view-controls {
    display: flex;
    gap: 7px;
    padding: 10px 18px 0;
}

.small-btn {
    padding: 7px 10px;
    font-size: 12px;
}

.stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 9px;
    padding: 12px 18px 0;
}

.stat {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(140,150,185,0.10);
    border-radius: 11px;
    padding: 10px 12px;
}

.stat-label {
    color: #727a94;
    font-size: 10px;
    margin-bottom: 4px;
}

.stat-value {
    color: #dce1f4;
    font-size: 13px;
    font-weight: 650;
}

/* ---------- SKETCH ---------- */

.sketch-card {
    margin-top: 18px;
}

.sketch-body {
    padding: 0 18px 20px;
}

.sketch-description {
    color: #828aa4;
    font-size: 12px;
    line-height: 1.6;
    margin-bottom: 13px;
}

.sketch-toolbar {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.sketch-result {
    margin-top: 13px;
    padding: 12px 14px;
    border-radius: 11px;
    background: rgba(91, 105, 240, 0.07);
    border: 1px solid rgba(103, 116, 240, 0.16);
    color: #cbd1eb;
    font-size: 13px;
    display: none;
}

.sketch-result strong {
    color: #aeb9ff;
}

/* ---------- MUSIC ---------- */

.music-card {
    margin-top: 18px;
}

.music-body {
    padding: 0 18px 22px;
}

.music-grid {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 15px;
}

.settings-panel,
.layers-panel {
    background: rgba(255,255,255,0.018);
    border: 1px solid rgba(140,150,185,0.10);
    border-radius: 15px;
    padding: 15px;
}

.setting-row {
    display: grid;
    grid-template-columns: 130px 1fr;
    align-items: center;
    gap: 12px;
    margin-bottom: 13px;
}

.setting-row:last-child {
    margin-bottom: 0;
}

.setting-label {
    color: #8d95af;
    font-size: 12px;
}

.select {
    width: 100%;
    color: #edf0fa;
    background: #0c101c;
    border: 1px solid rgba(140,150,185,0.16);
    border-radius: 10px;
    padding: 10px 11px;
    outline: none;
}

.layer-title {
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 11px;
}

.layer {
    display: grid;
    grid-template-columns: 22px 1fr 105px;
    gap: 8px;
    align-items: center;
    margin-bottom: 9px;
}

.layer:last-child {
    margin-bottom: 0;
}

.layer-name {
    color: #bec4d8;
    font-size: 12px;
}

.layer input[type="range"] {
    width: 100%;
}

input[type="range"] {
    accent-color: #7180ef;
}

.layer-volume {
    font-size: 10px;
    color: #6f7791;
    text-align: right;
}

.transport {
    display: flex;
    align-items: center;
    gap: 9px;
    margin-top: 15px;
}

.play-btn {
    min-width: 120px;
}

.progress-wrap {
    flex: 1;
}

.progress-track {
    height: 8px;
    background: #0b0e18;
    border-radius: 999px;
    overflow: hidden;
    border: 1px solid rgba(130,140,175,0.10);
}

.progress-fill {
    width: 0%;
    height: 100%;
    background: linear-gradient(90deg, #6577ef, #9b72ed);
    border-radius: inherit;
    transition: width 0.05s linear;
}

.time-text {
    display: flex;
    justify-content: space-between;
    color: #727b96;
    font-size: 10px;
    margin-top: 6px;
}

.music-status {
    margin-top: 12px;
    min-height: 22px;
    color: #8f98b4;
    font-size: 12px;
}

.success {
    color: #8fe0b1;
}

.warning {
    color: #e9c77e;
}

/* ---------- PRINCIPLE ---------- */

.principle {
    margin-top: 18px;
    padding: 18px 20px;
    border-radius: 17px;
    background:
        linear-gradient(135deg, rgba(82,96,216,0.08), rgba(153,79,217,0.045));
    border: 1px solid rgba(111,125,235,0.13);
}

.principle-title {
    font-size: 13px;
    font-weight: 750;
    margin-bottom: 8px;
}

.principle-text {
    color: #9199b3;
    font-size: 12px;
    line-height: 1.75;
}

.formula-flow {
    color: #cbd2ed;
    margin-top: 8px;
    font-size: 12px;
    word-break: keep-all;
}

/* ---------- RESPONSIVE ---------- */

@media (max-width: 900px) {
    .graph-controls {
        grid-template-columns: 1fr 1fr;
    }

    .music-grid {
        grid-template-columns: 1fr;
    }

    .stats {
        grid-template-columns: repeat(2, 1fr);
    }

    .header {
        align-items: flex-start;
        gap: 15px;
    }

    .header-badge {
        display: none;
    }
}

@media (max-width: 600px) {
    .cosmos {
        padding: 18px 10px 50px;
    }

    .canvas-wrap {
        min-height: 350px;
        height: 55vh;
    }

    .setting-row {
        grid-template-columns: 1fr;
        gap: 6px;
    }

    .layer {
        grid-template-columns: 22px 1fr 75px;
    }
}
</style>
</head>

<body>

<div class="cosmos">

    <div class="header">
        <div class="brand">
            <div class="logo">∿</div>
            <div>
                <div class="title">Cosmos</div>
                <div class="subtitle">Function Graph → Music</div>
            </div>
        </div>

        <div class="header-badge">
            MATHEMATICS × SOUND
        </div>
    </div>


    <!-- ================= GRAPH ================= -->

    <section class="card graph-card">

        <div class="card-header">
            <div>
                <div class="card-title">Graph Lab</div>
                <div class="card-description">
                    함수의 형태를 관찰하고 소리로 변환합니다.
                </div>
            </div>
        </div>

        <div class="canvas-wrap" id="canvasWrap">

            <canvas id="graphCanvas"></canvas>

            <div class="canvas-help" id="canvasHelp">
                휠: 확대/축소 · 드래그: 이동
            </div>

            <div class="canvas-status" id="canvasStatus">
                FUNCTION MODE
            </div>

            <div id="playPoint"></div>

        </div>


        <div class="graph-controls">

            <input
                id="functionInput"
                class="input"
                value="x^2"
                placeholder="예: x^2, sin(x), -x^2, 2*x+1"
            >

            <button class="btn primary" id="plotBtn">
                그래프 그리기
            </button>

            <button class="btn danger" id="deleteBtn">
                삭제
            </button>

            <button class="btn" id="resetBtn">
                초기화
            </button>

            <button class="btn" id="fitBtn">
                화면 맞춤
            </button>

        </div>


        <div class="view-controls">

            <button class="btn small-btn" id="zoomInBtn">
                확대 +
            </button>

            <button class="btn small-btn" id="zoomOutBtn">
                축소 −
            </button>

            <button class="btn small-btn" id="centerBtn">
                원점으로
            </button>

        </div>


        <div class="stats">

            <div class="stat">
                <div class="stat-label">FUNCTION</div>
                <div class="stat-value" id="statFunction">x²</div>
            </div>

            <div class="stat">
                <div class="stat-label">X RANGE</div>
                <div class="stat-value" id="statX">−10 ~ 10</div>
            </div>

            <div class="stat">
                <div class="stat-label">Y RANGE</div>
                <div class="stat-value" id="statY">−10 ~ 10</div>
            </div>

            <div class="stat">
                <div class="stat-label">GRAPH POINTS</div>
                <div class="stat-value" id="statPoints">0</div>
            </div>

        </div>

    </section>


    <!-- ================= SKETCH ================= -->

    <section class="card sketch-card">

        <div class="card-header">
            <div>
                <div class="card-title">Sketch → Function</div>
                <div class="card-description">
                    좌표평면에 직접 그린 곡선을 3차 함수로 근사합니다.
                </div>
            </div>
        </div>

        <div class="sketch-body">

            <div class="sketch-description">
                아래 버튼을 누른 뒤 그래프 위에서 마우스로 곡선을 그려보세요.
                수집한 점들을 3차 다항식으로 근사하여 매끄러운 함수 그래프로 변환합니다.
            </div>

            <div class="sketch-toolbar">

                <button class="btn" id="sketchBtn">
                    손으로 그래프 그리기
                </button>

                <button class="btn primary" id="fitSketchBtn">
                    그린 점을 함수로 근사
                </button>

                <button class="btn danger" id="clearSketchBtn">
                    손그림 지우기
                </button>

            </div>

            <div class="sketch-result" id="sketchResult">
                <strong>추정 함수식:</strong>
                <span id="estimatedFunction"></span>
            </div>

        </div>

    </section>


    <!-- ================= MUSIC ================= -->

    <section class="card music-card">

        <div class="card-header">
            <div>
                <div class="card-title">Music Studio</div>
                <div class="card-description">
                    그래프 전체를 곡 전체 시간에 대응시켜 하나의 선율로 변환합니다.
                </div>
            </div>
        </div>


        <div class="music-body">

            <div class="music-grid">

                <div class="settings-panel">

                    <div class="setting-row">

                        <div class="setting-label">
                            음악 길이
                        </div>

                        <select id="durationSelect" class="select">

                            <option value="10">10초</option>
                            <option value="20">20초</option>
                            <option value="30">30초</option>
                            <option value="60" selected>1분</option>
                            <option value="120">2분</option>
                            <option value="180">3분</option>
                            <option value="240">4분</option>
                            <option value="300">5분</option>

                        </select>

                    </div>


                    <div class="setting-row">

                        <div class="setting-label">
                            음악 스타일
                        </div>

                        <select id="styleSelect" class="select">

                            <option value="pop">Pop</option>
                            <option value="kpop">K-pop</option>
                            <option value="jpop">J-pop</option>
                            <option value="lofi" selected>Lo-fi</option>
                            <option value="edm">EDM</option>

                        </select>

                    </div>


                    <div class="setting-row">

                        <div class="setting-label">
                            배경 음계
                        </div>

                        <select id="scaleSelect" class="select">

                            <option value="major" selected>Major</option>
                            <option value="minor">Minor</option>
                            <option value="pentatonic">Pentatonic</option>
                            <option value="chromatic">Chromatic</option>

                        </select>

                    </div>

                    <div class="transport">

                        <button class="btn primary play-btn" id="playBtn">
                            ▶ 재생
                        </button>

                        <button class="btn" id="stopBtn">
                            ■ 정지
                        </button>

                        <div class="progress-wrap">

                            <div class="progress-track">
                                <div class="progress-fill" id="progressFill"></div>
                            </div>

                            <div class="time-text">
                                <span id="currentTime">0:00</span>
                                <span id="totalTime">1:00</span>
                            </div>

                        </div>

                    </div>

                    <div class="music-status" id="musicStatus">
                        그래프를 음악으로 변환할 준비가 되었습니다.
                    </div>

                </div>


                <div class="layers-panel">

                    <div class="layer-title">
                        음악 레이어
                    </div>


                    <div class="layer">

                        <input type="checkbox" id="layerMelody" checked>

                        <div class="layer-name">
                            그래프 멜로디
                        </div>

                        <div class="layer-volume">
                            <input type="range" id="volMelody" min="0" max="1" step="0.01" value="0.80">
                        </div>

                    </div>


                    <div class="layer">

                        <input type="checkbox" id="layerDrums" checked>

                        <div class="layer-name">
                            드럼
                        </div>

                        <div class="layer-volume">
                            <input type="range" id="volDrums" min="0" max="1" step="0.01" value="0.38">
                        </div>

                    </div>


                    <div class="layer">

                        <input type="checkbox" id="layerBass" checked>

                        <div class="layer-name">
                            베이스
                        </div>

                        <div class="layer-volume">
                            <input type="range" id="volBass" min="0" max="1" step="0.01" value="0.32">
                        </div>

                    </div>


                    <div class="layer">

                        <input type="checkbox" id="layerChords" checked>

                        <div class="layer-name">
                            코드
                        </div>

                        <div class="layer-volume">
                            <input type="range" id="volChords" min="0" max="1" step="0.01" value="0.22">
                        </div>

                    </div>


                    <div class="layer">

                        <input type="checkbox" id="layerArp">

                        <div class="layer-name">
                            아르페지오
                        </div>

                        <div class="layer-volume">
                            <input type="range" id="volArp" min="0" max="1" step="0.01" value="0.20">
                        </div>

                    </div>


                    <div class="layer">

                        <input type="checkbox" id="layerPad" checked>

                        <div class="layer-name">
                            패드
                        </div>

                        <div class="layer-volume">
                            <input type="range" id="volPad" min="0" max="1" step="0.01" value="0.18">
                        </div>

                    </div>


                    <div class="layer">

                        <input type="checkbox" id="layerPerc">

                        <div class="layer-name">
                            퍼커션
                        </div>

                        <div class="layer-volume">
                            <input type="range" id="volPerc" min="0" max="1" step="0.01" value="0.18">
                        </div>

                    </div>


                    <div class="layer">

                        <input type="checkbox" id="layerTexture">

                        <div class="layer-name">
                            텍스처
                        </div>

                        <div class="layer-volume">
                            <input type="range" id="volTexture" min="0" max="1" step="0.01" value="0.12">
                        </div>

                    </div>

                </div>

            </div>

        </div>

    </section>


    <!-- ================= PRINCIPLE ================= -->

    <section class="principle">

        <div class="principle-title">
            Cosmos의 핵심 원리
        </div>

        <div class="principle-text">
            함수 그래프의 y값을 시간에 따른 음높이로 대응시키고,
            그래프 전체 구간을 곡 전체 재생 시간에 대응시켜
            함수의 형태 자체를 하나의 선율로 표현합니다.
        </div>

        <div class="formula-flow">
            함수 그래프 → y값 추출 → 주파수 변환 → 그래프 전체를 곡 전체에 대응
            → 그래프 멜로디 + 반주 레이어 → 하나의 음악
        </div>

    </section>

</div>


<script>

/* =========================================================
   COSMOS
   Graph → Music
   ========================================================= */


/* ---------------------------------------------------------
   DOM
--------------------------------------------------------- */

const canvas = document.getElementById("graphCanvas");
const wrap = document.getElementById("canvasWrap");
const ctx = canvas.getContext("2d");

const functionInput = document.getElementById("functionInput");

const statFunction = document.getElementById("statFunction");
const statX = document.getElementById("statX");
const statY = document.getElementById("statY");
const statPoints = document.getElementById("statPoints");

const playPoint = document.getElementById("playPoint");
const progressFill = document.getElementById("progressFill");
const currentTimeText = document.getElementById("currentTime");
const totalTimeText = document.getElementById("totalTime");
const musicStatus = document.getElementById("musicStatus");
const canvasStatus = document.getElementById("canvasStatus");

const durationSelect = document.getElementById("durationSelect");
const styleSelect = document.getElementById("styleSelect");
const scaleSelect = document.getElementById("scaleSelect");


/* ---------------------------------------------------------
   GRAPH STATE
--------------------------------------------------------- */

let expression = "x^2";

let xMin = -10;
let xMax = 10;

let yMin = -10;
let yMax = 10;

let samples = [];

let sketchMode = false;
let sketchPoints = [];
let drawing = false;

let dragging = false;
let lastMouseX = 0;
let lastMouseY = 0;

let playbackPercent = 0;


/* ---------------------------------------------------------
   AUDIO STATE
--------------------------------------------------------- */

let audioCtx = null;

let playing = false;

let songStartTime = 0;
let songDuration = 60;

let animationFrame = null;
let schedulerTimer = null;

let nextBeatTime = 0;
let beatIndex = 0;

let activeAudioNodes = [];

let melodyOsc = null;
let melodyGain = null;

let scheduledEvents = new Set();


/* ---------------------------------------------------------
   STYLE CONFIGURATION
--------------------------------------------------------- */

const styles = {

    pop: {
        bpm: 108,
        melodyWave: "triangle",
        bassWave: "triangle",
        chordWave: "sine",
        padWave: "sine",
        step: 0.555,
        bassEvery: 2
    },

    kpop: {
        bpm: 118,
        melodyWave: "sawtooth",
        bassWave: "triangle",
        chordWave: "sawtooth",
        padWave: "sine",
        step: 0.508,
        bassEvery: 2
    },

    jpop: {
        bpm: 128,
        melodyWave: "triangle",
        bassWave: "square",
        chordWave: "triangle",
        padWave: "sine",
        step: 0.469,
        bassEvery: 2
    },

    lofi: {
        bpm: 82,
        melodyWave: "sine",
        bassWave: "triangle",
        chordWave: "sine",
        padWave: "sine",
        step: 0.732,
        bassEvery: 2
    },

    edm: {
        bpm: 126,
        melodyWave: "sawtooth",
        bassWave: "square",
        chordWave: "sawtooth",
        padWave: "triangle",
        step: 0.476,
        bassEvery: 1
    }

};


/* ---------------------------------------------------------
   SCALES
--------------------------------------------------------- */

const scales = {

    major: [0, 2, 4, 5, 7, 9, 11],

    minor: [0, 2, 3, 5, 7, 8, 10],

    pentatonic: [0, 2, 4, 7, 9],

    chromatic: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

};


/* ---------------------------------------------------------
   UTILITIES
--------------------------------------------------------- */

function clamp(value, min, max) {
    return Math.max(min, Math.min(max, value));
}


function formatTime(seconds) {

    seconds = Math.max(0, Math.floor(seconds));

    const minutes = Math.floor(seconds / 60);

    const secs = seconds % 60;

    return minutes + ":" + String(secs).padStart(2, "0");
}


function midiToFreq(midi) {

    return 440 * Math.pow(2, (midi - 69) / 12);

}


function formatNumber(n) {

    if (!Number.isFinite(n)) {
        return "0";
    }

    if (Math.abs(n) < 0.0001) {
        return "0";
    }

    return Number(n.toFixed(4)).toString();
}


/* ---------------------------------------------------------
   SAFE FUNCTION PARSER
--------------------------------------------------------- */

function normalizeExpression(text) {

    let s = String(text)
        .trim()
        .toLowerCase()
        .replace(/\s+/g, "");

    s = s.replace(/\^/g, "**");

    s = s.replace(/π/g, "PI");

    s = s.replace(/\bpi\b/g, "PI");

    s = s.replace(/\bsin\(/g, "Math.sin(");
    s = s.replace(/\bcos\(/g, "Math.cos(");
    s = s.replace(/\btan\(/g, "Math.tan(");

    s = s.replace(/\bsqrt\(/g, "Math.sqrt(");
    s = s.replace(/\babs\(/g, "Math.abs(");

    s = s.replace(/\blog\(/g, "Math.log(");
    s = s.replace(/\bln\(/g, "Math.log(");

    s = s.replace(/\bexp\(/g, "Math.exp(");

    s = s.replace(/\bPI\b/g, "Math.PI");

    return s;
}


function compileFunction(text) {

    let original = String(text).trim();

    if (!original) {
        throw new Error("함수식을 입력해주세요.");
    }

    /*
       허용되는 문자를 제한하여
       함수 입력을 계산식 용도로만 사용한다.
    */

    const check = original
        .replace(/sin|cos|tan|sqrt|abs|log|ln|exp/gi, "")
        .replace(/pi/gi, "")
        .replace(/[0-9xX+\-*/^().,\s]/g, "");

    if (check.length > 0) {
        throw new Error("허용되지 않는 문자가 포함되어 있습니다.");
    }

    const normalized = normalizeExpression(original);

    const fn = new Function(
        "x",
        "\"use strict\"; return (" + normalized + ");"
    );

    /*
       실제 숫자가 나오는지 확인
    */

    const test = fn(0);

    if (typeof test !== "number" || !Number.isFinite(test)) {

        const test2 = fn(1);

        if (
            typeof test2 !== "number" ||
            !Number.isFinite(test2)
        ) {
            throw new Error("계산할 수 없는 함수식입니다.");
        }
    }

    return fn;
}


/* ---------------------------------------------------------
   GRAPH SAMPLING
--------------------------------------------------------- */

function sampleFunction(fn) {

    const width = Math.max(700, Math.min(1400, Math.floor(canvas.clientWidth * 1.3)));

    const N = width;

    const result = [];

    for (let i = 0; i < N; i++) {

        const x =
            xMin +
            (xMax - xMin) * i / (N - 1);

        let y;

        try {
            y = fn(x);
        } catch (e) {
            y = NaN;
        }

        if (
            Number.isFinite(y) &&
            Math.abs(y) < 100000
        ) {
            result.push({
                x: x,
                y: y
            });
        } else {
            result.push({
                x: x,
                y: null
            });
        }
    }

    return result;
}


/* ---------------------------------------------------------
   GRAPH COORDINATE TRANSFORM
--------------------------------------------------------- */

function resizeCanvas() {

    const rect = wrap.getBoundingClientRect();

    const dpr = Math.min(window.devicePixelRatio || 1, 2);

    canvas.width = Math.floor(rect.width * dpr);

    canvas.height = Math.floor(rect.height * dpr);

    canvas.style.width = rect.width + "px";

    canvas.style.height = rect.height + "px";

    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    drawGraph();
}


function xToPixel(x) {

    return (
        (x - xMin) /
        (xMax - xMin) *
        canvas.clientWidth
    );
}


function yToPixel(y) {

    return (
        canvas.clientHeight -
        (y - yMin) /
        (yMax - yMin) *
        canvas.clientHeight
    );
}


function pixelToX(px) {

    return (
        xMin +
        px / canvas.clientWidth *
        (xMax - xMin)
    );
}


function pixelToY(py) {

    return (
        yMax -
        py / canvas.clientHeight *
        (yMax - yMin)
    );
}


/* ---------------------------------------------------------
   GRAPH DRAWING
--------------------------------------------------------- */

function drawGrid() {

    const w = canvas.clientWidth;
    const h = canvas.clientHeight;

    ctx.clearRect(0, 0, w, h);

    ctx.fillStyle = "#080b15";

    ctx.fillRect(0, 0, w, h);


    /*
       Grid
    */

    ctx.lineWidth = 1;

    const xStep = chooseGridStep(xMax - xMin);
    const yStep = chooseGridStep(yMax - yMin);

    ctx.strokeStyle = "rgba(124,136,176,0.075)";

    for (
        let x = Math.ceil(xMin / xStep) * xStep;
        x <= xMax;
        x += xStep
    ) {

        const px = xToPixel(x);

        ctx.beginPath();
        ctx.moveTo(px, 0);
        ctx.lineTo(px, h);
        ctx.stroke();
    }


    for (
        let y = Math.ceil(yMin / yStep) * yStep;
        y <= yMax;
        y += yStep
    ) {

        const py = yToPixel(y);

        ctx.beginPath();
        ctx.moveTo(0, py);
        ctx.lineTo(w, py);
        ctx.stroke();
    }


    /*
       Axis
    */

    ctx.strokeStyle = "rgba(205,213,240,0.35)";
    ctx.lineWidth = 1.3;


    if (xMin <= 0 && xMax >= 0) {

        const px = xToPixel(0);

        ctx.beginPath();
        ctx.moveTo(px, 0);
        ctx.lineTo(px, h);
        ctx.stroke();
    }


    if (yMin <= 0 && yMax >= 0) {

        const py = yToPixel(0);

        ctx.beginPath();
        ctx.moveTo(0, py);
        ctx.lineTo(w, py);
        ctx.stroke();
    }


    /*
       Axis labels
    */

    ctx.fillStyle = "rgba(164,173,204,0.62)";
    ctx.font = "11px sans-serif";


    if (yMin <= 0 && yMax >= 0) {

        const py = yToPixel(0);

        for (
            let x = Math.ceil(xMin / xStep) * xStep;
            x <= xMax;
            x += xStep
        ) {

            if (Math.abs(x) < 0.00001) {
                continue;
            }

            const px = xToPixel(x);

            ctx.fillText(
                formatNumber(x),
                px + 4,
                py - 6
            );
        }
    }


    if (xMin <= 0 && xMax >= 0) {

        const px = xToPixel(0);

        for (
            let y = Math.ceil(yMin / yStep) * yStep;
            y <= yMax;
            y += yStep
        ) {

            if (Math.abs(y) < 0.00001) {
                continue;
            }

            const py = yToPixel(y);

            ctx.fillText(
                formatNumber(y),
                px + 7,
                py - 4
            );
        }
    }
}


function chooseGridStep(range) {

    if (range <= 4) return 0.5;
    if (range <= 10) return 1;
    if (range <= 25) return 2.5;
    if (range <= 50) return 5;
    if (range <= 100) return 10;
    return 20;
}


function drawFunction() {

    if (!samples.length) {
        return;
    }

    ctx.save();

    ctx.lineWidth = 3;

    ctx.strokeStyle = "#7b8cff";

    ctx.shadowColor = "rgba(109,126,255,0.45)";
    ctx.shadowBlur = 12;

    ctx.beginPath();

    let started = false;

    for (let i = 0; i < samples.length; i++) {

        const p = samples[i];

        if (p.y === null) {
            started = false;
            continue;
        }

        const px = xToPixel(p.x);
        const py = yToPixel(p.y);

        if (!started) {

            ctx.moveTo(px, py);

            started = true;

        } else {

            ctx.lineTo(px, py);
        }
    }

    ctx.stroke();

    ctx.restore();
}


function drawSketch() {

    if (!sketchPoints.length) {
        return;
    }

    ctx.save();

    ctx.strokeStyle = "#f2a7ff";
    ctx.lineWidth = 2.2;

    ctx.shadowColor = "rgba(240,125,255,0.45)";
    ctx.shadowBlur = 8;

    ctx.beginPath();

    sketchPoints.forEach((p, i) => {

        const px = xToPixel(p.x);
        const py = yToPixel(p.y);

        if (i === 0) {
            ctx.moveTo(px, py);
        } else {
            ctx.lineTo(px, py);
        }
    });

    ctx.stroke();

    ctx.restore();


    /*
       Drawing points
    */

    ctx.fillStyle = "#ffb9ff";

    for (let i = 0; i < sketchPoints.length; i += 5) {

        const p = sketchPoints[i];

        const px = xToPixel(p.x);
        const py = yToPixel(p.y);

        ctx.beginPath();
        ctx.arc(px, py, 2.2, 0, Math.PI * 2);
        ctx.fill();
    }
}


function drawGraph() {

    if (!canvas.clientWidth || !canvas.clientHeight) {
        return;
    }

    drawGrid();

    drawFunction();

    drawSketch();

    updateStats();

    updatePlaybackPoint(playbackPercent);
}


/* ---------------------------------------------------------
   GRAPH STATS
--------------------------------------------------------- */

function updateStats() {

    statFunction.textContent = expression || "없음";

    statX.textContent =
        formatNumber(xMin) +
        " ~ " +
        formatNumber(xMax);

    statY.textContent =
        formatNumber(yMin) +
        " ~ " +
        formatNumber(yMax);

    statPoints.textContent =
        samples.filter(p => p.y !== null).length.toString();
}


/* ---------------------------------------------------------
   PLOT FUNCTION
--------------------------------------------------------- */

function plotFunction(text) {

    try {

        const fn = compileFunction(text);

        expression = text.trim();

        samples = sampleFunction(fn);

        statFunction.textContent = expression;

        musicStatus.textContent =
            "함수 그래프가 준비되었습니다.";

        musicStatus.className = "music-status";

        drawGraph();

        updateMusicStatus();

    } catch (error) {

        musicStatus.textContent =
            "함수식을 확인해주세요: " + error.message;

        musicStatus.className = "music-status warning";
    }
}


/* ---------------------------------------------------------
   DELETE / RESET
--------------------------------------------------------- */

function deleteFunction() {

    expression = "";

    samples = [];

    functionInput.value = "";

    stopMusic();

    drawGraph();

    musicStatus.textContent =
        "그래프가 삭제되었습니다.";

    musicStatus.className = "music-status";
}


function resetGraph() {

    stopMusic();

    expression = "x^2";

    functionInput.value = "x^2";

    xMin = -10;
    xMax = 10;

    yMin = -10;
    yMax = 10;

    sketchPoints = [];

    sketchMode = false;

    canvasStatus.textContent = "FUNCTION MODE";

    document.getElementById("sketchResult").style.display = "none";

    plotFunction("x^2");
}


/* ---------------------------------------------------------
   AUTO FIT
--------------------------------------------------------- */

function fitGraph() {

    if (!samples.length) {
        return;
    }

    const valid = samples.filter(p => p.y !== null);

    if (!valid.length) {
        return;
    }

    let minY = Infinity;
    let maxY = -Infinity;

    valid.forEach(p => {

        minY = Math.min(minY, p.y);
        maxY = Math.max(maxY, p.y);

    });

    /*
       극단적으로 큰 값 때문에 화면이 망가지는 것을 방지
    */

    if (
        !Number.isFinite(minY) ||
        !Number.isFinite(maxY)
    ) {
        return;
    }

    const range = Math.max(maxY - minY, 2);

    const padding = range * 0.15;

    yMin = minY - padding;
    yMax = maxY + padding;

    drawGraph();
}


/* ---------------------------------------------------------
   ZOOM / PAN
--------------------------------------------------------- */

function zoomAt(factor, centerX = 0.5, centerY = 0.5) {

    const cx =
        xMin +
        centerX * (xMax - xMin);

    const cy =
        yMax -
        centerY * (yMax - yMin);


    const newXRange =
        (xMax - xMin) * factor;

    const newYRange =
        (yMax - yMin) * factor;


    xMin =
        cx -
        centerX * newXRange;

    xMax =
        cx +
        (1 - centerX) * newXRange;


    yMax =
        cy +
        centerY * newYRange;

    yMin =
        cy -
        (1 - centerY) * newYRange;


    drawGraph();
}


/* ---------------------------------------------------------
   SKETCH MODE
--------------------------------------------------------- */

function setSketchMode(active) {

    sketchMode = active;

    if (active) {

        canvasStatus.textContent =
            "SKETCH MODE";

        canvas.style.cursor = "crosshair";

        document.getElementById("canvasHelp").textContent =
            "마우스로 그래프를 그려주세요";

    } else {

        canvasStatus.textContent =
            "FUNCTION MODE";

        canvas.style.cursor = "default";

        document.getElementById("canvasHelp").textContent =
            "휠: 확대/축소 · 드래그: 이동";
    }

    drawGraph();
}


function clearSketch() {

    sketchPoints = [];

    document.getElementById("sketchResult").style.display = "none";

    setSketchMode(false);

    drawGraph();
}


/* ---------------------------------------------------------
   MOUSE EVENTS
--------------------------------------------------------- */

canvas.addEventListener("mousedown", (event) => {

    const rect = canvas.getBoundingClientRect();

    const px = event.clientX - rect.left;
    const py = event.clientY - rect.top;


    if (sketchMode) {

        drawing = true;

        sketchPoints = [];

        sketchPoints.push({
            x: pixelToX(px),
            y: pixelToY(py)
        });

        drawGraph();

        return;
    }


    dragging = true;

    lastMouseX = event.clientX;
    lastMouseY = event.clientY;
});


canvas.addEventListener("mousemove", (event) => {

    const rect = canvas.getBoundingClientRect();

    const px = event.clientX - rect.left;
    const py = event.clientY - rect.top;


    if (sketchMode && drawing) {

        const point = {
            x: pixelToX(px),
            y: pixelToY(py)
        };

        const last =
            sketchPoints[sketchPoints.length - 1];

        /*
           너무 가까운 점은 합치지 않고
           일정 거리 이상의 점만 추가하여
           데이터 크기를 적절하게 유지한다.
        */

        if (!last) {

            sketchPoints.push(point);

        } else {

            const dx = point.x - last.x;
            const dy = point.y - last.y;

            if (Math.sqrt(dx * dx + dy * dy) > 0.03) {

                sketchPoints.push(point);
            }
        }

        drawGraph();

        return;
    }


    if (dragging) {

        const dx = event.clientX - lastMouseX;
        const dy = event.clientY - lastMouseY;

        const xShift =
            dx / canvas.clientWidth *
            (xMax - xMin);

        const yShift =
            dy / canvas.clientHeight *
            (yMax - yMin);


        xMin -= xShift;
        xMax -= xShift;

        yMin += yShift;
        yMax += yShift;


        lastMouseX = event.clientX;
        lastMouseY = event.clientY;

        drawGraph();
    }

});


window.addEventListener("mouseup", () => {

    drawing = false;
    dragging = false;

});


canvas.addEventListener("mouseleave", () => {

    if (!sketchMode) {
        dragging = false;
    }

});


canvas.addEventListener("wheel", (event) => {

    event.preventDefault();

    const rect = canvas.getBoundingClientRect();

    const px =
        event.clientX -
        rect.left;

    const py =
        event.clientY -
        rect.top;

    const centerX =
        px / canvas.clientWidth;

    const centerY =
        py / canvas.clientHeight;

    const factor =
        event.deltaY > 0 ? 1.12 : 0.89;

    zoomAt(factor, centerX, centerY);

}, { passive: false });


/* ---------------------------------------------------------
   SKETCH → CUBIC REGRESSION
--------------------------------------------------------- */

function solveLinearSystem(A, b) {

    const n = b.length;

    const M = A.map((row, i) => [
        ...row,
        b[i]
    ]);


    for (let col = 0; col < n; col++) {

        let pivot = col;

        for (let row = col + 1; row < n; row++) {

            if (
                Math.abs(M[row][col]) >
                Math.abs(M[pivot][col])
            ) {
                pivot = row;
            }
        }


        if (
            Math.abs(M[pivot][col]) <
            1e-12
        ) {
            throw new Error(
                "함수를 근사하기에 충분한 점이 없습니다."
            );
        }


        [M[col], M[pivot]] =
            [M[pivot], M[col]];


        for (let row = col + 1; row < n; row++) {

            const factor =
                M[row][col] /
                M[col][col];

            for (let j = col; j <= n; j++) {

                M[row][j] -=
                    factor * M[col][j];
            }
        }
    }


    const result =
        new Array(n).fill(0);


    for (let i = n - 1; i >= 0; i--) {

        let sum = M[i][n];

        for (let j = i + 1; j < n; j++) {

            sum -=
                M[i][j] *
                result[j];
        }

        result[i] =
            sum /
            M[i][i];
    }

    return result;
}


function cubicRegression(points) {

    if (points.length < 4) {

        throw new Error(
            "최소 4개 이상의 점이 필요합니다."
        );
    }


    /*
       y = ax^3 + bx^2 + cx + d

       정규방정식
       XᵀXβ = Xᵀy
    */

    const A = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ];

    const b = [0,0,0,0];


    points.forEach(p => {

        const x = p.x;
        const y = p.y;

        const row = [
            x*x*x,
            x*x,
            x,
            1
        ];


        for (let i = 0; i < 4; i++) {

            b[i] += row[i] * y;

            for (let j = 0; j < 4; j++) {

                A[i][j] +=
                    row[i] * row[j];
            }
        }

    });


    return solveLinearSystem(A, b);
}


function coefficientsToExpression(c) {

    const a = c[0];
    const b = c[1];
    const d = c[3];
    const e = c[2];

    let parts = [];


    function addTerm(value, power, variable) {

        if (
            !Number.isFinite(value) ||
            Math.abs(value) < 0.00005
        ) {
            return;
        }

        const absValue =
            Math.abs(value);

        const sign =
            value < 0 ? "-" : "+";


        let coefficient =
            formatNumber(absValue);


        let term = "";


        if (power === 0) {

            term = coefficient;

        } else if (power === 1) {

            if (Math.abs(absValue - 1) < 0.00005) {
                term = variable;
            } else {
                term = coefficient + "*" + variable;
            }

        } else {

            if (Math.abs(absValue - 1) < 0.00005) {
                term = variable + "^" + power;
            } else {
                term =
                    coefficient +
                    "*" +
                    variable +
                    "^" +
                    power;
            }
        }


        if (parts.length === 0) {

            if (value < 0) {
                parts.push("-" + term);
            } else {
                parts.push(term);
            }

        } else {

            parts.push(sign + term);
        }
    }


    addTerm(a, 3, "x");
    addTerm(b, 2, "x");
    addTerm(e, 1, "x");
    addTerm(d, 0, "x");


    if (!parts.length) {
        return "0";
    }


    return parts.join(" ");
}


function fitSketchToFunction() {

    if (sketchPoints.length < 4) {

        musicStatus.textContent =
            "손그림 점이 너무 적습니다. 조금 더 길게 그려주세요.";

        musicStatus.className =
            "music-status warning";

        return;
    }


    try {

        const coefficients =
            cubicRegression(sketchPoints);


        const estimated =
            coefficientsToExpression(
                coefficients
            );


        document.getElementById(
            "estimatedFunction"
        ).textContent = estimated;


        document.getElementById(
            "sketchResult"
        ).style.display = "block";


        functionInput.value =
            estimated;


        /*
           근사 함수식을 실제 그래프로 변환
        */

        plotFunction(estimated);

        setSketchMode(false);

        musicStatus.textContent =
            "손그림을 3차 함수로 근사하여 정밀한 그래프를 생성했습니다.";

        musicStatus.className =
            "music-status success";

    } catch (error) {

        musicStatus.textContent =
            "손그림 근사에 실패했습니다: " +
            error.message;

        musicStatus.className =
            "music-status warning";
    }
}


/* ---------------------------------------------------------
   MUSIC GRAPH POINTS
--------------------------------------------------------- */

function createMusicPoints() {

    const valid =
        samples.filter(
            p =>
                p.y !== null &&
                Number.isFinite(p.y)
        );


    if (valid.length < 2) {
        return [];
    }


    /*
       곡 길이와 관계없이
       그래프 전체를 균등하게 다시 샘플링한다.

       중요:
       반복(index % samples.length)을 사용하지 않는다.
       그래프의 처음부터 끝까지 한 번만 진행한다.
    */

    const pointCount =
        Math.min(600, Math.max(180, Math.floor(songDuration * 2)));


    const points = [];


    for (let i = 0; i < pointCount; i++) {

        const ratio =
            i / (pointCount - 1);

        const index =
            Math.round(
                ratio * (valid.length - 1)
            );

        points.push(valid[index]);
    }


    return points;
}


/* ---------------------------------------------------------
   GRAPH Y → CONTINUOUS FREQUENCY
--------------------------------------------------------- */

function graphFrequency(y, lowY, highY) {

    if (highY <= lowY) {
        return 440;
    }


    const normalized =
        clamp(
            (y - lowY) /
            (highY - lowY),
            0,
            1
        );


    /*
       약 2.5 octave 정도의 음역.

       y가 올라갈수록 frequency가 증가한다.
    */

    const minFreq = 110;

    const maxFreq = 880;


    return (
        minFreq *
        Math.pow(
            maxFreq / minFreq,
            normalized
        )
    );
}


/* ---------------------------------------------------------
   BACKGROUND NOTE HELPERS
--------------------------------------------------------- */

function scaleMidi(degree, root = 48) {

    const scale =
        scales[scaleSelect.value] ||
        scales.major;


    const octave =
        Math.floor(degree / scale.length);

    const index =
        degree % scale.length;


    return (
        root +
        octave * 12 +
        scale[index]
    );
}


function currentGraphNoteAtRatio(ratio) {

    const points =
        createMusicPoints();

    if (!points.length) {
        return 60;
    }


    const index =
        Math.round(
            clamp(ratio, 0, 1) *
            (points.length - 1)
        );


    const p = points[index];


    const valid =
        points.map(v => v.y);


    const lo =
        Math.min(...valid);

    const hi =
        Math.max(...valid);


    const freq =
        graphFrequency(
            p.y,
            lo,
            hi
        );


    return (
        69 +
        12 *
        Math.log2(freq / 440)
    );
}


/* ---------------------------------------------------------
   AUDIO NODE HELPERS
--------------------------------------------------------- */

function trackNode(node) {

    activeAudioNodes.push(node);

    return node;
}


function makeTone(
    frequency,
    duration,
    volume,
    wave,
    startTime,
    attack = 0.015,
    release = 0.08
) {

    if (!audioCtx) {
        return;
    }


    const osc =
        trackNode(
            audioCtx.createOscillator()
        );

    const gain =
        trackNode(
            audioCtx.createGain()
        );


    osc.type = wave;

    osc.frequency.setValueAtTime(
        frequency,
        startTime
    );


    gain.gain.setValueAtTime(
        0.0001,
        startTime
    );


    gain.gain.linearRampToValueAtTime(
        volume,
        startTime + attack
    );


    const releaseStart =
        Math.max(
            startTime + attack,
            startTime + duration - release
        );


    gain.gain.setValueAtTime(
        volume,
        releaseStart
    );


    gain.gain.linearRampToValueAtTime(
        0.0001,
        startTime + duration
    );


    osc.connect(gain);

    gain.connect(
        audioCtx.destination
    );


    osc.start(startTime);

    osc.stop(
        startTime + duration + 0.03
    );


    return osc;
}


/* ---------------------------------------------------------
   NOISE / DRUM
--------------------------------------------------------- */

function makeNoise(
    duration,
    volume,
    startTime,
    type = "noise"
) {

    if (!audioCtx) {
        return;
    }


    const buffer =
        audioCtx.createBuffer(
            1,
            audioCtx.sampleRate * duration,
            audioCtx.sampleRate
        );


    const data =
        buffer.getChannelData(0);


    for (let i = 0; i < data.length; i++) {

        data[i] =
            Math.random() * 2 - 1;
    }


    const source =
        trackNode(
            audioCtx.createBufferSource()
        );


    const gain =
        trackNode(
            audioCtx.createGain()
        );


    source.buffer = buffer;


    if (type === "hat") {

        const filter =
            audioCtx.createBiquadFilter();

        filter.type = "highpass";

        filter.frequency.value = 4500;

        source.connect(filter);

        filter.connect(gain);

    } else {

        source.connect(gain);
    }


    gain.gain.setValueAtTime(
        volume,
        startTime
    );


    gain.gain.exponentialRampToValueAtTime(
        0.0001,
        startTime + duration
    );


    gain.connect(
        audioCtx.destination
    );


    source.start(startTime);

    source.stop(
        startTime + duration + 0.02
    );
}


/* ---------------------------------------------------------
   MELODY
--------------------------------------------------------- */

function scheduleGraphMelody(startTime) {

    if (!document.getElementById("layerMelody").checked) {
        return;
    }


    const points =
        createMusicPoints();


    if (points.length < 2) {
        return;
    }


    const yValues =
        points.map(p => p.y);


    const lowY =
        Math.min(...yValues);

    const highY =
        Math.max(...yValues);


    melodyOsc =
        trackNode(
            audioCtx.createOscillator()
        );


    melodyGain =
        trackNode(
            audioCtx.createGain()
        );


    const style =
        styles[styleSelect.value];


    melodyOsc.type =
        style.melodyWave;


    melodyOsc.connect(
        melodyGain
    );


    melodyGain.connect(
        audioCtx.destination
    );


    const volume =
        parseFloat(
            document.getElementById(
                "volMelody"
            ).value
        );


    melodyGain.gain.setValueAtTime(
        0.0001,
        startTime
    );


    const segmentDuration =
        songDuration /
        points.length;


    /*
       핵심 구현:

       i번째 그래프 포인트 =
       songStart + i * segmentDuration

       그래프 전체가 곡 전체에 정확히 한 번 대응한다.
    */

    for (let i = 0; i < points.length; i++) {

        const point =
            points[i];


        const ratio =
            i / (points.length - 1);


        const frequency =
            graphFrequency(
                point.y,
                lowY,
                highY
            );


        const time =
            startTime +
            i * segmentDuration;


        if (i === 0) {

            melodyOsc.frequency.setValueAtTime(
                frequency,
                time
            );

            melodyGain.gain.linearRampToValueAtTime(
                volume,
                time + Math.min(0.08, segmentDuration)
            );

        } else {

            /*
               연속적인 주파수 변화.
               특정 음계 음 하나로 강제하지 않는다.
            */

            melodyOsc.frequency.linearRampToValueAtTime(
                frequency,
                time
            );
        }
    }


    const endTime =
        startTime +
        songDuration;


    melodyGain.gain.setValueAtTime(
        volume,
        Math.max(
            startTime,
            endTime - 0.25
        )
    );


    melodyGain.gain.linearRampToValueAtTime(
        0.0001,
        endTime
    );


    melodyOsc.start(startTime);

    melodyOsc.stop(
        endTime + 0.05
    );
}


/* ---------------------------------------------------------
   BACKGROUND SCHEDULER
--------------------------------------------------------- */

function scheduleBackgroundEvent(index, time) {

    const style =
        styles[styleSelect.value];


    const beatLength =
        60 / style.bpm;


    const scale =
        scales[scaleSelect.value];


    const ratio =
        clamp(
            (time - songStartTime) /
            songDuration,
            0,
            1
        );


    /*
       그래프의 현재 위치를 반주 코드 변화에도 사용한다.
       그래프 전체 진행과 반주도 함께 움직인다.
    */

    const graphMidi =
        currentGraphNoteAtRatio(ratio);


    const baseRoot =
        48 +
        Math.round(
            (graphMidi - 60) / 12
        ) * 12;


    const chordDegree =
        Math.floor(
            ratio * 8
        ) % 8;


    const chordRoot =
        scaleMidi(
            chordDegree,
            baseRoot
        );


    /* ---------------- DRUMS ---------------- */

    if (
        document.getElementById("layerDrums").checked
    ) {

        const volume =
            parseFloat(
                document.getElementById(
                    "volDrums"
                ).value
            );


        /*
           4분의 4박자 느낌을 만들기 위해
           킥과 스네어를 자동 배치한다.
        */

        const beatInBar =
            index % 4;


        if (
            beatInBar === 0 ||
            beatInBar === 2
        ) {

            makeKick(
                time,
                volume
            );

        } else {

            makeSnare(
                time,
                volume * 0.75
            );
        }
    }


    /* ---------------- PERCUSSION ---------------- */

    if (
        document.getElementById("layerPerc").checked
    ) {

        const volume =
            parseFloat(
                document.getElementById(
                    "volPerc"
                ).value
            );


        if (index % 2 === 1) {

            makeNoise(
                0.045,
                volume * 0.7,
                time,
                "hat"
            );
        }
    }


    /* ---------------- BASS ---------------- */

    if (
        document.getElementById("layerBass").checked &&
        index % style.bassEvery === 0
    ) {

        const volume =
            parseFloat(
                document.getElementById(
                    "volBass"
                ).value
            );


        const bassMidi =
            chordRoot - 12;


        makeTone(
            midiToFreq(bassMidi),
            beatLength * style.bassEvery * 0.85,
            volume,
            style.bassWave,
            time,
            0.025,
            0.12
        );
    }


    /* ---------------- CHORDS ---------------- */

    if (
        document.getElementById("layerChords").checked &&
        index % 4 === 0
    ) {

        const volume =
            parseFloat(
                document.getElementById(
                    "volChords"
                ).value
            );


        const chordIntervals =
            scale === scales.minor
                ? [0, 3, 7]
                : [0, 4, 7];


        chordIntervals.forEach(interval => {

            makeTone(
                midiToFreq(
                    chordRoot + interval
                ),
                beatLength * 3.6,
                volume / 3,
                style.chordWave,
                time,
                0.12,
                0.4
            );

        });
    }


    /* ---------------- ARPEGGIO ---------------- */

    if (
        document.getElementById("layerArp").checked
    ) {

        const volume =
            parseFloat(
                document.getElementById(
                    "volArp"
                ).value
            );


        const arpNotes =
            [0, 2, 4, 2];


        const note =
            scaleMidi(
                chordDegree + arpNotes[index % 4],
                baseRoot
            );


        makeTone(
            midiToFreq(note + 12),
            beatLength * 0.65,
            volume,
            style.melodyWave,
            time,
            0.01,
            0.08
        );
    }


    /* ---------------- PAD ---------------- */

    if (
        document.getElementById("layerPad").checked &&
        index % 8 === 0
    ) {

        const volume =
            parseFloat(
                document.getElementById(
                    "volPad"
                ).value
            );


        const padNotes =
            [0, 4, 7];


        padNotes.forEach(interval => {

            makeTone(
                midiToFreq(
                    chordRoot +
                    interval +
                    12
                ),
                beatLength * 7.5,
                volume / 3,
                style.padWave,
                time,
                0.45,
                1.0
            );

        });
    }


    /* ---------------- TEXTURE ---------------- */

    if (
        document.getElementById("layerTexture").checked &&
        index % 8 === 4
    ) {

        const volume =
            parseFloat(
                document.getElementById(
                    "volTexture"
                ).value
            );


        makeNoise(
            0.8,
            volume,
            time,
            "noise"
        );
    }
}


/* ---------------------------------------------------------
   KICK
--------------------------------------------------------- */

function makeKick(time, volume) {

    const osc =
        trackNode(
            audioCtx.createOscillator()
        );

    const gain =
        trackNode(
            audioCtx.createGain()
        );


    osc.type = "sine";

    osc.frequency.setValueAtTime(
        125,
        time
    );

    osc.frequency.exponentialRampToValueAtTime(
        48,
        time + 0.15
    );


    gain.gain.setValueAtTime(
        volume,
        time
    );

    gain.gain.exponentialRampToValueAtTime(
        0.0001,
        time + 0.18
    );


    osc.connect(gain);

    gain.connect(
        audioCtx.destination
    );


    osc.start(time);

    osc.stop(
        time + 0.2
    );
}


/* ---------------------------------------------------------
   SNARE
--------------------------------------------------------- */

function makeSnare(time, volume) {

    makeNoise(
        0.12,
        volume,
        time,
        "noise"
    );
}


/* ---------------------------------------------------------
   AUDIO START
--------------------------------------------------------- */

async function startMusic() {

    if (playing) {
        return;
    }


    if (!samples.some(p => p.y !== null)) {

        musicStatus.textContent =
            "먼저 함수 그래프를 만들어주세요.";

        musicStatus.className =
            "music-status warning";

        return;
    }


    songDuration =
        parseInt(
            durationSelect.value
        );


    if (!audioCtx) {

        audioCtx =
            new (
                window.AudioContext ||
                window.webkitAudioContext
            )();
    }


    if (audioCtx.state === "suspended") {

        await audioCtx.resume();
    }


    stopAudioNodesOnly();


    playing = true;

    playbackPercent = 0;

    beatIndex = 0;

    scheduledEvents.clear();


    songStartTime =
        audioCtx.currentTime +
        0.12;


    const style =
        styles[styleSelect.value];


    const beatLength =
        60 / style.bpm;


    nextBeatTime =
        songStartTime;


    totalTimeText.textContent =
        formatTime(songDuration);


    musicStatus.textContent =
        "그래프 전체를 곡 전체 시간에 대응하여 재생 중입니다.";

    musicStatus.className =
        "music-status";


    /*
       그래프 멜로디는 하나의 OscillatorNode를 사용한다.
       수백 개의 oscillator를 만들지 않고
       frequency ramp를 연결하여 5분 재생도 효율적으로 처리한다.
    */

    scheduleGraphMelody(
        songStartTime
    );


    schedulerTimer =
        setInterval(
            audioScheduler,
            100
        );


    animationFrame =
        requestAnimationFrame(
            updatePlayback
        );
}


/* ---------------------------------------------------------
   AUDIO SCHEDULER
--------------------------------------------------------- */

function audioScheduler() {

    if (!playing || !audioCtx) {
        return;
    }


    const style =
        styles[styleSelect.value];


    const beatLength =
        60 / style.bpm;


    const lookAhead =
        0.5;


    const now =
        audioCtx.currentTime;


    while (
        nextBeatTime <
        now + lookAhead
    ) {

        const elapsed =
            nextBeatTime -
            songStartTime;


        if (
            elapsed >=
            songDuration
        ) {
            break;
        }


        const eventKey =
            beatIndex;


        if (
            !scheduledEvents.has(
                eventKey
            )
        ) {

            scheduledEvents.add(
                eventKey
            );


            scheduleBackgroundEvent(
                beatIndex,
                nextBeatTime
            );
        }


        beatIndex++;

        nextBeatTime += beatLength;
    }
}


/* ---------------------------------------------------------
   PLAYBACK UI
--------------------------------------------------------- */

function updatePlayback() {

    if (!playing || !audioCtx) {
        return;
    }


    const elapsed =
        audioCtx.currentTime -
        songStartTime;


    playbackPercent =
        clamp(
            elapsed /
            songDuration,
            0,
            1
        );


    progressFill.style.width =
        (playbackPercent * 100) +
        "%";


    currentTimeText.textContent =
        formatTime(elapsed);


    updatePlaybackPoint(
        playbackPercent
    );


    if (
        elapsed >=
        songDuration
    ) {

        finishMusic();

        return;
    }


    animationFrame =
        requestAnimationFrame(
            updatePlayback
        );
}


/* ---------------------------------------------------------
   GRAPH PLAYBACK POINT
--------------------------------------------------------- */

function updatePlaybackPoint(percent) {

    if (
        !samples.length ||
        !canvas.clientWidth ||
        !canvas.clientHeight
    ) {

        playPoint.style.display =
            "none";

        return;
    }


    const valid =
        samples.filter(
            p =>
                p.y !== null &&
                Number.isFinite(p.y)
        );


    if (!valid.length) {

        playPoint.style.display =
            "none";

        return;
    }


    const index =
        Math.round(
            percent *
            (valid.length - 1)
        );


    const point =
        valid[
            clamp(
                index,
                0,
                valid.length - 1
            )
        ];


    const px =
        xToPixel(point.x);

    const py =
        yToPixel(point.y);


    playPoint.style.display =
        "block";


    playPoint.style.left =
        px + "px";

    playPoint.style.top =
        py + "px";
}


/* ---------------------------------------------------------
   STOP AUDIO NODES
--------------------------------------------------------- */

function stopAudioNodesOnly() {

    activeAudioNodes.forEach(node => {

        try {

            node.disconnect();

        } catch (e) {}

        try {

            if (
                typeof node.stop ===
                "function"
            ) {
                node.stop();
            }

        } catch (e) {}

    });


    activeAudioNodes = [];


    melodyOsc = null;

    melodyGain = null;
}


/* ---------------------------------------------------------
   STOP MUSIC
--------------------------------------------------------- */

function stopMusic() {

    playing = false;


    if (schedulerTimer) {

        clearInterval(
            schedulerTimer
        );

        schedulerTimer = null;
    }


    if (animationFrame) {

        cancelAnimationFrame(
            animationFrame
        );

        animationFrame = null;
    }


    stopAudioNodesOnly();


    playbackPercent = 0;


    progressFill.style.width =
        "0%";


    currentTimeText.textContent =
        "0:00";


    updatePlaybackPoint(0);


    musicStatus.textContent =
        "재생이 정지되었습니다.";

    musicStatus.className =
        "music-status";
}


/* ---------------------------------------------------------
   FINISH
--------------------------------------------------------- */

function finishMusic() {

    playing = false;


    if (schedulerTimer) {

        clearInterval(
            schedulerTimer
        );

        schedulerTimer = null;
    }


    if (animationFrame) {

        cancelAnimationFrame(
            animationFrame
        );

        animationFrame = null;
    }


    playbackPercent = 1;


    progressFill.style.width =
        "100%";


    currentTimeText.textContent =
        formatTime(songDuration);


    updatePlaybackPoint(1);


    musicStatus.textContent =
        "✓ 그래프를 하나의 곡으로 변환했습니다.";

    musicStatus.className =
        "music-status success";


    /*
       이미 종료 시간이 지나면
       AudioNode는 자연스럽게 끝난다.
    */

    setTimeout(() => {

        stopAudioNodesOnly();

    }, 500);
}


/* ---------------------------------------------------------
   STATUS
--------------------------------------------------------- */

function updateMusicStatus() {

    if (!samples.some(p => p.y !== null)) {

        musicStatus.textContent =
            "그래프를 먼저 만들어주세요.";

        return;
    }


    const duration =
        parseInt(
            durationSelect.value
        );


    musicStatus.textContent =
        formatTime(duration) +
        " 길이의 음악을 만들 준비가 되었습니다.";
}


/* ---------------------------------------------------------
   BUTTON EVENTS
--------------------------------------------------------- */

document.getElementById(
    "plotBtn"
).addEventListener(
    "click",
    () => {

        plotFunction(
            functionInput.value
        );
    }
);


functionInput.addEventListener(
    "keydown",
    event => {

        if (event.key === "Enter") {

            plotFunction(
                functionInput.value
            );
        }
    }
);


document.getElementById(
    "deleteBtn"
).addEventListener(
    "click",
    deleteFunction
);


document.getElementById(
    "resetBtn"
).addEventListener(
    "click",
    resetGraph
);


document.getElementById(
    "fitBtn"
).addEventListener(
    "click",
    fitGraph
);


document.getElementById(
    "zoomInBtn"
).addEventListener(
    "click",
    () => zoomAt(0.8)
);


document.getElementById(
    "zoomOutBtn"
).addEventListener(
    "click",
    () => zoomAt(1.25)
);


document.getElementById(
    "centerBtn"
).addEventListener(
    "click",
    () => {

        const width =
            xMax - xMin;

        const height =
            yMax - yMin;


        const centerX =
            (xMin + xMax) / 2;

        const centerY =
            (yMin + yMax) / 2;


        xMin =
            centerX -
            width / 2;

        xMax =
            centerX +
            width / 2;

        yMin =
            centerY -
            height / 2;

        yMax =
            centerY +
            height / 2;


        drawGraph();
    }
);


/* ---------------------------------------------------------
   SKETCH BUTTONS
--------------------------------------------------------- */

document.getElementById(
    "sketchBtn"
).addEventListener(
    "click",
    () => {

        setSketchMode(
            !sketchMode
        );

        if (sketchMode) {

            musicStatus.textContent =
                "그래프 위에서 원하는 모양을 그려주세요.";

        }
    }
);


document.getElementById(
    "fitSketchBtn"
).addEventListener(
    "click",
    fitSketchToFunction
);


document.getElementById(
    "clearSketchBtn"
).addEventListener(
    "click",
    clearSketch
);


/* ---------------------------------------------------------
   MUSIC CONTROLS
--------------------------------------------------------- */

document.getElementById(
    "playBtn"
).addEventListener(
    "click",
    startMusic
);


document.getElementById(
    "stopBtn"
).addEventListener(
    "click",
    stopMusic
);


durationSelect.addEventListener(
    "change",
    () => {

        if (!playing) {
            updateMusicStatus();
        }

        totalTimeText.textContent =
            formatTime(
                parseInt(
                    durationSelect.value
                )
            );
    }
);


styleSelect.addEventListener(
    "change",
    () => {

        if (!playing) {
            updateMusicStatus();
        }
    }
);


scaleSelect.addEventListener(
    "change",
    () => {

        if (!playing) {
            updateMusicStatus();
        }
    }
);


/* ---------------------------------------------------------
   WINDOW EVENTS
--------------------------------------------------------- */

window.addEventListener(
    "resize",
    resizeCanvas
);


/* ---------------------------------------------------------
   INITIALIZE
--------------------------------------------------------- */

resizeCanvas();

plotFunction("x^2");

totalTimeText.textContent =
    formatTime(
        parseInt(
            durationSelect.value
        )
    );

updateMusicStatus();

</script>

</body>
</html>
"""

components.html(
    HTML,
    height=1450,
    scrolling=True
)
