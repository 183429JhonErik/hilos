import time #pip install time
from threading import Thread
import math
def holamundo(n):
    time_ini = time.time()
    print("Inicio_")

    for i in range(n):
        if i % 2 ==0:
            print(i)
    

    print("holaaaa ")
    print ("Fin_")
    time_end = time.time()
    total = time_end - time_ini
    print(total, "\t")

def n2(n):
    time_ini = time.time()
    print("Inicio_")

    numeros = []

    numero = 0
    while numero<n:
        numero+=1
        if numero%2 == 0:
            numeros.append(numero)#Añade el numero al array
    print(numeros) 

    print("holaaaa ")
    print ("Fin_")
    time_end = time.time()
    total = time_end - time_ini
    print(total, "\t")

    
for i in range(2):
    #t = Thread(target=holamundo, args=(5030,))
    t1 = Thread(target= n2, args=(5030,))
    #t.start()
    t1.start()
