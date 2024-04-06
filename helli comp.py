n = int(input())
height = []
if n >= 100 & n >= 2:
    for i in range(n):
        i = int(input('Enter :'))
        height.append(i)

height.sort()
print(height[1])
