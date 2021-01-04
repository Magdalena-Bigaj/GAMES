import random
from operator import itemgetter
import pyinputplus as pyip

dice_1 = ''
dice_2 = ''
dice_3 = ''
dice_4 = ''
dice_5 = ''
dice = {1: dice_1, 2: dice_2, 3: dice_3, 4: dice_4, 5: dice_5}

ones = ''
twos = ''
threes = ''
fours = ''
fives = ''
sixes = ''

upper_section_category_named = {1: ones, 2: twos, 3: threes, 4: fours, 5: fives, 6: sixes}
upper_section_category = {1: "ones", 2: "twos", 3: "threes", 4: "fours", 5: "fives", 6: "sixes"}

three_of_a_kind = ''
four_of_a_kind = ''
full_house = ''
small_straight = ''
large_straight = ''
chance = ''
yahtzee = ''
yahtzee_bonus = ''

lower_section_category_named = {1: three_of_a_kind, 2: four_of_a_kind, 3: full_house, 4: small_straight,
                                5: large_straight, 6: chance, 7: yahtzee}
lower_section_category = {1: "three_of_a_kind", 2: "four_of_a_kind", 3: "full_house", 4: "small_straight",
                          5: "large_straight", 6: "chance", 7: "yahtzee"}

upper_categories = []
lower_categories = []
upper_section_sum = 0
lower_section_sum = 0
total_sum = 0
scores = []
on_the_table = {}
round_number = 1
roll = 1
category = ''
print("\n\n\n* * * *WELCOME TO YAHTZEE GA"
      "ME * * * * ")
while round_number < 14:
    while roll < 4:
        input(f"\n\n*** Round {round_number}, roll {roll}: Press ENTER to roll a dice !\n")
        for d in dice:
            dice[d] = random.randint(1, 6)
            print(f"dice{d} : {dice[d]} ")
        if roll < 3:
            # roll_again= list(map(int, pyip.inputNum(prompt= "\n*** Which dice you want to roll again? "
            #                                  "Put the numbers of the dice separated by comma. \n"
            #                                  "If you want to leave all the dice on the table press 0\n", allowRegexes=[r'(1|2|3|4|5|6|0|,)$']).split(",")))
            roll_again = list(map(int, input("\n*** Which dice you want to roll again? "
                                             "Put the numbers of the dice separated by comma. \n"
                                             "If you want to leave all the dice on the table press '0'\n").split(",")))
        else:

            roll_again = [0]

            for d in roll_again:
                if d not in dice and roll_again != [0]:
                    roll_again = list(map(int, input(
                        "\n***You've already thrown this dice, please choose the dice to roll again \n").split(",")))
        print("\n*** Left on the table:")
        for d in dice:
            if d not in roll_again or roll_again == [0]:
                on_the_table[d] = dice[d]
                scores.append(dice[d])
        for d in sorted(on_the_table):
            if roll < 3:
                print(f"dice {d} : {on_the_table[d]}")
        if roll == 3:
            print("Nothing left")
        print("\nYour current scores are: ", sorted(scores))
        for d in set(dice):
            if d not in roll_again:
                del dice[d]
        roll += 1
        if len(scores) == 5:
            if round_number < 7:
                category = pyip.inputNum("What category you want to score? Enter the corresponding letter:\n"
                                     "1 for ones\n2 for twos\n3 for threes\n4 for fours\n5 for fives\n6 for sixes\n", min=1, max=6 )
                print(type(category))
                if category in upper_categories:
                    category = int(input("\n***You've already scored this dice,"
                                         " please choose the other category\n"))
                upper_categories.append(category)
                on_the_table = {}
                for d in upper_section_category_named:
                    if d == category:
                        upper_section_category_named[d] = sum(score for score in scores if score == d)
                        upper_section_sum = upper_section_sum + upper_section_category_named[d]
                    print(f"{upper_section_category.get(d)} : {upper_section_category_named.get(d)}")
                print(f"Your total score for upper section is: {upper_section_sum}")
                roll = 1
                dice = {1: dice_1, 2: dice_2, 3: dice_3, 4: dice_4, 5: dice_5}
                scores = []
                round_number += 1
                break
            if round_number > 6:
                category = pyip.inputNum("What category you want to score? Enter the corresponding letter:\n"
                                     "1 for three_of_a_kind\n2 for four_of_a_kind\n3 for full_house\n4"
                                     " for small_straight\n5 for large_straight\n6 for chance \n7 for yahtzee\n", min=1, max=7 )
                if category in lower_categories:
                    category = int(input("\n***You've already scored this dice,"
                                         " please choose the other category\n"))
                lower_categories.append(category)
                on_the_table = {}
                for d in lower_section_category_named:
                    if d == category:
                        if d <= 3:
                            c = dict()
                            for item in scores:
                                c[item] = c.get(item, 0) + 1
                            q = c.items()
                            m = max(c.items(), key=itemgetter(1))
                            n = min(c.items(), key=itemgetter(1))
                            (a, b) = m
                            (x, y) = n
                            lower_section_category_named[d] = a * 3 if d == 1 and b >= 3 else 0
                            lower_section_category_named[d] = a * 4 if d == 2 and b >= 4 else 0
                            lower_section_category_named[d] = 25 if d == 3 and (b == 2 and y == 3 or b == 3 and y == 2) else 0
                        elif d == 4:
                            scores = frozenset(scores)
                            lower_section_category_named[d] = 30 if scores.issuperset({1, 2, 3, 4}) or scores.issuperset({2, 3, 4, 5}) or scores.issuperset({3, 4, 5, 6}) else 0
                        elif d == 5:
                            scores = frozenset(scores)
                            for score in scores:
                                lower_section_category_named[d] = 40 if scores.issuperset({1, 2, 3, 4,5}) or scores.issuperset({2, 3, 4, 5,6}) else 0
                        elif d == 6:
                            lower_section_category_named[d] = sum(score for score in scores)
                        elif d == 7:
                            lower_section_category_named[d] = 50 if all(score == scores[0] for score in scores) else 0
                        lower_section_sum = lower_section_sum + lower_section_category_named.get(d)
                    print(f"{lower_section_category.get(d)} : {lower_section_category_named.get(d)}")
                print(f"Your total score for lower section is: {lower_section_sum}")
                roll = 1
                dice = {1: dice_1, 2: dice_2, 3: dice_3, 4: dice_4, 5: dice_5}
                scores = []
            round_number += 1
            break
if lower_section_sum >= 65:
    lower_section_sum + 65
total_sum = upper_section_sum + lower_section_sum
print(f"\n\nYour score for YAHTZEE game is {total_sum}")
#TODO multiplayer: add dictionary player1 when points would be stored