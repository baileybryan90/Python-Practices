#I know its not like c++ but get used to typing data of the right side
num = int(input('enter your favorite positive whole number: '))
num2 = int(input('enter your second favority positive whole number: '))
if num % 2 == 0:
    print(num," is even")
    if num % 4 == 0:
        print("and also divisible by 4")
else:
    print(num," is odd")

if num % num2 == 0:
    print(num," is also evenly divisible by ", num2)
