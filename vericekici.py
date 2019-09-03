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
        cur.execute("SELECT sicaklik1, sicaklik2, sicaklik3, sicaklik4 FROM veri ")
        print("Bulunan satir ", cur.rowcount)
        row = cur.fetchone()
    
        while row is not None:
            data.append(row)
            print(row)
            row = cur.fetchone()
            son=data.pop() 
            son_degerler=list(son)
        cur.close()
        print("En son satir = ",son_degerler)
        sicaklik1=son_degerler[0]
        sicaklik2=son_degerler[1]
        sicaklik3=son_degerler[2]
        sicaklik4=son_degerler[3]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return sicaklik1,sicaklik2,sicaklik3,sicaklik4
class Utku:
    def utku(self):
        (self.sicaklik1, self.sicaklik2, self.sicaklik3,self.sicaklik4) = get_vendors()
        return (self.sicaklik1, self.sicaklik2, self.sicaklik3,self.sicaklik4)
