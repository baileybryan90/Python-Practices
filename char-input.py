print('Introduce yourself')
name = str(input('enter your name: '))
age = int(input('enter your age: '))
print("Your name is ",name,"your age is ",age)
oldAge = int(age+100)
print("in 100 years, you will be ", oldAge)

loop = int(input("enter a number "))

for x in range(loop):
    print("Your name is ",name,"your age is ",age)
    
