import streamlit as st

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Yeeun | Persona Page",
    layout="centered"
)

# -------------------------
# CSS
# -------------------------
st.markdown("""
<style>
body {
    background-color: #f6f7f4;
    color: #1c1c1e;
}

.card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 6px 14px rgba(0,0,0,0.07);
    margin-bottom: 16px;
}

.section-title {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 10px;
    font-weight: 600;
    color: #4f5d32;
    font-size: 15px;
}

.section-title img {
    width: 18px;
    height: 18px;
}

p, li {
    font-size: 14px;
    line-height: 1.6;
}

.icon img {
    width: 38px;
    padding: 9px;
    border-radius: 12px;
    background-color: #f1f3ec;
    transition: 0.2s;
}

.icon img:hover {
    background-color: #AEB877;
}
            
.profile-wrapper {
    display: flex;
    justify-content: center;
    margin-top: 14px;
    margin-bottom: 6px;
}

.profile-img {
    width: 110px;
    height: 110px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid #ffffff;
    box-shadow: 0 8px 20px rgba(0,0,0,0.12);
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------
st.markdown("""
<h1 style="text-align:center; color:#4f5d32; margin-bottom:2px;">yeeun 🌿☁️ </h1>
<p style="text-align:center; color:#6e6e73; margin-top:0; font-size:14px;">
INFP · 감정을 기록하는 사람 · 바이브 코딩
</p>
""", unsafe_allow_html=True)

st.markdown("""
<div class="profile-wrapper">
    <img 
        src="https://images.unsplash.com/photo-1507146426996-ef05306b995a"
        class="profile-img"
    >
</div>
""", unsafe_allow_html=True)


st.write("")

# -------------------------
# Layout
# -------------------------
col1, col2 = st.columns([1, 1])

# ---------- LEFT ----------
with col1:
    st.markdown("""
    <div class="card">
        <div class="section-title">
            <img src="https://cdn-icons-png.flaticon.com/512/847/847969.png">
            소개
        </div>
        <p>
        원예은 (won yeeun)<br>
        한성대학교 컴퓨터공학과<br>
        sesac 2기
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<a href="https://youtu.be/J_RddSZnATU?si=jJny0tReUPysiqCF" 
   target="_blank" 
   style="text-decoration:none; color:inherit;">
    <div class="card" style="cursor:pointer;">
        <div class="section-title">
            <img src="https://cdn-icons-png.flaticon.com/512/777/777242.png">
            좋아하는 영화
        </div>
        <p>
        <b>만약에 우리</b><br>
        사랑과 기억이 겹쳐지는 순간을 그린 이야기
        </p>
    </div>
</a>
""", unsafe_allow_html=True)

    st.markdown("""
<a href="https://youtu.be/BA-_KVEZc1U?si=FVfW2vSmDMaAYWZn" 
   target="_blank"
   style="text-decoration:none; color:inherit;">
    <div class="card" style="cursor:pointer;">
        <div class="section-title">
            <img src="https://cdn-icons-png.flaticon.com/512/727/727245.png">
            좋아하는 노래
        </div>
        <p style="margin-bottom:12px;">
            <b>잔향 – 윤석원</b><br>
            조용히 마음에 남는 이별의 온기
        </p>
    </div>
</a>
""", unsafe_allow_html=True)



# ---------- RIGHT ----------
with col2:
    st.markdown("""
    <div class="card">
        <div class="section-title">
            <img src="https://cdn-icons-png.flaticon.com/512/1828/1828884.png">
            취향
        </div>
        <ul style="padding-left:18px; margin:0;">
            <li>플레이리스트 만들기</li>
            <li>감정적인 영화 감상</li>
            <li>다이어리 적기</li>
            <li>조용한 카페</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="section-title">
            <img src="https://cdn-icons-png.flaticon.com/512/3075/3075977.png">
            요즘 관심사
        </div>
        <p>
        Streamlit 기반 UI 설계<br>
        생성형 AI와 함께하는 개발<br>
        감정이 남는 사용자 경험
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="section-title">
            <img src="https://cdn-icons-png.flaticon.com/512/929/929564.png">
            연결
        </div>
        <div style="display:flex; gap:12px;">
            <a class="icon" href="https://instagram.com/1_ye.tk" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174855.png">
            </a>
            <a class="icon" href="https://github.com/yetk124" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png">
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# Footer
# -------------------------
st.markdown("""
<p style="text-align:center; color:#8e8e93; font-size:12px; margin-top:28px;">
© 2026 Yeeun · Vibe Coding
</p>
""", unsafe_allow_html=True)
