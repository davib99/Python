#-*- coding:utf-8 -*-

import turtle
import os
import time

path = '/home/dawid/Dokumenty/PYTHON/conf.txt'
plik = open(path,'r')

obwod=int(plik.readline())
sciezka=plik.readline()

print obwod
print sciezka+'!'



def kierunek(zolw,litera):
    if litera=='N':
        zolw.setheading(90)
    elif litera=='W':
        zolw.setheading(180)
    elif litera=='S':
        zolw.setheading(270)
    elif litera=='E':
        zolw.setheading(0)    
    
t = turtle.Turtle()

for i in sciezka[0:len(sciezka)-1]:
    kierunek(t,i)
    
    t.forward(50)
    time.sleep(1)

turtle.getscreen()._root.mainloop()


'''
t = turtle.Turtle()
t.write('START')
t.setheading(90)

print t.heading()
t.right(90)
t.forward(50)
t.right(90)
t.forward(250)

print t.heading()
    

turtle.getscreen()._root.mainloop()
'''