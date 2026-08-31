def solution(s):
    stack = [] # list로 선언
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack: # if len(stack) == 0:
                return False # 바로 False 처리
            else:
                stack.pop()
            
    if not stack:
        return True
    else:
        return False