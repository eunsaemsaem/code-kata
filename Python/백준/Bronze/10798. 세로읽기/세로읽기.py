words = []
result = ''

# 5줄의 입력을 읽어들임
for i in range(5):
	words.append(input())

for j in range(15):
        for i in range(5):
            if j < len(words[i]):
                result += words[i][j]
				
print(result)