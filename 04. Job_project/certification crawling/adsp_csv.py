import pandas as pd
import csv

URL = 'https://allaboutwealth.tistory.com/410'
tables = pd.read_html(URL)
print(len(tables),'개의 테이블이 있습니다')
tables[1]


df=tables[1]

df.to_csv("adsp.csv", index=False, encoding="utf-8-sig")


# file_name='abc.xlsx'
# f = open(file_name,'w', encoding='cp949', newline='')
# csv_writer = csv.writer(f)


# print(f'{file_name} 파일 저장 완료')