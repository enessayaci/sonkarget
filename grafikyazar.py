# Veri Çekici #
#---------------------------------------------# 
import psycopg2
from psycopg2 import Error

#a = [[1,2,3],[2,3,4],[4,5,6]]
#i = 0
#for a in range(a):
#   i +=1
#   dic[sicaklik].append([i,a[0][:3]])
#   dic[gerilim].append([i,[a[0][3:7]]])
#   a.pop(0)
data=[]
def verilendin(tumveri):
    sayac=0
    a=0
    dic = {"sicaklik":[],"gerilim":[],"batarya":[],"hiz":[]}
    while sayac is not 60:
            try:
                temp=list(tumveri[a])
                sicaklik = temp[:4]
                gerilim = temp[4:8]
                batarya = [temp[8]]
                hiz = [temp[9]]
                sicaklik.insert(0,sayac+1)
                gerilim.insert(0,sayac+1)
                batarya.insert(0,sayac+1)
                hiz.insert(0,sayac+1)
                dic["sicaklik"].append(sicaklik)
                dic["gerilim"].append(gerilim)
                dic["batarya"].append(batarya)
                dic["hiz"].append(hiz)
                #print(dic["sicaklik"])
                a=a+10
                sayac=sayac+1
                
                
            except:
                return dic

    return dic
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
        #print(tumveri,"------")
        yedekdata=[]
        dic=verilendin(tumveri)
        gerilim = dic["gerilim"]
        sicaklik= dic["sicaklik"]
        batarya = dic["batarya"]
        hiz=dic["hiz"]
        #gerilims=gerilim(data)
        #print(sicaklik)
        #datam=sicaklik(yedekdata)
        
        

        #print(gerilims)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        #print("4")
        print(error)
    finally:
        #print("5")
        if conn is not None:
            conn.close()
    return sicaklik,gerilim,batarya,hiz
class Ceran:
    def ceran(self):
        (self.sicaklik,self.gerilim,self.batarya,self.hiz) = get_vendors()
        return (self.sicaklik,self.gerilim,self.batarya,self.hiz)