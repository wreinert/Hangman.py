import random


def checkTries(tries):
    if tries == 0:
        print("------\n|\n|\n|")
    elif tries == 1:
        print("------\n|    O\n|\n|")
    elif tries == 2:
        print("------\n|    O\n|    |\n|")
    elif tries == 3:
        print("------\n|    O\n|   /|\n|")
    elif tries == 4:
        print("------\n|    O\n|   /|\ \n|")
    elif tries == 5:
        print("------\n|    O\n|   /|\ \n|   /")
    elif tries == 6:
        print("------\n|    X\n|   /|\ \n|   / \ ")

with open("sowpods.txt",'r') as sp:
    line = sp.readlines()
    word = line[random.randint(0,len(line))]
    #print(word)

hiddenword = list(word.strip())
#print(hiddenword)
result = False
show = ['-']*len(hiddenword)
guesses = []
tries = 0
while result == False and tries < 6:
    counter = 0
    guess = input('Pick a letter: ').upper()
    if guess in guesses:
        print('Try another letter')
    else:
        if guess in hiddenword:
            while counter < len(hiddenword):
                if guess == hiddenword[counter]:
                    show[counter] = guess
                counter += 1
            guesses.append(guess)
        else:
           tries += 1
           guesses.append(guess)
           checkTries(tries)
        print(show)
        if hiddenword == show:
            result = True
            print(f"The word is: {''.join(show)}")
        if tries == 6:
            print('Game over: out of tries')
            print(f"The word is: {''.join(hiddenword)}")

