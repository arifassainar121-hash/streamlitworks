from os import process_cpu_count

import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete
from streamlit.navigation import page


i=st.number_input('enter id: ',min_value=0)
st.title("update book record")


title=st.text_input('enter new title:')
auther=st.text_input('enter new auther: ')
price=st.number_input("enter new number",min_value=0)
page=st.number_input('enter new number: ',min_value=0)
language=st.number_input('enter new language: ',min_value=0)

btn=st.button('update')
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.update(i,  auther,price,page,language)
    if record:
        st.success('record update successfully')

    else:
        st.error("update not successfully")