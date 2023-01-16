#data_test.py

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://weather.naver.com/today"
with urlopen(url) as response:
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    elims = soup.select("._cnTimeTable ._cnItemTime")
    f = open("bs_learn/today.txt", "w", encoding="utf-8") # 한글깨짐 수정 (현재 파일 기준 bs_learn폴더에 들어있음)
    str = ""
    for elim in elims: # th들 찾기
        t = elim["data-ymdt"] # 시간
        w = elim["data-wetr-txt"] # 날씨
        p = elim["data-tmpr"] # dhseh
        str += t + "," + w + "," + p + "℃" + "\n"
    f.write(str) # 파일에 쓰기
    f.close()    