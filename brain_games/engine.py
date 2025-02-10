import prompt


def main(Name_of_User, list_of_questions, list_of_answers):
    i = 0
    while i < len(list_of_questions):
        print(f'Question: {list_of_questions[i]}')
        check = prompt.string('Your answer: ')
        if (check == list_of_answers[i]):
            print('Correct!')
        else:
            print(f"'{check}' is wrong answer ;(.")
            print(f" Correct answer was '{list_of_answers[i]}'.")
            print(f"Let's try again, {Name_of_User}!")
            return
        i += 1
    print(f"Congratulations, {Name_of_User}!")