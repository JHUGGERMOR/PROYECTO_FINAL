materias_notas = []  # Inicializar una lista vacía para almacenar las materias y notas

while True:
    materia = input("Ingresa el nombre de la materia (ingresa 'fin' para detener): ")
    
    if materia.lower() == 'fin':
        break  # Salir del ciclo si se ingresa 'fin'
    
    nota = float(input("Ingresa la nota de la materia: "))
    materias_notas.append((materia, nota))  # Agregar la tupla (materia, nota) a la lista

print("Materias y notas cursadas:")
for materia, nota in materias_notas:
    print(f"Materia: {materia}, Nota: {nota}")



#DIVISAS
divisas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

print('\nEuro Dollar Yen')
a=input('\nEscoge la divisa  ')
        
Euro=4449.69
Dollar=4096.17 
Yen=28.31


if a in divisas:
  b=int(input('\nEscribe la Cantidad a Convertir  '))
  if a=='Euro':
   print('\nLa conversion es: ',divisas['Euro'], b/Euro)
  elif a=='Dollar':
   print('\nLa conversion es: ',divisas['Dollar'], b/Dollar)
  else:
    print('\nLa conversion es: ',divisas['Yen'], b/Yen)
else:
  print('\nEsta divisa no se encuentra en el Diccionario')

