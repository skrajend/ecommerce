from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.constants import ClientFlag
import socket

app = Flask(__name__)

config = {
    'user': 'root',
    'password': 'Welcome1234',
    'host': 'mycluster.default.svc.cluster.local',
    'port': '6446',
    'database': 'test'
}


@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    message = "Welcome to E-Commerce Application. Pod Name  : " + hostname
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            message = "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            message = "Database does not exist"
        else:
            print(err)
            message = "Not Sure What is the Problem"
    else:
        cur = cnx.cursor(buffered=True)
        cur.execute("insert into test11(name) values ('A');")
        cur.execute("select * from test.test11")
        cur.fetchall()
        rc = cur.rowcount
        cnx.commit()
        cur.close()
        cnx.close()
        message = message + "You've visited me {} times.\n".format(rc)
    return message

#if __name__ == "__main__":
#    app.run()