from flask import render_template, redirect, url_for, request, flash
from go import app, db
from go.models import Message
from go.models import User2
from go.models import data12
import json
import time
from datetime import timezone
from datetime import datetime


@app.route('/', methods=['GET'])
def st():
    return render_template('index.html')

@app.route('/hello', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/go')
def test():
    return render_template('loginpage.html')



@app.route('/chat', methods=['GET'])
def chat():
    return render_template('main.html', messages=Message.query.all())

@app.route('/loginpage', methods=['GET'])
def login():
    return render_template('loginpage.html')

@app.route('/data_base', methods=['POST'])
def data_base():
    file1 = open('heart_data.json')
    heart_data = json.load(file1)
    heart_list = []
    for ind in range(len(heart_data["point"])):
        heart_point = {}
        ms = heart_data["point"][ind]["modifiedTimeMillis"]
        m = datetime.fromtimestamp(float(ms) // 1000.0)
        time1 = m.replace(tzinfo=timezone.utc)
        heart_point["time"] = time1
        heart_point["bpm"] = heart_data["point"][ind]["value"][0]["fpVal"]
        source = heart_data["point"][ind]["originDataSourceId"].split(':')
        heart_point["datasource"] = source[2]
        heart_point["manufacturer"] = ""
        heart_point["device_type"] = ""
        heart_point["uid"] = ""
        if heart_point["datasource"] != "com.google.android.gms":
            heart_point["manufacturer"] = source[3]
            heart_point["device_type"] = source[4]
            heart_point["uid"] = source[5]
        fav=data12(bpm=heart_point.get('bpm'), time = (heart_point.get('time')), datasource = heart_point.get('datasource'),
          manufacturer=heart_point.get('manufacturer'), device_type=heart_point.get('device_type'), uid= heart_point.get('uid'))
        db.session.add(fav)
        db.session.commit()
    file1.close()
    return render_template('index.html')


@app.route('/add_text', methods=['POST'])
def add_text():
    usertext = request.form['text']
    go = request.form['tag']
    db.session.add(Message(usertext, go))
    db.session.commit()
    return redirect(url_for('chat'))

@app.route('/login_add', methods=['POST'])
def login_add():
    login1 = request.form['login1']
    password1 = request.form['password1']
    db.session.add(User2(login1, password1))
    db.session.commit()
    return redirect("http://localhost:8080/")



