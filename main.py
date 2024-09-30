import random

words = ["pizza", "plane", "sword", "apple", "teeth"]
lives = 9
clue = list("?????")
heart_symbol = u'\u2764'
guessed = False

rand_word = random.choice(words)
print(rand_word)

while lives > 0:
    print(clue)
    print("Lives left: ", heart_symbol * lives)
    guess = input("Guess letter or a whole word: ")

    if guess == rand_word:
        guessed = True
        clue = list(rand_word)
        break
    
    elif guess in rand_word:
        i = rand_word.index(guess)
        clue[i] = guess
            
    else:
        lives -= 1

if guessed:
    print(clue)
else:
    print("Game Over!")

    


    

