print("\n\nH-A-N-G-M-A-N  G-A-M-E\nYou can only make a mistake with 6 letters !!!Please use lowercase\n\n")

import json
import random

data = json.load(open("words.json"))
word = (random.choice(data))

def split_word(x):
    return ([char for char in x])

word2 = "".join(["-" * len(word)])
print(word2)

letter = input("Guess a letter !\n")

missed_letters = 0
hangman = (("|\n|\n|\n|\n|"),
           (" _______\n|\n|\n|\n|\n|"),
           (" _______\n|     |\n|    ('')\n|\n|\n|\n|"),
           (" _______\n|     |\n|    ('')\n|     /\\\n|    /  \\\n|         \n|          \n"),
           (" _______\n|     |\n|    ('')\n|     /\\\n|    /[]\\\n|         \n|         \n"),
           (" _______\n|     |\n|    ('')\n|     /\\\n|    /[]\\\n|     /\\\n|    /  \\"))

while word != word2:
    if letter in word:
        if letter in word2:
            print("\nYou've already picked this letter")
        else:
            print("\nYour letter's position in the word is:")
            res = [i + 1 for i, item in enumerate(word) if item in set(split_word(letter))]
            print(res)
            w2 = split_word(word2)
            for i in res:
                w2[i - 1] = letter
            print("".join(w2))
            if (split_word(word)) == w2:
                print(f"\nBingo! You guessed it ! The word is -{word}-.\n")
                break
            word2 = w2
    if letter not in word:
        print("\n\nThis is not the letter we are looking for !!")
        print(hangman[(missed_letters)])
        if (missed_letters) == 5:
            print(f"\nSorry!! You loose.... The word is -{word}-.\n")
            break
        missed_letters += 1

    letter = input("\nGuess another letter !\n")

