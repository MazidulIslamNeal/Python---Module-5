num = int(input("Enter an integer: "))

for i in range(2, num):
if num % i == 0:
print("The entered integer is not prime")
break
else:
print("The number is prime.")
