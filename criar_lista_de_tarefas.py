import os
import padrao
from Lista_de_Tarefas import Lista_de_Tarefas

lista_tarefas = Lista_de_Tarefas()


def funcao_ver_listas():
    padrao.limpar()
    print(padrao.NEGRITO+"="*90+padrao.RESET )
    print(padrao.WBLUE  + f"{"--- LISTAS DE TAREFAS EXISTENTES ---":^90}"+ padrao.RESET)
    print(padrao.NEGRITO+"="*90+padrao.RESET )    

    
    try:
        with open("dados_listas_tarefas.txt", "r", encoding='utf-8') as f:
            listas = f.readlines()
        if not listas:
            print("\nNenhuma lista foi criada ainda.")
        else:
            for linha in listas:
                partes = linha.strip().split(' | ')
                info_lista = partes[0]
                tarefas = partes[1] if len(partes) > 1 and partes[1] else "Nenhuma tarefa associada."
                
                print(padrao.NEGRITO + f"Lista: {info_lista}" + padrao.RESET)
                print(f"  Tarefas: {tarefas}")
                print(padrao.NEGRITO + "-" * 90)
    except FileNotFoundError:
        print("\nNenhuma lista foi criada ainda.")
    input("\nPressione Enter para voltar...")



def menu_principal_listas():
    opcoes = ["Criar nova lista (Certifique-se que todas tarefas para sua lista já estão criadas)", "Ver listas existentes", "Remover lista", "Voltar ao Menu Principal"]
    opcao_atual = 0
    while True:
        padrao.limpar()
        print(padrao.NEGRITO+"="*90+padrao.RESET )
        print(padrao.WBLUE  + f"{"--- GERENCIAR LISTAS DE TAREFAS ---":^90}"+ padrao.RESET)
        print(padrao.NEGRITO+"="*90+padrao.RESET )  
        print()
        for i, item in enumerate(opcoes):
            if i == opcao_atual: print("  " + padrao.SUBLINHADO + f"  {item}  " + padrao.RESET)
            else: print(f"  {item}")
        print()
        print(padrao.NEGRITO+"="*90+padrao.RESET ) 
        tecla = padrao.tecla_apertada()
        if tecla == 'cima': opcao_atual = (opcao_atual - 1) % len(opcoes)
        elif tecla == 'baixo': opcao_atual = (opcao_atual + 1) % len(opcoes)
        elif tecla == 'enter':
            if opcao_atual == 0: 
                lista_tarefas.funcao_criar_lista()
            elif opcao_atual == 1: 
                funcao_ver_listas()
            elif opcao_atual == 2: 
                lista_tarefas.funcao_remover_lista()
            elif opcao_atual == 3: 
                break
        

menu_principal_listas()