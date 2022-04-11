from random import randint

def evalua_numero(supuesto_numero, numero_por_adivinar):
    if supuesto_numero==numero_por_adivinar:
        respuesta='Correcto '+str(supuesto_numero)+' es el numero. Ganaste!'
    elif supuesto_numero>numero_por_adivinar:
        respuesta='El numero correcto es menor que '+str(supuesto_numero)
    elif supuesto_numero<numero_por_adivinar:
        respuesta='El numero correcto es mayor que '+str(supuesto_numero)
    else:
        respuesta='La cadena ingresada:'+str(supuesto_numero)+'no es un numero'
 
    return respuesta


def run():

    numero_por_adivinar= randint(1,100)
    supuesto_numero=0
    while numero_por_adivinar!=supuesto_numero:
        supuesto_numero=int(input("El numero es: "))
        print(evalua_numero(supuesto_numero,numero_por_adivinar))


if __name__ =='__main__':
    run()