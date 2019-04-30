from datetime import datetime
import pymysql

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

db = pymysql.connect(host=HOST, port=3306, user=USER, passwd=PASSWORD, db=DB, charset='utf8')
cursor = db.cursor()
current_time = datetime.now()

add_facility = ("INSERT INTO facilities (name, type, address, tel_number, top_district_id, createdAt, updatedAt)"
                "VALUES (%s, %s, %s, %s, '%s', %s, %s ) ")
data_facility = ('name', 'resident', 'address', 'tel_number', disitricts.index("경기도")+1, current_time, current_time)
# data_facility = ('강원도청', 'resident', '강원도 춘천시 중앙로 1 (봉의동)', '033-254-2011', 1, current_time, current_time)

print(add_facility)
print(data_facility)

# Insert new facility
print('inserting...')
cursor.execute(add_facility, data_facility)

# Make sure data is committed to the database
db.commit()
cursor.close()
db.close()

print('done')