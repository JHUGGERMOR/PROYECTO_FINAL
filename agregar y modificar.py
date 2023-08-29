
#Se crea una Variable del nombre que se llamara el Diccionario

print('SUPER PRECIOS \n')

#Las cantidades son el Libras
precios={'Arroz':2000, 
         'Carne de Res':11000, 
         'Sal':1000,
         'Azucar':2500,
         'Frijol':6000,
         'Lenteja':2000,
         'Pollo':6000}

print(precios)

c=precios.keys()
print(c)

#Agregar Elementos al Diccionario
precios['Lulo']=3000
print(precios)

#Agregar Elementos con una Entrada
precios[input('Escribe el Elemento a Agregar  ')]=int(input('\nEscribe su Precio  '))
print(precios)

#Cambiar Valores
precios['Sal']=1200
print(precios)

#Cambiar Valores con una Entrada
precios['Carne de Res']=int(input('\nEscribe un Precio, Carne de Res  '))
print(precios)