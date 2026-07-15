import streamlit as e
import pandas as pd

# Streamlit 페이지 기본 설정 (타이틀, 아이콘, 레이아웃)
e.set_page_config(
    page_title="스마트 건의함 (Smart Suggestion Box)",
    page_icon="📥",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 웹앱의 전반적인 완성도를 높이기 위한 CSS 스타일 정의
e.markdown("""
    <style>
    /* 메인 타이틀 디자인 */
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    /* 서브 타이틀 디자인 */
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 2rem;
    }
    /* 카드 스타일 컨테이너 */
    .status-card {
        background-color: #F3F4F6;
        border-radius: 12px;
        padding: 1.5rem;
        border-left: 5px solid #3B82F6;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 건의사항 실제 구글 폼 또는 네이버 폼 링크를 이곳에 붙여넣어 주세요!
FORM_URL = "https://malleable-verdict-0bb.notion.site/a943a7db7654827b882a01be2d3c83d2?pvs=105"

# 메인 화면 타이틀 및 소개글
e.markdown("<div class='main-title'>🚨스마트 건의함</div>", unsafe_allow_html=True)
e.markdown("<div class='sub-title'>여러분의 소중한 의견이 더 나은 3-8반을 만듭니다. 언제든 편하게 건의해 주세요!</div>", unsafe_allow_html=True)


# 핵심 요구사항: 단순 링크 대신 시선을 사로잡는 세련된 이동 버튼 및 FAQ 정보 제공
e.subheader("✍️ 건의 및 안내 센터")

# 탭을 생성하여 탭1에는 제출 버튼을, 탭2에는 자주 묻는 질문(FAQ)을 배치합니다.
tab1, tab2 = e.tabs(["건의제", "🔍 자주 묻는 질문 (FAQ)"])

with tab1:
    # 1. HTML & CSS를 가미하여 한눈에 띄고 클릭하고 싶게 만든 고급스러운 카드 버튼
    # 애니메이션 효과와 그림자가 포함되어 있어 직관적입니다.
    e.write("아래 버튼을 클릭하시면 익명이 보장되는 안전한 건의 접수 폼으로 연결됩니다.")
    button_html = f"""
    <div style="text-align: center; margin: 20px 0;">
        <a href="{FORM_URL}" target="_blank" style="text-decoration: none;">
            <div style="
                background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
                color: white;
                padding: 18px 30px;
                font-size: 20px;
                font-weight: bold;
                border-radius: 50px;
                box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3), 0 4px 6px -2px rgba(37, 99, 235, 0.05);
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                display: inline-block;
                cursor: pointer;
                width: 90%;
                max-width: 500px;
            " onmouseover="this.style.transform='scale(1.02)'; this.style.boxShadow='0 20px 25px -5px rgba(37, 99, 235, 0.4)';" 
               onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='0 10px 15px -3px rgba(37, 99, 235, 0.3)';">
                📢 의견/건의사항 제출하기 (클릭)
            </div>
        </a>
    </div>
    """
    e.markdown(button_html, unsafe_allow_html=True)
with tab2:
    # 기존 화면 하단에 있던 질문 리스트들을 탭2 내부로 깔끔하게 정리했습니다.
    e.markdown("### 🔍 건의함 운영 안내")
    
    with e.expander("❓ 건의를 제출하면 누가 확인하나요?", expanded=True):
        e.write("""
        제출하신 소중한 건의사항은 건의함 담당 운영진 외에는 열람할 수 없도록 철저히 관리됩니다.
        """)

    with e.expander("❓ 정말 익명이 보장되나요?"):
        e.write("""
        네, 안심하셔도 좋습니다! 저희 스마트 건의함이 사용하는 시스템은 제출자의 계정 정보를 수집하지 않도록 설정되어 있습니다.  
        개인정보 침해 걱정 없이 자유로운 의견을 남겨주세요!!
        """)

    with e.expander("❓ 처리 결과는 어떻게 확인하나요?"):
        e.write("""
        검토 및 처리가 완료된 건의사항은 폼 내 상단 혹은 공지방을 통해 정기적으로 피드백 상황이 업데이트될 예정입니다.
        """)

e.divider()

# 하단 저작권 및 푸터 정보
e.markdown("<br><br>", unsafe_allow_html=True)
e.caption("💡 스마트 건의함 v1.0 | Created with Streamlit & GitHub")
