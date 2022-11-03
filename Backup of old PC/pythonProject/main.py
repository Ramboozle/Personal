import random
num = random.randint(1,111)
print("I'm thinking of a number between 1 and 111")
correct = 0
tries = 1
#print(correct,num,tries)
while correct == 0:
    guess = int(input())
    if guess == num:
        correct = 1
        print ('You got it in',tries,'tries!')
    elif guess < num:
        print('The number is higher')
        tries = tries+1
    else:
        print('The number is lower')
        tries = tries+1