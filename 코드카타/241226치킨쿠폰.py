# 치킨을 시켜먹으면 한 마리당 쿠폰을 한 장 발급합니다. 
# 쿠폰을 열 장 모으면 치킨을 한 마리 서비스로 받을 수 있고, 서비스 치킨에도 쿠폰이 발급됩니다. 
# 시켜먹은 치킨의 수 chicken이 매개변수로 주어질 때 
# 받을 수 있는 최대 서비스 치킨의 수를 return하도록 solution 함수를 완성해주세요.

def solution(chicken):
    service_chicken = 0  # 서비스 치킨 수
    coupon = chicken  # 1치킨 당 1쿠폰
    while coupon >= 10: # 쿠폰이 10장 이상일때 반복문 실행
        service_chicken += coupon // 10  # 10으로 나눈 몫을 서비스 치킨 수에 더함
        coupon = coupon // 10 + coupon % 10  # 쿠폰도 10으로 나눈 몫에 + 나머지(정수만 구해서) 더함
    return service_chicken # 서비스 치킨 수 반환

print(solution(100)) # 서비스 치킨 11마리

