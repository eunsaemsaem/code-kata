list1 = [[0 for j in range(9)] for i in range(9)]

for i in range(9):
    n = input()
    n1 = n.split(' ')
    for j in range(9):
        list1[i][j] = int(n1[j])

# max_num = max(map(max, list1))
max_num = -1
r = 0
c = 0

for i in range(9):
    for j in range(9):
        if list1[i][j] > max_num:
            max_num = list1[i][j]
            r = i
            c = j

print(max_num)
print(r+1, c+1)