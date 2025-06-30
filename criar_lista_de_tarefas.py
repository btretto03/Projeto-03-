import os
import sys
import datetime as dt
from Lista_de_Tarefas import Lista_de_Tarefas
import padrao
  

with open("Nomes_listas_tarefas.txt", "r", encoding="utf-8") as dados:
    procurar = dados.read()


id_file = 'ultima_lista_id.txt'
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

    
def nome_lista():
  nome = input("Nome da lista: ")
  if nome not in procurar:
    nova_lista = Lista_de_Tarefas(id = id, titulo = nome, tarefas = "")
  else:
    print("Esse nome ja foi escolhido, escolha outro")
    print()
    return nome_lista()
  with open("dados_listas_tarefas.txt", "a") as escrever:
    escrever.write(f"{nova_lista.id} {nova_lista.titulo}" )
  with open("Nomes_listas_tarefas.txt", "a") as escrever:
    escrever.write(nome)
  
def interface():
  print(padrao.NEGRITO + "="* 70 + padrao.RESET)
  print(padrao.WBLUE + " "* 20 + padrao.WBLUE + " Criar nova lista de tarefas " + padrao.WBLUE + " "* 21 + padrao.WNEGRITO )
  print(padrao.NEGRITO + "="* 70 + padrao.RESET)
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
            print( " "* 2 + padrao.SUBLINHADO + " "* 1 + f"  {item}     " + padrao.RESET)
        else:

            print(f"    {item}" )

while True:
        escolher_tarefa()
        tecla = padrao.tecla_apertada()
        if tecla == 'cima':
            padrao.limpar()
            opcao_tarefas = (opcao_tarefas - 1) % len(tarefas_disponiveis)

        elif tecla == 'baixo':
            padrao.limpar()
            opcao_tarefas = (opcao_tarefas + 1) % len(tarefas_disponiveis)
            
        elif tecla == 'enter':
            tarefas_disponiveis[opcao_tarefas]
            padrao.limpar()
            break

  
  
    
        








