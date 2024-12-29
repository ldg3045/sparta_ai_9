# 약수 구하기

# 정수 n이 매개변수로 주어질 때, 
# n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n): 
    answer = []                # 약수를 담을 리스트
    for i in range(1, n//2+1): # 1부터 n//2까지 반복
        if n % i == 0:         # n이 i로 나누어 떨어지면
            answer.append(i)   # 약수를 answer 리스트에 추가
    answer.append(n)           # 24는 2로 나눠지면 12까지만 추가되니, 마지막에 따로 추가
    return answer              

print(solution(24))

# 출력 결과: [1, 2, 3, 4, 6, 8, 12, 24]