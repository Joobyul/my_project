'''
Naver 뉴스 워드 클라우드
- https://myjamong.tistory.com/48
- https://everyday-tech.tistory.com/entry/쉽게-따라하는-네이버-뉴스-크롤링python-2탄

'''

from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import time
import re
import platform

def get_titles(search_word, title_list):
    # start_num ~ end_num까지 크롤링

    url = 'https://search.naver.com/search.naver?where=cafe&query={}&ie=utf8&stnm=members&sm=tab_opt&nso=so%3Ar%2Cp%3A1y%2Ca%3Aall&nso_open=1&t=0&mson=0'.format(
            search_word)
    # url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}&start={}'.format(
    #         search_word, start_num)

    req = requests.get(url)
    time.sleep(1)

    if req.ok: # 정상적인 request 확인
        soup = BeautifulSoup(req.text, 'html.parser')

        # 뉴스제목 뽑아오기
        list_news = soup.find('ul', {'class' : 'lst_cafe_wrap'})
        #li_list = list_news.find_all('li', {'id': re.compile('sp_nws.*')})
        li_bxs = list_news.find_all('div', {'class': 'detail'})
        for li_bx in li_bxs:
            news_title = li_bx.find('a', {'class':'txt_group'})
            title_list.append(news_title.get_text())

    print(title_list)


def make_wordcloud(word_count, title_list):
    okt = Okt()

    sentences_tag = []
    # 형태소 분석하여 리스트에 넣기
    for sentence in title_list:
        morph = okt.pos(sentence)
        sentences_tag.append(morph)
        print(morph)
        print('-' * 30)

    print(sentences_tag)
    print('\n' * 3)

    noun_adj_list = []
    # 명사와 형용사만 구분하여 이스트에 넣기
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun']:
                noun_adj_list.append(word)

    # 형태소별 count
    counts = Counter(noun_adj_list)
    tags = counts.most_common(word_count)
    print(tags)

    # wordCloud생성
    # 한글꺠지는 문제 해결하기위해 font_path 지정
    if platform.system() == 'Windows':
        path = 'malgun.ttf'
    # elif platform.system() == 'Darwin':  # Mac OS
    #     path = r'/System/Library/Fonts/AppleGothic'
    # else:
    #     path = r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

    wc = WordCloud(font_path=path, background_color='white', width=800, height=600)
    print(dict(tags))
    cloud = wc.generate_from_frequencies(dict(tags))
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()


if __name__ == '__main__':
    search_word = "데이터 자격증"  # 검색어 지정
    title_list = []
    # 1~200번게시글 까지 크롤링
    get_titles(search_word, title_list)
    # 단어 30개까지 wordcloud로 출력
    make_wordcloud(1000, title_list)
