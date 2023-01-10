# file02.py

# 읽기 모드 - r

f = open("file/새파일.txt", "r")

# 한줄 읽기
# aLine = f.readline()
# print(aLine)

#여러줄 읽기(while사용)
# while True:
#     aLine = f.readline()
#     if not aLine: # 읽을 문장이 없다면 종료
#         break
#     print(aLine, end="") #end 기본값은 엔터

# 여러줄 읽기 - readlines
# lines = f.readlines()
# print(lines) # 줄 단위의 List를 반환한다. ['1번째 줄입니다. \n', ...]
# for line in lines:
#     print(line.strip()) # strip - 화이트스페이스(공백, 탭, 엔터 등)을 제거

# 파일 전체 읽기 - read
# data = f.read()
# print(data)

# 파일 객체 자체 사용 - 줄단위 작업 - readlines처럼 사용된다
for line in f:
    print(line.strip())
f.close()
