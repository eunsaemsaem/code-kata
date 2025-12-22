# 기준이 되는 배열 선언 (올바른 체스 말 개수)
ans = [1, 1, 2, 2, 2, 8]

# 사용자에게 가장 처음 입력받는 input : 전체가 하나의 string
ori_input = input ()
# ori_input을 공백을 기준으로 자르고, 각 요소를 int로 타입변환 (map 객체는 일종의 Iterator)
mapped_object = map(int, ori_input.split())
# int로 변환한 mapped_object을 리스트 형태로 저장
list_input = list(mapped_object)

# 최종 output
append_out = ""
# 6번 반복
for i in range(6):
    # 원본에서 입력값을 뺀 값을 out에 저장
    out = ans[i] - list_input[i]
    # 결과값을 append_out에 공백과 함께 붙임
    append_out += str(out) + " "

# 최종 결과값 출력
print(append_out)