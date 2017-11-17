#-*- coding:utf-8 -*-
import numpy

sciezka = '/home/dawid/programowanie/python/nauka/wejscie.txt'
plik = open(sciezka,'r')
ile = int(plik.readline())

macierz1=numpy.zeros((ile,1))
macierz2=numpy.zeros((ile,1))


for i in range(0,ile):
    linia = plik.readline()
    print linia
    liczba1=int(linia[0:linia.find(' ')])
    liczba2=int(linia[linia.find(' '):])
    macierz1[i] = liczba1
    macierz2[i] = liczba2
print macierz1

print macierz2

print macierz1*macierz2


