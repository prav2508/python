import mysql.connector
try:
    db = mysql.connector.connect(host="localhost",user="root",passwd="root",database="py_db")
    cur = db.cursor()
    cur.execute("select * from student where sid=1")
    res = cur.fetchall()
    for i in res:
        sid = i[0]
        fname = i[1]
        lname = i[2]
        isadmin = i[3]
        passwd = i[4]
        #print(i)
    print("sid: {}\nfirstname: {}\nlastname: {}\nisadmin: {}\npassword: {}".format(sid,fname,lname,isadmin,passwd))
except Exception as e:
    print(e)
finally:
    db.close()