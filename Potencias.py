from unicodedata import name
def potencias(numero_base,exponente):
    potencia=numero_base**exponente
    return potencia


def run():
    numero=input("Ingresa un numero: ")
    exponente=0
    potencia_resultante=0
    MAXIMO_RESULTADO=1000
    while(potencia_resultante<MAXIMO_RESULTADO):
        potencia_resultante=potencias(int(numero),exponente)
        if potencia_resultante<MAXIMO_RESULTADO:
            print("La potencia de "+numero+" elevado a la "+ str(exponente) +" es:"+ str(potencia_resultante)) 
        exponente=exponente+1


if __name__ == '__main__' :
    run()
