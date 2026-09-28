import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

tab1,tabb2,tab3,tab4,tab5=st.tabs(['add','read','retrive','update','delete'])

b=BookListCreateRetrieveUpdateDelete()

with tab1:
    st.title('add')
with tab2:
    st.title('read')
