# ch06_02.py

from urllib.request import urlopen
from bs4 import BeautifulSoup 

url = "https://weather.naver.com/today"
with urlopen(url) as response:
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    # elims = soup.select(".weather_now > div > strong") # select는 css요소를 가지고 찾아낼 수 있다.
    # print(elims[0].text) # 현재 온도0.5°
    elims = soup.select("._cnTimeTable ._cnItemTime")
    for elim in elims: # th들 찾기
        t = elim["data-ymdt"] # 시간
        w = elim["data-wetr-txt"] # 날씨
        p = elim["data-tmpr"] # dhseh
        print(t + "," + w + "," + p + "℃")