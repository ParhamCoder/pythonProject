n = int(input())
height = []
if n >= 100 & n >= 2:
    for i in  range(1, (n+1)):
        a = int(input('Enter :'))
        height.append(a)
        height = height.sort()

    print(height[1])
