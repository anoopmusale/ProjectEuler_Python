first = 1
second = 1
sum = 0
while second < 4000000:
    if second%2 == 0:
        sum +=second
    temp,first = first,second
    second = temp+second
print(sum)


