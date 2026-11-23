"""
What's reality? I don't know. When my bird was looking at my computer
monitor I thought, "That bird has no idea what he's looking at." And
yet what does the bird do? Does he panic? No, he can't really panic,
he just does the best he can. Is he able to live in a world where
he's so ignorant? Well, he doesn't really have a choice. Yeah, he can
kinda live. Usually the bird is okay even though he doesn't understand
the world. He can kinda learn what's safe and what's dangerous. That's
where I've been living. You're that bird looking at the monitor, and
you're thinking to yourself, "I can figure this out." Maybe you have
some bird ideas. Maybe that's the best you can do.
"""
"""
getgeschwister(id,index) jüngstes 1, 2jüngstes 2; ältestes -1, 2ältestes-2
getopa(id,väter/mütterlicherseits) vater = true; mutter=false
int, int
int boolean
seite: väter/mütterlicherseits
"""
import sqlite3

def getkind(id,index,geschlecht):
    pass
def getgeschwister(id,index,geschlecht):
    pass
def gethalbgeschwister(id,index,geschlecht,seite):
    pass
def getelternteil(id,geschlecht):
    pass
def getgrosselternteil(id,geschlecht,seite):
    pass
def getelterngeschwister(id,index,geschlecht,seite):   #onkel/tante
    pass
def getnibling(id,index,geschlecht,seite):#neffe/nichte
    pass
def getgeschwisterzweitengrades(id, index,geschlecht,seite):
    pass

"""
def getvater(id):
    conn = sqlite3.connect("treelist.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT vater FROM trees WHERE uuid=?", (id,))
    va = cur.fetchall()
    vater = va[0]
    vater = vater[0]
    return vater
def getmutter(id):
    conn = sqlite3.connect("treelist.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT mutter FROM trees WHERE uuid=?", (id,))
    mu = cur.fetchall()
    #mutter = mu[0]
    #mutter = mutter[0]
    #return mutter
    return mu[0][0]

def getgeschwister(id):
    vater = getvater(id)
    mutter = getmutter(id)
    conn = sqlite3.connect("treelist.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT uuid FROM trees WHERE vater=? OR mutter=?", (vater, mutter,))
    ge = cur.fetchall()
    #geschwister = []
    #for i in ge:
     #   i = i[0]
      #  geschwister.append(i)
    #geschwister.remove(id)
    #return geschwister
    return ge
def getkinder(id):
    conn = sqlite3.connect("treelist.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT uuid FROM trees WHERE vater=? OR mutter=?",(id,id,))
    ki = cur.fetchall()
    kinder =[]
    for i in ki:
        i = i[0]
        kinder.append(i)
    return kinder
"""