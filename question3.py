# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.
def sum_of_numbers():
     sum = 0
     number=int(input("Enter a number (0 to quit):"))
if sum ==0:
    sum +=sum_of_numbers
    print("The sum of the entered number is:", sum)
  





# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2
for num in range(1, 101):
    if num % 2 != 0:
        print(num)
