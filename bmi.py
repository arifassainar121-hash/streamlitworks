import streamlit as st

st.title('BMI')

num1=st.number_input('enter you weight')
print(num1)
num2=st.number_input('enter your height')
print(num2)
bmi=(num1/(num2/100)**2)
bmi=st.button('calculate')
if bmi:
if bmi<18.5:
    st.info('you are underweight')
elif bmi>18.5 and bmi<25:
    st.success('you are normal')
elif bmi>25 and bmi<30:
    st.warning('you are overweight')
elif bmi>30:
    st.error('you are obese')