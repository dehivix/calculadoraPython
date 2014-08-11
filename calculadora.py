'''
    Calculadoras hecha en python
'''
resp = 's'
while resp == 's':
    #TODO:
    #sumar, restar, multiplicar y dividir

    numero1 = input('Ingrese el valor 1: ')
    numero2 = input('ingrese valor 2: ')

    #suma
    print 'la suma es: ' +str(numero1 + numero2)
    print 'la resta es: ' +str(numero1 - numero2)
    print 'la division es: ' +str(numero1 / numero2)

    resp = raw_input('Desea volver a ejecutar(S/N): ')

