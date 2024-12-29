def solution():
    answer = 5
    return answer

def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        if len(arr1)>len(arr2):
            return 1
        else:
            return -1
    elif sum(arr1) != sum(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        else:
            return -1
    else:
        return 0
    
from collections import Counter










def solution(array):
    # 배열의 요소들의 빈도를 계산
    count = Counter(array)
    
    # 빈도 수가 가장 높은 요소를 찾음
    most_common = count.most_common()
    
    # 가장 높은 빈도 수를 가진 요소를 찾음
    max_frequency = most_common[0][1]
    
    # 가장 높은 빈도 수를 가진 요소가 여러 개 있는지 확인
    if len([item for item in most_common if item[1] == max_frequency]) > 1:
        return -1
    else:
        return most_common[0][0]

# 테스트
print(solution([1, 2, 3, 3, 3, 4]))  # 출력: 3
print(solution([1, 1, 2, 2]))        # 출력: -1
print(solution([1])) 


def solution(array):
	count = [0] * (max(array)+1) # 숫자 출연 횟수를 셀 리스트

	for i in array:
		count[i] += 1

	m = 0 # 최빈값의 개수
	for c in count:
		if c == max(count):
			m += 1
    
	if m > 1: # 최빈값이 2개 이상이면 -1을 리턴
		return -1
	else: # 최빈값이 1개이면 해당 숫자를 리턴
		return count.index(max(count))
     


a = ('민정', 27)
b = ('민정', 27)
print(id(a))
print(id(b))