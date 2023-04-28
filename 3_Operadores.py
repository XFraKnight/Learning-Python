#Operadores

#Diferentes operadores int
 
print(2 + 3)  # Suma
print(2 - 3)  # Resta
print(2 * 3)  # Multiplicación
print(2 ** 3) # Exponente
print(2 / 3)  # Division
print(2 // 3) # Division aproximada
print(2 % 3)  # Division de modulo 

#Concatenación str > Entre tipos da error

print('Hola' + 'Mundo')
print('Hola' + str(5))

#Multiplicación str con int
print('Hola' * 5)

#Multiplicación str con int(float)
float = 2.5 * 2
print(float)
print(int(float))
print('Hola' * int(float)) 

# Operadores comparativos

print(2 < 3)  #Menor -> True
print(2 <= 3) #Menor o igual -> True
print(2 > 3)  #Mayor > False
print(2 >= 3) #Mayor o igual -> False
print(2 == 2) #Igual -> True
print(2 != 2) #Distinto -> False

#Operadors lógicos
print('-----------------------')
print(2 < 3  and 2 == 2) # AND -> Se cumplen los dos
print(2 < 3  and 3 == 2) 

print(2 < 3  or 2 != 2) # OR -> Se cumplen uno u otro
print(2 > 3  or 2 != 2)

print(not(3 == 2)) # NOT -> Niega
print(not(2 == 2)) 
