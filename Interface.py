import os
import sys
import datetime as dt
import padrao


a = True

    
while a:
    opcoes_do_menu = ["Criar nova lista de tarefas", "Criar nova tarefa","Criar nova Tag", "Modificar tarefas", "Visualizar tarefas", "Sair"]
    opcao = 0

    
    
    def mostrar_menu():
        '''Interface principal
        
        '''
        
        padrao.limpar()
        largura = 40
        print(padrao.NEGRITO + "="* 57 + padrao.RESET)
        print(padrao.WBLUE + " "* 20 + padrao.WBLUE + " MENU PRINCIPAL " + padrao.WBLUE + " "* 21 + padrao.WNEGRITO )
        print(padrao.NEGRITO + "="* 57 + padrao.RESET)
        dia = dt.date.today()           
        dia_formatado = dia.strftime("%d/%m/%Y")
        print(
            padrao.GREEN
            + f" {' '*43} |{dia_formatado}|"
            + padrao.WNEGRITO
            + padrao.RESET 
    )
        for i, item in enumerate(opcoes_do_menu):
            if i == opcao and opcao != 3:
                print( " "* 2 + padrao.SUBLINHADO + " "* 3 + f"  {item}     " + padrao.RESET)
            elif i == opcao and opcao == 3:
                print( " "* 2 + padrao.SUBLINHADO_VERMELHO + " "* 3 + f"  {item}     " + padrao.RESET)

            else:
                print(f"    {item}" )
        print()
        print(padrao.NEGRITO + "="* 57 + padrao.RESET)
    

    while True:
        mostrar_menu()
        tecla = padrao.tecla_apertada()
        if tecla == 'cima':
            opcao = (opcao - 1) % len(opcoes_do_menu)
            if opcao == -1:
                opcao = 5
                continue
        elif tecla == 'baixo':
            opcao = (opcao + 1) % len(opcoes_do_menu)
            if opcao == 6:
                opcao = 0
                continue
        elif tecla == 'enter':
            padrao.limpar()
            if "Criar nova lista de tarefas" in opcoes_do_menu[opcao]:
                while True:
                    exec(open("criar_lista_de_tarefas.py", encoding='utf-8').read())
                    
            elif "Criar nova tarefa" in opcoes_do_menu[opcao]:
                exec(open("criar_tarefas.py", encoding='utf-8').read())
            elif "Modificar tarefas" in opcoes_do_menu[opcao]:
                exec(open("Modificar_tarefas.py",encoding='utf-8').read())
            elif "Visualizar tarefas" in opcoes_do_menu[opcao]:
                exec(open("Visualisar_tarefas.py",encoding='utf-8').read())
            elif "Criar nova Tag" in opcoes_do_menu[opcao]:
                exec(open("Criar_nova_Tag.py",encoding='utf-8').read())
            
                    
            elif "Sair" in opcoes_do_menu[opcao]:
                input("\nPressione Enter para sair...")
                if tecla == 'enter':
                    a = False
                    break