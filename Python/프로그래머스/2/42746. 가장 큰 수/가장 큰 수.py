from functools import cmp_to_key

# 새 정렬 정의
def mySort(a, b):
    if (a+b) < (b+a): # ex) 303 vs. 330
        return 1 # 1이면 자리 바꿈
    elif (a+b) > (b+a):
        return -1 
    elif (a+b) == (b+a):
        return 0

def solution(numbers):
    answer = ''
    
    # numbers(int)를 string으로 변환
    numbers = list(map(str, numbers))
    # string인 상태에서 정렬 => 문자열의 가장 앞글자 기준으로 정렬됨
    numbers.sort(key=cmp_to_key(mySort))
    # 문자열 합치기
    answer = "".join(numbers)
    
    if (answer[0] == '0'): # int는 범위가 한정되어 있으니 효율적인 방법으로 비교
        answer = '0'
    
    return answer