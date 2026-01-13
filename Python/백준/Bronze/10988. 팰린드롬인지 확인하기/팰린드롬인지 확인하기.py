s = input()
result = 0
leng = int(len(s) / 2)

if (len(s) == 1):
    result = 1

for i in range(leng):
    if(s[i] == s[-i-1]):
        result = 1
    else:
        result = 0
        break

print(result)