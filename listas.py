# Listas.py --- Demuestra el uso basico de listas 

# Creacion de listas ---------

print("CREANDO LISTAS")
print("--------------")

myList=[]
print(myList)

myList=[1,2,3]
print(myList)

myList=[1,"Hola", 3.4]
print(myList)

myListComposite=["mouse",[8,4,6],(1,2)]
print(myListComposite)

print("Presiona ENTER para continuar ....")
input()

# Indexacion ---------------------

print("INDEXANDO LISTAS")
print("----------------")

myList=['p','r','o','b','e']
myListC=['Happy',[2,0,1,5]]

print(myList[0])      #p
print(myList[2])      #o
print(myListC[0])     #'Happy'
print(myListC[1][3])  #5
print(myListC[-2])     #'Happy'

print("Presiona ENTER para continuar ....")
input()

# Slicing ---------------------------------

print("SLICING DE LISTAS")
print("------------------")

myList=['R','a','f','a','e','l']
print(myList[1:4])       #[‘a’,’f’,’a’]
print(myList[:-2])       #[‘R’,’a’,’f’,’a’]
print(myList[3:])        #[‘a’,’e’,’l’]

print("Presiona ENTER para continuar ....")
input()

# Cambios ------------------
print('CAMBIOS EN LISTAS')
print('-----------------')

pares=[0,2,4,6,8]
print(pares)       # [0,2,4,6,8] 

pares[0]=1         # [1,2,4,6,8] 
print(pares)

pares[1:4]=[3,5,7] # [1,3,5,7,8]
print(pares)

print("Presiona ENTER para continuar ....")
input()

# Agregando --------------------

print('AGREGANDO EN LISTAS')
print('-------------------')

impares=[1,3,5]
print(impares)             # [1,3,5]

impares.append(7)          # [1,3,5,7]
print(impares)

impares.extend([9,11,13])  # [1,3,5,7,9,11,13]
print(impares)

print("Presiona ENTER para continuar ....")
input()

# Concatenacion y repeticion -----------------------
print('CONCATENACION Y REPETICION')
print('--------------------------')

impares=[1,3,5]
print(impares)

impares=impares+[9,7,5]    # [1,3,5,9,7,5]
print(impares)

print([2,4,6] * 2)        # [2,4,6,2,4,6]

print("Presiona ENTER para continuar ....")
input()

# Insercion --------------------------------

print('INSERCION EN LISTAS')
print('-------------------')

impares=[1,9]
print(impares)      # [1,9]

impares.insert(1,3) # [1,3,9]
print(impares)

print("Presiona ENTER para continuar ....")
input()

# Remover por posicion -------------------------

print('REMOVER POR POSICION')
print('--------------------')

pares=[0,2,4,6,8]
print(pares)        # [0,2,4,6,8]

del pares[2]        # [0,2,6,8]
print(pares)

del pares[1:3]      # [0,8]
print(pares)

del pares           #
print('Lista pares no existe ....')

print("Presiona ENTER para continuar ....")
input()

# Remover por elemento -----------------------

print('REMOVER POR ELEMENTO')
print('--------------------')

myList=['c','a','r','l','o','s']
print(myList)       # ['c','a','r','l','o','s']

myList.remove('c') # [’a’,’r’,’l’,’o’,’s’]
print(myList)

myList.pop()       # [’a’,’r’,’l’,’o’]
print(myList)

myList.pop(1)      # [’a’,’l’,’o’]
print(myList)

myList.clear()     # [] 
print(myList)

print("Presiona ENTER para continuar ....")
input()

# Indice de elemento ----------------------

print('INDICE DE UN ELEMENTO')
print('---------------------')

myList=[3,8,1,6,0,8,4]
print(myList)             # [3,8,1,6,0,8,4]

print(myList.index(8))    # 1

print("Presiona ENTER para continuar ....")
input()

# Conteo en listas --------------

print('CONTEO EN LISTAS')
print('----------------')

myList=[3,8,1,6,0,8,4]
print(myList)           # [3,8,1,6,0,8,4]

print(myList.count(8))  # 2

print("Presiona ENTER para continuar ....")
input()

# Ordenar ---------------------------
print('ORDERNAR LISTAS')
print('---------------')

myList=[3,8,1,6,0,8,4]
print(myList)           # [3,8,1,6,0,8,4]

myList.sort()
print(myList)           # [0,1,3,4,6,8,8]

print("Presiona ENTER para continuar ....")
input()

# Reversa ---------------------

print('REVERSA DE UNA LISTA')
print('--------------------')

myList=[7,2,3,5]
print(myList)       # [7,2,3,5]

myList.reverse()   
print(myList)       # [5,3,2,7]

print("Presiona ENTER para continuar ....")
input()

# List comprehension -----------

print('LIST COMPREHENSION')
print('------------------')

pot2 = [2 ** x for x in [1,3,5]]
print(pot2)   # [2,8,32]

pot2excepto3 = [2 ** x for x in [1,3,5] if x != 3]
print(pot2excepto3)   # [2,32]

print("Presiona ENTER para continuar ....")
input()

# Membresia en listas -----------------

print('MEMBRESIA EN LISTAS')
print('-------------------')

myList=[2,4,6,8,9]
print(myList)       # [2,4,6,8,9]

print(2 in myList)  #True
print(1 in myList)  #False

print("Presiona ENTER para continuar ....")
input()

# Longitud/Max/Min/Suma ------

print('LONGITUD/MAX/MIN/SUMA')
print('---------------------')

myList=[2,4,6,8,9]
print(myList)       #[2,4,6,8,9]

print(len(myList))   #5
print(max(myList))   #9
print(min(myList))   #2
print(sum(myList))   #29

print("Presiona ENTER para continuar ....")
input()