# bs02.py

from bs4 import BeautifulSoup as bs

with open("index.html", "r", encoding="utf-8") as f:
    html_doc = f.read()
    soup = bs(html_doc) # soup = BeautifulSoup(html_doc)
    print(soup.prettify())
    print("=" * 50)
    # 자식
    # print(soup.p.b) # . : 첫번째 나오는 자식 1개  <b>a</b>
    # head_tag = soup.head
    # print(head_tag.contents) # 자식 엘리먼트 ( > )
                             # DOM 구조에서 한단계 아래 자식들
                             # .content - 태그안의 모든 요소 및 값들, 리스트 형태 ['\n', <title>index.html의 title</title>, '\n']
    # print(soup.body.contents)
    # print(soup.body.contents[1]) # eq:1, eq(1)
    
    # 자손 (자식 + 후손) - descendants
    # print(list(soup.head.descendants))
    # print(len(soup.head.contents)) # <title>
    # print(len(list(soup.head.descendants))) # <title>, string 까지 포함
    
    # 부모
    # print(soup.title.parent) # <head>
    # print(soup.head.parent) # <html>
    
    # 조상(부모 + @)
    # print(list(soup.p.parents))
    
    # 형 - 앞의 EL(prev), 동생 - 뒤의 EL(next)
    # previous_sibling, next_sibling
    html_doc2 = '''
    <html>
        <body>
            <p>
                <a>text1</a>
                <b>text2</b>
            </p>
        </body>
    </html>
    '''
    soup = bs(html_doc2, "html.parser")
    # print(soup.a)  # <a>text1</a>
    # print(soup.a.next_sibling.next_sibling) # \n 다음꺼 , next_sibling 한번 -> \n으로 읽음
    # print(soup.b) # <b>text2</b>
    # print(soup.b.previous_sibling.previous_sibling) # \n 이전꺼, previous_sibling 한번 -> \n으로 읽음
    
    # next_siblings, previous_siblings - 앞(뒤) 형제 엘리먼트, 줄바꿈 요소까지 포함됨.(\n)
    # print(list(soup.a.next_siblings)) # ['\n', <b>text2</b>, '\n']
    # print(list(soup.b.previous_siblings)) # ['\n', <a>text1</a>, '\n']
    
    # next_element, next_sibling 차이점?
    # sibling - 태그가 끝난 시점(요소 밖), element - 요소안에서 부터 찾기 시작...
    # print(soup.a.next_element) # text1  
    # print(soup.a.next_sibling) # \n
    print(soup.b.previous_element) # \n
    print(list(soup.a.next_elements)) # a태그 이하의 요소를 다 읽어냄..