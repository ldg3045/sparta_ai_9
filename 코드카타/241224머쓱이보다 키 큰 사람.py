# 머쓱이보다 키 큰 사람 구하기

# 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 
# 머쓱이보다 키 큰 사람 수를 return 하세요.

#   리스트 컴프리헨션을 사용해 표현식(i)을 만들고, 
def solution(array, height):   # 리스트 컴프리헨션은 array를 기반으로 if 값만 선택 됨
    return len([i for i in array.coun if i > height]) 
#   for 문에서 array 안에 있는 각각의 값을 임시로 i라고 하고, 
#   array에서 i가 height보다 큰 값을 찾고, 그 값의 개수를 반환  

print("머쓱이보다 큰 친구는",solution([150,180,176,161],175),'명')
#   친구들 키는 [150,180,176,161], 머쓱이의 키는 175
#   결과 : 머쓱이보다 큰 친구는 2 명

