import os
import validaciones.vaexer1 as v1
#1. Se requiere realizar un programa en Python que permita leer 3 números enteros positivos e imprima
#La sumatoria de los tres números.
os.system('clear')
numeros=[]
suma=0
bandera=True
while bandera:
    for i in range (3):
        numero=v1.vali_e()
        numeros.append(numero)
        suma+=numeros[i]
    print(suma)
    bandera=bool(input('Desea hacer mas sumas? enter(no) x(si)\n'))
    os.system('clear')