'''hangman game'''
from random import randint
import os

def find_letter_indexes(letter,word):
	indexes = []
	i = 0
	while i<len(word):
		if (word[i]==letter):
			indexes.append(i)
		i+=1
	return indexes	



words = open('words.txt','r+')
word_list = words.readlines()


random_word = list(word_list[randint(0,len(word_list))])
random_word = random_word[:len(random_word)-1]



guess = ['_']

for i in range(0,len(random_word)-1):
	guess.append('_')

print('welcome to hangman! ')
used_letters=[]
user_guess = ''
tries = 8

while (tries > 0):
	if ('_' not in guess):
		print('CONGRATZ! U GUESSED THE WORD ', guess)
		input('you have won the game! press anything to contiue!')
		break

	print('can you guess the word: ' ,guess,'?')
	user_guess=input('->')[0]
	
	indexes = []


	if (user_guess not in used_letters):

		if (user_guess in random_word):
			indexes = find_letter_indexes(user_guess,random_word)

			for i in indexes:
				guess[i] = user_guess
			os.system('cls')

		else :
			os.system('cls')
			print('nope! this letter is not a part of the word!, you have ')
			tries -= 1
			print(tries, ' left!')

		used_letters.append(user_guess)

	else:
		os.system('cls')
		print("you already used this letter...")

if (tries == 0):
	os.system('cls')
	print('the word was: ',random_word)
	input('you lost the game! press any key to continue!')
	




