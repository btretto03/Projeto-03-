import os
import sys
from Tarefa import Tarefa
import padrao

  
nova_lista = [] 
with open("dados_tarefas.txt", "r", encoding='utf-8') as dados: #Visualizar as tarefas no arquivo e adiciona-las a uma lista
    for lista in dados:
        nova_lista.append(lista.strip())

padrao.limpar()
def desenhar_layout():

    while True:
        if len(nova_lista) == 0:
            print("Nenhuma tarefa adicionada")
            sair = input("Pressione qualquer tecla para sair \n")
            break
        else:

            
            print(padrao.NEGRITO+"="*114+padrao.RESET )
            print(f"{"        Tarefas":25} | {"       Tag":20} | {"    Prioridade":20} | {"     Data":20} | {"     Concluida"} ")
            print(padrao.NEGRITO+"-"*114+padrao.RESET )
            print(f"     {"":20} | {"":20} | {"":20} | {"":20} | {"":20} ")
            for i in range(len(nova_lista)):
                print(i, nova_lista[i])
                print(f"     {"":20} | {"":20} | {"":20} | {"":20} | {"":20} ")
                print(padrao.NEGRITO+"-"*114+padrao.RESET )
            sair = input("Aperte qualquer tecla para sair\n")
            break
            
desenhar_layout()


