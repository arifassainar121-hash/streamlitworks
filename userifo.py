import streamlit as st

name=st.text_input('name')
age=st.number_input('age')
place=st.text_input('place')

gender=st.radio('Gender',['male','female'])
qualification=st.selectbox('qualification',['bba','bca','bsc'])
btn=st.button('submit')
# if btn:
#     st.title('user info: ')
#     st.write(f'NAME: {name}')
#     st.write(f'age{age}')
#     st.write(f'PLACE: {place}')
#     st.write(f'Gender: {gender}')
#     st.write(f'qualification: {qualification}')