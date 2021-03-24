#Det si un triangulo es isoceles/ equilatero / escaleno


#def error fnct
def error():
    error = print('\n Error! \n')
    return(error)

lst = []

#ask 3x input to user
for i in range(3):
    x = float(input('Ingrese su angulo: '))
    lst.append(x)                   # append = add object to list


#def var & sums
n1 = lst[0]
n2 = lst[1]
n3 = lst[2]

suma = n1 + n2 + n3
suma1 = n1 + n2
suma2 = n2 + n3
suma3 = n1 + n3


#avoid buggy code w/ general conditions
def conditions():
    if suma != 180:
        error()
    elif suma1 == 180 or suma3 == 180 or suma2 == 180:
        error()
    elif n1 == 0 or n2 == 0 or n3 == 0:    #deberia ser: si se ingresa un 0 como angulo, lanzar error
        error()
    else:
        pass

conditions()

# No me gusta tener tanta variable independiente del resultado aca, prefiero pasarlo a conditions() como reglas generales, y solo definir las particulas a cada caso aca abajo.

#triangle conditions

if n1 == 60 and n2 == 60 and n3 == 60:
    print('\n Triangulo Equilatero \n')
elif n1 == 90 and n2 != 0 and n3 != 0 and suma == 180 and n1 <= 90 and n2 <= 90 and n3 <= 90 or n2 == 90 and n1 != 0 and n3 != 0 and suma == 180 and n1 <= 90 and n2 <= 90 and n3 <= 90 or n3 == 90 and n1 != 0 and n2 != 0 and suma == 180 and n1 <= 90 and n2 <= 90 and n3 <= 90:
    print('\n Triangulo Rectangulo \n')
elif n1 != n2 and n2 != n3 and n1 != n3 and n1 > 90 and suma == 180 or n2 > 90 and suma == 180 or n3 > 90 and suma == 180:
    print('\n Triangulo Escaleno \n')
elif n1 == n2 and n1 != 0 and n2 != 0 and n3 != 0 and suma == 180 or n2 == n3 and n1 != 0 and n2 != 0 and n3 != 0 and suma == 180 or n1 == n3 and n1 != 0 and n2 != 0 and n3 != 0 and suma == 180:
    print('\n Triangulo isoceles \n')


# error al poner p.e: 170, 5 y 5 (dice que es isoceles, pero tambien es escaleno)





# intento de condiciones especificas para cada triangulo, y las generales que queden aparte pero tampoco me cranio como hacerlo jaja

# if n1 == 60 and n2 == 60 and n3 == 60:
#     print('\n Triangulo Equilatero \n')
# elif n1 == 90 or n2 == 90 or n3 = 90:
#     print('\n Triangulo Rectangulo \n')
# elif n1 > n2 + n3 or n2 > n1 + n3 or n3 > n1 + n2:
#     print('\n Triangulo Escaleno \n')
# elif n1 == n2 or n2 == n3 or n1 == n3:
#     print('\n Triangulo isoceles \n')