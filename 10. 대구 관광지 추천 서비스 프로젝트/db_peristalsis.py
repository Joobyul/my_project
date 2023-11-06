# ------------------------------------------
# MariaDB & Python 연동
# ------------------------------------------
# 모듈 로딩
import mariadb as mdb
import sys
import pandas as pd
import numpy as np


# mariaDB 접속값
conn_params={'host':'localhost',
            'port':3307,
            'user':'root',
            'password':'root',
            'autocommit':True,
            'db':'place'}

df=pd.read_csv(r'./data/db_entertain.csv')
df2=pd.read_csv(r'./data/db_restaurant.csv')
df3=pd.read_csv(r'./data/db_cafe.csv')

try:
    # mariaDB 연결
    conn=mdb.connect(**conn_params)

    # DB에 접근할 수 있는 Cursor객체 가져오기
    cursor = conn.cursor()

    # entertain 데이터 입력
    for i in range(0,len(df)):
        e_name=df.iloc[i][0]
        e_address=df.iloc[i][1]
        e_latitude=df.iloc[i][2]
        e_longitude=df.iloc[i][3]
        # print(e_name,e_address,e_latitude,e_longitude)

        cursor.execute('insert into entertain(e_name,e_address,e_latitude,e_longitude) values(?,?,?,?);',[e_name,e_address,e_latitude,e_longitude])
    
    # DB에서 모든 데이터 조회하는 SQL 실행
    # cursor.execute('select * from entertain;')
    # data=cursor.fetchall()
    # print(data)

    # restaurant 데이터 입력
    for i in range(0,len(df2)):
        r_name=df2.iloc[i][0]
        r_star=df2.iloc[i][1]
        r_address=df2.iloc[i][2]
        r_latitude=df2.iloc[i][3]
        r_longitude=df2.iloc[i][4]
        print(r_name,r_star,r_address,r_latitude,r_longitude)

        cursor.execute('insert into restaurant(r_name,r_star,r_address,r_latitude,r_longitude) values(?,?,?,?,?);',[r_name,r_star,r_address,r_latitude,r_longitude])
    
    # DB에서 모든 데이터 조회하는 SQL 실행
    # cursor.execute('select * from restaurant;')
    # data=cursor.fetchall()
    # print(data)

    # cafe 데이터 입력
    for i in range(0,len(df3)):
        c_name=df3.iloc[i][0]
        c_star=df3.iloc[i][1]
        c_address=df3.iloc[i][2]
        c_latitude=df3.iloc[i][3]
        c_longitude=df3.iloc[i][4]
        # print(e_name,e_address,e_latitude,e_longitude)

        cursor.execute('insert into cafe(c_name,c_star,c_address,c_latitude,c_longitude) values(?,?,?,?,?);',[c_name,c_star,c_address,c_latitude,c_longitude])
    
    # DB에서 모든 데이터 조회하는 SQL 실행
    # cursor.execute('select * from cafe;')
    # data=cursor.fetchall()
    # print(data)

    # mariaDB 종료
    conn.close()

except mdb.Error as e:
    print(f'Error connecting to MariaDB Platform : {e}')
    sys.exit(1)