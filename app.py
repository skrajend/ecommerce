from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
from mysql.connector.constants import ClientFlag
import socket

app = Flask(__name__)

config = {
    'user': 'root',
    'password': 'Welcome1234',
    'host': 'mycluster',
    'port': '6446',
    'database': 'test',
    'autocommit': 'true'
}


@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    message = "Welcome to E-Commerce Application. Pod Name  : " + hostname

    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor(buffered=True)
    cur.execute("select * from test.test11")
    cur.fetchall()
    rc = cur.rowcount
    print(rc)
    cur.execute("insert into test11(name) values ('A');")
    cur.close()
    cnx.close()
    message = message + "You've visited me {} times.\n".format(rc)
    return message

