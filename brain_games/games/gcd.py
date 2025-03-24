import random

import brain_games.cli
import brain_games.engine


def main():
    Name_of_User = brain_games.cli.welcome_user()
    print('Find the greatest common divisor of given numbers.')
    list_of_questions = []
    list_of_answers = []
    i = 0
    while i < 3:
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        list_of_questions.append(f'{a} {b}')
        biggest = 0
        smallest = 0
        check = 0
        if a > b:
            biggest = a
            smallest = b
        else:
            biggest = b
            smallest = a
        while check == 0:
            c = biggest % smallest
            if c == 0:
                check = 1
                list_of_answers.append(str(smallest))
            else:
                biggest = smallest
                smallest = c
        i += 1    
    brain_games.engine.main(Name_of_User, list_of_questions, list_of_answers)