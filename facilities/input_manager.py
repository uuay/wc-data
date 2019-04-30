# -*- coding: utf-8 -*-
class InputManager(object):

    def __init__(self, conn):
        self.dbconn = conn
        self.cursor = self.dbconn.cursor()
        return

    def csv_into_db(self, _query, data):
        """
            csv의 내용을 DB에 저장
        """
        print(_query, data)
        try:
            cursor = self.dbconn.cursor()
            print('inserting...')
            vResult = cursor.execute(_query, data)
            print("DB Insert Result:", vResult)  # 결과 출력
            self.dbconn.commit()

        except Exception as ex:
            print("Error: ", "csv_into_db", str(ex))

        return
