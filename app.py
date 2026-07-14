import streamlit as st

# 1. 웹페이지 기본 설정 (타이틀, 아이콘, 레이아웃)
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
st.markdown("""
<style>

.boom{
    position:fixed;
    font-size:55px;
    animation: explode 2.5s ease-out forwards;
    z-index:9999;
}

.b1{left:10%; top:80%;}
.b2{left:30%; top:75%;}
.b3{left:50%; top:85%;}
.b4{left:70%; top:70%;}
.b5{left:90%; top:80%;}

@keyframes explode{
    0%{
        transform:translateY(0) scale(0.2) rotate(0deg);
        opacity:1;
    }
    40%{
        transform:translateY(-250px) scale(1.8) rotate(180deg);
        opacity:1;
    }
    100%{
        transform:translateY(-450px) scale(3) rotate(360deg);
        opacity:0;
    }
}

</style>

<div class="boom b1">🚨</div>
<div class="boom b2">🚨</div>
<div class="boom b3">🚨</div>
<div class="boom b4">🚨</div>
<div class="boom b5">🚨</div>

""", unsafe_allow_html=True)
