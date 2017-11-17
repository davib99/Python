#-*- coding:utf-8 -*-

#slownik
kod_litera_1 = {'A':0,'B':1, 'C':2, 'D':3,'E':4, 'F':5, 'G':6, 'H':7, 'I':8,'J':9, 'K':10, 'L':11,'M':12,'N':13,'O':14,'P':15}
kod_litera_2 = {'A':0,'B':16, 'C':32, 'D':48,'E':64, 'F':80, 'G':96, 'H':112, 'I':128,'J':144, 'K':160, 'L':176,'M':192,'N':208,'O':224,'P':240}

haslo = 'BA8D8D908DCA'
haslo_deszyfr=''

for i in range(0,len(haslo),2):
    print haslo[i]+haslo[i+1]
    kod_ascii = int('0x'+haslo[i]+haslo[i+1],0)
    print 'kod ascii= ',kod_ascii
    roznica = 255-kod_ascii
    print 'nowy kod ascii= ',roznica
    print 'Nowa litera: ',chr(roznica)
    haslo_deszyfr=haslo_deszyfr+chr(roznica)
    
print haslo_deszyfr