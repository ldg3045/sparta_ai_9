def cat(x):        # x는 매개변수(parameter)입니다
    answer = x     # x로 받은 값을 answer에 저장
    return answer 

print(cat(7))


def num(a,b) :
    answer = a + b
    if 10 < answer :
        print("크다")
    elif 10 > answer :
        print("작다")
    else:
        print("같다")
    return answer
print(num(7,5))



def num(a,b):
    answer = 0
    if a == b :
        return "같음"
    elif a > b :
        return "첫째"
    elif a < b :
        return "둘째"
print(num(1,8))




def num(a,b):
    answer = a + b
    if answer > 10 and a==b :
        return "특별"
    elif answer > 10 :
        return "크다"
    elif answer < 10 :
        return "작다"
    else:
        return "같다"
print(num(1,8))


# 세 개의 숫자를 비교하여 같은 숫자가 있는지 확인하는 함수
def num(a,b,c):
    if a == b == c :
        return "삼삼"
    elif a == b or a == c or b == c :
        return "둘둘"
    else:
        return "다달라"
print(num(1,8,5))



# 리스트의 특징
a_list = [1,2,3,4,5]

a_list[3] = 7
print(a_list)
# [1, 2, 3, 7, 5]


a_list= range(5)
length = len(a_list)
print(length)
# 5


i = [6,98,1]
i.sort(reverse=True)
print(i)
#[98, 6, 1]

result = [123,455,61]
print(result[:])

# #1부터 15까지의 숫자 중에서
# 3의 배수만 선택해
# 각 숫자를 2배로 만드는 리스트
result = [num *2 for num in range(1,16) if num % 3 == 0]
print(result)

# #1부터 20까지의 숫자 중에서
# 4의 배수이면서
# 6보다 큰 숫자만 선택해서
# 각 숫자를 3배로 만드는 리스트

result = [num * 3  for num in range(1,21) if num %4 == 0 and num >6 ]
print(result)


# 1부터 30까지의 숫자 중에서:
# 3의 배수는 "삼"
# 5의 배수는 "오"
# 3과 5의 배수(15의 배수)는 "삼오"
# 나머지 숫자는 그대로 숫자를
# 리스트로 만들어보세요.

#리스트 컴프리헨션 방식
result = ["삼오"if num %15 == 0 else
          "삼"if num %3 == 0 else
          "오"if num %5 == 0 else 
          num for num in range(1,31)]
print(result)

## 일반 함수 버전 (더 읽기 쉬움)
def get_numbers():
    result = []
    for num in range(1,31):
        if num % 15 == 0:
            result.append("삼오")
        elif num % 3 == 0:
            result.append("삼")
        elif num % 5 == 0:
            result.append("오")
        else:
            result.append(num)
    return result

print(get_numbers())


# 리스트 [10, 20, 40, 50]에서 30을 올바른 위치에 삽입해보세요.
num = [10,20,40,50]

num.insert(2,30)
print(num)

# 1. 모든 숫자 사이에 그 숫자들의 평균을 삽입하세요
# 예상 결과: [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

num = [1, 2, 3, 4, 5]
num.insert(1,(num[0]+num[1])/2)
num.insert(3,(num[2]+num[3])/2)
num.insert(5,(num[4]+num[5])/2)
num.insert(7,(num[6]+num[7])/2)
print(num)





#매개변수 학습



def double(number):
   print(number*2) 


#합
def add(a, b):
    return a +b
result = add(3, 4) 
print(result)   

#평균
def average(a, b, c):
    return a+b+c /3
result = average(3, 4, 5)   # result에는 4.0이 저장됩니다
print(result)    



# 인사하기
# name의 기본값은 "Guest"입니다
def greet(name="Guest"):
    print(f"안녕하세요, {name}님!")

# 실행 예시
greet()          # 출력: "안녕하세요, Guest님!"
greet("영희")    # 출력: "안녕하세요, 영희님!"




# 곱하기
# 두 수를 곱하는 함수입니다. b의 기본값은 1입니다
def multiply(a, b=1):
   return a*b

# 실행 예시
print(multiply(3))     # 출력: 3  (3 * 1)
print(multiply(3, 4))  # 출력: 12 (3 * 4)



# 거듭제곱
# 숫자 n을 power번 거제곱하는 함수입니다. power의 기본값은 2입니다
def power_n(n, power=2):
    return n ** power

# 실행 예시
print(power_n(3))     # 출력: 9   (3의 2제곱)
print(power_n(3, 3))  # 출력: 27  (3의 3제곱)



# 학생 정보 출력하기
# 학생의 이름, 나이, 학년을 출력합니다. 
# 나이의 기본값은 20, 학년의 기본값은 1입니다
def print_student(name, age=20, grade=1):
    print(f"{name}님은 {age}살이고 {grade}학년입니다.")

# 실행 예시
print_student("김철수")             # 출력: "김철수님은 20살이고 1학년입니다."
print_student("박영희", 19)         # 출력: "박영희님은 19살이고 1학년입니다."
print_student("이민수", 21, 3)      # 출력: "이민수님은 21살이고 3학년입니다."




# 상품 정보 출력하기
# 상품의 이름, 가격, 수량을 출력합니다.
# 가격의 기본값은 1000, 수량의 기본값은 1입니다
def print_product(name, price=1000, quantity=1):
    print(f"{name}의 가격은 {price}원이고 {quantity}개 있습니다.")

# 실행 예시
print_product("연필")                # 출력: "연필의 가격은 1000원이고 1개 있습니다."
print_product("지우개", 500)         # 출력: "지우개의 가격은 500��이고 1개 있습니다."
print_product("노트", 2000, 5)       # 출력: "노트의 가격은 2000원이고 5개 있습니다."



# 상품 정보와 총 가격 출력하기
# 상품의 이름, 가격, 수량을 출력하고 총 가격도 계산합니다.
# 가격의 기본값은 1000, 수량의 기본값은 1입니다
def print_product_total(name, price=1000, quantity=1):
    print(f"{name}의 가격은 {price}원이고 {quantity}개 있습니다. 총 가격: {price*quantity}원")

# 실행 예시
print_product_total("연필")          # 출력: "연필의 가격은 1000원이고 1개 있습니다. 총 가격: 1000원"
print_product_total("지우개", 500)    # 출력: "지우개의 가격은 500원이고 1개 있습니다. 총 가격: 500원"
print_product_total("노트", 2000, 5)  # 출력: "노트의 가격은 2000원이고 5개 있습니다. 총 가격: 10000원"



# 상품 정보와 할인된 가격 출력하기
# 상품의 이름, 가격, 수량, 할인율을 받아서 출력합니다.
# 가격의 기본값은 1000, 수량의 기본값은 1, 할인율의 기본값은 0입니다
def print_product_discount(name, price=1000, quantity=1, discount=0):
    print(f"{name}의 가격은 {price}원이고 {quantity}개 있습니다. 할인된 가격: {int((price*quantity)*(1-discount))}원")

# 실행 예시
print_product_discount("연필")                    # 출력: "연필의 가격은 1000원이고 1개 있습니다. 할인된 가격: 1000원"
print_product_discount("지우개", 500, 2, 0.1)     # 출력: "지우개의 가격은 500원이고 2개 있습니다. 할인된 가격: 900원"
print_product_discount("노트", 2000, 5, 0.2)      # 출력: "노트의 가격은 2000원이고 5개 있습니다. 할인된 가격: 8000원"



# 상품 정보, 할인율, 세금을 계산하여 출력하기
# 상품의 이름, 가격, 수량, 할인율을 받아서 출력합니다.
# 가격의 기본값은 1000, 수량의 기본값은 1, 할인율의 기본값은 0입니다
# 세금은 10%로 고정입니다
def print_product_tax(name, price=1000, quantity=1, discount=0):
    discount_1=int((price*quantity)*(1-discount))
    print(f"{name}의 가격은 {price}원이고 {quantity}개 있습니다. 할인된 가격: {discount_1}원, 세금포함 가격: {int((discount_1)*1.1)}원")

# 실행 예시
print_product_tax("연필")                    # 출력: "연필의 가격은 1000원이고 1개 있습니다. 할인된 가격: 1000원, 세금포함 가격: 1100원"
print_product_tax("지우개", 500, 2, 0.1)     # 출력: "지우개의 가격은 500원이고 2개 있습니다. 할인된 가격: 900원, 세금포함 가격: 990원"
print_product_tax("노트", 2000, 5, 0.2)      # 출력: "노트의 가격은 2000원이고 5개 있습니다. 할인된 가격: 8000원, 세금포함 가격: 8800원"




# 상품 정보, 할인율, 세금, 배송비를 계산하여 출력하기
# 상품의 이름, 가격, 수량, 할인율을 받아서 출력합니다.
# 가격의 기본값은 1000, 수량의 기본값은 1, 할인율의 기본값은 0입니다
# 세금은 10%로 고정입니다
# 배송비는 3만원 이상 구매시 무료, 그 외에는 3000원입니다
# 포인트는 최종 가격의 1% 적립됩니다
def print_product_point(name, price=1000, quantity=1, discount=0):

    discount_price = int((price*quantity)*(1-discount))
    tax_price = int(discount_price* 1.1)
    delivery_cost = 3000 if discount_price <= 30000 else 0
    final_price = tax_price + delivery_cost
    point = int(final_price * 0.01)

    print(f"{name}의 가격은 {price}이고 {quantity}개 있습니다.",
          f"할인된 가격: {discount_price}원,",
          f"세금포함 가격:{tax_price}원,",
          f"배송비:{delivery_cost}원,",
          f"최종 가격:{final_price}원,",
          f"적립 포인트:{point}원")

# 실행 예시
print_product_point("연필")                    
# 출력: "연필의 가격은 1000원이고 1개 있습니다. 
# 할인된 가격: 1000원, 세금포함 가격: 1100원, 배송비: 3000원, 최종 가격: 4100원, 
# 적립 포인트: 41원"

print_product_point("지우개", 500, 2, 0.1)     
# 출력: "지우개의 가격은 500원이고 2개 있습니다. 
# 할인된 가격: 900원, 세금포함 가격: 990원, 배송비: 3000원, 최종 가격: 3990원, 
# 적립 포인트: 39원"

print_product_point("노트", 2000, 20, 0.2)      
# 출력: "노트의 가격은 2000원이고 20개 있습니다. 
# 할인된 가격: 32000원, 세금포함 가격: 35200원, 배송비: 0원, 최종 가격: 35200원, 
# 적립 포인트: 352원"





# ---
# 조건부 표현식 (삼항 연산자)
# result = 값 if 조건 else 값2



# --- 
# 리스트 컴프리헨션 
# numbers = [ 표현식 for 항목 in 반복가능객체 ]
# numbers = [ 표현식 for 항목 in 반복가능객체 if 조건문 ]


# ---
# 딕셔너리 컴프리핸션
# squares = { 키:값 for 항목 in 반복가능객체 }
# squares = { 키:값 for 항목 in 반복가능객체 if 조건문 }



# 문제 1: 다음 조건을 만족하는 리스트 컴프리헨션을 작성해보세요
# - 1부터 20까지의 숫자 중
# - 3의 배수이면서 4의 배수인 수만 선택
# - 선택된 수를 2배로 만들기

num = [i*2 for i in range(1,21) if  i % 3 == 0 and i % 4 ==0]
print(num)
# 문제 2: 다음 조건을 만족하는 딕셔너리 컴프리헨션을 작성해보세요
# - 1부터 10까지의 숫자에 대해
# - 키는 숫자 자체
# - 값은 숫자의 제곱
# - 단, 짝수인 경우만 선택

dic = {i : i**2 for i in range(1,11) if i % 2 ==0 }
print(dic)







# -- while 반복문 
# 기본적인 while문 예제

# 1부터 5까지 출력하기
number = 1
while number <= 5:
    print(number)    # 먼저 출력
    number += 1      # 그 다음 증가
# 출력 결과:
# 1
# 2
# 3
# 4
# 5

number = 1
while number <= 5:
    number += 1      # 먼저 증가
    print(number)    # 그 다음 출력
# 출력 결과:
# 2
# 3
# 4
# 5
# 6


# while문을 사용한 구구단 (2단) 출력
num = 1
while num <= 9:
    print(f"2 x {num} = {2 * num}")
    num += 1

# break를 사용한 while문
# 사용자가 'q'를 입력하면 종료
while True:
    answer = input("계속하려면 아무 키나, 종료하려면 'q'를 입력하세요: ")
    if answer == 'q':
        break
    print("계속 진행합니다.")




# 문제 1: while문을 사용하여------------------------
# 1부터 시작하여 합이 100을 넘지 않는 
# 가장 큰 수를 찾아보세요


num = 1          # 더해갈 숫자
total = 0        # 합계를 저장할 변수

while total + num <= 100:    # 다음 숫자를 더했을 때 100을 넘지 않으면
    total += num             # 합계에 현재 숫자를 더함
    num += 1                 # 다음 숫자로 이동

print(f"마지막으로 더한 숫자: {num-1}")    # 마지막으로 더한 숫자
print(f"총합: {total}")                    # 최종 합계




# while True:는 무한 반복문을 만들 때 사용합니다. 
# True는 항상 참이기 때문에 계속 반복되죠. 
# break로 반복문을 빠져나갈 수 있게 합니다.

# 사용자가 'q'를 입력할 때까지 계속 반복
while True:
    text = input("아무 글자나 입력하세요 (종료하려면 'q'): ")
    if text == 'q':
        break    # q를 입력하면 반복문을 빠져나감
    print(f"입력한 글자: {text}")
   # break를 뒤에 두면 무조건 한 번만 실행되고 종료됨
   # 뒤에 두면 반복이 되지 않음

#반드시 실행 코드를 작성할 때는 앞에 break를 두기



# 문제: while문을 사용하여-----------------------
# 1. 사용자에게 숫자를 계속 입력받고
# 2. 입력받은 숫자들의 합을 계산하다가
# 3. 사용자가 0을 입력하면 
# 4. 지금까지의 합계를 출력하고 종료하는 
# 프로그램을 작성해보세요

# 초기화가 필요한 이유:
        # 출력값 앞에 num += total은 num = num + total의 축약형입니다
        # 만약 num이 없다면, 처음 더할 때 num의 값이 없어 오류가 발생
num = 0 # 합계를 계산할 때는 항상 시작값이 필요합니다
        
while True :    # 참으로 계속 반복
    total = int(input("입력하세요: ")) # 입력받은 값을 정수로 변환
    if total == 0: # 0을 입력하면 반복문을 빠져나감
        break #
    num += total # 입력받은 값이랑 더함
    print(f"총합: {num}") # 총합을 출력





# 문제: while문을 사용하여----------------------
# 1. 사용자에게 숫자를 입력받고
# 2. 1부터 입력받은 숫자까지의 합을 계산하는
# 프로그램을 작성해보세요

# 예시:
# 숫자를 입력하세요: 5
# 1부터 5까지의 합: 15  (1+2+3+4+5 = 15)

num = 0                        # 합계를 저장
total = int(input("입력: "))   # 숫자를 한 번만 입력받음

current = 1                    # 1부터 시작
while current <= total:        # total까지만 반복
    num += current            # 현재 숫자를 더함
    current += 1              # 다음 숫자로

print(f"1부터 {total}까지의 합: {num}")


#    1.먼저 필요한 변수들을 생각합니다:
num = 0        # 합계를 저장할 변수
total = int(input("입력: "))   # 목표 숫자
current = 1    # 1부터 시작할 변수

#   2. while문의 조건을 생각합니다:
#    "1부터 입력받은 숫자까지" → current <= total

#   3.반복할 작업을 생각합니다:
#     현재 숫자를 합계에 더하기 → num += current
#    다음 숫자로 이동 → current += 1

#   4.마지막으로 결과를 출력합니다



# 문제: while문을 사용하여----------------------------
# 1. 사용자에게 숫자를 계속 입력받고
# 2. 입력받은 숫자가 양수면 더하고
# 3. 음수면 더하지 않고 넘어가고
# 4. 0을 입력하면 지금까지 더한 양수들의 합계를 출력하고 종료하는
# 프로그램을 작성해보세요

num = 0            # 합계를 저장할 변수
while True :
    current = int(input("숫자 입력: "))
    if current == 0 :
        break            # 0이면 종료
    if current > 0 :
        num += current   # 양수면 더하기
    # 음수는 아무 작업도 하지 않음 (그냥 넘어감)
    print(f"현재까지 합: {num}")
print(f"양수들의 합: {num}") # 0을 입력하면 나오는 합들의 값



