AMBIGUOUS_TERMS = {

    "best": {
        "question": "How should customers be ranked?",
        "options": [
            "Highest total spending",
            "Highest number of orders",
            "Highest average order value"
        ]
    },

    "top": {
        "question": "What should determine the ranking?",
        "options": [
            "Highest revenue",
            "Highest number of orders",
            "Highest quantity sold"
        ]
    },

    "popular": {
        "question": "How should popularity be measured?",
        "options": [
            "Most orders",
            "Highest quantity sold",
            "Highest revenue"
        ]
    }
}


def detect_ambiguity(question):

    question_lower = question.lower()

    for term, information in AMBIGUOUS_TERMS.items():

        if term in question_lower:

            return {
                "needs_clarification": True,
                "term": term,
                "question": information["question"],
                "options": information["options"]
            }

    return {
        "needs_clarification": False
    }