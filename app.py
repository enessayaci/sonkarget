

"""
CoDeR= Furkan Ceran
"""
#-------iMPORTLAR---------------------------------------------------------------------------------------------------
import time
import os
import random
from os import environ
import sys
import urllib
from flask import Flask, redirect, render_template, request, url_for,flash
from flask_socketio import SocketIO, emit
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
import requests		
from random import randint
from vericekici import Utku
async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
thread = None
def background_thread():
    ext=fr=kt=bd=elec=0
    while True:
        
        socketio.sleep(2)

        vites= randint(1,5)
        rpm = randint(1,8)
        (s1, s2, s3, s4, ext, fr, kt, bd, elec, hiz) = Utku().utku()

        
        socketio.emit('my_response',
                      {'data':'Values', 'elec': elec,'ext': ext,'fr': fr,'kt': kt,'bd': bd, "hiz" : hiz, "vites" : vites,"rpm" : rpm,"sicak1" : s1,"sicak2" : s2,"sicak3" : s3, "sicak4" : s4 },
                      namespace='/carpi')



##################################################################################################################
#--------------------DECODE--------------------------------------------------------------------------------------#
##################################################################################################################

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/navi", methods=['GET', 'POST'])
def navigation():
    return render_template("navigation.html")
@app.route("/message", methods=['GET', 'POST'])	
def message():
    return render_template("chat.html")
@app.route("/about")
def about():
        return render_template("about.html")
@app.route("/exit", methods=['GET', 'POST'])
def exit():
        return render_template("index.html")
@app.route("/advise")
def advise():
        return render_template("suggestions.html")
@app.route("/sifremiunuttum", methods=['GET', 'POST'])
def sifremiunuttum():
    return render_template("sifremiunuttum.html")
@app.route("/grafik", methods=['GET', 'POST'])
def grafik():
        from grafikyazar import Ceran
        (sicaklik,gerilim,batarya,hiz) = Ceran().ceran()
        json.dumps(sicaklik)
        json.dumps(gerilim)
        json.dumps(batarya)
        json.dumps(hiz)

        return render_template("grafik.html",sicaklik = sicaklik, gerilim = gerilim,batarya = batarya,hiz = hiz)
@app.route("/log", methods=['GET', 'POST'])
def log():
        from logcekici import Logs
        Loglar = Logs().log()
        return render_template("loglariizle.html",Loglar = Loglar)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def server_error(e):
	return render_template('404.html'), 500


mesg = 'we are here...'

	

@socketio.on('connect', namespace='/carpi')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
    if json==None:
            print ("json yok")
    else:
        a = str(json)
        print (a)
        import psycopg2
        from psycopg2 import Error
        try:
            connection = psycopg2.connect(user = "vfrhjnyxtlicam",
                                          password = "5bd15794ceeeccce46189ba66b458d30d50c66627e29ea52e220bb3a8c7904ad",
                                          host = "ec2-107-20-230-70.compute-1.amazonaws.com",
                                          port = "5432",
                                          database = "d6j61pnoq4r9to")
            isim=None
            mesaj=None
            cursor = connection.cursor()
            
            postgres_insert_query = """ INSERT INTO iletisim (isim,mesaj) VALUES (%s,%s)"""

            print ("mesaj gonderme basarili")
            record_to_insert = (isim,mesaj)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
            
        except (Exception, psycopg2.Error) as error :
            if(connection):
                print("Failed to insert record into veri table", error)
    



@app.route("/aks", methods = ["GET", "POST"])	   # GET,POST Methodlari ile html formlarindan veri cekme kisimi:
def search():										   # arama sayfasi tanimladim
        if request.method == "POST":				   # eger post methoduysa
                if request.form["action"] == "aks":     
                    user = request.form.get("user")   # seed formumdan seedi al
                    passw = request.form.get("pass")	# keyword formumdan keywordu al
                    if str(user)==("KARATAY") and str(passw) == ("1251"):
                        print ("Giris basarili")
                        speed = randint(0,133)
                        templateData={
                                'mesg' :mesg,
                                'speed' :speed
                        }
                        return render_template('aks.html', async_mode=socketio.async_mode, **templateData, user = user)
                    else:
                        flash("Kullanıcı Adı veya Şifreniz Hatalı") 
                        return redirect(request.url)
                        
                if request.form["action"] == "navi":           
                        return redirect(url_for('navi'))
     
                if request.form["actions"] == "message":
                        return redirect(url_for('message'))                    
                    
                if request.form["sifermiunuttumm"] == "sifermiunuttum":
                            return redirect(url_for('sifermiunuttum'))
                if request.form["grafikk"] == "grafik":
 
                            return redirect(url_for('grafik'))
                if request.form["logg"] == "log":
     
                            return redirect(url_for('loglariizle'))
                if request.form["exitt"] == "cikis_yap":
                            return redirect(url_for('index'))

					# eski sekmede diger sonuclari listelettim
                


        else:
                return redirect(url_for("index"))
if __name__ == '__main__':
    HOST = environ.get('0.0.0.0', 'localhost')
    try:
        PORT = int(environ.get('80', '5000'))
    except ValueError:
        PORT = 80
    #Sinif().sinif()
#    app.run(HOST, PORT)
    socketio.run(app, debug=True)


##################################################################################################################
