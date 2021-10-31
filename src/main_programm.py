from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

import string
import random
import datetime

#from main_programm import db
#from main_programm import andmebaas
#andmebaas.query.all()
#db.session.delete(andmebaas.query.get())
#db.session.commit()
#andmebaas.query.count()
#db.session.add()


#dPsAmQrCzjoBircuLKKL


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
    
    def __repr__(self):
        return 'checklist ' + str(self.id)
    
@app.route('/', methods=['GET', 'POST']) #avaleht
def AAAAAAA():
    return render_template('avaleht.html')

@app.route('/checklist', methods=['GET', 'POST']) #querry code generaator
def generaator():
    andmed = andmebaas.query.all()
    string_pikkus = 20

    suvakad_tahed = "".join(random.choice(string.ascii_letters) for i in range(string_pikkus))
    x = datetime.datetime.now()
    
    last_update = 99
    if last_update != x.day:
        last_update = x.day
    
    uus_leht = andmebaas(veebileht=suvakad_tahed, viimane_uuendus=last_update)
    db.session.add(uus_leht)
    db.session.commit()
    
    viimane_id = uus_leht.id
    
    
    return redirect('/checklist/' + suvakad_tahed + "/" + str(viimane_id))

# kasutaja chcklisti leht    
@app.route('/checklist/<veebileht_str>/<int:id>', methods=['GET', 'POST'])
def kasutaja_checklist(veebileht_str, id):
    
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht   
    if veebikood == veebileht_str:
        #vaatab kuna on checklisti viimati uuendatud
        x = datetime.datetime.now()
        last_update = kasutaja.viimane_uuendus
        
        # kui on uus päev, siis checklist un-checked
        if last_update != x.day:
            
            kasutaja.list_1_checked = 0
            kasutaja.list_2_checked = 0
            kasutaja.list_3_checked = 0
            kasutaja.list_4_checked = 0
            kasutaja.list_5_checked = 0
            kasutaja.list_6_checked = 0
            kasutaja.list_7_checked = 0
            kasutaja.list_8_checked = 0
            kasutaja.list_9_checked = 0
            kasutaja.list_10_checked = 0
            kasutaja.list_11_checked = 0
            kasutaja.list_12_checked = 0
            kasutaja.list_13_checked = 0
            kasutaja.list_14_checked = 0
            kasutaja.list_15_checked = 0
            kasutaja.list_16_checked = 0
            kasutaja.list_17_checked = 0
            kasutaja.list_18_checked = 0
            kasutaja.list_19_checked = 0
            kasutaja.list_20_checked = 0
            db.session.commit()
            
            last_update = x.day
        
        return render_template('checklist.html', kasutaja=kasutaja)
    else:
        return render_template('vale.html')

# 1 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/1/<number>', methods=['GET', 'POST'])
def checker1(veebileht_str, id, number):
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

# 2 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/2/<number>', methods=['GET', 'POST'])
def checker2(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_2_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_2_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 3 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/3/<number>', methods=['GET', 'POST'])
def checker3(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_3_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_3_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 4 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/4/<number>', methods=['GET', 'POST'])
def checker4(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_4_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_4_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 5 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/5/<number>', methods=['GET', 'POST'])
def checker5(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_5_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_5_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 6 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/6/<number>', methods=['GET', 'POST'])
def checker6(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_6_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_6_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')

# 7 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/7/<number>', methods=['GET', 'POST'])
def checker7(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_7_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_7_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 8 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/8/<number>', methods=['GET', 'POST'])
def checker8(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_8_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_8_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 9 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/9/<number>', methods=['GET', 'POST'])
def checker9(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_9_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_9_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 10 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/10/<number>', methods=['GET', 'POST'])
def checker10(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_10_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_10_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 11 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/11/<number>', methods=['GET', 'POST'])
def checker11(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_11_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_11_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')

# 12 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/12/<number>', methods=['GET', 'POST'])
def checker12(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_12_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_12_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 13 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/13/<number>', methods=['GET', 'POST'])
def checker13(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_13_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_13_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 14 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/14/<number>', methods=['GET', 'POST'])
def checker14(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_14_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_14_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 15 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/15/<number>', methods=['GET', 'POST'])
def checker15(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_15_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_15_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 16 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/16/<number>', methods=['GET', 'POST'])
def checker16(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_16_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_16_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')

# 17 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/17/<number>', methods=['GET', 'POST'])
def checker17(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_17_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_17_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 18 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/18/<number>', methods=['GET', 'POST'])
def checker18(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_18_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_18_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 19 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/19/<number>', methods=['GET', 'POST'])
def checker19(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_19_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_19_checked = 0
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
    else:
        return render_template('vale.html')
    
# 20 checker    
@app.route('/checklist/<veebileht_str>/<int:id>/20/<number>', methods=['GET', 'POST'])
def checker20(veebileht_str, id, number):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        if int(number) == 0:
            kasutaja.list_20_checked = 1
            db.session.commit()
            return redirect('/checklist/' + veebikood + "/" + str(id))
        elif int(number) == 1:
            kasutaja.list_20_checked = 0
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
def kustuta1(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_1 = ""
        kasutaja.list_1_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')

# 2 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/2', methods=['GET', 'POST'])
def kustuta2(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_2 = ""
        kasutaja.list_2_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')
    
# 3 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/3', methods=['GET', 'POST'])
def kustuta3(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_3 = ""
        kasutaja.list_3_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')
    
# 4 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/4', methods=['GET', 'POST'])
def kustuta4(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_4 = ""
        kasutaja.list_4_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')

# 5 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/5', methods=['GET', 'POST'])
def kustuta5(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_5 = ""
        kasutaja.list_5_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')
    
# 6 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/6', methods=['GET', 'POST'])
def kustuta6(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_6 = ""
        kasutaja.list_6_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')

# 7 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/7', methods=['GET', 'POST'])
def kustuta7(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_7 = ""
        kasutaja.list_7_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')
    
# 8 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/8', methods=['GET', 'POST'])
def kustuta8(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_8 = ""
        kasutaja.list_8_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')
    
# 9 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/9', methods=['GET', 'POST'])
def kustuta9(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_9 = ""
        kasutaja.list_9_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')

# 10 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/10', methods=['GET', 'POST'])
def kustuta10(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_10 = ""
        kasutaja.list_10_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')
    
# 11 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/11', methods=['GET', 'POST'])
def kustuta11(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_11 = ""
        kasutaja.list_11_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')

# 12 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/12', methods=['GET', 'POST'])
def kustuta12(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_12 = ""
        kasutaja.list_12_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')
    
# 13 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/13', methods=['GET', 'POST'])
def kustuta13(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_13 = ""
        kasutaja.list_13_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')
    
# 14 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/14', methods=['GET', 'POST'])
def kustuta14(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_14 = ""
        kasutaja.list_14_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')

# 15 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/15', methods=['GET', 'POST'])
def kustuta15(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_15 = ""
        kasutaja.list_15_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')
    
# 16 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/16', methods=['GET', 'POST'])
def kustuta16(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_16 = ""
        kasutaja.list_16_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')

# 17 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/17', methods=['GET', 'POST'])
def kustuta17(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_17 = ""
        kasutaja.list_17_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')
    
# 18 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/18', methods=['GET', 'POST'])
def kustuta18(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_18 = ""
        kasutaja.list_18_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')
    
# 19 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/19', methods=['GET', 'POST'])
def kustuta19(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_19 = ""
        kasutaja.list_19_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')

# 20 delete
@app.route('/checklist/<veebileht_str>/<int:id>/edit/delete/20', methods=['GET', 'POST'])
def kustuta20(veebileht_str, id):
    kasutaja = andmebaas.query.get_or_404(id)
    veebikood = kasutaja.veebileht
    if veebikood == veebileht_str:
        kasutaja.list_20 = ""
        kasutaja.list_20_checked = ""
        db.session.commit() 
        return redirect('/checklist/' + veebikood + "/" + str(id) + "/edit")
    else:
        return render_template('vale.html')

#debugger 
if __name__ == "__main__":
    app.run(debug=True)

