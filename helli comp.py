n = int(input('How many people are in race?'))
s = 0
m = 0
if n<=2 and 100<n:
    print('You cant enter 2>n !')
else:
    for i in range(1, (n+1)) :
        if i>s :
            s = i
    for i in range(1, (n+1)) :
        if s>i>m :
