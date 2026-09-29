import sqlite3

def getelternteile(uuid):
    conn = sqlite3.connect("treelist.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT vater AND mutter FROM trees WHERE uuid=?",(uuid,))
    result = cur.fetchall()
    print(result)
    return(result)

def getvater(uuid):
    pass
def getmutter(uuid):
    pass

def getallgeschwister(uuid):
    pass
def getgeschwister(uuid,geschlecht,jungalt,index):
    pass


getelternteile(3)
