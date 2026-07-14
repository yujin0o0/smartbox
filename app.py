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


# 4. 노션 폼 링크 설정 (본인의 Tally 또는 노션 폼 링크로 변경하세요!)
# 예: "https://tally.so/embed/xxxxxx" 형태로 넣으면 내부에 깔끔하게 들어갑니다.
notion_form_url = "https://malleable-verdict-0bb.notion.site/a943a7db7654827b882a01be2d3c83d2?pvs=105"

# 6. 푸터(Footer) 및 안내
st.markdown("---")
st.caption("⚙️ 제작: [yujin] (UI/UX 및 스트림릿 기반 노코드 웹앱 프로토타입)")
