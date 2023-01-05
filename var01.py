#var01.py

# 변수
a = [1, 2, 3]
print(a)
print(id(a)) # 주소(메모리 위치) 확인

b = a # 값복사X 참조값 복사
print(id(b)) 
print(a == b)
print(a is b)

# a의 데이터 변경 => b의 데이터도 변경된다
a[1] = 4
print(a)
print(b)

# 값(데이터)을 복사
c = a[:] # 참조값 복사가 아닌 실제 값을 복사한 것이다.
print(c)
a[1] = 5
print(a)
print(b)
print(c)
print(id(a) == id(c)) #False a와 c는 다르다

d = a.copy() #위에서 처럼 split을 하지 않고 카피하면 복사가 된다.
print(id(a))
print(id(d))

# 튜플 사용(형식만 튜플... 튜플이 아님.. 데이터)
a, b = 1, 2  # (a, b) = (1, 2) // 괄호 생략 가능
print(a) 
print(b)

# temp를 사용한 스와핑을 쉽게 할 수 있다.
a, b = b, a
print(a)
print(b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # False

# 연습문제