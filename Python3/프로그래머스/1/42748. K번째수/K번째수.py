def solution(array, commands):
    answer = []
    
    for a in range(len(commands)):
        i = commands[a][0]
        j = commands[a][1]
        k = commands[a][2]
        new_arr = [0]*(j-i+1)
        
        cnt = 0
        for b in range(i-1, j):
            new_arr[cnt] = array[b]
            cnt += 1
        
        new_arr.sort()
        answer.append(new_arr[k-1])
    
    return answer