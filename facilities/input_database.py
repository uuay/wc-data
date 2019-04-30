import csv
import time
from datetime import datetime
import pymysql

from input_manager import InputManager

disitricts = [
    '강원도'
    , '경기도'
    , '경상남도'
    , '경상북도'
    , '광주광역시'
    , '대구광역시'
    , '대전광역시'
    , '부산광역시'
    , '서울특별시'
    , '세종특별자치시'
    , '울산광역시'
    , '인천광역시'
    , '전라남도'
    , '전라북도'
    , '제주특별자치도'
    , '충청남도'
    , '충청북도'
]

def get_connection():
    connection = pymysql.connect(
        host=HOST,
        port=3306,
        user=USER,
        passwd=PASSWORD,
        db=DB
        charset='utf8')

    return connection

def main():
    connection = get_connection()
    manager = InputManager(connection)
    sql = ("INSERT INTO facilities (name, type, address, tel_number, top_district_id, createdAt, updatedAt)"
                "VALUES (%s, %s, %s, %s, '%s', %s, %s ) ")
    current_time = datetime.now()

    print('start')
    try:
        print('read csv')
        f = open('new.csv', 'r', encoding="euc-kr")  # csv 파일 오픈
        print('create reader')
        rdr = csv.reader(f)
        for line in rdr:
            if line[0] == '기관코드': continue
            data = (line[5], 'resident', line[8], line[6], disitricts.index(line[3]) + 1, current_time, current_time)
            manager.csv_into_db(sql, data)  # DB저장
            time.sleep(0.01)
        connection.close()

    except Exception as ex:
        print('exception! stop input')
        connection.close()

    print('done')
    return

main()