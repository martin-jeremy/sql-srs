import duckdb
import streamlit as st
import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')


def app():
    st.write("Hello world!")

    tab1, tab2, tab3, tab4 = st.tabs(['Cat', 'Dog', 'Owl', 'Bat'])

    with tab1:
        st.header('Test input:')
        input_query = st.text_area('Input query:')
        if input_query:
            result = duckdb.execute(input_query)
        st.write(input_query)
        st.subheader('iris table:')
        st.write(iris)
        st.subheader('queried results:')
        st.write(result)

    with tab2:
        st.header('Dog:')
        st.image('https://cdn.midjourney.com/36e542d4-2c53-4234-be3c-2d0a7e5e0cb3/0_0.png', width=200)

    with tab3:
        st.header('Owl:')
        st.image('https://cdn.midjourney.com/e60d2053-a3fb-4625-98e9-387016b5412b/0_1.png', width=200)

    with tab4:
        st.header('Bat:')
        st.image('https://cdn.midjourney.com/bd145cc1-63e5-4e21-bfa2-e7c190f578b5/0_3.png', width=200)

if __name__ == "__main__":
    app()
