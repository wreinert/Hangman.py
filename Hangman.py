import random
import requests
from bs4 import BeautifulSoup
from Game_clss import Game

#Function the draws the man
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

#Fetches random word from sowpods.txt
with open("sowpods.txt",'r') as sp:
    line = sp.readlines()
    word = line[random.randint(0,len(line))]
    #print(word)

#The guessing game
name = input("Please insert your username: ")
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
            win_lose = "W"
        if tries == 6:
            print('Game over: out of tries')
            print(f"The word is: {''.join(hiddenword)}")
            win_lose = "L"

#Fetches the meaning of the word on the web and displays it
base_url = 'https://www.dictionary.com/browse/'+''.join(hiddenword)
r = requests.get(base_url)
soup = BeautifulSoup(r.content, features="html.parser")
classa = "css-xxaj7r"

results = soup.find(class_= "css-10ul8x e1q3nk1v2")
print("Meaning: "+results.text)


#Store results on database via Postgre
import psycopg2 as conector

game = Game(name, win_lose, tries, ''.join(hiddenword))

try:
    conexao = conector.connect("dbname = hangman user=postgres password=null")
    cursor = conexao.cursor()

    comando = '''INSERT INTO GAME (name, result, tries, word) VALUES (%s, %s, %s, %s);'''
    cursor.execute(comando, (game.name, game.w_l, game.tries, game.word))
    conexao.commit()

except conector.DatabaseError as err:
    print('Erro de banco de dados', err)

finally:
    if conexao:
        cursor.close()
        conexao.close()