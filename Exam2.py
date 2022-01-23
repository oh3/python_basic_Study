#연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8

#나머지
print(5%3) # 5/3 = 2
print(10%3) # 10/3 = 1

#몫
print(5//3) # 1
print(10//3) # 3

#비교연산자
print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # 앞뒤가 같지 않다 True
print(not(1 != 3)) # False

# 2개 이상의 항을 연산
# ( and / &  ) 같은 의미
print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) #True 

# ( or / | ) 같은의미
print((3 > 0) or (3 > 5)) # True
print((3 > 0 | (3 > 5))) # True


#절대값
print(abs(-5)) # 5
print(pow(4,2)) # 4^2 = 4*4 = 16

#최대값 최소값
print(max(5, 12)) # 12
print(min(5, 12)) # 5

#반올림
print(round(3.14)) # 3
print(round(4.99)) # 5

#math 라이브러리 활용
from math import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4



#random 함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0~10.0 미만의 임의의 값 생성

print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성

print(int(random() * 10) + 1) # 1 ~ 10이하의 임의의 값 생성

#로또번호
print(int(random() * 45) + 1) # 1~ 45 이하의 임의의 값 생성

print(randrange(1,46))

print(randint(1, 45)) # 1~45 이하의 임의의 값 생성

#퀴즈2
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임날짜 : " + str(date)  + "일로 선정되었습니다")
