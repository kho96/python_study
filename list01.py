# list01.py

# 리스트 - 배열

a = []
print(a)
a = list() #빈 리스트 생성
print(a)

# 숫자로 이루어진 리스트
a = [1, 3, 5, 7, 9]
print(a)

# 문자열 리스트
a = ["a", "b", "c", "d"]
print(a)

# 숫자, 문자 혼합 리스트
a = [1, 3, "a", "b"]
print(a)

# 인덱스로 데이터 추출 - [index] : 0부터 시작함
print(a[0])
# print(a[4]) #존재하지 않는 인덱스를 입력한 경우 error (index out of range)

# 리스트를 원소로 갖는 리스트
a = [1, 2, 3, [4, 5]]
print(a)
print(a[3]) #[4,5]
print(a[0] + a[3][1]) #(1 + 5)

#삼중 리스트
a = [1, 2, 3, [4, [5, 6]]] 
print(a[3][1][0]) #5

# 원소변경? -- 가능하다. 단, 문자열(문자열 상수)은 불가능하다
a[0] = 10
print(a)

# 리스트 슬라이싱(부분 데이터) - [시작인덱스:끝인덱스]
# 시작인덱스 부터 끝인덱스-1 까지 (끝인덱스는 미포함)
a = [1, 2, 3, 4, 5]
print(a[:3])
print(a[3:])

# 중첩된 리스트에서의 슬라이싱
a = [1, 2, 3, [4, 5, 6], 7]
print(a[1:4])
print(a[3][1:2])

# 리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6, 7]
print(a+b) # 덧셈이 아닌 두개의 리스트를 합친다.
print(a * 3) # 리스트를 3번 합친다.

# 리스트 길이(크기) 구하기  /문자열의 길이를 구하는 것과 같다. len()
a = [1, 2, 3, 4, 5]
print(len(a))

print(type(a))
print(type("hi"))
# print(a+"hi") type mismatch 에러

# 리스트 원소 삭제
del a[1] # a의 [1]번째 원소 삭제
print(a)

a = [1, 2, 3, 4, 5]
del a[1:4] # 슬라이싱을 이용한 삭제도 가능하다
print(a)

# 리스트 관련 함수

# 마지막 원소 추가(append)
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

#데이터(원소) 정렬 //오름차순 sort
a = [3, 7, 2, 1]
a.sort()
print(a)

# 글자 정렬 //가나다순, 사전순 sort
a = ["B", "Z", "C"]
a.sort()
print(a)

# 역순(reverse) 
a = [3, 7, 2]
a.reverse()
print(a)

# 내림차순 
a = [3, 5, 2]
a.sort() # [2, 3, 5]
a.reverse() # [5, 3, 2]
print(a)

#원소의 위치(index) //없는 원소를 확인하는 경우 error, 리스트에는 find라는 함수가 존재하지 않음.
print(a.index(5))

# 중간에 원소 삽입하기 - insert(index, value)
a = [1, 2, 3]
a.insert(0, 4)
print(a)
a.insert(3,5)
print(a)

# append <-> pop() (제일 뒤의 원소 꺼내기)
a = [1,2,3]
print(a.pop()) #얻어내는 것이 아닌 빼서 가져오는 것
print(a)

# insert <-> remove(data)
a = [1, 2, 3]
a.remove(2)
print(a)

# insert <-> pop(index)
a = [1, 2, 3]
a.pop(1)
print(a)

# 중복된 원소를 가진 경우 remove -> 제일 처음의 원소를 찾아내서 삭제함
a = [1, 2, 3, 1, 2, 3]
a.remove(2)
print(a)

# 특정 값 갯수 세기
a = [1, 2, 3, 1, 2, 3]
print(a.count(2))

# 리스트 더하기(확장하기)
a = [1, 2, 3]
a.extend([7, 8, 9])
print(a)