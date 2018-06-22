import pymysql

from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    conn = pymysql.connect(host='192.168.21.57', user='bootcamp', password='bootcamp', db='employees')
    a = conn.cursor();
    sql = 'select * from emplpoyees'
    a.execute(sql);
    co = a.execute(sql)
    print("no of row ", co)
    data = a.fetchone()
    print(data);

    return data

@app.route('/id/<no>')
def id(no):
    conn = pymysql.connect(host='192.168.21.57', user='bootcamp', password='bootcamp', db='employees')
    a = conn.cursor();
    sql = 'select * from employees where id=no '
    a.execute(sql);
    co = a.execute(sql)
    data = a.fetchone()
    print(data);

    return 'hi specific data  %s'% data


if __name__ == '__main__':
    app.run()


