import random

import brain_games.cli
import brain_games.engine


def main():
    Name_of_User = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    list_of_questions = []
    list_of_answers = []
    i = 0
    while i < 3:
        list_of_questions.append(random.randint(0, 99))
        if list_of_questions[i] % 2 == 0:
            list_of_answers.append('yes')
        else:
            list_of_answers.append('no')
        i += 1
    brain_games.engine.main(Name_of_User, list_of_questions, list_of_answers)