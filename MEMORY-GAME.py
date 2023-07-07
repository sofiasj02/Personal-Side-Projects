# Sofia Schneider Jimenez
# A01173896
# ITC
# Proyecto - Memorama para que el alumno aprenda objetos del salón de clases en inglés
# Grupo 413

from colorama import init, Fore, Back, Style
init()

import random


#crear lista de pares
def pares( ):
    pars =    """cellphone
\U0001F4F1
telephone
\U0000260E
pencil
\U0000270F
magnifying glass
\U0001F50D
pen
\U0001F58A
scissors
\U00002702
paperclip
\U0001F4CE
ruler
\U0001F4CF
book
\U0001F4D6
notebook
\U0001F4D2
binder
\U0001F4C1
pushpin
\U0001F4CC
printer
\U0001F5A8
trash bin
\U0001F5D1
calendar
\U0001F4C6
chair
\U0001FA91
clock
\U000023F0
computer
\U0001F5A5"""

    
    lista = pars.split("\n")

#    print("Longitud = ", len(lista))
#    for elemento in lista:
#       print(elemento)
#         
#
    return lista

import random, os

def limpia():
    '''Función que limpia a pantalla sin importar el sistema operativo
      de la máquina donde esté corriendo'''
    if os.name == 'nt': #Windows
        os.system('cls') 
    else:  #'posix'
        os.system('clear') #Mac/linux


def llena_tablero():
  '''Llena el tablero con las "cartas volteadas"'''
  matriz = []
  for r in range(6):
      renglon = []
      for c in range(6):
          # Agrega un emoji
          renglon.append('\U0001F48E')
      matriz.append(renglon)
  return matriz


def despliega_matriz(matriz,r1 = -1, c1 = -1, r2 = -1, c2 = -1):
  #Desplegar en pantalla la matriz, poniendo numeros en los renglones y columnas
  renglones = len(matriz)
  columnas = len(matriz[0])
  count = 0
  mensaje = "Encuentra los objetos del salón de clases"
  print(Back.MAGENTA + f"{mensaje}".center(85) + Back.RESET, end="")
  print('\n'+"=============="*renglones)
  for cada_renglon in range(columnas):
    count += 1
    print(f'{count}'.center(14), end="")
  print('\n'+"=============="*renglones)
    
    
  print("==============" * renglones)
  for r in range(renglones):
      print(r + 1,"|", end="")
      for c in range(columnas):
          if r1 != -1 and r == r1 and c == c1:
              print(Back.CYAN + f"{matriz[r][c]}".center(12) + Back.RESET, end="")
          elif r2 != -1 and r == r2 and c == c2:
                print(Back.CYAN + f"{matriz[r][c]}".center(12) + Back.RESET, end="")
          else:
              print(f"{matriz[r][c]}".center(12), end="")
              
          print("|", end="")
          
      print('\n' + "==============" * renglones)
    
    
def llena_escondida(lista):
  '''Llena una matriz con emojis y palabras en inglés, el alumno tiene que encontrar la palabra correspondiente al emoji'''
  matriz = []
  
  # shuffle - desordena lista de pares
  for r in range(6):
      renglon = []
      for c in range(6):
          # Agrega un 0 a 1 de manera aleatoria
          renglon.append(lista.pop())
      matriz.append(renglon)
      
  return matriz


def validar_carta(tablero,r1,c1,r2 = -1,c2 = -1):
    
    #validar la carta1
  if r2 == -1 and c2 == -1:
      while r1 < 1 or r1 > 6 or c1 < 1 or c1 > 6 or tablero[r1 - 1][c1 -1] != '\U0001F48E':
          r1 = int(input('Error!! Ingresa de nuevo Carta1\nRenglón: '))
          c1 = int(input('Columna: '))
             
      return r1 -1, c1 -1
    
  else:
      #validar la carta2
      #while, condiciones que verifican que no se cumple
      while r1 == r2 -1 and c1 == c2 -1 or r2 < 1 or r2 > 6 or c2 < 1 or c2 > 6 or tablero[r2 - 1][c2 -1] != '\U0001F48E':
        r2 = int(input('Error!! Ingresa de nuevo Carta2\nRenglón: '))
        c2 = int(input('Columna: '))
            
      return r2 -1, c2 -1


def validar_carta_compu(tablero,r1,c1,r2 = -1,c2 = -1):

    #validar la carta1
  if r2 == -1 and c2 == -1:
        #validar carta1    
    while tablero[r1 - 1][c1 -1] != '\U0001F48E':
      r1 = random.randint(1,6)
      c1 = random.randint(1,6)
    return r1 -1, c1 -1 
    
  else:
        #validar la carta2

    while r1 == r2 -1 and c1 == c2 -1 or tablero[r2 - 1][c2 -1] != '\U0001F48E':
      r2 = random.randint(1,6)
      c2 = random.randint(1,6)
            
    return r2 -1, c2 -1    


def verificar_pares(tablero,escondidas,lista_pares,lista_impares,r1,c1,r2,c2):
    
    
    #destapar las cartas escogidas y desplegar
    tablero[r1][c1] = escondidas[r1][c1]
    tablero[r2][c2] = escondidas[r2][c2]  
    limpia()
    despliega_matriz(escondidas)
    despliega_matriz(tablero,r1,c1,r2,c2)
       
    gano = 0
    
    #ver si son pares
    if escondidas[r1][c1] in lista_pares:
        #sacar la posicion
        posicion = lista_pares.index(escondidas[r1][c1])
        #verificar si la carta2 es par con carta1
        if escondidas[r2][c2] == lista_impares[posicion]:
            salida = Back.LIGHTYELLOW_EX + Fore.RED + "F E L I C I D A D E S! Encontraste un par!" + Fore.RESET + Back.RESET
            print(salida.center(105,"*"))
            gano = 1
        else:
            print('No es par!\n')
            #esconder no pares
            tablero[r1][c1] = '\U0001F48E' 
            tablero[r2][c2] = '\U0001F48E'
        
    elif escondidas[r1][c1] in lista_impares:
        posicion = lista_impares.index(escondidas[r1][c1])
        if escondidas[r2][c2] == lista_pares[posicion]:
            salida = Back.LIGHTYELLOW_EX + Fore.RED + "F E L I C I D A D E S! Encontraste un par!" + Fore.RESET + Back.RESET
            print(salida.center(105,"*"))
            gano = 1
        else:
            print('No es par!\n')
            #esconder no pares
            tablero[r1][c1] = '\U0001F48E' 
            tablero[r2][c2] = '\U0001F48E'


    return gano
    
    
def main():
    
  lista = pares()
  lista_pares = lista[ : :2]
  lista_impares = lista[1: :2] 

  
  # Llamamos a las funciones que llenan las matrices
  tablero = llena_tablero()
  escondidas = llena_escondida(lista)
  
  #iniciamos el número pares de cada jugador
  
  pares_j1 = 0
  pares_j2 = 0
  
  #ejecute mientras existan cartas, mientras quieras seguir jugando
  while pares_j1 + pares_j2 < 18 :
    limpia()
    despliega_matriz(escondidas)
    despliega_matriz(tablero)

    print('Escribe la posición de las 2 cartas que quieres destapar\n')
    
    ########## TIRO JUGADOR
    
    r1 = int(input('Ingresa Carta 1\nRenglon: '))
    c1 = int(input('Columna: '))
    r1,c1 = validar_carta(tablero,r1,c1)
    
    r2 = int(input('Ingresa Carta 2\nRenglon: '))
    c2 = int(input('Columna: '))
    r2,c2 = validar_carta(tablero,r1,c1,r2,c2)
    
    tablero[r1][c1] = escondidas[r1][c1]
    tablero[r2][c2] = escondidas[r2][c2]  
    limpia()
    despliega_matriz(tablero)
    
    pares_j1 = pares_j1 + verificar_pares(tablero,escondidas,lista_pares,lista_impares,r1,c1,r2,c2)

    
    print("Pares del jugador = ", pares_j1)
    print("Pares de la computadora = ", pares_j2)
    
    if pares_j1 + pares_j2 == 18:
        break
    ############   TIRO COMPUTADORA
    
    r1 = random.randint(1,6)
    c1 = random.randint(1,6)
    r1,c1 = validar_carta_compu(tablero,r1,c1)
    
    r2 = random.randint(1,6)
    c2 = random.randint(1,6)
    r2,c2 = validar_carta_compu(tablero,r1,c1,r2,c2)
    
    
    print(f"La computadora eligió carta:{[r1+1]},{[c1+1]}")
    print(f"La computadora eligió carta:{[r2+1]},{[c2+1]}")
    input('Enter para continuar')

    
    pares_j2 = pares_j2 + verificar_pares(tablero,escondidas,lista_pares,lista_impares,r1,c1,r2,c2)

    
    print("Pares del jugador = ", pares_j1)
    print("Pares de la computadora = ", pares_j2)
    print("Observa las cartas elegidas por la computadora\n\n")
    

    input('Enter para continuar')
    cont = input("Quieres continuar jugando? si = enter o no = n : ")
    if cont == "n":
        break
    limpia()
     # Se acaba el ciclo verifico el resultado
  limpia()
  despliega_matriz(tablero)
  if pares_j1 == pares_j2:
      salida = Back.LIGHTYELLOW_EX + Fore.RED + "E M P A T A M O S" + Fore.RESET + Back.RESET
      print(salida.center(105,"*"))
      mensaje = Back.LIGHTYELLOW_EX + Fore.RED + f"Obtuviste {pares_j1} pares" + Fore.RESET + Back.RESET
      mensaje2 = Back.LIGHTGREEN_EX + Fore.BLACK + f"La computadora obtuvo {pares_j2} pares" + Fore.RESET + Back.RESET
      print(mensaje.center(100))
      print(mensaje2.center(100))
      
  elif pares_j1 > pares_j2:
      salida = Back.BLUE + "G A N A S T E  F E L I C I D A D E S" + Back.RESET
      print(salida.center(95,"*"))
      mensaje = Back.LIGHTYELLOW_EX + Fore.RED + f"Obtuviste {pares_j1} pares" + Fore.RESET + Back.RESET
      mensaje2 = Back.LIGHTGREEN_EX + Fore.BLACK + f"La computadora obtuvo {pares_j2} pares" + Fore.RESET + Back.RESET
      print(mensaje.center(100))
      print(mensaje2.center(100))
      
  else:
      salida = Back.BLUE + "TE GANE, no dejes para mañana lo que puedes aprender hoy !" + Back.RESET
      print(salida.center(80,"*"))
      mensaje = Back.LIGHTYELLOW_EX + Fore.RED + f"Obtuviste {pares_j1} pares" + Fore.RESET + Back.RESET
      mensaje2 = Back.LIGHTGREEN_EX + Fore.BLACK + f"La computadora obtuvo {pares_j2} pares" + Fore.RESET + Back.RESET
      print(mensaje.center(100))
      print(mensaje2.center(100))
      
main()