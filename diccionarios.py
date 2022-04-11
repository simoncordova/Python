from threading import main_thread
from pip import main


def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    #print (mi_diccionario['llave1'])

    poblacion_paises = {
        'Peru': 33000000,
        'Noruega': 2515151454,
        'Brasil': 545481524,
    }

    for pais in poblacion_paises.keys():
        print(pais)
    
    for pais in poblacion_paises.values():
        print(pais)
    
    for pais, poblacion in poblacion_paises.items():
        print(pais+ ' tiene '+ str(poblacion)+' habitantes')

if __name__=='__main__':
    run()
