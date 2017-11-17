#-*- coding: utf-8 -*-


slownik = {"wartosc1":1,"wartosc2":2}

print '\n'.join(['%s=%s'% (k,v) for k,v in slownik.items()])

tab=['a','b','c']
print tab[0:2]

a = list()
a.append('a')
a.extend(['b','c'])
print 'a=',a
if True:
    print 'tat'
    
    
(a,b,c)=(1,2,3)

print 'a=',a
print 'b=',b
print 'c=',c

slownik = {'jeden':1,'dwa':2}

li=[1,2,3,4,5]

print ['%s=%s' % (k,v) for k,v in slownik.items()]

import types
a=dict()
print type(a)
if type(a)==types.DictType:
    print 'boolean'
    
sl={'jeden':1,'dwa':2}
    
wypisz=getattr(sl,'items')
print wypisz()


wypisz=getattr(sl,'asd',sl.clear)


