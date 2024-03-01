import os
from tabulate import tabulate
import modulos.vaexer2 as v

#2. El centro de salud de campuslands desea realizar un programa que le permita calcular el IMC de los
#Estudiantes nuevos.
Datos=[[],[],[],[],[],[]]
for i in range (1,3,1):
    os.system('cls')
    print("Bienvenido al centro de salud de campuslands para calculo de IMC personalizado.")
    print (f'Estudiante #{i}')
    print("Ingrese su nombre: ")
    nombre=v.validacion1()
    print("Ingrese su edad: ")
    edad=v.validacion2()
    print("Ingrese su peso: ")
    peso=v.validacion3()
    print("Ingrese su altura: ")
    altura=v.validacion4()
    os.system('cls')
    imc=(peso/(altura**2))
  
    if imc<18.5:
        Datos[0].append(imc)
    elif imc<=24.9:
        Datos[1].append(imc)
    elif imc<=29.9:
        Datos[2].append(imc)
    elif imc<=34.9:
        Datos[3].append(imc)
    elif imc<=39.9:
        Datos[4].append(imc)
    else:
        Datos[5].append(imc)
    
bajo=len(Datos[0])
normal=len(Datos[1])
Sobrepeso=len(Datos[2])
ob_grado1=len(Datos[3])
ob_grado2=len(Datos[4])
ob_grado3=len(Datos[5])
cantidad=[[str(bajo),str(normal),str(Sobrepeso),str(ob_grado1),str(ob_grado2),str(ob_grado3)]]
print(tabulate(cantidad, headers=['Bajo','Normal','Sobrepeso','Obesidad grado 1', 'Obesidad grado 2', 'Obesidad grado 3'],tablefmt="mixed_grid"))
print ('Gracias por usar la plataforma campuslands.')