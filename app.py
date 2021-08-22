from flask import Flask
import socket
import psycopg2

app = Flask(__name__)

#'host': 'pq1-postgresql-ha-pgpool.default.svc.cluster.local',
config = {
    'user': 'postgres',
    'password': 'Welcome123',
    'host': 'pq1-postgresql-ha-pgpool.default.svc.cluster.local',
    'port': '5432',
    'database': 'test'
}

@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    message = "Welcome to E-Commerce Application. Pod Name  : " + hostname
    try:
        cnx = psycopg2.connect(**config)
    except (Exception, psycopg2.DatabaseError) as err:
        print(err)
        message = "Not Sure What is the Problem"
    else:
        cur = cnx.cursor()
        cur.execute("insert into test1(name) values ('A')")
        cur.execute("select * from test1")
        cur.fetchall()
        rc = cur.rowcount
        cnx.commit()
        cnx.close()
        message = message + "<br>You've visited me {} times.\n".format(rc)
    return message

#if __name__ == "__main__":
#    app.run()
