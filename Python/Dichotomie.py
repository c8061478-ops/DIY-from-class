import random
user_choice = int(input('Enter a number between 1 and 9999: '))
choice = None
bmin= 0
bmax= 10000
choice = (bmax - bmin) // 2
print(choice)
while choice != user_choice:
    rep = input('Enter + if the number is higher, - if it is lower: ')
    if rep == '+':
        choice += (bmax - bmin) // 2
        print(choice)
        bmin = choice
    elif rep == '-':
        choice -= (bmax - bmin) // 2
        print(choice)
        bmax = choice
print(f'Your number is: {choice}')