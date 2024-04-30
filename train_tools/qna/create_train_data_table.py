# When you implement this py file, the table in sql syntax will be created in the database.



import pymysql
from config.DatabaseConfig import *

db = None

try:
    db = pymysql.connect(
        host='127.0.0.1',
        user='DB_HOST',
        passwd='DB_PASSWORD',
        db='DB_NAME',
        charset='utf8'
    )

    # 테이블 생성 sql 정의
    sql = '''
    CREATE TABLE IF NOT EXISTS 'chatbot_train_data' (
        `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
        `intent` VARCHAR(45) NULL,
        `ner` TEXT NULL,
        `query` TEXT NOT NULL,
        `answer` TEXT NOT NULL,
        `answer_image` VARCHAR(2048) NULL,
        PRIMARY KEY (`id`))
    ENGINE=InnoDB DEFAULT CHARSET=utf8
    '''

    # 테이블 생성
    with db.cursor() as cursor:
        cursor.execute(sql)
        print('테이블 생성 성공')


except Exception as e:
    print(e)  # db 연결 실패시 오류 내용 출력

finally:
    if db is not None:
        db.close()
        print('DB 연결 닫기 성공')
