print("\n\nH-A-N-G-M-A-N  G-A-M-E\nYou can only make a mistake with 6 letters !!!Please use lowercase\n\n")

import json
data = json.load(open("words.json"))
# print(data)

import random
word = (random.choice(data))
# print(word)

def split_word(x):
    return([char for char in x])
# print(type(split_word(word)))
# print(split_word(word))

word2= "".join(["-" * len(word)])
print(word2)
# print(type(word2))
# def setowanie(x):
#     return ([char for char in x])
# print(type(setowanie(word2)))

# print(setowanie(word2))
import re

letter = input("Guess a letter !\n")
# print(type(letter))
missed_letters=0
hangman=(("|\n|\n|\n|\n|"),
         (" _______\n|\n|\n|\n|\n|"),
         (" _______\n|     |\n|    ('')\n|\n|\n|\n|"),
         (" _______\n|     |\n|    ('')\n|     /\\\n|    /  \\\n|         \n|          \n"),
         (" _______\n|     |\n|    ('')\n|     /\\\n|    /[]\\\n|         \n|         \n"),
         (" _______\n|     |\n|    ('')\n|     /\\\n|    /[]\\\n|     /\\\n|    /  \\"))

while word!=word2:
    if letter in word:
        if letter in word2:
            print("\nYou've already picked this letter")
        else:
            print("\nYour letter's position in the word is:")
            # print(type(split_word(word)))
            # print(type(set([word2])))
            res = [i+1 for i, item in enumerate(word) if item in set(split_word(letter))]
            print(res)
            # print(type(res))
            w2=split_word(word2)
            for i in res:
                w2[i-1]=letter
            # print(w2)
            print("".join(w2))
            # print(type(word))
            if (split_word(word))==w2:
                print(f"\nBingo! You guessed it ! The word is -{word}-.\n")
                break
            word2=w2
    if letter not in word:
        print("\n\nThis is not the letter we are looking for !!")
        print(hangman[(missed_letters)])
        if (missed_letters)==5:
            print(f"\nSorry!! You loose.... The word is -{word}-.\n")
            break
        missed_letters+=1

    letter = input("\nGuess another letter !\n")

# poprawic jesli ta sama litera znow


#         loc=word.index(letter)
#         word2[loc]=letter
# #         if item in list:
# > >  loc = list.index(item)
# > >  list[loc] = str

# >>> foo = [1,2,3]
# >>> foo[0]
# 1
# >>> foo[0] = 'a'
# >>> foo
# ['a', 2, 3]
        # word2=[for i in word2 ]

        # new_list = [x if i >= 2 else "z" for i, x in enumerate(mylist)]
# a = [1, 2, 3, 4, 5]
# b = set([9, 7, 6, 5, 1, 0])
# print(type(setowanie(word2)))
# u=[i for i, item in enumerate(a) if item in b]
# print(u)
# [0, 4]

    # print([(word.index(letter)+1)])
        # word2[(int(m.end()):] = [(letter)]
# else:
#     print("n")

# Python3 code to demonstrate
# Get match indices
# using list comprehension and enumerate()

# # initializing lists
# test_list1 = [5, 4, 1, 3, 2]
# test_list2 = [1, 2]
#
# # printing original lists
# print("The original list 1 : " + str(test_list1))
# print("The original list 2 : " + str(test_list2))
#
# # using list comprehension and enumerate()
# # Get match indices
# res = [key for key, val in enumerate(test_list1)
#        if val in set(test_list2)]
#
# # print result
# print("The Match indices list is : " + str(res))
# # Output :
# # The original list 1 : [5, 4, 1, 3, 2]
# # The original list 2 : [1, 2]
# # The Match indices list is : [2, 4]
#

