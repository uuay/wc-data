import csv
import time
from datetime import datetime

from src.DBConnector import DBConnector

class CsvSaver:

    def openCsv(self, filepath):
        f = open(filepath, 'r', encoding="euc-kr")  # csv 파일 오픈
        rdr = csv.reader(f)
        return rdr

    def insertServices(self, filepath):
        connector = DBConnector()
        sql = ("INSERT INTO welfare_targets (service_id, disability_type, disability_grade, age_group, createdAt, updatedAt)"
                    "VALUES (%s, %s, %s, %s, %s, %s) ")
        current_time = datetime.now()

        print('='*20 + 'start')
        rdr = self.openCsv(filepath)
        for column in rdr:
            data = (column[1], column[3], column[4], column[2], current_time, current_time)
            print("-"*20)
            print(data)
            connector.csv_into_db(sql, data)  # DB저장
            time.sleep(0.01)
        print('done')

    def insertAllServices(self, filepath):
        connector = DBConnector()
        # sql = ("INSERT INTO welfare_services (service_id, name, application_agency, application_method, url, desc, registedAt, createdAt, updatedAt) "
        #        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ")
        sql = ("INSERT INTO welfare_services (service_id, name, application_agency, application_method, url, registedAt, createdAt, updatedAt) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ")
        current_time = datetime.now()

        print('start')
        f = open(filepath, 'r', encoding='utf-8')  # csv 파일 오픈
        rdr = csv.reader(f)
        for column in rdr:
            if (column[0] != '#'):
                resigtedAt = datetime.strptime(column[8], '%Y-%m-%d')
                print(resigtedAt)
                data = (column[6], column[7], column[2], column[3], column[5], resigtedAt, current_time, current_time)
                # data = (column[6], column[7], column[2], column[3], column[5], column[4], resigtedAt, current_time, current_time)
                print(data)
                connector.csv_into_db(sql, data)
                time.sleep(0.01)
        print('done')


object = CsvSaver()
# object.insertServices("./govServices.csv")
object.insertAllServices("./all.csv")