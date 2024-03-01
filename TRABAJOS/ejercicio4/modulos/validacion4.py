def vali():
    try:
        numeros= int(input(';) ')) 
        if numeros> 0: 
            return numeros
        else:
            print('Numero no valido')
            return vali()
    except ValueError:
        print('Dato no valido')
        return vali()
  
  
  
  

  
  
 