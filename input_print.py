# input_print.py

# input - 사용자로 부터 입력을 받음(scanner.nextLine()과 유사 - 반환값이 문자열)
# a = input("숫자를 입력해주세요:")
# print(a)
# print(type(a)) # 입력값-> 문자열로 취급 str
# print(type(int(a))) # 문자열 -> 숫자열로 변경함.

# print - 출력(출력 후 처리 - \n(기본값), 다른값으로 변경 가능)
for i in range(1, 11):
    print(i, end="-") # 1-2-3-4-5-6-7-8-9-10- 