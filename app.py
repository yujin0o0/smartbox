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
st.write("https://malleable-verdict-0bb.notion.site/a943a7db7654827b882a01be2d3c83d2?pvs=105")

# 6. 푸터(Footer) 및 안내
st.markdown("---")
st.caption("⚙️ 제작: [yujin] (UI/UX 및 스트림릿 기반 노코드 웹앱 프로토타입)")
</script>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* 전체 페이지 */
.stApp{
    border:12px solid #ff0000;
    border-radius:25px;
    padding:25px;
    background:linear-gradient(135deg,#fff7f7,#ffeaea,#fff7f7);
    animation:borderGlow 1.5s infinite alternate;
}

/* 빨간 테두리 빛나는 효과 */
@keyframes borderGlow{
    from{
        box-shadow:0 0 15px red;
    }
    to{
        box-shadow:0 0 45px crimson;
    }
}

/* 제목 */
h1{
    text-align:center;
    color:#d10000;
    text-shadow:
        0 0 8px red,
        0 0 20px red;
    animation:titleFlash 1s infinite alternate;
}

@keyframes titleFlash{
    from{transform:scale(1);}
    to{transform:scale(1.03);}
}

/* 버튼 */
.stButton>button{
    background:#ff2020;
    color:white;
    border-radius:15px;
    border:none;
    font-size:20px;
    transition:0.3s;
}

.stButton>button:hover{
    transform:scale(1.08);
    box-shadow:0 0 30px red;
}

</style>
""", unsafe_allow_html=True)
import random

html = """
<style>

.siren{
    position:fixed;
    bottom:-80px;
    font-size:55px;
    animation:boom 3s linear forwards;
    z-index:9999;
}

@keyframes boom{

0%{
transform:translateY(0) scale(.2) rotate(0deg);
opacity:1;
}

50%{
opacity:1;
}

100%{
transform:translateY(-110vh)
translateX(var(--x))
scale(2.5)
rotate(720deg);
opacity:0;
}

}

</style>
"""

for i in range(40):

    left=random.randint(0,95)

    delay=random.random()*1.2

    move=random.randint(-250,250)

    size=random.randint(35,75)

    html+=f"""
<div class='siren'
style='left:{left}%;
font-size:{size}px;
animation-delay:{delay}s;
--x:{move}px;'>
🚨
</div>
"""

st.markdown(html, unsafe_allow_html=True)
