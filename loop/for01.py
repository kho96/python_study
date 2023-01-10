# for01.py

#for 변수 in 리스트/튜플/문자열

test_list = ["one", "two", "thre"]

for s in test_list:
    print(s)
    
a, b = 1, 2
print(a)
print(b)
(c, d) = (3, 4)
print(c)
print(d)

a = [(1, 2), (3, 4), (5, 6)]
for (first,last) in a:
    print(first + last)
    
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생 : 합격입니다." % number)
    else:
        print("%d번 학생 : 불합격입니다." % number)
        
#break ,continue - while과 동일함

# 범위 표현 - range(시작값, 끝값) - 시작값 생략시 0부터, 끝값은 미포함..(미만..)
a = range(10)
print(a)

add = 0
for a in range(1, 11):
    print(a)
    add += a
print("합계 : " + str(add))

marks = [90, 25, 67, 45, 80]
# for (int i = 0; i < marks.length; i++)에 해당
for number in range(len(marks)):
    mark = marks[number]
    print(mark)
    if mark >= 60:
        print("%d번 학생 : 합격입니다." % (number+1))
    else:
        print("%d번 학생 : 불합격입니다." % (number+1))
    
# for, range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print("{0}".format(i*j), end=" ") # end의 기본값은 엔터
    print()    


