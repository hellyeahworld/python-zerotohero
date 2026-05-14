import random
computer_choice = random.randint(1, 3)

print("1.sang 2. kakhaz 3.gheychi")
user_choice = int(input("please enter your choice(1, 2, 3)"))

if user_choice == computer_choice:
    print("Mosavi! ")
elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):    print("You won! ")
else:
    print("you lost! ")