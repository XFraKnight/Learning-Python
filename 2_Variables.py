# Variables

# Imprimir una variable

variable_uno = "Variable"   # str
print(variable_uno)

variable_dos = 1            # int
print(variable_dos)

variable_tres = True        # bool
print(variable_tres)

# Imprimir variables juntas

print ('Prueba de', variable_uno, "1 +", variable_dos,"= 2 = ", variable_tres) # Prueba de Variable 1 + 1 = 2 =  True

# Transformar int a str

variable_cuatro = str(variable_dos)
print(type(variable_cuatro))

# Funcion del sistema = len

print(len(variable_uno)) # Longitud de "Variable" = 8

# Multiples variables en una linea > No aconsejable

a, b, c = 1, 2, 3 
print(a,'perro,', b, 'gatos y', c, 'peces') # 1 perro, 2 gatos y 3 peces

# Funcion del sistema = Input

pregunta = input('¿Cuantos animales tienes?')
print('Tienes', pregunta, 'animales')


