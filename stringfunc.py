# stringfunc.py

# 문자열 관련 함수

#문자 갯수 세기 - count
a = "hobby"
print(a.count("b")) 

#문자의 위치 얻기 - find
a = "Python is the best choice"
print(a.find("b"))
print(a.find("k")) #문자열에 해당 문자가 존재하지 않는 경우 -1을 반환함

# 문자의 위치 얻기 - index // find와는 다르게 없는 문자를 찾는 경우 에러발생
print(a.index("b"))

# 문자 삽입
a = ",".join("abcd") # "abcd"를 ","로 연결해서 하나의 문자열로 반환
print(a)

# 문자삽입 - 리스트에 적용하기  // 리스트 - 배열이라고 생각하자...
a = ",".join(["a", "b", "c", "d"]) # 각 원소를 ","로 연결한 문자열 반환
print(a)

# 대문자로 변경 - upper
a = "hi"
print(a.upper())

# 소문자 변경 - lower
a = "HI"
print(a.lower())

# 공백제거 lstrip(왼쪽 공백 제거), rstrip(오른쪽 공백 제거), strip(양쪽 공백 제거)
a = "     hi      "
b = "==="
print(b + a.lstrip() + b)
print(b + a.rstrip() + b)
print(b + a.strip() + b)
 
a = "    h    i     "
print(b + a.strip() + b) #문자열 중간의 공백은 제거되지 않는다.

#문자열 바꾸기 - replace
a = "Life is too short"
a.replace("Life", "Your leg")
print(a) # 변경 되지않음 (문자열은 immutable)
b = a.replace("Life", "Your leg") #바꿔서 새로운 문자열을 반환
print(b) 

# 문자열 쪼개기 - split => 리스트로 반환함
a = "a:b:c:d"
b = a.split(":")
print(b)

# 특정 문자 미지정시 - 화이트 스페이스(공백, 탭, 엔터)로 쪼갠다.
a = "Life is too short"
b= a.split()
print(b)