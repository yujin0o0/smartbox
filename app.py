import streamlit as st

st.set_page_config(
    page_title="스마트 건의함",
    page_icon="📢",
    layout="centered"
)

# 2. 메인 화면 타이틀 및 소개
st.title("📢 3학년8반 스마트 건의함")
st.markdown("---")
st.subheader("우리 반의 목소리가 현실이 되는 공간입니다.")
st.write("익명성이 철저히 보장되니, 학급의 발전과 편의를 위한 소중한 의견을 자유롭게 남겨주세요!")

import random

html = "<style>"
html += """
.boom{
position:fixed;
font-size:45px;
animation:explode 2s ease-out forwards;
z-index:9999;
}
@keyframes explode{
0%{transform:translateY(0) scale(.2);opacity:1;}
100%{transform:translateY(-500px) scale(2.5) rotate(720deg);opacity:0;}
}
"""
html += "</style>"

for i in range(25):
    left = random.randint(0,95)
    delay = random.random()*0.8
    html += f"""
    <div class="boom"
    style="left:{left}%;bottom:0;
    animation-delay:{delay}s;">
    🚨
    </div>
    """

st.markdown(html, unsafe_allow_html=True)
