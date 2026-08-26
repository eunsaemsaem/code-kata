def solution(phone_book):
    answer = True
    phone_book.sort() # 정렬 후 인접한 숫자끼리만 비교
    
    for i in range(len(phone_book) -1):
        # 뒷 번호가 앞 번호로 시작하는지만 확인하면 됨
        if phone_book[i+1].startswith(phone_book[i]): 
            answer = False
    
    return answer