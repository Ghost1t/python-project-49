import prompt


def welcome_user():
	name = prompt.string('Welcome to the Brain Games! May I have your name? ')
	print(f'Hello, {name}!')
	return (name)