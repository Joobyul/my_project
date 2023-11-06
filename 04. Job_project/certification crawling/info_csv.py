import pandas as pd
import csv
from bs4 import BeautifulSoup
# URL = 'https://www.q-net.or.kr/crf005.do?id=crf00505&jmCd=1320'
# tables = pd.read_html(URL)
# print(len(tables),'개의 테이블이 있습니다')
# tables[0]


# df=tables[0]

# df.to_csv("info.csv", index=False, encoding='utf-8-sig')


# file_name='abc.xlsx'
# f = open(file_name,'w', encoding='cp949', newline='')
# csv_writer = csv.writer(f)


# print(f'{file_name} 파일 저장 완료')


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from html_table_parser import parser_functions as parse

url = 'https://www.q-net.or.kr/crf005.do?id=crf00505&jmCd=1320'
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
driver.implicitly_wait(5)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"#tab2").click()

time.sleep(2)
html = driver.page_source
bs = BeautifulSoup(html,"html.parser")
table = bs.select_one("#contentView > div.tbl_normal.tdCenter > table")

time.sleep(2)


# 두 개의 테이블 중에 첫 번째 테이블 사용
#table = bs.find_all('table', {'class':'wikitable'})[0]
#rows = table.find_all('tr')
table_data = parse.make2d(table) # 2차원 배열

# 테이블의 2행을 출력 
print('[0]:', table_data[0])
print('[1]:', table_data[1])
print('-' * 100)
# Pandas DataFrame으로 저장 (2행부터 데이터 저장, 1행은 column 이름으로 사용)
df = pd.DataFrame(table_data[1:], columns=table_data[0])
print(df.head())

# csv 파일로 저장
csvFile = open('info.csv', 'w', encoding='utf-8-sig') # t: text mode
writer = csv.writer(csvFile)

for row in table_data:
    writer.writerow(row)

csvFile.close()


