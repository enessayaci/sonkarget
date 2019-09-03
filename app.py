

"""
CoDeR= Furkan Ceran
"""
#-------iMPORTLAR---------------------------------------------------------------------------------------------------
import time
import os                       # Sistem dosyalarina erisim icin import ettigim saf python modulu
import random					# crawl sisteminde her seferinde farkli sonuclar alabilmek adina
from os import environ
import sys						# bunu flaskda web sitesini olustururken encode hatasinin cozumu olarak importladim.
import urllib					# Html sitelerimizden veri ceken bir modul
from flask import Flask, redirect, render_template, request, url_for # tum projenin internette calismasini saglayan modul
		# Bu Flask icin gerekli __init__ verilerini almaya yariyor
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
import requests		
from random import randint
from vericekici import Utku
async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
thread = None
def background_thread():
    """Example of how to send server generated events to clients."""
    ext=fr=kt=bd=elec=0
    while True:
        
        socketio.sleep(2)
        ext = randint(0,100)
        fr = randint(0,100)
        kt = randint(0,100)
        bd = randint(0,100)
        elec = randint(0,100)
        hiz = randint(0,100)
        vites= randint(1,5)
        rpm = randint(1,8)
        (s1, s2, s3, s4) = Utku().utku()

        
        socketio.emit('my_response',
                      {'data':'Values', 'elec': elec,'ext': ext,'fr': fr,'kt': kt,'bd': bd, "hiz" : hiz, "vites" : vites,"rpm" : rpm,"sicak1" : s1,"sicak2" : s2,"sicak3" : s3, "sicak4" : s4 },
                      namespace='/carpi')



##################################################################################################################
#--------------------DECODE--------------------------------------------------------------------------------------#
##################################################################################################################

						# Flaskta UTF8 Olmayan sonuclarda server kapanmasin diye decoce edip sistemi yeniden 
#sys.setdefaultencoding('utf8')  #baslatmaya yariyan kisim
#reload(sys)
##################################################################################################################
#--------------------/App.Route ve Html'e Gidecekler\------------------------------------------------------------#
##################################################################################################################
@app.route("/")										   # Burada app.route ile html sayfasina yonlendirme yapiyoruz
def index():										   # Anasayfayi tanimladim
    return render_template("index.html")
@app.route("/navi", methods=['GET', 'POST'])										   # Burada app.route ile html sayfasina yonlendirme yapiyoruz
def navigation():										   # Anasayfayi tanimladim
    return render_template("navigation.html")
@app.route("/message", methods=['GET', 'POST'])	
def message():										   # Anasayfayi tanimladim
    return render_template("chat.html")
@app.route("/about")								   # Hakkimda sayfasi icin yonlendirme..
def about():										   # Hakkimda sayfasini tanimladim
        return render_template("about.html")		   # render template ile html dosyami python serverime attim
@app.route("/advise")								   # advise tavsite sayfasi yonlendirmesi..
def advise():										   # advise tavsiye sayfasini tanimladim
        return render_template("suggestions.html")	   # render template ile html dosyami python serverime attim
@app.errorhandler(404)
def page_not_found(e):								   # Burada 404 hatasi cikarsa diye bir sayfa olusturdum
    return render_template('404.html'), 404
@app.errorhandler(500)								   # Burada server hatasi cikarsa 404 e yonlendirdim
def server_error(e):
	return render_template('404.html'), 500
						   # advise tavsite sayfasi yonlendirmesi..

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
                        print ("Hatali giris")
                if request.form["action"] == "navi":           
                        return redirect(url_for('navi'))
     
                if request.form["actions"] == "message":
                        return redirect(url_for('message'))                    
                    
        elif request.form["action"] == "luck":        
            return render_template("aks.html")
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
