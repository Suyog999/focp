#this variable takes a input
number = input("Enter a number: ")
#this converts it to int
number = int(number)
#this prints the enteed number
print("The numbered entered was", number)
#this branch condition shows either it is odd or even
if (number % 2) == 0:
	print("That is an even number")
else:
	print("That is an odd number")
if (number % 10) == 0:
	print("This number can be divisible by 10")
else:
	print("This number can not be divisible by 10")