# #함수

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# #함수의 전달값과 반환값

# #입금함수
# def deposit(balance, money):
#     print("입금이 완료 되었습니다. 잔액은 {0} 원 입니다.".format(balance+money))
#     return balance + money # 계좌+잔액

# #출금함수
# def withdraw(balance, money) :
#     if balance >= money : # 잔액이 출금액 보다 많으면
#         print("출금이 완료되었습니다. 잔액은{0} 원입니다.".format(balance - money))
#         return balance - money
#     else :
#         print("출금이 실패했습니다. 잔액은 {0}원입니다.".format(balance))

# #출금함수 (야간_수수료)
# def withdraw_night(balance, money):
#     commisstion = 100 # 수수료 100원
#     return commisstion, balance - money - commisstion


# balance = 0 # 잔액 
# balance = deposit(balance, 1000) # 입금
# balance = withdraw(balance, 500) # 출금

# commisstion, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원 이며, 잔액은 {1} 원입니다.".format(commisstion,balance))


# 함수 기본값
# def profile(name, age, main_lang):
#     print("이름 {0}\t 나이 : {1}\t 주 사용 언어 {2}"\
#     .format(name,age,main_lang))

# profile("유재석", 20, "파이썬")    
# profile("김태호", 20, "자바")   

#같은학교 같은학년 같은반 같은수업
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 {0}\t 나이 : {1}\t 주 사용 언어 {2}"\
#     .format(name,age,main_lang))

# profile("유재석")   
# profile("김태호")

# 키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

#가변인자를 이용한 함수 호출
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t 나이 : {1} \t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t 나이 : {1} \t".format(name,age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# print("유재석", 20, "Pyton", "Java", "C", "C++", "C#", "JS")
# print("김태호", 25, "Kotrlin", "Swift", "", "", "")

# 지역변수와 전역변수

# gun = 10

# def checkpoint(soldires): #경계근무
#     global gun # 전역 공간에 있는 gun변수 사용
#     gun = gun - soldires
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ref(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감

# gun = checkpoint_ref(gun, 2)
# print("남은 총 : {0}".format(gun))


# 함수 퀴즈
def std_weight(height, gender) : #키 m 단위(실수), 성별 : 남자, 여자
    if gender == "남자":
        return height * height * 22
    else :
        return height * height * 21
height = 175 # cm 단위
gender = "남자"        
weight = round(std_weight(height / 100, gender),2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))

