def identifica_palindromos(palabra):
    palabra=palabra.upper()
    palabra=palabra.replace(" ","")
    palabra_invertida=palabra[::-1]
    if palabra==palabra_invertida:
        palindromo=True
    else:
        palindromo=False
    return palindromo


def run():
    palabra_ingresada=input("Ingresa palabra:")

    if identifica_palindromos(palabra_ingresada):
        print("Palabra ingresada es un palindromo")
    else:
        print("Palabra ingresada no es un palindromo")


if __name__ == '__main__':
    run()