import streamlit as st

from datetime import date
name=st.text_input('enter name: ')
age=st.number_input('enter age: ')
dob=st.date_input('enter date  of birth: ',min_value=date(1990,1,1))
                                                # max_value=date(2020,12,31)
                                                # value=date.today()

email=st.text_input('enter email: ')
gender=st.radio('select gender: ',['male','female'])
course=st.selectbox('select course: ',['java','python'])

btn=st.button('submit')
if btn:
    st.write(name)
    st.write(age)
    st.write(dob)
    st.write(email)