n = int(input())
height = []
first = 0
for i in range(n):
    num = int(input())
    height.append(num)
height.sort()
print(height[-2])
