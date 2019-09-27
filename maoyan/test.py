import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    charset='utf8',
    autocommit=True,
    db='spider'
)

container = ['大话西游', 'https://www.maoyan.com/board/4']

cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = 'insert into maoyan (title, link) values (%s, %s);'

cursor.execute(sql, container)

print('successfully')

