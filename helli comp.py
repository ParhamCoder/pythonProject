n = int(input())
height = []
first = 0
for i in range(n):
    num = int(input())
    height.append(num)
height2 = height
height.sort()
answer = height[-2]
answer2 = height2.index(answer)
print(answer, 'index=',answer2 + 1)
