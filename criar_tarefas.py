import os
import sys
import re
import padrao
from datetime import datetime
from Tarefa import Tarefa

lista_titulos = []
lista_tags = []
lista_prioridades = []
lista_repeticao = []
lista_data = []
lista_geral = []


if __name__ == "__main__":

    def menu_criar(titulo = "", descricao = '', tags = "",prioridade = "",repetição = "",data = ""):
        ''' Menu para criar novas tarefas
        
        '''
        print(padrao.NEGRITO+"="*42+padrao.RESET )
        print(padrao.WBLUE + f"{"Criar tarefa":^42}" + padrao.RESET)
        print(padrao.NEGRITO+"="*42+padrao.RESET )
        print(f"| Título:{titulo:32}|")
        print("-"*42)
        print(f"| Descrição:{descricao:29}|")    
        print("-"*42)
        print(f"| Tags: {tags:33}|")
        print("-"*42)
        print(f"| Prioridade: {prioridade:27}|")
        print("-"*42)
        print(f"| Repetição: {repetição:28}|")
        print("-"*42)
        print(f"| Data: {data:33}|")
        print(padrao.NEGRITO+ ("-"*42) + padrao.RESET)
        print()
        

    # Inicial
    titulo = ""
    descricao = ''
    tags = ""
    prioridade = ""
    repetição = ""
    data = ""
    

    menu_criar(titulo, descricao , tags, prioridade, repetição, data)

    # Input Nome
    def escolher_titulo():
        titulo = input("Titulo: ")
        padrao.limpar()
        return titulo
    titulo = escolher_titulo()
    menu_criar(titulo = titulo, descricao = '' ,tags = "",prioridade = "",repetição = "",data = "")

    
    
    id_file = 'ultima_tarefa_id.txt'

    def carregar_ultimo_id():
        '''Carrega o id da ultima tarefa'''
        if os.path.exists(id_file):
            with open(id_file, 'r') as f:
                try:
                    return int(f.read().strip())
                
                # se o arquivo estiver vazio começa do 0
                except ValueError:
                    return 0
    
    def salvar_ultimo_id(novo_id):
        '''Salva o ID númerico atual no arquivo'''
        with open(id_file, 'w') as f:
            f.write(str(novo_id))

    def gerar_proximo_id():
        '''
        Gera o próximo id sequencial como um inteiro
        '''
        ultimo_id = carregar_ultimo_id()
        novo_id = ultimo_id + 1
        salvar_ultimo_id(novo_id)
        return novo_id
    
    id = gerar_proximo_id()

    def criar_descricao():
        '''Possibilita ao usuario dar uma descrição para sua tarefa'''
        descricao = input('Descrição: ')


        while len(descricao) > 38:
            print('Sua descrição é muito grande, favor alterar')
            descricao = input('Descrição: ')
        padrao.limpar()
        return descricao  
    
    descricao = criar_descricao()
    menu_criar(titulo = titulo, descricao = descricao ,tags = "",prioridade = "",repetição = "",data = "")  

    
    # Input tags

    tags = []
    with open("dados_tag.txt", "r") as dados: #Visualizar as tarefas no arquivo e adiciona-las a uma lista
        for lista in dados:
            tags.append(lista.strip())

    opcao_tags = 0
    def escolher_tag(): 
        print("Escolha a tag:")
        global opcao_tags  
        for i, item in enumerate(tags):
            if i == opcao_tags :
                print( " "* 2 + padrao.SUBLINHADO + " "* 1 + f"  {item}     " + padrao.RESET)
            else:
                print(f"    {item}" )
        
    while True:  
            escolher_tag()
            tecla = padrao.tecla_apertada()
            if tecla == 'cima':
                padrao.limpar()
                menu_criar(titulo = titulo,tags = "",prioridade = "",repetição = "",data = "")
                opcao_tags = (opcao_tags - 1) % len(tags)
            elif tecla == 'baixo':
                padrao.limpar()
                menu_criar(titulo = titulo,tags = "",prioridade = "",repetição = "",data = "")
                opcao_tags = (opcao_tags + 1) % len(tags)
            elif tecla == 'enter':
                tags = tags[opcao_tags]
                padrao.limpar()
                break      
    menu_criar(titulo, descricao, tags, prioridade, repetição, data)


    # Input prioridade
    prioridades = ["Baixa", "Media", "Alta"]
    opcao_prioridades = 0
    def escolher_prioridades(): 
        print("Defina a prioridade:")
        global opcao_prioridades  
        for i, item in enumerate(prioridades):
            if i == opcao_prioridades :
                print( " "* 2 + padrao.SUBLINHADO + " "* 1 + f"  {item}     " + padrao.RESET)
            else:

                print(f"    {item}" )

    while True:
            escolher_prioridades()
            tecla = padrao.tecla_apertada()
            if tecla == 'cima':
                padrao.limpar()
                opcao_prioridades = (opcao_prioridades - 1) % len(prioridades)
                menu_criar(titulo = titulo,tags = tags,prioridade = "",repetição = "",data = "")
            elif tecla == 'baixo':
                padrao.limpar()
                opcao_prioridades = (opcao_prioridades + 1) % len(prioridades)
                menu_criar(titulo = titulo,tags = tags,prioridade = "",repetição = "",data = "")
            elif tecla == 'enter':
                prioridade = prioridades[opcao_prioridades]
                padrao.limpar()
                break
    menu_criar(titulo, descricao, tags, prioridade, repetição, data)


    # Input repeticao
    repeticao = ["Nenhuma","Diária", "Semanal","Mensal","Anual"]
    opcao_repeticao = 0
    def escolher_repeticao(): 
        print("Escolha a frêquencia:")
        global opcao_repeticao  
        for i, item in enumerate(repeticao):
            if i == opcao_repeticao :
                print( " "* 2 + padrao.SUBLINHADO + " "* 1 + f"  {item}     " + padrao.RESET)
            else:
                print(f"    {item}" )

    while True:
            escolher_repeticao()
            tecla = padrao.tecla_apertada()
            if tecla == 'cima':
                padrao.limpar()
                opcao_repeticao = (opcao_repeticao - 1) % len(repeticao)
                menu_criar(titulo = titulo,tags = tags,prioridade = prioridade,repetição = "",data = "")
            elif tecla == 'baixo':
                padrao.limpar()
                opcao_repeticao = (opcao_repeticao + 1) % len(repeticao)
                menu_criar(titulo = titulo,tags = tags,prioridade = prioridade,repetição = "",data = "")
            elif tecla == 'enter':
                repetição = repeticao[opcao_repeticao]
                padrao.limpar()
                break
    menu_criar(titulo, descricao, tags, prioridade, repetição, data)

   
    def escolher_data():
        '''
        Solicita uma data para o usuário no formato dd/mm/aaaa
        Continua pedindo até que seja inserida no formato válido
        '''
        while True:
            data = input('data (dd/mm/aaaa): ')
            padrao.limpar()


             # permite a entrada vazia
            if not data.strip():
                return ''

            
            #Verifica o formato dd/mm/aaaa
            if re.match(r'^\d{2}\/\d{2}\/\d{4}$', data):
                
                # Verifica se a data é real
                try:
                    datetime.strptime(data, '%d/%m/%Y')

                    return data
                except ValueError:
                    print('Data inválida. Por favor, insira uma data real no formato dd/mm/aaaa.')
            else:
                print('Formato Inválido. Por favor, insira a data no formato dd/mm/aaaa.')
                print('Exemplo: 01/01/2025')

    data = escolher_data()
    menu_criar(titulo, descricao, tags, prioridade, repetição, data)
    
    nova_tarefa = Tarefa(titulo = titulo, id=id,descricao = descricao, tags = tags, prioridade = prioridade, repetição = repetição, data = data)
    
    lista_titulos.append(nova_tarefa.titulo)
    lista_tags.append(nova_tarefa.tags)
    lista_prioridades.append(nova_tarefa.prioridade)
    lista_repeticao.append(nova_tarefa.repetição)
    lista_data.append(nova_tarefa.data)
    
    lista_geral.append(lista_titulos)
    lista_geral.append(lista_tags)
    lista_geral.append(lista_prioridades)
    lista_geral.append(lista_repeticao)
    lista_geral.append(lista_data)
    
    with open("dados_tarefas.txt", "a", encoding = 'utf-8') as escrever:
        escrever.write(f"-  {titulo:20} | {tags:20} | {prioridade:20} | {data:20} | {"Não concluida":20} " "\n")
    with open("Nomes_tarefas.txt", "a", encoding = 'utf-8') as escrever:
        escrever.write(f"{titulo} - {id}" "\n")
            