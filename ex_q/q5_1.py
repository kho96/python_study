#주어진 자연수가 홀수인지 짝수인지 판단하는 함수
def is_odd(num):
    if (num%2 == 0): #짝수
        return True  
    else: #홀수
        return False
        
# 입력으로 들어오는 모든 수의 평균값(단, 입력한 수는 정해지지 않음)
def avg_num(*num):
    result = 0
    for i in num:
        result += i
    return result/len(num)
print(avg_num(1,2)) 
print(avg_num(1,2,3,4,5))

# 두개의 숫자를 입력받아 더하여 돌려주는 프로그램
input1 = input("첫번째 수를 입력하세요:")
input2 = input("두번째 수를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다." % str(total))

#test.txt라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램
f1 = open("ex_q/test.txt", "w")
f1.write("Life is too short")
f1.close()
f2 = open("ex_q/test.txt", "r")
print(f2.read())
f2.close()

# 사용자의 입력을 test.txt에 저장하는 프로그램을 작성해보자(덮어쓰기x 추가)
user_input = input("저장할 내용을 입력하세요.")
f = open("ex_q/test.txt", "a")
f.write(user_input)
f.write("\n")
f.close()
f = open("ex_q/test.txt", "r")
print(f.read())
f.close()

# test.txt -> java라는 문자열을 python으로 변경하자
f = open("ex_q/test.txt", "w")
f.write("Life is too short \n" + "you need java")
f.close()
f = open("ex_q/test.txt", "r")
body = f.read()
f.close()
print(body)
body = body.replace("java", "python")
f = open("ex_q/test.txt", "w")
f.write(body)
f.close()
f = open("ex_q/test.txt", "r")
print(f.read())
f.close()

  