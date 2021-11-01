from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

import string
import random
import datetime

#from main_test import db
#from main_test import andmebaas
#andmebaas.query.all()
#db.session.delete(andmebaas.query.get())
#db.session.commit()
#andmebaas.query.count()
#db.session.add()


#/checklist/dPsAmQrCzjoBircuLKKL/1


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///checklist.db'
db = SQLAlchemy(app)

class andmebaas(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    veebileht = db.Column(db.Text, nullable=False)

    viimane_uuendus = db.Column(db.Text, nullable=False)

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

# kasutaja chcklisti leht    
@app.route('/checklist/<veebileht_str>/<int:id>', methods=['GET', 'POST'])
def kasutaja_checklist(veebileht_str, id):

    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:                                   
        return render_template('checklist.html', kasutaja=kasutaja)
    else:
        return render_template('vale.html')

# 1 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/1/<number>', methods=['GET', 'POST'])
def checker(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_1_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_1_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')

#edit page
@app.route('/checklist/<veebileht_str>/<int:id>/edit', methods=['GET', 'POST'])
def edit(veebileht_str, id):

    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if request.method == 'POST':
            kasutaja.list_1 = request.form['list_1']
            if kasutaja.list_1_checked == "":
                kasutaja.list_1_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        else:
            return render_template('edit.html', kasutaja=kasutaja)
    else:
        return render_template('vale.html')

# 1 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/1', methods=['GET', 'POST'])
def kustuta(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_1 = ""
        kasutaja.list_1_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')

#debugger 
if __name__ == "__main__":
    app.run(debug=True) 