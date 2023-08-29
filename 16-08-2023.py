#Listas
lista = ["Juan",2,"Mango", 1.85]
print(lista)
print('\n',lista[0])

del lista[0] 
for z in lista:
    print(z)

w = len(lista)
q = 0



while q < w:
    print('\n',lista[q])
    q +=1

varlista=['hola', 12, 8 , 'hol']

del varlista[0] #elimina el elemento en lz primera posicion
varlista.insert(1,'juan') #agrega un elemento en la posicion 1
varlista.append("alejo") #agrega un elemento en la ultima posicion
#varlista.append(input('inserte ciudad')) #agrega un elemento en la ultima posicion

eliminar=input('digite el vallor a eliminar')
contador=0

for z in varlista:
  if eliminar ==z:
     del varlista[contador]
  else :
     contador +=1

print(varlista)

datos = [['hola','efe','rodrigo'],['holis','veneco','huila'],['javio', 'pola','o miedo']]

for z in lista: #Con este codigo podemos eliminar un valor
    for u in z:
        print(u)
    print("----------------")
