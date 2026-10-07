from random import *
active = True
def generate_random_number():
    variable = randint(1, 9999)
    return variable
def lancerpartie():
    variable = generate_random_number()
    while active == True:
        user_choice = int(input('Enter a number between 1 and 9999: '))
        if user_choice == variable:
            print("You won!")
            break
        while variable != user_choice:
            print(variable)
            if user_choice < variable:
                print("+")
                break
            else:
                print("-")
                break

while True:
    lancerpartie()
    user_input = input('Continue ? (y/n) ')
    if user_input == 'n':
        active = False
        break