import random

dice = int(input("Enter how many dice you want to roll?: "))
total = 0

for _ in range(dice):
roll = random.randint(1,6)
total += roll
print(f"The sum of dice rolls is: {roll}")
