# Veri Çekici #
#---------------------------------------------# 
import psycopg2
from psycopg2 import Error


data=[]

def verilendin(tumveri):
    sayac=0
    a=0
    while sayac is not 60:
            try:
                temp=list(tumveri[a])
                temp.insert(0,sayac+1)
                data.append(temp)
                #print(data)
                a=a+10
                sayac=sayac+1
                
                
            except:
                return data

    return data
def sicaklik(datam):
    for i in datam:
        i.pop()
        i.pop()
        i.pop()
        i.pop()
        i.pop()
        i.pop()
    return datam
#def gerilim(datalar):
#    for i in datalar:
 #       if i == None or "" or len(i)==0:
 #           return datalar
 #       else:
 #           i.pop()
 #           i.pop()
  #          i.pop(1)
   #         i.pop(1)
    #        i.pop(1)
     #       i.pop(1)
    #return datalar
def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
        conn = psycopg2.connect(user = "vfrhjnyxtlicam",
                                  password = "5bd15794ceeeccce46189ba66b458d30d50c66627e29ea52e220bb3a8c7904ad",
                                  host = "ec2-107-20-230-70.compute-1.amazonaws.com",
                                  port = "5432",
                                  database = "d6j61pnoq4r9to")
        
        cur = conn.cursor()
        cur.execute("SELECT sicaklik1, sicaklik2, sicaklik3, sicaklik4, gerilim1, gerilim2, gerilim3, gerilim4, batarya, hiz FROM veri ")
        print("Bulunan satir ", cur.rowcount)
        tumveri = cur.fetchall()
        #print(tumveri)
        yedekdata=[]
        data=verilendin(tumveri)
        yedekdata=data
        #gerilims=gerilim(data)
      
        datam=sicaklik(yedekdata)
        
        

        #print(gerilims)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        #print("4")
        print(error)
    finally:
        #print("5")
        if conn is not None:
            conn.close()
    return datam
class Ceran:
    def ceran(self):
        (self.datam) = get_vendors()
        return (self.datam)
