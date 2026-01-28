import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Dino Jump", layout="centered")

# =====================
# App UI (Game App 느낌)
# =====================
st.markdown("""
<style>
body,[data-testid="stApp"]{
    background: linear-gradient(#f6f4ef, #eae6dc);
}
.app{
    max-width:480px;
    margin:auto;
}
.card{
    background: linear-gradient(#1b1b1b, #0f0f0f);
    border-radius:22px;
    padding:16px;
    box-shadow:0 16px 40px rgba(0,0,0,0.35);
}
.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    color:#AEB877;
    margin-bottom:50px;
}
.title{
    font-weight:800;
    letter-spacing:0.5px;
}
.sub{
    font-size:12px;
    opacity:.7;
}
.legend{
    display:flex;
    justify-content:space-around;
    margin-top:10px;
    font-size:11px;
    color:#576A8F;
}
.legend span{
    display:flex;
    align-items:center;
    gap:6px;
}
.icon{
    width:14px;
    height:14px;
    border-radius:4px;
}
.cactus{background:#ff5a5a}
.water{background:#4aa3ff}
.glue{background:#ffd84a}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="app">', unsafe_allow_html=True)

# =====================
# Header
# =====================
st.markdown("""
<div class="header">
  <div class="title">🦖 DINO JUMP</div>
  <div class="sub">SPACE / TAP</div>
</div>
""", unsafe_allow_html=True)

# =====================
# Game (HTML + Canvas)
# =====================
html("""
<!DOCTYPE html>
<html>
<head>
<style>
body{margin:0}
canvas{
  display:block;
  margin:auto;
  background: linear-gradient(#2c2b28, #1b1a18);
}
</style>
</head>
<body>

<canvas id="game" width="400" height="400"></canvas>

<script>
const c = document.getElementById("game");
const ctx = c.getContext("2d");

const GROUND = 320;
let gameOver = false;

// Dino
const dino = { x: 60, y: GROUND, vy: 0, jumping: false };

// Hitbox
function hitbox(){
  return { x: dino.x+6, y: dino.y-28, w:18, h:26 };
}

// Obstacles
let obstacles = [];
let frame = 0;

// Physics
const GRAVITY = 0.8;
const JUMP = -12;
let baseSpeed = 4;
let speed = 4;
let score = 0;

// Effects
let slowUntil = 0;
let freezeUntil = 0;

function resetGame(){
  obstacles=[];
  dino.y=GROUND; dino.vy=0; dino.jumping=false;
  gameOver=false; score=0;
  baseSpeed=4; speed=4;
  slowUntil=0; freezeUntil=0;
}

function spawnObstacle(){
  const r = Math.random();
  let type = r < 0.55 ? "cactus" : r < 0.75 ? "water" : "glue";
  obstacles.push({ x:400, type:type });
}

function update(){
  if(gameOver) return;
  frame++;

  const now = Date.now();
  if(now < freezeUntil) return;
  speed = now < slowUntil ? baseSpeed * 0.4 : baseSpeed;

  // Dino physics
  dino.vy += GRAVITY;
  dino.y += dino.vy;
  if(dino.y >= GROUND){ dino.y=GROUND; dino.vy=0; dino.jumping=false; }

  if(frame % 120 === 0) spawnObstacle();

  obstacles.forEach(o => o.x -= speed);
  obstacles = obstacles.filter(o => o.x > -40);

  const hb = hitbox();
  obstacles.forEach(o=>{
    let ow=22, oh=32;
    if(
      hb.x < o.x+ow &&
      hb.x+hb.w > o.x &&
      hb.y < GROUND &&
      hb.y+hb.h > GROUND-oh
    ){
      if(o.type==="cactus") gameOver=true;
      if(o.type==="water") slowUntil = Date.now()+2000;
      if(o.type==="glue") freezeUntil = Date.now()+900;
      o.hit=true;
    }
  });

  obstacles = obstacles.filter(o=>!o.hit || o.type==="cactus");
  score++; baseSpeed+=0.0005;
}

function drawDino(){
  ctx.fillStyle="#fff";
  ctx.fillRect(dino.x, dino.y-30, 28, 30);
  ctx.fillRect(dino.x+18, dino.y-42, 20, 18);
  ctx.fillRect(dino.x-10, dino.y-20, 10, 10);
  ctx.fillRect(dino.x+4, dino.y-10, 6, 10);
  ctx.fillRect(dino.x+16, dino.y-10, 6, 10);
}

function drawObstacle(o){
  if(o.type==="cactus"){
    ctx.fillStyle="#ff5a5a";
    ctx.fillRect(o.x, GROUND-34, 18, 34);
    ctx.fillRect(o.x-6, GROUND-20, 6, 10);
    ctx.fillRect(o.x+18, GROUND-24, 6, 12);
  }
  if(o.type==="water"){
    ctx.fillStyle="#4aa3ff";
    ctx.beginPath();
    ctx.arc(o.x+11, GROUND-10, 10, 0, Math.PI*2);
    ctx.fill();
  }
  if(o.type==="glue"){
    ctx.fillStyle="#ffd84a";
    ctx.beginPath();
    ctx.moveTo(o.x, GROUND-6);
    ctx.quadraticCurveTo(o.x+11, GROUND-22, o.x+22, GROUND-6);
    ctx.fill();
  }
}

function draw(){
  ctx.clearRect(0,0,400,400);

  // Ground
  ctx.fillStyle="#5c4b2a";
  ctx.fillRect(0, GROUND+2, 400, 6);

  drawDino();
  obstacles.forEach(drawObstacle);

  ctx.fillStyle="#ddd";
  ctx.font="14px Arial";
  ctx.fillText("Score: "+score, 12, 22);

  if(gameOver){
    ctx.fillStyle="#fff";
    ctx.font="20px Arial";
    ctx.fillText("GAME OVER", 130, 180);
    ctx.font="12px Arial";
    ctx.fillText("Tap or Space to Restart", 118, 210);
  }
}

function loop(){ update(); draw(); requestAnimationFrame(loop); }

function jump(){
  if(gameOver){ resetGame(); return; }
  if(!dino.jumping){ dino.vy=JUMP; dino.jumping=true; }
}

window.addEventListener("keydown",e=>{ if(e.code==="Space") jump(); });
c.addEventListener("click",jump);

loop();
</script>
</body>
</html>
""", height=520)

# =====================
# Legend
# =====================
st.markdown("""
<div class="legend">
  <span><i class="icon cactus"></i> 선인장 (Game Over)</span>
  <span><i class="icon water"></i> 물 (느려짐)</span>
  <span><i class="icon glue"></i> 본드 (멈춤)</span>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
