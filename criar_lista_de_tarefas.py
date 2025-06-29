import os
import sys
import datetime as dt
from Lista_de_Tarefas import Lista_de_Tarefas

EH_WINDOWS = os.name == 'nt'

#Cores de texto
RED = "\033[3;0;41m"
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
WBLUE = "\033[1;44m"
WNEGRITO = "\033[0m"
WRESET = "\033[1m"
WWHITE = "\033[0;47m"
SUBLINHADO = "\033[3;30;47m"
SUBLINHADO_VERMELHO = "\033[3;30;47m"
FRACO =  "\033[0;30m"

def limpar():
        """ Limpa o terminal após cada print
            
            """
        os.system('cls' if EH_WINDOWS else 'clear')

if EH_WINDOWS: #Caso o sistema operacional seja windows, usamos esse codigo para capturar a tecla
    import msvcrt

    def tecla_apertada():
        """ Reconhece se o usuario aperta alguma tecla(nesse caso, as setas para navegar pelo menu)
        
        """
        key = msvcrt.getch()
        if key == b'\xe0':
            key = msvcrt.getch()
            if key == b'H': 
                return 'cima'
            elif key == b'P': 
                return 'baixo'
        elif key in [b'\r', b'\n']:
            return 'enter'
        return None
    
else: #Caso o sistema operacional seja linux ou macOS, usamos esse codigo para capturar a tecla
    import termios
    import tty

    def tecla_apertada():
        """ Reconhece se o usuario aperta alguma tecla(nesse caso, as setas para navegar pelo menu)
        
        """
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch1 = sys.stdin.read(1)
            if ch1 == '\x1b':
                ch2 = sys.stdin.read(1)
                ch3 = sys.stdin.read(1)
                if ch2 == '[':
                    if ch3 == 'A': return 'cima'
                    elif ch3 == 'B': return 'baixo'
            elif ch1 == '\r':
                return 'enter'
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return None
    

with open("Nomes_listas_tarefas.txt", "r", encoding="utf-8") as dados:
    procurar = dados.read()
    
def nome_lista():
  nome = input("Nome da lista: ")
  if nome not in procurar:
    nova_lista = Lista_de_Tarefas(id = "", titulo = nome, tarefas = "")
  else:
    print("Esse nome ja for escolhido, escolha outro")
    print()
    return nome_lista()
  with open("dados_listas_tarefas.txt", "a") as escrever:
    escrever.write(f"{nova_lista.id} {nova_lista.titulo}" )
  with open("Nomes_listas_tarefas.txt", "a") as escrever:
    escrever.write(nome)
  
def interface():
  print(NEGRITO + "="* 70 + RESET)
  print(WBLUE + " "* 20 + WBLUE + " Criar nova lista de tarefas " + WBLUE + " "* 21 + WNEGRITO )
  print(NEGRITO + "="* 70 + RESET)
  nome_lista()

interface()  

tarefas_disponiveis = []
with open("Nomes_tarefas.txt", "r") as dados: #Visualizar as tarefas no arquivo e adiciona-las a uma lista
    for lista in dados:
        tarefas_disponiveis.append(lista.strip())
opcao_tarefas = 0

def escolher_tarefa(): 
    print("Escolha a tarefa para adicionar a lista:")
    global tarefas_disponiveis  
    for i, item in enumerate(tarefas_disponiveis):
        if i == tarefas_disponiveis :
            print( " "* 2 + SUBLINHADO + " "* 1 + f"  {item}     " + RESET)
        else:

            print(f"    {item}" )

while True:
        escolher_tarefa()
        tecla = tecla_apertada()
        if tecla == 'cima':
            limpar()
            opcao_tarefas = (opcao_tarefas - 1) % len(opcao_tarefas)

        elif tecla == 'baixo':
            limpar()
            opcao_tarefas = (opcao_tarefas + 1) % len(opcao_tarefas)
            
        elif tecla == 'enter':
            tarefas_disponiveis[opcao_tarefas]
            limpar()
            break
