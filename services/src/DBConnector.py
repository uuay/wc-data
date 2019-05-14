# -*- coding: utf-8 -*-
import pymysql
import json

class DBConnector():

    def __init__(self):
        with open('config.json', 'r') as f:
            config = json.load(f)

        self.database = {
            "host" : config['DEFAULT']['database']['host'],
            "port" : config['DEFAULT']['database']['port'],
            "user" : config['DEFAULT']['database']['user'],
            "passwd" : config['DEFAULT']['database']['password'],
            "db" : config['DEFAULT']['database']['db'],
            "charset" : config['DEFAULT']['database']['charset']
        }

        print(self.database)

    def getConnection(self):
        return pymysql.connect(
            host = self.database.get('host'),
            port = self.database.get('port'),
            user = self.database.get('user'),
            passwd = self.database.get('passwd'),
            db = self.database.get('db'),
            charset = self.database.get('charset')
        )

    def csv_into_db(self, _query, data):
        """
            csv의 내용을 DB에 저장
        """
        print(_query, data)
        try:
            connection = self.getConnection()
            cursor = connection.cursor()
            print('inserting...')
            vResult = cursor.execute(_query, data)
            print("DB Insert Result:", vResult)  # 결과 출력
            connection.commit()
            connection.close()

        except Exception as ex:
            print("Error-: ", "csv_into_db: ", str(ex))
