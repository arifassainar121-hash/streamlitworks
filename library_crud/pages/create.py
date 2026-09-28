import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("add new book record  ")



t=st.text_input('book name:')
a=st.text_input('author name: ')
p=st.number_input('price: ',min_value=0)
pg=st.number_input('pages:',min_value=0)
l=st.text_input('language:')
btn=st.button('add')
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(t,a,p,l,pg)
    st.success('record created successfully')



