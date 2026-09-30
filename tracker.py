import sqlite3

def getelternteile(uuid):
    conn = sqlite3.connect("treelist.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT vater FROM trees WHERE uuid=?",(uuid,))
    vater = cur.fetchall()
    cur.execute("SELECT mutter FROM trees WHERE uuid=?",(uuid,))
    mutter = cur.fetchall()
    return(vater,mutter)

def getvater(uuid):
    conn = sqlite3.connect("treelist.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT vater FROM trees WHERE uuid=?",(uuid,))
    va = cur.fetchall()
    vater = va[0]
    vater = vater[0]
    return vater
def getmutter(uuid):
    conn = sqlite3.connect("treelist.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT mutter FROM trees WHERE uuid=?", (uuid,))
    mu = cur.fetchall()
    mutter = mu[0]
    mutter = mutter[0]
    return mutter

def getallgeschwister(uuid):
    elternteil = [getvater(uuid), getmutter(uuid)]
    print(elternteil)
    conn = sqlite3.connect("treelist.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT uuid FROM trees WHERE vater=? OR mutter=?",(elternteil[0],elternteil[1],))
    result = cur.fetchall()
    print(result)
    #output muss noch cleaner sein!!!






def getgeschwister(uuid,geschlecht,jungalt,index):
    pass

getallgeschwister(3)
