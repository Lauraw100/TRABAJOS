def vali_e():    
    try:
        numero_entero = int(input("Ingrese un número entero positivo: ")) 
        if numero_entero > 0: 
            return numero_entero
        else:
            print('Numero no valido')
            return vali_e()
    except ValueError:
        print('Dato no valido')
        return vali_e()
  
  
  
  
  