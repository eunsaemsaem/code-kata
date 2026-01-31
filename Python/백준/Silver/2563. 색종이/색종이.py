white = [[False for j in range(100)] for i in range(100)]

n = int(input())
cnt = 0

for i in range(n):
    s_point = input().split(' ')
    x_p = int(s_point[0])
    y_p = int(s_point[1])

    for x in range(10):
        for y in range(10):
            white[x_p + x][y_p + y] = True

for i in range(100):
    for j in range(100):
        if white[i][j] == True:
            cnt += 1

print(cnt)