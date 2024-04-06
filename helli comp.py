n = int(input())
height = []
first = 0
for i in range(n):
    num = int(input())
    height.append(num)
height2 = height.sort()
answer = height2[1] + 1
print(answer)
