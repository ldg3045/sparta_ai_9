# 정수 배열 emergency가 매개변수로 주어질 때 
# 응급도가 높은 순서대로 진료 순서를 정한 
# 배열을 return하도록 solution 함수를 완성해주세요.

def solution(emergency):
    answer = []
    # sorted()를 사용하면 오름차순으로 정렬되는데
    # 내림차순으로 정렬하기 위해 reverse=True를 추가
    sorted_emergency = sorted(emergency, reverse=True)

                        # 각 응급도 값의 순위를 찾아서 저장
    for i in emergency: # append로 요소 추가
        answer.append(sorted_emergency.index(i) + 1) 
    return answer       # index로 값을 찾고, 순서가 0부터 시작하므로 +1

print(solution([3, 76, 24]))  # [3, 1, 2] 출력


