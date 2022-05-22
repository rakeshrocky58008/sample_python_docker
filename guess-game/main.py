import random
from art import art

print(art)
print("enter to nums game : ")
a = random.randint(0,100)
print("Guess the number bw 0 to 100 ")
val = input("choose difficulty easy or hard ").lower
print(f"psst the ans might be {a} ")
choice = 5
numrig = False
if val == 'easy':
    choice = 10
while numrig != True :
    if choice > 0:
        num = int(input(f'guess the number  , guesses u have left with {choice} :'))
    else:
        print("no more chnaces left , please run again to play ")    
    if num != a and choice >  0:    
        
        choice -=1
        if num < a:
            print("entered number is too low, guess higher ")
        else:
            print("entered number is too high, guess lower ")
    else:
        if num == a: 
            print("\n YAAY , You guessed right number Congrulations \n ")
        numrig = True
    