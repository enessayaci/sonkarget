
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
        cur.execute("SELECT sicaklik1, sicaklik2, sicaklik3, sicaklik4, gerilim1, gerilim2, gerilim3, gerilim4, batarya, hiz, zaman FROM veri ")
        veri = cur.fetchone()
        while veri != None:
            data.append(list(veri))
            veri = cur.fetchone()
            
        
        
        

        #print(gerilims)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        #print("4")
        print(error)
    finally:
        #print("5")
        if conn is not None:
            conn.close()
    return data
class Logs:
    def log(self):
        (self.data) = get_vendors()
        return (self.data)
