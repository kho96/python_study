# bool01.py

# 불 자료형 - 참/거짓 (True/False) 

a = True
b = False
c = "True"
d = "False"
print(a) #True
print(b) #False
print(c) #글자True
print(d) #글자False
print(type(a)) #bool
print(type(b)) #bool
print(type(c)) #str
print(type(d)) #str

# 비교 연산자의 결과 -> 참/거짓
print(2>1)
print(2==2)

# 데이터가 존재하는 경우 True를 반환한다.
# 문자열
# 타입 변환 - bool():불형으로 변환 ,int():정수형으로 변환, str():문자형으로 변환
print(bool("python")) #문자열 존재 -> True
print(bool("")) #문자열 존재X -> False

#리스트
print(bool([1, 2, 3])) #리스트에 데이터 존재 -> True
print(bool([])) #리스트에 데이터 존재X -> False

#튜플 -> 데이터가 있으면 True, 없으면 False
print(bool((1,2,3))) #True
print(bool(())) #False

#딕셔너리 -> 데이터가 있으면 True, 없으면 False
print(bool({"age":20}))
print(bool({}))

#숫자 -> 0인 경우 False, 나머지 True
print(bool(1)) #True
print(bool(0)) #False
print(bool(-1)) #True

#널(Null)값 = None -> False로 처리된다.
print(bool(None))

#반복문에서 활용
a = [1, 2, 3, 4]
while a: #a가 True이면 반복(리스트에 원소가 있는 경우 반복..)
    print(a.pop()) #리스트에서 마지막 원소 빼내기
    print(a)

print("while 종료")
