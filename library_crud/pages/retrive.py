import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete

st.title("retrive book record")


i=st.number_input('enter id',min_value=0)

btn=st.button('retrive')

if btn:
    b = BookListCreateRetrieveUpdateDelete()

    record=b.retrieve(i)
    print(record)

    if record:
        st.write('title',record[0])
        st.write('author',record[1])
        st.write('page',record[2])
        st.write('price',record[3])
        st.write('language',record[4])
    else:
        st.error('no record')