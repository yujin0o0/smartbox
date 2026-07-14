import streamlit as st

# 1. 웹페이지 기본 설정 (타이틀, 아이콘, 레이아웃)
st.set_page_config(
    page_title="스마트 건의함",
    page_icon="📢",
    layout="centered"
)

# 2. CSS(빨간 테두리) 및 자바스크립트(접속 시 자동 🚨 폭죽) 주입
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

# 3. 메인 화면 타이틀 및 소개
st.title("📢 3학년8반 스마트 건의함")
st.markdown("---")
st.subheader("우리 반의 목소리가 현실이 되는 공간입니다.")
st.write("익명성이 철저히 보장되니, 학급의 발전과 편의를 위한 소중한 의견을 자유롭게 남겨주세요!")

# 페이지 로딩 시 스트림릿 자체 풍선 효과도 함께 자동으로 스르륵 올라옵니다!
st.balloons()

st.markdown("---")

# 4. 노션 링크 안내 (Iframe으로 웹앱 내부에 노션 페이지를 바로 보여줍니다)
st.subheader("📝 건의사항 제출 및 확인")
st.write("아래 창에서 직접 내용을 확인하고 건의를 남겨주세요.")

notion_url = "https://malleable-verdict-0bb.notion.site/a943a7db7654827b882a01be2d3c83d2?pvs=105"
st.components.v1.iframe(notion_url, height=600, scrolling=True)

# 5. 푸터(Footer) 및 안내
st.markdown("---")
st.caption("⚙️ 제작: [yujin] (UI/UX 및 스트림릿 기반 노코드 웹앱 프로토타입)")
