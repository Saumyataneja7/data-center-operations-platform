import streamlit as st

from ai.sql_generator import generate_sql
from ai.sql_executor import execute_generated_sql
from ai.answer_generator import generate_answer
from ai.report_generator import generate_daily_report

from components.sidebar import render_sidebar
from components.kpi_cards import render_kpis
from components.charts import show_chart
from components.suggested_questions import render


def run():

    st.set_page_config(
        page_title="Data Center AI Copilot",
        page_icon="🤖",
        layout="wide"
    )

    # ---------------- Sidebar ---------------- #

    clear_chat, generate_report = render_sidebar()

    if clear_chat:
        st.session_state.messages = []
        st.rerun()

    # ---------------- Title ---------------- #

    st.title("🤖 Data Center AI Copilot")
    st.caption("Ask questions about your Data Center using Natural Language")

    # ---------------- KPI Cards ---------------- #

    render_kpis()

    # ---------------- AI Daily Report ---------------- #

    if generate_report:

        with st.spinner("Generating Daily Operations Report..."):

            report = generate_daily_report()

        st.subheader("📄 Daily Operations Report")

        st.markdown(report)

        st.divider()

    # ---------------- Suggested Questions ---------------- #

    button_question = render()

    typed_question = st.chat_input(
        "Ask a question about your Data Center..."
    )

    question = typed_question or button_question

    # ---------------- Chat History ---------------- #

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            if message["role"] == "user":

                st.markdown(message["content"])

            else:

                st.markdown(message["answer"])

                with st.expander("Generated SQL"):

                    st.code(
                        message["sql"],
                        language="sql"
                    )

                st.dataframe(
                    message["data"],
                    use_container_width=True
                )

                show_chart(message["data"])

    # ---------------- New Question ---------------- #

    if question:

        # Display user message

        with st.chat_message("user"):

            st.markdown(question)

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        try:

            # Generate SQL

            with st.spinner("🧠 Generating SQL..."):

                sql = generate_sql(question)

            # Execute SQL

            with st.spinner("🗄 Running Query..."):

                df = execute_generated_sql(sql)

            # Generate AI Summary

            with st.spinner("🤖 Generating AI Summary..."):

                answer = generate_answer(question, df)

            # Assistant Response

            with st.chat_message("assistant"):

                st.markdown(answer)

                with st.expander("Generated SQL"):

                    st.code(
                        sql,
                        language="sql"
                    )

                st.subheader("Query Results")

                st.dataframe(
                    df,
                    use_container_width=True
                )

                show_chart(df)

                st.download_button(
                    label="⬇ Download Results",
                    data=df.to_csv(index=False),
                    file_name="results.csv",
                    mime="text/csv",
                    use_container_width=True
                )

            # Save Conversation

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "answer": answer,
                    "sql": sql,
                    "data": df
                }
            )

        except Exception as e:

            st.error(f"❌ {e}")
