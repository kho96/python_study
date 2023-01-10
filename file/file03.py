# file03.py

# 파일에 내용 추가하기 - a (append)

# f = open("file/새파일.txt", "a")
# for i in range(11, 20):
#     data = "%d번째 줄입니다." %i
#     f.write(data)
    

# f.close()
# print("파일 쓰기(추가) 완료")

# with ~ as 와 함께 사용하기 - close를 자동으로 해준다.
with open("file/새파일.txt", "r") as f:
    data = f.read()
    print(data)