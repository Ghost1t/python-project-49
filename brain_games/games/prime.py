import random

import brain_games.cli
import brain_games.engine


def main():
    Name_of_User = brain_games.cli.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    list_of_questions = []
    list_of_answers = []
    i = 0
    while i < 3:
        a = random.randint(1, 99)
        list_of_questions.append(f'{a}')
        check = 0
        j = 1
        while j <= a:
            if a % j == 0:
                check += 1
            j += 1
        if check == 2:
            list_of_answers.append('yes')
        else:
            list_of_answers.append('no')
        i += 1    
    brain_games.engine.main(Name_of_User, list_of_questions, list_of_answers)