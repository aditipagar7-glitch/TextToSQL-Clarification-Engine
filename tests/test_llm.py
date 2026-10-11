from backend.llm import ask_llm


response = ask_llm(
    "Explain SQL in one sentence."
)

print(response)