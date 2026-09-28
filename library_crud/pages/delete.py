import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.title('delete record')
i=st.number_input('enter id',min_value=0)

btn=st.button('delete')

if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.delete(i)
    if record:
        st.success('record deleted')
    else:
        st.error('record not deleted')
