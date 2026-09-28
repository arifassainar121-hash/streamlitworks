import streamlit as st

st.title('subtraction')

num1=st.number_input("enter number 1", min_value=0)
print(num1)
num2=st.number_input("enter number 2", min_value=0)
print(num2)
btn=st.button("sub")

if btn:
    result=num1-num2
    #print(result)

    st.write(result)  # show in interface