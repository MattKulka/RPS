#RockPaperScissors
import random

choices= ["R","P","S"]

def get_choice(input):
	if input == "R":
		return "Rock"
	elif input =="P":
		return "Paper"
	elif input == "S":
		return "Scissors"
	else:
		return "Invalid Input"

print('Rock, Paper, Scissors.... SHOOT!')
print('[R]= Rock, [P]= Paper, [S]= Scissors, [Q] = Quit')
counter = 1

while True:

	print('Game '+str(counter)+':')
	print('Please choose a letter:')
	user_choice = input()

	if user_choice == "Q":
		print('Thanks for Playing!')
		break;

	random_index= random.randint(0,2)
	computer_choice = choices[random_index]

	print('You chose' + get_choice(user_choice) +  'the computer chose'+  get_choice(computer_choice))

	if user_choice == "R" and computer_choice =="S":
		print('You Win, Rock Beats Scissors')
	elif user_choice=="P" and computer_choice ==" R":
		print('You Win, Paper Beats Rock')
	elif user_choice == "S" and computer_choice == "P":
		print('You Win, Scissors Beat Rock')
	elif user_choice== "R" and computer_choice == "P":
		print('You Lose, Paper Beats Rock')
	elif user_choice == "P" and computer_choice == "S":
		print('You Lose, Scissors Beat Paper')
	elif user_choice== "S" and computer_choice == "R":
		print('You Lose, Rock Beats Scissors')
	elif user_choice == computer_choice:
		print('Its a Tie!')
	else:
		print('Please Enter [R, P, S OR Q]')

	counter= counter+1
	print('\n')



