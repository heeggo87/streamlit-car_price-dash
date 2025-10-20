import streamlit as st

def run_home():
    # CSS 스타일 추가
    st.markdown("""
        <style>
        .welcome-text {
            font-size: 1.8rem;
            color: #2E7D32;
            text-align: center;
            margin-bottom: 2rem;
        }
        .description {
            font-size: 1.2rem;
            color: #424242;
            text-align: center;
            margin: 1rem 0;
            padding: 1rem;
            background-color: #F5F5F5;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    # 환영 메시지
    st.markdown('<p class="welcome-text">🚙 자동차 데이터 분석 및 가격 예측 시스템</p>', unsafe_allow_html=True)
    
    # 설명 컨테이너
    with st.container():
        st.markdown('<p class="description">이 앱은 캐글의 Car_Purchasing_Data.csv 데이터를 기반으로<br>탐색적 데이터 분석과 머신러닝을 통한 자동차 구매 예상 금액을 제공합니다.</p>', unsafe_allow_html=True)
    
    # 이미지 컨테이너
    with st.container():
        col1, col2, col3 = st.columns([1,3,1])
        with col2:
            st.image('./image/car.jpg', use_container_width=True, width='stretch')
    
    # 기능 설명
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📊 데이터 분석
        - 상세한 데이터 통계
        - 상관관계 분석
        - 시각화된 데이터 차트
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 가격 예측
        - 개인 정보 기반 예측
        - 실시간 결과 제공
        - 정확한 예측 모델 사용
        """)