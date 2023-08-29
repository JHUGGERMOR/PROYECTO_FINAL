#CREACION DE CONTRASEÑA PARA EL INGRESO A UNA PLATAFORMA
print('CREACION DE CONTRASEÑA \n')
a = input('Escribe Una Contraseña   ')

print("-------------")
print("-------------")

b = input('Confirma tu Contraseña   ') 

while a != b:
    print('Contraseña Incorrecta, Vuelve a Intentarlo')
    b = input('Confirma tu Contraseña   ') 

print('Contraseña Correcta \n')

#CALCULADORA DIVISORA
print('\nCalculadora Divisora \n')
a = int(input('Escribe el Numerador de la Division  '))
b = int(input('Escribe el Denominador de la Division  '))

while b==0:
  print('ERROR. No se puede dividir entre 0 ')
  b = int(input('Escribe el Denominador de la Division  '))

print('El Resultado Obtenido', a/b)

#ES UN NUMERO PAR O IMPAR?
print('\n\nEs Par o Impar? \n')
a = int(input('Escribe un Numero  '))

if a % 2 == 0:
    print(a, "Es un Número Par\n")
else:
    print(a, "Es un número Impar\n")

#SOLICITUD DE EDAD PARA EL INGRESO A UN ESTABLECIMIENTO
print('\nDISCOCLUB \n')
a = int(input('Edad Primera Persona '))
b = int(input('Edad Segunda Persona '))
c = int(input('Edad Tercera Persona '))
d = int(input('Edad Cuarta Persona '))
e = int(input('Edad Quinta Persona '))

print("\n-------------")
print("-------------\n")

item =[a,b,c,d,e]

for i in item:

  if(i >= 19):
    print('¡BIENVENIDO!\n')
  else:
    print('¡No Puede Ingresar!\n')