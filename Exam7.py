#표준입출력

#sep=""  / , 사이의 값을 지정해 줄 수 있다

# print("Pyton", "java", "JS", sep=" vs ")

# print("Pyton", "java", "JS", sep="," ,end="?")
# print("무엇이 더 재밌을 까요?")

#표준 출력
# import sys
# print("Pyton", "java", file=sys.stdout) #표준출력
# print("Pyton", "java", file=sys.stderr) #에러처리

#시험성적
# score = {"수학":0, "영어":50, "코딩":100}
# for subject, score in score.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

#은행 대기 순번표
# 001,002,003
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer +"입니다.")

#빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))

# #양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >10}".format(-500))

# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))

# # 3자리마다 콤마를 찍어주기
# print("{0:,}".format(10000000000))

# # 3자리마다 콤마를 찍어주기, + - 부호도 붙이기
# print("{0:+,}".format(10000000000))
# print("{0:-,}".format(10000000000))

# # 3자리마다 콤마를 찍어주기, + - 부호도 붙이기, 자릿수 확보하기
# # 빈자리는 ^로 채워주기
# print("{0:^<+30,}".format(1000000000))

# # 소수점 출력
# print("{0:f}".format(5/3))

# #소수점 특정 자리수 까지만표시 (소수점 3째자리에서 반올림)
# print("{0:.2f}".format(5/3))


#파일 입출력

# w 쓰기
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# a 덮어쓰기
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("코딩 : 100")
# score_file.close()

# 읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline(), end="") # 줄바꿈 없이는 end=""
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()


#리스트에 넣어서
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # List 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()

#Pickle
# import pickle
# profile_file = open("profile.pickle","wb")
# profile ={"이름":"박명수", "나이":30, "취미":["축구","골프","롤"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file에 저장
# profile_file.close()

import pickle

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf-8") as study_file:
  study_file  .write("파이썬 학습중")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())


