numbers = []
for _ in range(999):
user_input = input("Enter a number (or press empty to exit): ")
if user_input == "":
break
try:
num = float(user_input)
numbers.append(num)
except ValueError :
print("Invalid Input")


greatest_number = sorted(numbers, reverse=True)[:5]

print("The five greatest number in descending order:")
for num in greatest_number :
print(num)
