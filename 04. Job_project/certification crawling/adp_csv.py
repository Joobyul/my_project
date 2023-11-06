import pandas as pd
import csv

URL = 'https://yogyui.tistory.com/entry/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D%EC%A0%84%EB%AC%B8%EA%B0%80ADP-%EC%9E%90%EA%B2%A9-%EC%B7%A8%EB%93%9D-%ED%86%B5%EA%B3%84-2022%EB%85%84-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8'
tables = pd.read_html(URL)
print(len(tables),'개의 테이블이 있습니다')
tables[1]


df=tables[1]

df.to_csv("adp.csv", index=False, encoding="utf-8-sig")
# file_name='abc.xlsx'
# f = open(file_name,'w', encoding='cp949', newline='')
# csv_writer = csv.writer(f)


# print(f'{file_name} 파일 저장 완료')