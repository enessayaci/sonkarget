# Veri Çekici #
#---------------------------------------------# 
import psycopg2
from psycopg2 import Error


data=[]

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
        row = cur.fetchone()
    
        while row is not None:
            data.append(row)
#            print(row)
            row = cur.fetchone()
            son=data.pop() 
            son_degerler=list(son)
        cur.close()
        print("En son satir = ",son_degerler)
        sicaklik1=son_degerler[0]
        sicaklik2=son_degerler[1]
        sicaklik3=son_degerler[2]
        sicaklik4=son_degerler[3]
        gerilim1=son_degerler[4]
        gerilim2=son_degerler[5]
        gerilim3=son_degerler[6]
        gerilim4=son_degerler[7]
        batarya=son_degerler[8]
        hiz=son_degerler[9]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return sicaklik1,sicaklik2,sicaklik3,sicaklik4,gerilim1,gerilim2,gerilim3,gerilim4,batarya,hiz
class Utku:
    def utku(self):
        (self.sicaklik1, self.sicaklik2, self.sicaklik3,self.sicaklik4,self.gerilim1,self.gerilim2,self.gerilim3,self.gerilim4,self.batarya,self.hiz) = get_vendors()
        return (self.sicaklik1, self.sicaklik2, self.sicaklik3,self.sicaklik4,self.gerilim1,self.gerilim2,self.gerilim3,self.gerilim4,self.batarya,self.hiz)
