n = int(input())
height = []
height2 = []
first = 0
a = 1
if n >= 100 or n <= 2:
    print('The amount of players is not valid')
else:
    for i in range(n):
        num = int(input(f'Enter height {a} : '))
        height.append(num)
        a += 1
        height2.append(num)
    height.sort()
    answer = height[-2]
    answer2 = height2.index(answer)
    print(answer, 'index=', (answer2 + 1))