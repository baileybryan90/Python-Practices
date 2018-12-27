check = int(input("What number do you want to evaluate? : "))

#interesting, it doesn't evaluate check/check without an additional iteration
#turns out range generates a list of all integers in the range
#NOT including the right parameter. I would like to know why range
#is written that way.
# for reference: range([start], stop[, step]) #only integers
for x in range(1,check+1):
    if check % x == 0:
        print(x)
