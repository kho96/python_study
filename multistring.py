# multistring.py

print("=" * 10) # for사용할 필요없이 문자열 반복이 가능함.
print(" My Program ")
print("=" * 10)

a = "Life is too short. You need Python"
# 문자열 길이구하기(length)
b = len(a) #길이 구하기 :  len()
print(b)
# 문자열 슬라이싱(substring)
print(a[0:4]) # 변수[start-index:last-index] 0부터 4전까지 추출
print(a[19:]) # 변수[start-index:] start-index부터 끝까지 추출
print(a[:4]) # 변수[:last-index] 처음부터 last-index전까지 문자추출

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)
print(date +" / " + weather)
year = date[:4]
month = date[4:6]
day = date[6:8]
print(year + "-" + month + "-" + day + "/" + weather)

# a[8] = "r"  // error - 문자열 변경 불가
# print(a)
b = a[:8] + "r" + a[9:]
print(b)
# %d (d:decimal(10진 정수)) 3이 %d에 대입됨
print("I eat %d apples." % 3)
# %s (s:string(문자열))  five가 %s에 대입됨
print("I eat %s apples." % "five")
#자릿수, 10자리를 잡아서 five를 넣음
print("I eat %10s apples." % "five") #오른쪽정렬(양수)
print("I eat %-10s apples." % "five") #왼쪽정렬(음수)

# 소숫점(소숫점 이하 n자리 표시)
print("%0.4f" % 3.42134234) # 소숫점이하 4자리 표현

# 공백채우기
i = "...{0:=^10}...".format("hi")
print(i)