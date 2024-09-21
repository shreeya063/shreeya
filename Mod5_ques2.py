import random
num_dice = int(input("How many dice would you like to roll? "))
sum_of_rolls = 0
for _ in range(num_dice):
    roll = random.randint(1, 6)
    sum_of_rolls += roll
print(f"The sum of the dice rolls is: {sum_of_rolls}")
