#옷가게 할인 받기

# 10만 원 이상 사면 5%, 
# 30만 원 이상 사면 10%, 
# 50만 원 이상 사면 20%


#   제한사항
#        10 ≤ price ≤ 1,000,000
#            price는 10원 단위로(1의 자리가 0) 주어집니다.
#   소수점 이하를 버린 정수를 return합니다.


def solution(price):
    if price >= 500000:
        return int(price * 0.8) # 소수점 이하를 버린 정수
    elif price >= 300000:
        return int(price * 0.9) # 정수로 리턴
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price
    
    
print(solution(150000)) # 142500