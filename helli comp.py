n = int(input('How many people are in race?'))
s = 0
if n<=2 :
    print('You cant enter 2>n !')
if n>=100 :
    print('You cant enter 100<n !')
else:
    for i in range(1, (n+1)) :
        if i>s :
            s = i
    for i in range(1, (n+1)) :
        if s>i>