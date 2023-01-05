# 평균 구하기
dic = {"국어":80, "수학":55, "영어":75}
vals = dic.values()
addAll = 0
for val in vals:
    addAll += val
print("평균 : {0}".format(addAll/len(vals)))

# 자연수 13이 홀수인지 아닌지?
num = 13
state = bool(num%2)
print(state) #True면 홀수, False면 짝수

# 나눠서 출력하기(yyyymmdd, num)
pin = "881120-1068234"
a = pin.split("-")
num = a[1]
yyyymmdd = "19"+a[0]
print(yyyymmdd)
print(num)

# 주민번호 뒷자리 맨첫번째 숫자 불러오기 
pin = "881120-1068234"
a = pin.split("-")
back = a[1]
print(back[0])

# a:b:c:d -> a#b#c#d로 변경하기
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# [1, 3, 5, 4, 2] -> [5, 4, 3, 2, 1] 변경하기
list1 = [1,3,5,4,2]
list1.sort()
list1.reverse()
print(list1)

# ["Life", "is", "too", "short"]리스트 -> "Life is too short" 문자열로 변경
list1 = ["Life", "is", "too", "short"]
result = " ".join(list1)
print(result)

# (1, 2, 3) -> (1, 2, 3, 4)
t1 = (1, 2, 3)
print(t1+(4,))

# 오류발생하는 경우 -> a[[1]] = 'python' 왜냐하면, 딕셔너리에 key로 List는 허용하지 않음.

#  딕셔너리에서 B값 출력하기
dic = {"A":90, "B":80, "C":70}
print(dic.get("B"))

# 중복제거하기
a = [1,1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b= list(aSet)
print(b)

# a 두번째 값 요소 변화시 b값의 변화,이유
a = b = [1, 2, 3]
a[1] = 4
print(b) # b도 변한다. 값을 복사함...(a,b는 같은 id이다.)