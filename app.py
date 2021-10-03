from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import flash
import psycopg2 
import psycopg2.extras



app = Flask(__name__)
app.secret_key = "aaa_bbb"

conn = psycopg2.connect(user="postgres",
                        password = "wD5pem$n",
                        host= "localhost",
                        port = "5432",
                        database="mywork")

conn2 = psycopg2.connect(user="postgres",
                        password = "wD5pem$n",
                        host= "localhost",
                        port = "5432",
                        database="postgres")

@app.route('/')
def Index():    
    return render_template('index.html')

@app.route('/ipsearch', methods=['POST','GET'])
def ipsearch():
    if request.method == 'GET':
        return render_template('ipsearch.html')
    elif request.method == 'POST':
        ip = request.form['mysearch']
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        s = "SELECT * FROM abuse_uniq where ipaddress='{}'".format(ip)
        cur.execute(s)
        ipdata = cur.fetchall()
        return render_template('ipsearch.html', ipdata = ipdata)

@app.route('/shasearch', methods=['POST','GET'])
def shasearch():
    if request.method == 'GET':
        return render_template('shasearch.html')
    elif request.method == 'POST':
        sha = request.form['myshasearch']
        cur = conn2.cursor(cursor_factory=psycopg2.extras.DictCursor)
        s = "SELECT * FROM malwaredatatable where sha256_hash='{}'".format(sha)
        cur.execute(s)
        shadata = cur.fetchall()
        return render_template('shasearch.html', shadata = shadata)

@app.route('/ipdatas')
def ipdatas():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM abuse_uniq limit 100"
    cur.execute(s)
    list_datas = cur.fetchall()
    return render_template('ipdatas.html', list_datas = list_datas)

@app.route('/sha256datas')
def sha256datas():
    cur = conn2.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM malwaredatatable limit 100"
    cur.execute(s)
    malware_datas = cur.fetchall()
    return render_template('sha256datas.html', malware_datas = malware_datas)





if __name__ == "__main__":
    app.run(debug=True)