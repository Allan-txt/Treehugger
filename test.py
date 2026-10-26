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
choice = ["first", "second", "third", "fourth", "fitht"]


def main(choice):
    choicelist = getchoices(choice)
    amount = len(choicelist)
    cli = Bullet(choices = choicelist)
    result = cli.launch()
    main(result)

def getchoices(choice):
    choicelist = []
    choicelist.append(str(getvater(choice)))
    choicelist.append(str(getmutter(choice)))
    choicelist.append(str(getgeschwister(choice)))
    choicelist.append(str(getpartner(choice)))
    choicelist.append(str(getkinder(choice)))
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
    return None
def getpartner(id):
    return None
def getkinder(id):
    return None

main(3)
