import random

import brain_games.cli
import brain_games.engine


def main():
    Name_of_User = brain_games.cli.welcome_user()
    print('What is the result of the expression?')
    list_of_questions = []
    list_of_answers = []
    i = 0
    while i < 3:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 2)
        if c == 0:
            list_of_questions.append(f'{a} * {b}')
            list_of_answers.append(str(a * b))
        elif c == 1:
            list_of_answers.append(str(a + b))
            list_of_questions.append(f'{a} + {b}')
        else:
            list_of_questions.append(f'{a} - {b}')
            list_of_answers.append(str(a - b))
        i += 1    
    brain_games.engine.main(Name_of_User, list_of_questions, list_of_answers)