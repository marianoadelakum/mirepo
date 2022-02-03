# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:47:13 2021

@author: MarianoDjemilAdelaku
"""

print("Tabla and")
print("0 and 0=", 0 and 0)
print("0 and 1=", 0 and 1)
print("1 and 0=", 1 and 0)
print("1 and 1=", 1 and 1)

print("Tabla or")
print("0 or 0=", 0 or 0)
print("0 or 1=", 0 or 1)
print("1 or 0=", 1 or 0)
print("1 or 1=", 1 or 1)

print("Tabla and")
print("0 and 0=",bool(0 and 0))
print("0 and 1=",bool(0 and 1))
print("1 and 0=",bool(1 and 0))
print("1 and 1=",bool(1 and 1))

print("Tabla or")
print("0 or 0=",bool(0 or 0))
print("0 or 1=",bool(0 or 1))
print("1 or 0=",bool(1 or 0))
print("1 or 1=",bool(1 or 1))

<<<<<<< HEAD
print("vamos a calcular el IMC")

altura=float(input("introduce tu altura: "))
peso=float(input("introduce tu peso: "))
resultado=peso/(altura*altura)

print("tu IMC es: ",resultado)
=======
if resultado<19:
   print("peso inferior a lo normal")
elif resultado >=19 and resultado<=25:
    print("normal")
elif resultado >=25 and resultado<=30:
    print("peso superior al normal")
elif resultado>30:
    print("obesidad")
>>>>>>> newram

print("vamos a probar el conflicto con mi carpeta de trabajo")