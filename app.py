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
st.markdown("""
<style>
    /* 웹앱 메인 컨테이너에 빨간색 테두리와 부드러운 그림자 효과 추가 */
    .stAppViewMain > div {
        border: 4px solid #FF3333;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 4px 15px rgba(255, 51, 51, 0.2);
        margin-top: 20px;
        margin-bottom: 20px;
    }
</style>

<script>
// 페이지가 로딩 완료되면 자동으로 실행되는 함수
window.addEventListener('DOMContentLoaded', (event) => {
    // 스트림릿 내부 환경에서 상위 body를 찾아 🚨 파티클을 뿌려줍니다.
    const targetBody = window.parent.document.body;
    
    for (let i = 0; i < 40; i++) {
        const p = document.createElement('div');
        p.innerText = '🚨';
        p.style.position = 'fixed';
        p.style.left = '50%';
        p.style.top = '30%'; // 화면 상단 약간 위쪽 중심에서 발사
        p.style.transform = 'translate(-50%, -50%)';
        p.style.fontSize = Math.random() * (35 - 20) + 20 + 'px'; // 다양한 크기
        p.style.zIndex = '9999';
        p.style.pointerEvents = 'none';
        p.style.transition = 'all 1.5s cubic-bezier(0.1, 0.8, 0.3, 1)'; // 부드러운 사방 확산 효과
        
        targetBody.appendChild(p);
        
        // 360도 사방으로 랜덤하게 퍼지는 각도와 거리 계산
        const angle = Math.random() * Math.PI * 2;
        const velocity = Math.random() * 300 + 150; // 발사 속도 및 거리
        const x = Math.cos(angle) * velocity;
        const y = Math.sin(angle) * velocity;
        
        setTimeout(() => {
            p.style.left = `calc(50% + ${x}px)`;
            p.style.top = `calc(30% + ${y}px)`;
            p.style.opacity = '0'; // 날아가면서 점점 투명해짐
        }, 50);
        
        // 애니메이션 완료 후 요소 삭제
        setTimeout(() => { p.remove(); }, 1550);
    }
});
</script>
""", unsafe_allow_html=True)
