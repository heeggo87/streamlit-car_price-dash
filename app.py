import streamlit as st
from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml

def main():
    # 페이지 설정
    st.set_page_config(
        page_title="자동차 구매 금액 예측",
        page_icon="🚗",
        layout="wide"
    )

    # CSS 스타일 적용
    st.markdown("""
        <style>
        .main-header {
            font-size: 2.5rem;
            color: #1E88E5;
            text-align: center;
            padding: 1rem 0;
            font-weight: bold;
        }
        .sidebar .selectbox {
            background-color: #f0f2f6;
            border-radius: 10px;
            padding: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="main-header">🚗 자동차 구매 금액 예측</h1>', unsafe_allow_html=True)

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴 선택', menu, key='sidebar-select')

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()

if __name__ == '__main__':
    main()

