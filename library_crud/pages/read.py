import streamlit as st

st.title('read all book records')

from library_db import BookListCreateRetrieveUpdateDelete


b=BookListCreateRetrieveUpdateDelete()
records=b.list()
print('hello')
print(records)





