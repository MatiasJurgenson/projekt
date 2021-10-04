from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

#from main_programm import db
#db.create_all()
#from main_programm import Rawlaused
#Rawlaused.query.all()
#db.session.delete(Rawlaused.query.get())
#db.session.commit()
#Rawlaused.query.count()
#db.session.add()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///checklist.db'
db = SQLAlchemy(app)

class Rawlaused(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    veebileht = db.Column(db.Text, nullable=False)
    
    list_1 = db.Column(db.Text)
    list_1_checked = db.Column(db.Integer)
    
    list_2 = db.Column(db.Text)
    list_2_checked = db.Column(db.Integer)
    
    list_3 = db.Column(db.Text)
    list_3_checked = db.Column(db.Integer)
    
    list_4 = db.Column(db.Text)
    list_4_checked = db.Column(db.Integer)
    
    list_5 = db.Column(db.Text)
    list_5_checked = db.Column(db.Integer)
    
    list_6 = db.Column(db.Text)
    list_6_checked = db.Column(db.Integer)
    
    list_7 = db.Column(db.Text)
    list_7_checked = db.Column(db.Integer)
    
    list_8 = db.Column(db.Text)
    list_8_checked = db.Column(db.Integer)
    
    list_9 = db.Column(db.Text)
    list_9_checked = db.Column(db.Integer)
    
    list_10 = db.Column(db.Text)
    list_10_checked = db.Column(db.Integer)
    
    list_11 = db.Column(db.Text)
    list_11_checked = db.Column(db.Integer)
    
    list_12 = db.Column(db.Text)
    list_12_checked = db.Column(db.Integer)
    
    list_13 = db.Column(db.Text)
    list_13_checked = db.Column(db.Integer)
    
    list_14 = db.Column(db.Text)
    list_14_checked = db.Column(db.Integer)
    
    list_15 = db.Column(db.Text)
    list_15_checked = db.Column(db.Integer)
    
    list_16 = db.Column(db.Text)
    list_16_checked = db.Column(db.Integer)
    
    list_17 = db.Column(db.Text)
    list_17_checked = db.Column(db.Integer)
    
    list_18 = db.Column(db.Text)
    list_18_checked = db.Column(db.Integer)
    
    list_19 = db.Column(db.Text)
    list_19_checked = db.Column(db.Integer)
    
    list_20 = db.Column(db.Text)
    list_20_checked = db.Column(db.Integer)   
    
    dblaused = db.Column(db.Text)
    def __repr__(self):
        return 'checklist ' + str(self.id)
    
@app.route('/', methods=['GET', 'POST']) #avaleht
def AAAAAAA():
    return render_template('avaleht.html')

@app.route('/checklist', methods=['GET', 'POST']) #querry code generaator
def kustuta1():
    return redirect('/')

@app.route('/checklist/<string:veebileht>', methods=['GET', 'POST']) #kasutaja checlist
def kustuta2():
    return redirect('/')

@app.route('/checklist/<string:veebileht>/edit', methods=['GET', 'POST']) #editing
def kustuta3():
    return redirect('/')

#debugger 
if __name__ == "__main__":
    app.run(debug=True)