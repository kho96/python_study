#set01.py

# set - 집합 (중복x, 순서x)

s1 = set([1, 2, 3]) #리스트를 집합으로 변경
print(s1) #{1,2,3}
s1 = {1, 2, 3}
print(s1)

# 문자열을 set로 변환
s1 = set("Hello")
print(s1) # 순서가 없고, 중복을 제거함

# 리스트를 집합 변환 -> 집합을 리스트로 변환
s1 = set([1, 2, 3])
print(s1) #{1,2,3} 
print(list(s1)) #[1, 2, 3] 순서가 없기 때문에..[1, 2, 3]이 아닌 [2, 1, 3]등이 나올 수 있음

# 집합 -> 튜플 변환
s1 = {1, 2, 3}
print(tuple(s1)) #(1,2,3)

# 합집합(union) |,union()
s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8, 9}
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))

# 교집합(intersection) &,intersection()
print(s1 & s2) # {4, 5, 6}
print(s1.intersection(s2))

# 차집합(difference) -,difference()
print(s1-s2) #{1, 2, 3}
print(s1.difference(s2))

# 집합에 데이터 추가
s1 = {1, 2, 3}
s1.add(4)
print(s1)
s1.add(3) 
print(s1) # 중복데이터는 추가하지 않음

# 집합에 여러개의 데이터 추가하기
s1 = {1, 2, 3}
s1.update([4, 5, 6])
print(s1)
s1.update([1, 3, 5, 7])
print(s1) # 중복데이터는 추가하지 않고 중복이 아닌 부분만 추가됨.

# 집합에서 데이터 제거
s1.remove(1)
print(s1)

# 여러개의 데이터 제거하기
# s1.remove([2, 3])
# print(s1)  error 여러개의 데이터는 제거 되지 않음
