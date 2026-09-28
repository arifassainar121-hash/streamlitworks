import streamlit as st

from library_db import BookListCreateRetrieveUpdateDelete
tab1,tab2,tab3,tab4,tab5=st.tabs(['Add','read','retrive','Delete','update'])



with tab1:
    st.title('insert doner details')
    # id=st.number_input('id',min_value=0)
    name=st.text_input('name')
    group=st.text_input('blood group')
    phone=st.text_input('phone')
    city=st.text_input('city')
    last_donation=st.date_input('donation')
    btn=st.button('add')
    if btn:
        b=BookListCreateRetrieveUpdateDelete()
        b.create(name,group,phone,city,str(last_donation))
        st.success('Successfully added  record')


with tab2:
    st.title('doner details')
    b=BookListCreateRetrieveUpdateDelete()
    records=b.list()
    st.write(records)

with tab3:
    st.title('retrieve')

    i=st.number_input('retrieve id',min_value=0)
    btn=st.button('retrieve')
    if btn:
        b=BookListCreateRetrieveUpdateDelete()
        record=b.retrieve(i)
        if record:
            st.write('doner details',record)
        else:
            st.write('data not founded')
# with tab:
#     st.title('update')
#     del=st.number_input('delete id',min_value=0)
#     btn=st.button('update')
#     if btn:
#         b=BookListCreateRetrieveUpdateDelete()
#         b.update(del)
#         st.write(record)

