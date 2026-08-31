def solution(s):
    
    num = list(map(int, s.split(' '))) # 정수 리스트로 변환
    num.sort()
    
    return f'{min(num)} {max(num)}' # print f 활용