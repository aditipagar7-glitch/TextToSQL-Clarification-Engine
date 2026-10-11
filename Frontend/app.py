import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/ask"


st.set_page_config(
    page_title="Text-to-SQL Assistant",
    page_icon="🔎"
)


st.title("Text-to-SQL with Clarification Engine")

st.write(
    "Ask questions about the database using natural language."
)


question = st.text_input(
    "Enter your question:"
)


# ==========================================
# STEP 1 — ASK QUESTION
# ==========================================

if st.button("Ask"):

    if question:

        response = requests.post(
            API_URL,
            json={
                "question": question
            }
        )

        result = response.json()

        if result["status"] == "clarification_required":

            st.session_state["needs_clarification"] = True

            st.session_state["clarification_question"] = (
                result["question"]
            )

            st.session_state["options"] = (
                result["options"]
            )

            st.session_state.pop("sql", None)
            st.session_state.pop("data", None)

        elif result["status"] == "success":

            st.session_state["needs_clarification"] = False

            st.session_state["sql"] = result["sql"]

            st.session_state["data"] = result["data"]

        else:

            st.error(result["message"])


# ==========================================
# STEP 2 — CLARIFICATION
# ==========================================

if st.session_state.get(
    "needs_clarification",
    False
):

    st.subheader("Clarification Required")

    st.write(
        st.session_state["clarification_question"]
    )

    option = st.radio(
        "Choose an option:",
        st.session_state["options"]
    )


    # ======================================
    # STEP 3 — CONTINUE
    # ======================================

    if st.button("Continue"):

        response = requests.post(
            API_URL,
            json={
                "question": question,
                "clarification": option
            }
        )

        result = response.json()

        if result["status"] == "success":

            st.session_state["needs_clarification"] = False

            st.session_state["sql"] = result["sql"]

            st.session_state["data"] = result["data"]

            st.rerun()

        else:

            st.error(result["message"])


# ==========================================
# STEP 4 — DISPLAY SQL
# ==========================================

if "sql" in st.session_state:

    st.subheader("Generated SQL")

    st.code(
        st.session_state["sql"],
        language="sql"
    )


# ==========================================
# STEP 5 — DISPLAY ANSWER
# ==========================================

if "data" in st.session_state:

    st.subheader("Query Result")

    st.dataframe(
        st.session_state["data"],
        use_container_width=True
    )