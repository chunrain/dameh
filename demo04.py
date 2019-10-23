import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='test', charset='utf8')

cur = db.cursor()

def logging():
    user_name = []
    while True:
        id = int(input("ID:"))
        name = input("name:")
        passwd = input("passwd")
        sql = "insert into user (id,name,passwd) values (%d,%s,%s); "

        if name not in user_name:
            cur.execute(sql,[id,name,passwd])
            db.commit()
            user_name.append(name)
            return print("注册成功")

logging()
cur.close()
db.close()


