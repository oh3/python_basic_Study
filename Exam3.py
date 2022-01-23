
#문자열
sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


#슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 ~ 2 직전까지(0, 1)
print("월 : " + jumin[2:4]) 
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7번째 부터 끝까지

print("뒤 7자리 (뒤에부터) : " +  jumin[-7:])
#맨 뒤에서 7번째부터 끝까지

#문자열 처리함수
python = "Python is Amazing"

#소문자
print(python.lower())

#대문자
print(python.upper())

#변수 첫번째 값이 대문자이냐?
print(python[0].isupper())

#전체 문자열 길이 반환
print(len(python))

#글자를 찾아서 바꿔서 출력
print(python.replace("Python", "Java"))

#글자 위치 찾기
index = python.index("n")
print(index)

#두번째 위치 n 찾기
index = python.index("n", index + 1)
print(index)

#index와 find의 차이
#내가 원하는 값을 찾지 못하면 -1을 반환
print(python.find("Java"))

#index에서는 에러를 발생시킴
#print(python.index("Java"))

#문장에서 n이 몇개인지
print(python.count("n"))

#문자열포맷
print("a" + "b")
print("a" + "b")

# 방법 1
print("나는 %d살 입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")

# %s
print("나는 %s살입니다." % 20)

print("나는 %s색과  %s색을 좋아해요." % ("파란", "빨간"))

# 방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("빨간", "파란"))
print("나는 {0}색과 {1}색을 좋아해요.".format("빨간", "파란"))
print("나는 {1}색과 {0}색을 좋아해요.".format("빨간", "파란"))

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format( color = "빨간", age = 20))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩" 입니다.
print('저는 "나도코딩" 입니다.')

print("저는 \"나도코딩\" 입니다.")
print("저는 \'나도코딩\' 입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\osm96\\Desktop\\PythonWorkspace>")

# \r : 커서를 맨앞으로 이동
print("Red Apple \rPine")

# \b : 백스페이스 ( 한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("asd \t 1234")

# 퀴즈

url = "http://naver.com"

my_str = url.replace("http://" , "") # 규칙1
#print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙2
#print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # 규칙3
print("{0}의 비밀번호는 {1} 입니다.".format(url, password))



