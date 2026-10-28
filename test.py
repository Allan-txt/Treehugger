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
from bullet import Bullet
import sqlite3

def main(choice):
    print("Stammbaum von: ", choice)
    #print("\033[H\033[J", end='')
    choicelist = getchoices(choice)
    cli = Bullet(choices = choicelist)
    result = cli.launch()
    result = result.split(" ")
    result = int(result[1])
    print(result)

    main(result)

def getchoices(choice):
    choicelist = []
    choicelist.append("vater: " + str(getvater(choice)))
    choicelist.append("mutter: "+str(getmutter(choice)))
    for i in getgeschwister(choice):
        choicelist.append("geschwister: " + str(i))
    for i in getkinder(choice):
        choicelist.append("kinder: " + str(i))
    return choicelist

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
    mutter = mu[0]
    mutter = mutter[0]
    return mutter
def getgeschwister(id):
    vater = getvater(id)
    mutter = getmutter(id)
    conn = sqlite3.connect("treelist.sqlite")
    cur = conn.cursor()
    cur.execute("SELECT uuid FROM trees WHERE vater=? OR mutter=?", (vater, mutter,))
    ge = cur.fetchall()
    geschwister = []
    for i in ge:
        i = i[0]
        geschwister.append(i)
    geschwister.remove(id)
    return geschwister

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

main(4)
#getgeschwister(4)
