
import os
import modulos.validacion4 as v

suma=0
numpar=0
numimpar=0
prompar=0
promimpar=0
menor10=0
entre=0
mayor=0
sumanum=0
numeros=1
sumanumpar=0
sumanumimpar=0
pronim=0
prompa=0

while numeros>0:
    os.system('clear')
    print("Ingrese un numero entero positivo")
    numeros=v.vali()
    suma+=1
    if numeros % 2==0:
        numpar+=1
        # sumanumpar+=numeros
    else: 
        numimpar+=1
        # sumanumimpar+=numeros
    if numeros < 10:
        menor10+=1
    elif numeros >= 20 and numeros <= 50:
        entre+=1
    elif numeros > 100:
        mayor+=1
    
    
    prompa=numpar/suma
    promim=numimpar/suma
      
    
    print(f'EL TOTAL DE NUMEROS INGRESADOS ES DE {suma} ')    
    print(f'EL TOTAL DE NUMEROS PARES INGRESADOS ES DE {numpar} ')  
    print(f'EL PROMEDIO DE PARES INGRESADOS ES DE {prompa} ')  
    print(f'EL PROMEDIO DE IMPARES INGRESADOS ES DE {promim} ')  
    print(f'LA CANTIDAD DE NUMEROS MENORES QUE 10 ES DE {menor10} ') 
    print(f'LA CANTIDAD DE NUMEROS QUE ESTAN ENTRE 20 Y 50 ES DE {entre} ')
    print(f'LA CANTIDAD DE NUMEROS MAYORES QUE 100 SON {mayor} ') 
    input()