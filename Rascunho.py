import datetime as dt
import random

def interface2():

  dict = {}
  dict[1] = "\033[1m 1. \033[mCriar nova tarefa"
  dict[2] = "\033[1m 2. \033[mModificar tarefas"
  dict[3] = "\033[1m 3. \033[mVisualizar tarefas"



lista_de_tarefas = []
dicionario_tarefas = {}  
  
def criador_de_id(tarefa):
  '''Cria um id para a titulo da tarefa e associa ambos em um dicionario
  
  '''
  lista_id = []
  lista_de_tarefas.append(tarefa)
  for i in range(10): #gera um id de 10 digitos aleatorio
    id = random.randint(1, 10)
    lista_id.append(id)
  lista_id = map(str, lista_id) 
  lista_id = list(lista_id)
  dicionario_tarefas[tarefa] = int("".join(lista_id))
  



lista = ["leo", "dias"]
num = enumerate(lista)
print(num)

import datetime as dt
import time
import os
import curses

#Cores de texto
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
WHITE = "\033[0;37m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

#Cores de fundo
WRED = "\033[0;41m"
WGREEN = "\033[0;42m"
WYELLOW = "\033[0;43m"
WBLUE = "\033[0;44m"
WNEGRITO = "\033[0m"
WRESET = "\033[1m"
WWHITE = "\033[0;47m"

  
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def interface():
  """Exibe uma interface interativa que da três opções ao usuario
  
  """
  print(NEGRITO + BLUE + "1." + RESET, "Criar nova tarefa")
  print(NEGRITO + BLUE + "2." + RESET, "Modificar tarefas")
  print(NEGRITO + BLUE + "3." + RESET, "Visualizar tarefas")
  print()
  print(NEGRITO + "="* 51)
  
def relogio():
  """Mostra o dia e a hora em tempo real
  
  """
  while True:
    limpar_terminal()
    dia = dt.date.today()           
    dia_formatado = dia.strftime("%d/%m/%Y")
    hora = dt.datetime.now()
    hora_formatada = hora.strftime("%H:%M:%S")
    print(NEGRITO + "="* 51) #Barra superior
    print("\033[1;44;97m{:^51}\033[0m".format(" MENU PRINCIPAL")) #Titulo do menu
    print(NEGRITO + "="* 51) #Barras inferior
    print(
           GREEN
          + f" {' '*30} {dia_formatado} {hora_formatada}"
          + RESET, 
          end = "",
    )
    print()
    interface()
    time.sleep(1)


  
relogio()


  

  


  
  
  


  
    
    
    