import os
import sys
from Tarefa import Tarefa

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

EH_WINDOWS = os.name == 'nt'

def limpar():
    """ Limpa o terminal após cada print
        
        """
    os.system('cls' if EH_WINDOWS else 'clear')

  
nova_lista = [] 
with open("dados_tarefas.txt", "r") as dados: #Visualizar as tarefas no arquivo e adiciona-las a uma lista
    for lista in dados:
        nova_lista.append(lista.strip())

limpar()
def desenhar_layout():

    while True:
        if len(nova_lista) == 0:
            print("Nenhuma tarefa adicionada")
            sair = input("Pressione qualquer tecla para sair \n")
            break
        else:
            print(NEGRITO+"="*114+RESET )
            print(f"{"        Tarefas":25} | {"       Tag":20} | {"    Prioridade":20} | {"     Data":20} | {"     Concluida"} ")
            print(NEGRITO+"-"*114+RESET )
            print(f"     {"":20} | {"":20} | {"":20} | {"":20} | {"":20} ")
            for i in range(len(nova_lista)):
                print(i, nova_lista[i])
                print(f"     {"":20} | {"":20} | {"":20} | {"":20} | {"":20} ")
                print(NEGRITO+"-"*114+RESET )
            sair = input("Aperte qualquer tecla para sair\n")
            break
desenhar_layout()


