import random

print("Hello Python")

def salir():
    #print("hola")
    exit()


def numeroAleat():
    numero = int(input('Adivine un numero de uno a quince.\n'))
    if numero > 15:
        print('Debe ingresar un numero menor, que sea de uno a quince.')
        numeroAleat()
    elif numero == 0:
        print('Debe ingresar un numero mayor, que sea de uno a quince.')
        numeroAleat()
    else:
        aleatorio = random.randint(1,15)
        print(aleatorio)
        intentos=1
        validacion(numero, aleatorio, intentos)


def validacion(numero, aleatorio, intentos):  
    while intentos <= 3:  
        if numero == aleatorio:
            print("Usted ha ganado!")
            intentos=3
            exit()
        elif numero > aleatorio:
            if intentos != 3:
                intentos = intentos + 1
                print("Su numero es mayor", intentos)                            
                numero = int(input('Ingrese un numero menor.\n'))            
                validacion(numero, aleatorio, intentos)
            else:
                print("Agotó los intentos")
                exit()
        elif numero < aleatorio:
            if intentos != 3:
                intentos = intentos + 1
                print("Su numero es menor", intentos)            
                numero = int(input('Ingrese un numero mayor.\n'))            
                validacion(numero, aleatorio, intentos)  
            else:
                print("Agotó los intentos")
                exit()

    print("Agoto los intentos")
    exit()
    
     

#salir()
numeroAleat()
#numero = random.randint(1,numero)
#print(numero)
