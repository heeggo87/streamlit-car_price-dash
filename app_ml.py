import streamlit as st
import joblib
import pandas as pd

def run_ml():
    # CSS 스타일 추가
    st.markdown("""
        <style>
        .prediction-header {
            font-size: 1.8rem;
            color: #2E7D32;
            text-align: center;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #2E7D32;
        }
        .input-label {
            font-size: 1.1rem;
            color: #1565C0;
            margin-top: 1rem;
        }
        .prediction-result {
            background-color: #E8F5E9;
            padding: 1rem;
            border-radius: 10px;
            margin-top: 2rem;
            text-align: center;
            font-size: 1.2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h2 class="prediction-header">🎯 구매 금액 예측하기</h2>', unsafe_allow_html=True)

    with st.container():
        st.info('✨ 아래 정보를 입력하시면 AI가 최적의 구매 금액을 예측해드립니다.')

    gender_list = ['여자', '남자']
    gender = st.radio('성별을 입력하세요', gender_list)
    
    if gender == gender_list[0] :
        gender_data = 0
    else :
        gender_data = 1

    age = st.number_input('나이 입력', min_value=20, max_value=90)

    salary = st.number_input('연봉 입력 (달러)', min_value=10000)

    debt = st.number_input('카드빚 입력 (달러)' , min_value=0)

    worth = st.number_input('자산 입력(달러)' , min_value=10000, step=1000)

    if st.button('예측하기!') :

        # 모델을 가져온다.
        regressor = joblib.load('./model/regressor.pkl')

        # 유저가 입력한 데이터를, 예측할수 있게 가공해야 한다.
        new_data = [ {'Gender' :gender_data , 'Age':age, 'Annual Salary':salary, 'Credit Card Debt':debt , 'Net Worth' : worth } ]    
        df_new = pd.DataFrame(data=new_data)

        # 예측하고, 결과를 보여준다.
        y_pred = regressor.predict(df_new)  

        if y_pred < 0 :
            st.warning('구매 금액 예측이 어렵습니다.')
        else :
            price = format( round(y_pred[0]) ,  ',') 

            st.info( f'예측한 금액은 {price} 달러입니다.' )
        
