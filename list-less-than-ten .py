a = [1,1,2,3,5,8,13,21,34,55,89]
b=[]

check = int(input("less than what? : "))


for x in a:
    if x < check:
        b.append(x)

for x in b: print(x)
    


