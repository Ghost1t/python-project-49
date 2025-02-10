import random

import brain_games.cli
import brain_games.engine


def main():
    Name_of_User = brain_games.cli.welcome_user()
    print('What number is missing in the progression?')
    list_of_questions = []
    list_of_answers = []
    maximum = random.randint(5, 20)
    i = 0
    while i < 3:
        j = 0
        list_of_numbers = []
        first = random.randint(1, 99)
        list_of_numbers.append(first)
        step = random.randint(1, 9)
        index_of_number_for_delete = random.randint(0, maximum - 1)
        while j < maximum:
            new_number = list_of_numbers[j] + step
            list_of_numbers.append(new_number)
            j += 1
        number_for_delete = list_of_numbers[index_of_number_for_delete]
        list_of_answers.append(str(number_for_delete))
        question = ''
        for number in list_of_numbers:
            if number != first:
                question += ' '
            if number == number_for_delete:
                question += '..'
            else:
                question += str(number)
        list_of_questions.append(question)
        i += 1    
    brain_games.engine.main(Name_of_User, list_of_questions, list_of_answers)