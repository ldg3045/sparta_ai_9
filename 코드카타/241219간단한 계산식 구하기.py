# 문자열 binomial이 매개변수로 주어집니다. 
# binomial은 "a op b" 형태의 이항식이고 
# a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 
# 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 0 ≤ a, b ≤ 40,000
# 0을 제외하고 a, b는 0으로 시작하지 않습니다.
             # 바이너미얼 : 이항식
def solution(binomial):            # split 함수로 문자열을
    binomial = binomial.split(' ') # 공백을 기준으로 분리하여 리스트로 반환합니다.
    a = int(binomial[0])           # 0번째 인덱스를 정수로 변환
    op = binomial[1]               # 1번째 인덱스를 변수에 저장
    b = int(binomial[2])           # 2번째 인덱스를 정수로 변환
    
 #제한 사항 조건식 추가             # 만족하지 않으면 오류 메시지를 반환
    if not (0 <= a <= 40000 and 0 <= b <= 40000): 
        return "0보다 크고 40000보다 작은 수를 입력하세요."

# 연산자 조건식 추가
    if op == '+': # 연산자가 '+'인 경우
        return a+b
    elif op == '-': # 연산자가 '-'인 경우
        return a-b
    elif op == '*': # 연산자가 '*'인 경우
        return a*b
print(solution("4 + 7")) # 여기서 함수 호출