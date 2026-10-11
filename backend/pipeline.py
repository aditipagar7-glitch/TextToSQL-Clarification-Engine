from backend.clarification import detect_ambiguity
from backend.conversation import combine_question
from backend.sql_generator import generate_sql
from backend.validator import validate_sql
from backend.executor import execute_sql


def process_question(question, clarification=None):

    # --------------------------------
    # If clarification is provided
    # --------------------------------

    if clarification:

        final_question = combine_question(
            question,
            clarification
        )

        sql = generate_sql(final_question)

    else:

        # --------------------------------
        # Check whether clarification needed
        # --------------------------------

        ambiguity = detect_ambiguity(question)

        if ambiguity["needs_clarification"]:

            return {
                "status": "clarification_required",
                "question": ambiguity["question"],
                "options": ambiguity["options"]
            }

        sql = generate_sql(question)

    # --------------------------------
    # Validate SQL
    # --------------------------------

    is_valid, message = validate_sql(sql)

    if not is_valid:

        return {
            "status": "error",
            "message": message
        }

    # --------------------------------
    # Execute SQL
    # --------------------------------

    try:

        dataframe = execute_sql(sql)

        return {
            "status": "success",
            "sql": sql,
            "columns": list(dataframe.columns),
            "data": dataframe.to_dict(orient="records")
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }