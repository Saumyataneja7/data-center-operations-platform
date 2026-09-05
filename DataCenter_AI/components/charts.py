import streamlit as st


def show_chart(df):

    numeric = df.select_dtypes(include="number").columns

    if len(numeric) < 1:
        return

    if len(df.columns) < 2:
        return

    try:

        chart_df = df.set_index(df.columns[0])

        st.subheader("Visualization")

        st.bar_chart(chart_df)

    except Exception:

        pass