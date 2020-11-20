from lab2 import fuzzy_compare_string


ACCURACY = 0.7

# set of tuple(question: str, answer: str)
answers = set()

def get_answer(question: str):
    if question:
        if question == 'exit':
            exit()

        for quest, ans in answers:
            similarity = fuzzy_compare_string(question, quest)
            if similarity > ACCURACY:
                return f"уже спрашивали! {ans}"

    answer = "да" if hash(question) % 2 else "нет"
    answers.add((question, answer))
    return answer

while True:
    print(get_answer(input("Your question: ")))
