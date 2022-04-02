menu = """
Bienvenido a SimonConversor 
1- Soles a Dolares
2- Dolares a Soles
Elija una opcion: """
opcion=input(menu)

if opcion=="1":

    monto_en_soles=input("ingresa la cantidad en soles:")
    monto_en_soles=float(monto_en_soles)
    valor_dolar=3.7
    conversion_a_dolares=monto_en_soles/valor_dolar
    conversion_a_dolares=round(conversion_a_dolares, 2)
    print("Tienes "+ str(monto_en_soles)+ " soles que son $"+ str(conversion_a_dolares)+" dolares")
elif opcion=="2":
    monto_en_dolares=input("ingresa la cantidad en dolares:")
    monto_en_dolares=float(monto_en_dolares)
    valor_dolar=3.7
    conversion_a_soles=monto_en_dolares*valor_dolar
    conversion_a_soles=round(conversion_a_soles, 2)
    print("Tienes "+ str(monto_en_dolares)+ " dolares que son S/"+ str(conversion_a_soles)+" soles")
else:
    print("Ingresa la opcion correcta")