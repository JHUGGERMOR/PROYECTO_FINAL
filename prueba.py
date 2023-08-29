

a=int(input('\nEscriba la Cantidad de Valores que Quieras Verificar  '))
b=0
valores=()

while b<a:
    valor=input('\nEscibre números enteros,decimales, String, colecciones  ')
    valores +=(valor,)
    b=len(valores)


print("\nTipos de datos de los valores ingresados:  \n")
for valor in valores:
    if valor.isdigit():
        print(f"{valor} es un número entero\n")
    elif valor.replace('.', '', 1).isdigit():
        print(f"{valor} es un número decimal\n")
    else:
        print(f"{valor} es una cadena de caracteres\n")

print("Tupla completa:", valores)








