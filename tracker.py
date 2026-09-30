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
    vater = cur.fetchall()
    return vater
def getmutter(uuid):
    conn = sqlite3.connect("treelist.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT mutter FROM trees WHERE uuid=?", (uuid,))
    mutter = cur.fetchall()
    return mutter

def getallgeschwister(uuid):
    pass
def getgeschwister(uuid,geschlecht,jungalt,index):
    pass


print(getmutter(3))
