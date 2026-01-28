import streamlit as st
import pandas as pd
from datetime import date
import random
import os

# =========================
# 파일 경로
# =========================
DATA_DIR = "data"
DATA_FILE = f"{DATA_DIR}/diary.csv"
os.makedirs(DATA_DIR, exist_ok=True)

# =========================
# 페이지 설정
# =========================
st.set_page_config(
    page_title="하루끝",
    layout="centered"
)

# =========================
# 스타일
# =========================
st.markdown("""
<style>
body {
    background-color: #F7F8FC;
    color: #374151;
}

.card {
    background: linear-gradient(180deg, #FFFFFF, #FAFAFF);
    border-radius: 24px;
    padding: 26px;
    margin-bottom: 20px;
    box-shadow: 0 16px 36px rgba(99, 102, 241, 0.12);
}

.app-title {
    font-size: 34px;
    font-weight: 800;
    text-align: center;
    color: #6366F1;
}

.app-sub {
    text-align: center;
    color: #9CA3AF;
    margin-bottom: 36px;
}

.section-title {
    font-weight: 700;
    margin-bottom: 12px;
}

button {
    border-radius: 16px !important;
    height: 52px !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 데이터 로드
# =========================
if "기록" not in st.session_state:
    if os.path.exists(DATA_FILE):
        st.session_state.기록 = pd.read_csv(DATA_FILE).to_dict("records")
    else:
        st.session_state.기록 = []

if "선택된_기분" not in st.session_state:
    st.session_state.선택된_기분 = None

# =========================
# 헤더
# =========================
col_left, col_center, col_right = st.columns([1.05, 1, 0.95])


with col_center:
    st.image("assets/logo.png", width=180)
st.markdown('<div class="app-sub">하루를 부드럽게 정리하는 작은 습관</div>', unsafe_allow_html=True)

# =========================
# 탭 (캘린더 제거)
# =========================
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🌿 소개", "✍️ 작성", "📘 기록", "📊 감정 흐름", "🎁 랜덤 회고"]
)

# =========================
# 🌿 소개
# =========================
with tab1:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <div style="font-size:48px; margin-bottom:8px;">🌙</div>
        <h2 style="font-size:20px; color:#6366F1; margin:0;">
            오늘의 한 줄 회고
        </h2>
        <p style="color:#6B7280; margin-top:8px;">
            하루를 정리하는 가장 부드러운 방법
        </p>
        <div style="
            margin-top:32px;
            display:grid;
            grid-template-columns: repeat(3, 1fr);
            gap:16px;">
            <div style="background:#F3F4FF; padding:18px; border-radius:18px;">
                <div style="font-size:28px;">✍️</div>
                <b>한 줄 기록</b>
                <p style="font-size:13px; color:#6B7280; margin-top:6px;">
                    길게 쓰지 않아도 괜찮아요
                </p>
            </div>
            <div style="background:#ECFDF5; padding:18px; border-radius:18px;">
                <div style="font-size:28px;">😊</div>
                <b>감정 선택</b>
                <p style="font-size:13px; color:#6B7280; margin-top:6px;">
                    말로 설명하지 않아도 돼요
                </p>
            </div>
            <div style="background:#FFF7ED; padding:18px; border-radius:18px;">
                <div style="font-size:28px;">📊</div>
                <b>감정 흐름</b>
                <p style="font-size:13px; color:#6B7280; margin-top:6px;">
                    나의 패턴을 한눈에
                </p>
            </div>
        </div>
        <p style="margin-top:28px; color:#9CA3AF; font-size:14px;">
            오늘 하루도 잘 버텨냈어요 🌱
        </p>
    </div>
    """, unsafe_allow_html=True)


# =========================
# ✍️ 작성
# =========================
with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    selected_date = st.date_input("📅 회고 날짜", value=date.today())
    selected_date_str = selected_date.isoformat()

    if any(r["날짜"] == selected_date_str for r in st.session_state.기록):
        st.info("이 날짜에는 이미 회고가 있어요 🌙")
    else:
        moods = {"좋음": "😊", "보통": "🙂", "우울": "😔", "화남": "😡"}
        cols = st.columns(4)

        for i, (m, e) in enumerate(moods.items()):
            with cols[i]:
                if st.button(f"{e}\n{m}", key=f"{m}_{selected_date_str}"):
                    st.session_state.선택된_기분 = m

        content = st.text_area("오늘의 한 줄", placeholder="그날의 감정을 한 줄로 남겨보세요")

        if st.button("💾 저장하기", type="primary"):
            if not st.session_state.선택된_기분 or not content.strip():
                st.warning("기분과 내용을 모두 입력해주세요!")
            else:
                st.session_state.기록.append({
                    "날짜": selected_date_str,
                    "기분": st.session_state.선택된_기분,
                    "회고": content
                })
                pd.DataFrame(st.session_state.기록).to_csv(DATA_FILE, index=False, encoding="utf-8-sig")
                st.success("회고가 저장되었어요 🌸")
                st.session_state.선택된_기분 = None
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# 📘 기록
# =========================
with tab3:
    if st.session_state.기록:
        df = pd.DataFrame(st.session_state.기록).sort_values("날짜", ascending=False)
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.dataframe(df, hide_index=True, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# =========================
# 📊 감정 흐름 (새 기능)
# =========================
with tab4:
    if st.session_state.기록:
        import matplotlib.pyplot as plt
        import matplotlib.font_manager as fm
        import platform

        # =========================
        # 한글 폰트 설정
        # =========================
        if platform.system() == "Windows":
            font_path = "C:/Windows/Fonts/malgun.ttf"
            font_name = fm.FontProperties(fname=font_path).get_name()
            plt.rc("font", family=font_name)
        elif platform.system() == "Darwin":
            plt.rc("font", family="AppleGothic")
        else:
            plt.rc("font", family="NanumGothic")

        plt.rcParams["axes.unicode_minus"] = False

        # =========================
        # 데이터
        # =========================
        df = pd.DataFrame(st.session_state.기록)
        mood_count = df["기분"].value_counts()

        mood_colors = {
            "좋음": "#A5B4FC",
            "보통": "#93C5FD",
            "우울": "#D1D5DB",
            "화남": "#FCA5A5"
        }
        colors = [mood_colors.get(m, "#CBD5E1") for m in mood_count.index]

        # =========================
        # 카드 UI
        # =========================

        # =========================
        # 도넛 차트
        # =========================
        fig, ax = plt.subplots(figsize=(3.5, 3.5))

        wedges, texts = ax.pie(
            mood_count.values,
            labels=mood_count.index,
            colors=colors,
            startangle=90,
            counterclock=False,
            wedgeprops=dict(width=0.38, edgecolor="white")
        )

        # 중앙 텍스트
        total = mood_count.sum()
        ax.text(
            0, 0,
            f"{total}일\n기록",
            ha="center",
            va="center",
            fontsize=12,
            fontweight="bold",
            color="#374151"
        )

        ax.set(aspect="equal")
        fig.patch.set_alpha(0)

# =========================
# ✅ 가운데 정렬용 컬럼
# =========================
        col_left, col_center, col_right = st.columns([1, 2, 1])

        with col_center:
            st.pyplot(fig, use_container_width=False)

            most = mood_count.idxmax()
            st.markdown(
                f"""
                <p style="text-align:center; color:#6B7280; font-size:14px; margin-top:8px;">
                    최근에는 <b>{most}</b> 감정이 가장 많아요 🌱
                </p>
                """,
                unsafe_allow_html=True
            )



# =========================
# 🎁 랜덤 회고
# =========================
with tab5:
    if st.session_state.기록:
        if st.button("✨ 랜덤 회고 꺼내기", use_container_width=True):
            r = random.choice(st.session_state.기록)
            st.success(f"📅 {r['날짜']} · {r['기분']}\n\n{r['회고']}")
