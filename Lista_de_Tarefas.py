from dataclasses import dataclass


class Lista_de_Tarefas():
  def __init__(self):
    self.id =  int
    self.titulo =  str
    self.tarefas =  list
  

  def carregar_ultimo_id(self):
    import os
    id_file = 'ultima_lista_id.txt'
    if os.path.exists(id_file):
        with open(id_file, 'r') as f:
            try: 
                return int(f.read().strip())
            except ValueError: 
                return 0
    return 0

  def salvar_ultimo_id(self, novo_id):
    id_file = 'ultima_lista_id.txt'
    with open(id_file, 'w') as f: f.write(str(novo_id))

  def gerar_proximo_id(self):
    ultimo_id = self.carregar_ultimo_id()
    novo_id = ultimo_id + 1
    self.salvar_ultimo_id(novo_id)
    return novo_id
  
  def loop_adicionar_tarefas(self):
    import padrao
    try:
        with open("Nomes_tarefas.txt", "r", encoding="utf-8") as f:
            tarefas_disponiveis = [linha.strip() for linha in f.readlines()]
    except FileNotFoundError:
        print("\nArquivo 'Nomes_tarefas.txt' não encontrado. Nenhuma tarefa para adicionar.")
        input("Pressione Enter para continuar...")
        return []

    if not tarefas_disponiveis:
        print("\nNão há tarefas existentes para adicionar.")
        input("Pressione Enter para continuar...")
        return []

    tarefas_adicionadas = []
    while True:
        padrao.limpar()
        print(padrao.NEGRITO+"="*90+padrao.RESET ) 
        print(padrao.WBLUE  + f"{"--- Adicionar Tarefas à Lista ---":^90}"+ padrao.RESET)
        print(padrao.NEGRITO+"="*90+padrao.RESET ) 
        
        print("\nTarefas Disponíveis:")
        for i, tarefa in enumerate(tarefas_disponiveis):
            print(f"  {i + 1}: {tarefa}")
        
        print("\nTarefas já adicionadas a esta lista:")
        if not tarefas_adicionadas:
            print("  (Nenhuma)")
        else:
            for tarefa in tarefas_adicionadas:
                print(f"  - {tarefa}")
        print(padrao.NEGRITO + "-" * 90 + padrao.RESET)

        escolha = input("Digite o NÚMERO da tarefa para adicionar (ou 's' para sair): ")

        if escolha.lower() == 's':
            break

        try:
            indice = int(escolha) - 1
            if 0 <= indice < len(tarefas_disponiveis):
                tarefa_escolhida = tarefas_disponiveis[indice]
                if tarefa_escolhida not in tarefas_adicionadas:
                    tarefas_adicionadas.append(tarefa_escolhida)
                    print(f"'{tarefa_escolhida}' adicionada.")
                else:
                    print("Essa tarefa já foi adicionada.")
                input("Pressione Enter para continuar...")
            else:
                print("Número inválido.")
                input("Pressione Enter para continuar...")
        except ValueError:
            print("Entrada inválida. Digite um número ou 's'.")
            input("Pressione Enter para continuar...")
    
    return tarefas_adicionadas

  def funcao_criar_lista(self):
    import padrao
    padrao.limpar()
    print(padrao.NEGRITO+"="*90+padrao.RESET ) 
    print(padrao.WBLUE  + f"{"--- CRIAR NOVA LISTA ---":^90}"+ padrao.RESET)
    print(padrao.NEGRITO+"="*90+padrao.RESET ) 
    
    
    nome = input("Digite o nome da nova lista: ")

    if not nome:
        print("\nO nome não pode ser vazio."); input("Pressione Enter..."); 
        return
    
    id_gerado = self.gerar_proximo_id()

    tarefas_da_lista = self.loop_adicionar_tarefas()
    string_tarefas = ", ".join(tarefas_da_lista)
    linha_para_salvar = f"{id_gerado} {nome} | {string_tarefas}\n"

    with open("dados_listas_tarefas.txt", "a", encoding='utf-8') as f:
        f.write(linha_para_salvar)
    with open("Nomes_listas_tarefas.txt", "a", encoding='utf-8') as f:
        f.write(f"{nome}\n")

    print(f"\nLista '{nome}' criada com sucesso!")
    input("Pressione Enter para continuar...")
    
    
  def funcao_remover_lista(self):
    import padrao
    padrao.limpar()
    print(padrao.NEGRITO+"="*90+padrao.RESET ) 
    print(padrao.WBLUE  + f"{"--- REMOVER LISTA DE TAREFAS ---":^90}"+ padrao.RESET)
    print(padrao.NEGRITO+"="*90+padrao.RESET )   
    try:
        with open("dados_listas_tarefas.txt", "r", encoding='utf-8') as f:
            listas = f.readlines()
    except FileNotFoundError:
        listas = []

    if not listas:
        print("\nNenhuma lista para remover."); input("Pressione Enter..."); 
        return
        
    print("Listas atuais:")
    for linha in listas: print(f"  - {linha.strip().split(' | ')[0]}")
    print("-" * 90)

    id_para_remover = input("Digite o ID da lista a remover, uma por vez (ou 's' para sair): ")
    if id_para_remover.lower() == 's' or not id_para_remover.isdigit(): 
        return

    nome_removido = None
    listas_atualizadas = []
    for linha in listas:
        if linha.strip().startswith(id_para_remover + ' '):
            nome_removido = linha.strip().split(' | ')[0].split(' ', 1)[1]
        else:
            listas_atualizadas.append(linha)
    
    if nome_removido is None:
        print("\nID não encontrado.")
    else:
        with open("dados_listas_tarefas.txt", "w", encoding='utf-8') as f:
            f.writelines(listas_atualizadas)

        try:
            with open("Nomes_listas_tarefas.txt", "r", encoding="utf-8") as f:
                nomes = f.readlines()
            nomes_atualizados = [nome for nome in nomes if nome.strip() != nome_removido]
            with open("Nomes_listas_tarefas.txt", "w", encoding="utf-8") as f:
                f.writelines(nomes_atualizados)
        except FileNotFoundError:
            pass
            
        print("\nLista removida com sucesso.")
        
    input("Pressione Enter para continuar...")
  