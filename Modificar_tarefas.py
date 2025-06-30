import os
import sys
from Tarefa import Tarefa
import padrao


def menu_filtro():
    padrao.limpar()
    opcoes = ["Todas as Tarefas", "Tarefas Pendentes", "Tarefas Concluídas", "Sair para Menu Principal"]
    opcao_atual = 0
    while True:
        padrao.limpar()
        print("Como você deseja listar as tarefas?")
        for i, item in enumerate(opcoes):
            if i == opcao_atual:
                print("  " + padrao.SUBLINHADO + f"  {item}  " + padrao.RESET)
            else:
                print(f"    {item}")
        tecla = padrao.tecla_apertada()
        if tecla == 'cima':
            opcao_atual = (opcao_atual - 1) % len(opcoes)
        elif tecla == 'baixo':
            opcao_atual = (opcao_atual + 1) % len(opcoes)
        elif tecla == 'enter':
            return opcoes[opcao_atual]
        
def menu_gerenciar_acao(tarefa_selecionada):
    padrao.limpar()
    opcoes = ["Modificar Tarefa", "Marcar como Concluída", "Excluir Tarefa", "Cancelar"]
    opcao_atual = 0
    while True:
        padrao.limpar()
        print("Gerenciando a Tarefa:")
        print(f"-> {tarefa_selecionada}\n")
        print("Escolha uma ação:")
        for i, item in enumerate(opcoes):
            if i == opcao_atual:
                print("  " + padrao.SUBLINHADO + f"  {item}  " + padrao.RESET)
            else:
                print(f"    {item}")
        
        tecla = padrao.tecla_apertada()
        if tecla == 'cima':
            opcao_atual = (opcao_atual - 1) % len(opcoes)
        elif tecla == 'baixo':
            opcao_atual = (opcao_atual + 1) % len(opcoes)
        elif tecla == 'enter':
            return opcoes[opcao_atual]

def menu_modificar_atributo(tarefa_selecionada):
    padrao.limpar()
    opcoes = ["Título","Tag", "Prioridade", "Data", "Cancelar"]
    opcao_atual = 0
    while True:
        padrao.limpar()
        print("Modificando a Tarefa:")
        print(f"-> {tarefa_selecionada}\n")
        print("Qual atributo você deseja modificar?")
        for i, item in enumerate(opcoes):
            if i == opcao_atual:
                print("  " + padrao.SUBLINHADO + f"  {item}  " + padrao.RESET)
            else:
                print(f"    {item}")
        tecla = padrao.tecla_apertada()
        if tecla == 'cima':
            opcao_atual = (opcao_atual - 1) % len(opcoes)
        elif tecla == 'baixo':
            opcao_atual = (opcao_atual + 1) % len(opcoes)
        elif tecla == 'enter':
            return opcoes[opcao_atual]

def desenhar_layout(filtro):
    padrao.limpar()
    todas_as_tarefas = [] 
    try:
        with open("dados_tarefas.txt", "r", encoding='utf-8') as dados:
            for lista in dados:
                todas_as_tarefas.append(lista.strip())
    except FileNotFoundError:
        print("Nenhuma tarefa adicionada ainda.")
        input("Pressione qualquer tecla para sair \n")
        return "s", None
    
    lista_filtrada = []
    if filtro == "Tarefas Pendentes":
        for tarefa in todas_as_tarefas:
            if "Não concluida" in tarefa:
                lista_filtrada.append(tarefa)
    elif filtro == "Tarefas Concluídas":
        for tarefa in todas_as_tarefas:
            if "Concluida" in tarefa and "Não concluida" not in tarefa:
                lista_filtrada.append(tarefa)
    else:
        lista_filtrada = todas_as_tarefas

    if len(lista_filtrada) == 0:
        print(f"Nenhuma tarefa encontrada para o filtro: '{filtro}'")
        input("Pressione qualquer tecla para continuar...")
        return None, None
    else:
        print(padrao.NEGRITO+"="*114+padrao.RESET )
        print(f"Mostrando: {filtro}")
        print(padrao.NEGRITO+"-"*114+padrao.RESET )
        print(f"{"         Tarefas":25} | {"         Tag":20} | {"      Prioridade":20} | {"        Data":20} | {"      Concluida"} ")
        print(padrao.NEGRITO+"-"*114+padrao.RESET )
        for i in range(len(lista_filtrada)):
            print(f"{i+1}. {lista_filtrada[i]}")
            print(padrao.NEGRITO+"-"*114+padrao.RESET )
        modificar = input("Digite o numero da tarefa que deseja gerenciar. Para voltar digite s\n")
        return modificar, lista_filtrada

sim = True
while sim:
    filtro_escolhido = menu_filtro()
    if filtro_escolhido == "Sair para Menu Principal":
        sim = False
        break
    modificar, lista_de_tarefas_filtrada = desenhar_layout(filtro=filtro_escolhido)
    if modificar is None:
        continue
    if modificar.lower() == "s":
        continue
    try:
        indice_escolhido = int(modificar) - 1
        if not (0 <= indice_escolhido < len(lista_de_tarefas_filtrada)):
            print("\nNúmero da tarefa inválido.")
            input("Pressione Enter para tentar novamente...")
            continue
        
        tarefa_escolhida_str = lista_de_tarefas_filtrada[indice_escolhido]
        acao = menu_gerenciar_acao(tarefa_escolhida_str)

        if acao == "Cancelar":
            continue

        linhas_originais = []
        with open("dados_tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linhas_originais.append(linha.strip())

        indice_real_no_arquivo = linhas_originais.index(tarefa_escolhida_str)

        if acao == "Marcar como Concluída":
            partes_tarefa = linhas_originais[indice_real_no_arquivo].split('|')
            partes_tarefa[4] = f' {"Concluida":<20} '
            linhas_originais[indice_real_no_arquivo] = '|'.join(partes_tarefa)
        
        elif acao == "Excluir Tarefa":
            del linhas_originais[indice_real_no_arquivo]

        elif acao == "Modificar Tarefa":
            atributo_a_modificar = menu_modificar_atributo(tarefa_escolhida_str)

            if atributo_a_modificar == "Cancelar":
                continue

            partes_tarefa = linhas_originais[indice_real_no_arquivo].split('|')
            tarefa_para_modificar = Tarefa() 

            if atributo_a_modificar == "Título":
                novo_titulo = tarefa_para_modificar.escolher_titulo()
                partes_tarefa[0] = f' {novo_titulo:20} '
            elif atributo_a_modificar == "Tag":
                nova_tag = tarefa_para_modificar.escolher_tag()
                partes_tarefa[1] = f' {nova_tag:20} '
            elif atributo_a_modificar == "Prioridade":
                nova_prioridade = tarefa_para_modificar.escolher_prioridades()
                partes_tarefa[2] = f' {nova_prioridade:20} '
            elif atributo_a_modificar == "Data":
                nova_data = tarefa_para_modificar.escolher_data()
                partes_tarefa[3] = f' {nova_data:20} '
            
            linhas_originais[indice_real_no_arquivo] = '|'.join(partes_tarefa)

        with open("dados_tarefas.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas_originais:
                arquivo.write(linha + "\n")
        
    except (ValueError, TypeError):
        print("\nEntrada inválida. Por favor, digite um número válido.")
        input("Pressione Enter para tentar novamente...")