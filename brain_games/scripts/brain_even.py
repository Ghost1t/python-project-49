import brain_games.cli
import random
import prompt

def main():
    Name_of_User = brain_games.cli.welcome_user()
    list_of_numbers = []
    i = 0
    while i < 3:
        list_of_numbers.append(random.randint(0, 99))
        i += 1
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for number in list_of_numbers:
        print(f'Question: {number}')
        check = prompt.string('Your answer: ')
        if ((check == 'yes' and number % 2 == 0) or (check == 'no' and number % 2 != 0)):
            print('Correct!')
        else:
            right_answer = 'yes'
            if (check == 'yes' and number % 2 != 0):
                right_answer = 'no'
            print(f"'{check}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {Name_of_User}!")
            return
    print(f"Congratulations, {Name_of_User}!")

    


    