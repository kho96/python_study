# dict01.py

# 딕셔너리(사전형 데이터) - java에서 Map과 같다.. (key와 value를 가짐..)
dic = {}
print(dic) #비어있는 딕셔너리

dic = {"name":"홍길동", "phone":"010-1111-1111", "birth":"2002-01-01"}
print(dic)

# 키로 숫자지정(인덱스는 아님)
dic = {0:"홍길동", 1:"강감찬", 2:"김유신"}
print(dic)

# 값에 리스트 넣기
dic = {"nums":[1, 2, 3]}
print(dic)

# 데이터 추가 (key,value 1쌍으로 추가해야함)
dic["scores"] = [100, 90, 80]
print(dic)

#데이터 삭제(key이용)
del dic["nums"]
print(dic)

# 리스트를 키로 사용은 불가능하다.
# aList = [1, 2]
# dic[aList] = [3, 4] #error
# print(dic) 

# 딕셔너리 관련 함수
# Enumeration - keys()
dic = {"a":1, "b":2, "c":3}
keys = dic.keys() #key만 빼내기, .keys()
print(keys)
for key in keys: # 반복문 사용 (for 변수명 in 반복대상)
    print(key)
for key in keys:
    print(key, dic[key]) 

vals = dic.values() #값만 빼내기, .values()
print(vals) 

# 키, 값을 쌍을 튜플로 빼내기
print(dic.items())

# 딕셔너리의 데이터 모두 지우기
dic.clear()
print(dic)

dic = {"a":1, "b":2, "c":3}
print(dic.get("a"))

#사전식배열 형태를 연관배열이라고 한다.. 없는 키를 지정할 경우 연관배열은 error발생
# print(dic["d"]) error
print(dic.get("d")) #None, 연관배열보다는 get을 사용하는 것이 편리할듯....

# 해당 키가 존재하는지
print("a" in dic) #True
print("d" in dic) #False