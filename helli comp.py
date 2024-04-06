n = int(input())
height = []
first = 0
if n >= 100 & n >= 2:
    for i in range(n):
        num = int(input())
        height.append(num)
    for j in height:
        if j > first:
            first = j

else:
    print('this amount of players are not valid')