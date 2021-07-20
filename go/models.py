from go import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)
    def __init__(self, text, tags):
        self.text = text.strip()
        self.tags = [
            Tag(text=tag.strip()) for tag in tags.split(',')
        ]


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', backref=db.backref('tags', lazy=True))

class User2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login1 = db.Column(db.String(1024), primary_key=False)
    password1 = db.Column(db.String(1024), primary_key=False)
    def __init__(self, login1, password1):
        self.login1 = login1
        self.password1 = password1

class data12(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bpm = db.Column(db.Integer, primary_key=False)
    time = db.Column(db.DateTime, primary_key=False)
    datasource = db.Column(db.String(150), primary_key=False)
    manufacturer = db.Column(db.String(150), primary_key=False)
    device_type = db.Column(db.String(150), primary_key=False)
    uid = db.Column(db.String(150), primary_key=False)
    def __init__(self, bpm, time, datasource,  manufacturer, device_type, uid):
        self.bpm = bpm
        self.time = time
        self.datasource = datasource
        self.manufacturer = manufacturer
        self.device_type = device_type
        self.uid = uid
db.create_all()
