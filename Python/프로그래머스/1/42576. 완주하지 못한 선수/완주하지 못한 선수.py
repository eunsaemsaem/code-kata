def solution(participant, completion):
    answer = ''
    cnt = {}
    
    for i in participant:
        cnt[i] = cnt.get(i, 0) + 1
        
    for j in completion:
        cnt[j] -= 1
        
    for k in cnt:
        if cnt[k] >= 1:
            return k