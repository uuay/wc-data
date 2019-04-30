import pymysql

# 접속
db = pymysql.connect(host='localhost', port=3306, user='jeju', passwd='jejupw', db='jeju', charset='utf8')

# 커서 가져오기
cursor = db.cursor()

# SQL 문 만들기
sql = '''
            CREATE TABLE korea2 (
                   id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                   name VARCHAR(20) NOT NULL,
                   model_num VARCHAR(10) NOT NULL,
                   model_type VARCHAR(10) NOT NULL,
                   PRIMARY KEY(id)
            );
        '''

# 실행하기
cursor.execute(sql)

# DB에 Complete 하기
db.commit()

# DB 연결 닫기
db.close()
print('done')