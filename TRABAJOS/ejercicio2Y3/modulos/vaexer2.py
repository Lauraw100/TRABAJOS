def validacion1():
    try:
        nombre=str(input())
        return nombre
    except ValueError:
        print ('Ingrese solo letras por favor')
        return validacion1()

def validacion2():
    try:
        edad=int(input())
        return edad
    except ValueError:
        print('El numero ingresado no es valido')
        return validacion2()
    
def validacion3():
    try:
        peso=float(input())
        return peso
    except ValueError:
        print ('El numero ingresado no es valido')
        return validacion3()

def validacion4():
    try:
        altura=float(input())
        return altura
    except ValueError:
        print ('El numero ingresado no es valido: ')
        return validacion4()