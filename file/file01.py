# file01.py

# 파일 모드 - (w:write(덮어쓰기), r:read, a:append)

# 쓰기 모드 - w (덮어쓰기)
f = open("file/새파일.txt", "w")

for i in range(1, 11):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
    
# f.write("hello") # 덮어쓴다.

f.close()
print("파일 쓰기 종료")