#~~~~~~~~~~~TIMES TABLE TESTER~~~~~~~~~~~#
import random
numberList = []

whatToTest = input('would you like to test a times table or learn one? \n T/L \n ')
if  whatToTest == 'T':
    toTest = int(input("Enter a number to test: "))
    for i in range(11):
        number = random.randint(1,13)
        while number in numberList:
            number = random.randint(1,13)
        print('what is ', number, 'times ', toTest, '?')
        answer = number*toTest
        if int(input('answer: ')) == answer:
            print('correct')
        else:
            print('incorrect')
        numberList.append(number)
elif whatToTest== 'L':
    toLearn = int(input("Enter a number to learn: "))
    for i in range(1,13):
        print(toLearn, "x", i, "=", toLearn*i)
else:
    print("Invalid input")