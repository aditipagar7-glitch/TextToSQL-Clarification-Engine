from backend.clarification import detect_ambiguity


questions = [
    "Show me the best customers",
    "Show me customers from Pune",
    "Show me the top products",
    "Show all orders"
]


for question in questions:

    result = detect_ambiguity(question)

    print("\nQUESTION:")
    print(question)

    print("RESULT:")
    print(result)