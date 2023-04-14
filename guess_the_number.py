
from random import randint

answer = randint(1, 10)
# print(answer)

guess = None

tries = 3

while guess != answer and tries > 0:
    guess = input("Donnez un nombre entre 1 et 10 : ")
    guess = int(guess)
    tries = tries - 1

    if guess < answer :
        print("Votre nombre est trop petit.")
    elif guess > answer :
        print("Votre nombre est trop grand.")

if guess == answer :
    print("Bravo !")
else :
    print("Désolé, la bonne solution était : " + str(answer) + ".")

