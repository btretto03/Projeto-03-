import os
import sys
from Tarefa import Tarefa
import padrao
from datetime import datetime, timedelta, date
import re



lista_dados = []
with open("dados_tarefas.txt", "r", encoding='utf-8') as dados: #Visualizar as tarefas no arquivo e adiciona-las a uma lista
    for tarefa in dados:
        partes = [parte.strip() for parte in tarefa.split('|')]
        dicionario_dados ={
            'nome': partes[0],
            'tag': partes[1],
            'prioridade': partes[2] if partes[2] else 'Não informada',
            'data': partes[3] if partes[3] else 'Não informada',
            
            'concluida': partes[5]
        }
        
        lista_dados.append(dicionario_dados)

lista_lista_tarefas = []
with open("dados_listas_tarefas.txt", "r", encoding='utf-8') as dados_listas_tarefas:
    for lista in dados_listas_tarefas:

        partes = lista.split("|")
        nome_lista_bruto = partes[0].strip()
        match = re.match(r'^\d+\s*(.*)', nome_lista_bruto)
        
        if match:
            nome_lista = match.group(1).strip() 
        else:
            nome_lista = nome_lista_bruto


        nomes_dicionario = {}
        if len(partes) > 1:
            itens_str = partes[1].strip()
            pares_itens = itens_str.split(',')
            for par in pares_itens:
                sub_partes = par.strip().split('-')
                nome = sub_partes[0].strip()
                valor = int(sub_partes[1].strip())
                if nome:
                    nomes_dicionario[nome] = valor
        lista_tarefa = {
            'nome_lista': nome_lista,
            'nomes_tarefas': nomes_dicionario
        }
        lista_lista_tarefas.append(lista_tarefa)
        
def filtrar_tarefas_lista(lista_dados, lista_lista_tarefas, i):

    tarefas_na_lista = []
    with open("dados_tarefas.txt", "r", encoding='utf-8') as dados: #Visualizar as tarefas no arquivo e adiciona-las a uma lista
        for tarefa in dados:
         partes = [parte.strip() for parte in tarefa.split('|')]


    for tarefa in lista_dados:

        for valor in lista_lista_tarefas[i]['nomes_tarefas'].values():
            if int(partes[4]) == (valor):
                tarefas_na_lista.append(tarefa)

    return tarefas_na_lista

lista_tags = []
with open("dados_tag.txt", "r", encoding='utf-8') as dados_tag:
    for tag in dados_tag:
        lista_tags.append(tag.strip())

def filtrar_tarefas_tag(lista_dados, lista_tags, i):
    '''
    Recebe a lista de tarefas e filtra quais possuem uma tag especifica
    '''
    tarefas_com_tag = []
    for tarefa in lista_dados:
        if tarefa['tag'] == lista_tags[i]:
            tarefas_com_tag.append(tarefa)
    return tarefas_com_tag





def filtrar_tarefas_nao_concluidas(lista_dados):
    '''Recebe a lista de tarefas e
    filtra apenas aquelas que ainda nao foram concluidas
    '''
    tarefas_nao_concluidas = []
    for tarefa in lista_dados:
        if tarefa['concluida'] != 'Concluida':
            tarefas_nao_concluidas.append(tarefa)
    return tarefas_nao_concluidas

def filtrar_tarefas_ate_hoje(lista_dados):
    '''Recebe a lista de tarefas e
    filtra apenas aquelas em que a data limite é no máximo hoje
    '''
    tarefas_ate_hoje = []
    hoje = date.today()

    for tarefa in lista_dados:
        data_str = tarefa.get('data')

        try:
            data_tarefa = datetime.strptime(data_str, "%d/%m/%Y").date()
            if data_tarefa <= hoje:
                    tarefas_ate_hoje.append(tarefa)
        except ValueError:
            pass

    return tarefas_ate_hoje

def filtrar_data_ate_7_dias(lista_dados,):
    '''Recebe a lista de tarefas e
    filtra apenas aquelas em que a data limite é no máximo em 7 dias
    '''



    tarefas_ate_7_dias = []
    hoje = date.today()
    data_limite = hoje + timedelta(days=7)

    for tarefa in lista_dados:
        data_str = tarefa.get("data")

        try:
            data_tarefa = datetime.strptime(data_str, "%d/%m/%Y").date()
            if hoje <= data_tarefa <= data_limite:
                tarefas_ate_7_dias.append(tarefa)
        except ValueError:
            pass

    return tarefas_ate_7_dias

def ordenada_por_data(dicionario):
    '''Ordena os dicionarios primeiro pela data
    em caso de empate pela prioridade
    '''

    data_str = dicionario['data']
    prioridade = dicionario['prioridade']
    data_status = 0

    try:
        data_objeto = datetime.strptime(data_str, '%d/%m/%Y')

    except ValueError:
        data_objeto = data_str
        data_status = 1

    if prioridade == "Alta":
        prioridade_para_ordenar = (0, prioridade) 
    elif prioridade == "Media":
        prioridade_para_ordenar = (1, prioridade) 
    elif prioridade == "Baixa":
        prioridade_para_ordenar = (2, prioridade)
    else:
        prioridade_para_ordenar = (3, prioridade)
    
    return(data_status, data_objeto, prioridade_para_ordenar)

def ordena_por_prioridade(dicionario):
    '''Ordena os os dicionarios com base primeiro na prioridade
    e em caso de empate pela data
    '''

    data_str = dicionario['data']
    prioridade = dicionario['prioridade']


    if prioridade == "Alta":
        prioridade_para_ordenar = (0, prioridade) 
    elif prioridade == "Media":
        prioridade_para_ordenar = (1, prioridade) 
    elif prioridade == "Baixa":
        prioridade_para_ordenar = (2, prioridade)
    else:
        prioridade_para_ordenar = (3, prioridade)


    data_status = 0

    try:
        data_objeto = datetime.strptime(data_str, '%d/%m/%Y')

    except ValueError:
        data_objeto = data_str
        data_status = 1

    return (prioridade_para_ordenar, data_status, data_objeto)

def ver_tarefa(lista, prioridade):
    lista_ordenada = sorted(lista, key=prioridade)
    print(padrao.NEGRITO+"="*120+padrao.RESET )
    print(f"{"      Tarefas":17}   | {"       Tag":20}| {"  Prioridade":20}| {"    Data":20}| {"     Concluida   "} ")
    print(padrao.NEGRITO+"="*120+padrao.RESET )
    for item in lista_ordenada:
        for i in item.values():
            print(f"   {i:15}  | ", end = "")
        print()
    print()


padrao.limpar()
def desenhar_layout():

    while True:
        if len(lista_dados) == 0:
            print("Nenhuma tarefa adicionada")
            sair = input("Pressione qualquer tecla para sair \n")
            break
        else:
            print('Como você deseja visualizar suas tarefas?')
            print('[1] Visualizar todas as tarefas')
            print('[2] Visualizar tarefas de uma tag')
            print('[3] Visualizar tarefas de uma lista')
            print('[4] Sair')
            num1 = int(input('Digite o numero: '))
            if num1 == 4:
                break 

            elif num1 == 1:
                padrao.limpar()
                print('Como você deseja visualizar suas tarefas?')
                print('[1] Visualizar todas as tarefas ')
                print('[2] Visualizar todas as tarefas não concluidas')
                print('[3] Visualiar apenas tarefas com data até hoje')
                print('[4] Visualiar apenas tarefas com data até 7 dias')
                print('[5] Voltar ao menu principal')
                num2 = int(input('Digite o numero: '))
                if num2 == 5:
                    break

                elif num2 == 1:
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')
                    num3 = int(input('Digite o numero: '))
                    if num3 == 1:
                        ver_tarefa(lista_dados, ordenada_por_data)
                        
                                                 
                    elif num3 == 2:
                        ver_tarefa(lista_dados, ordena_por_prioridade)
      
      
                elif num2 == 2:
                    tarefas_nao_concluidas = filtrar_tarefas_nao_concluidas(lista_dados)
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')
                    num3 = int(input('Digite o numero: '))
                    if num3 == 1:
                        ver_tarefa(tarefas_nao_concluidas, ordenada_por_data)

                    elif num3 == 2:
                        ver_tarefa(tarefas_nao_concluidas, ordena_por_prioridade)


                elif num2 == 3:
                    tarefas_ate_hoje = filtrar_tarefas_ate_hoje(lista_dados)
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')                   
                    num3 = int(input('Digite o numero: '))
                    
                    if num3 == 1:
                        ver_tarefa(tarefas_ate_hoje, ordenada_por_data)

                    elif num3 == 2:
                        ver_tarefa(tarefas_ate_hoje, ordena_por_prioridade)


                elif num2 == 4:
                    tarefas_ate_7_dias = filtrar_data_ate_7_dias(lista_dados)
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')
                    num3 = int(input('Digite o numero: '))
                    if num3 == 1:
                        ver_tarefa(tarefas_ate_7_dias, ordenada_por_data)

                    elif num3 == 2:
                        ver_tarefa(tarefas_ate_7_dias, ordena_por_prioridade)

            
            if num1 == 2:
                print('De qual tag você gostaria de ver as tarefas')
                i = 0
                while i < len(lista_tags):
                    print('[',i+1,'] ', lista_tags[i], sep='')
                    i +=1
                num2 = int(input('Digite o numero: '))
                tarefas_com_tag = filtrar_tarefas_tag(lista_dados, lista_tags, num2 - 1)
                print('Como você deseja visualiza-las')
                print('[1] Visualizar todas as tarefas da tag ', lista_tags[num2-i])
                print('[2] Visualizar todas as tarefas não concluidasda da tag ', lista_tags[num2-i])
                print('[3] Visualiar apenas tarefas com data até hojeda da tag ', lista_tags[num2-i])
                print('[4] Visualiar apenas tarefas com data até 7 diasda da tag ', lista_tags[num2-i])
                print('[5] Voltar ao menu principal')
                num3 = int(input('Digite o numero: '))

                if num3 ==5:
                    break

                if num3 == 1:
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')
                    num4 = int(input('Digite o numero: '))
                    if num4 == 1:
                        ver_tarefa(tarefas_com_tag, ordenada_por_data)

                    elif num3 == 2:
                        ver_tarefa(tarefas_com_tag, ordena_por_prioridade)
 

                elif num3 == 2:
                    tarefas_nao_concluidas = filtrar_tarefas_nao_concluidas(tarefas_com_tag)
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')
                    num3 = int(input('Digite o numero: '))
                    if num3 == 1:
                        ver_tarefa(tarefas_nao_concluidas, ordenada_por_data)
                        
                    elif num3 == 2:
                        ver_tarefa(tarefas_nao_concluidas, ordena_por_prioridade)


                elif num2 == 3:
                    tarefas_ate_hoje = filtrar_tarefas_ate_hoje(tarefas_com_tag)
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')                   
                    num3 = int(input('Digite o numero: '))
                    if num3 == 1:
                        ver_tarefa(tarefas_ate_hoje, ordenada_por_data)

                    elif num3 == 2:
                        ver_tarefa(tarefas_ate_hoje, ordena_por_prioridade)

                elif num2 == 4:
                    tarefas_ate_7_dias = filtrar_data_ate_7_dias(tarefas_com_tag)
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')
                    if num3 == 1:
                        ver_tarefa(tarefas_ate_7_dias, ordenada_por_data)

                    elif num3 == 2:
                        ver_tarefa(tarefas_ate_7_dias, ordena_por_prioridade)


            if num1 == 3:
                print('De qual lista você gostaria de ver as tarefas')
                i = 0
                while i < len(lista_lista_tarefas):
                    print('[',i+1,'] ', lista_lista_tarefas[i]['nome_lista'], sep='')
                    i +=1
                num2 = int(input('Digite o numero: '))
                tarefas_na_lista = filtrar_tarefas_lista(lista_dados, lista_lista_tarefas, num2-1)
                print(tarefas_na_lista)
                print('Como você deseja visualiza-las')
                print('[1] Visualizar todas as tarefas da lista ', lista_lista_tarefas[num2-1]['nome_lista'])
                print('[2] Visualizar todas as tarefas não concluidas da lista ', lista_lista_tarefas[num2-1]['nome_lista'])
                print('[3] Visualiar apenas tarefas com data até hoje da lista ', lista_lista_tarefas[num2-1]['nome_lista'])
                print('[4] Visualiar apenas tarefas com data até 7 dias da lista ', lista_lista_tarefas[num2-1]['nome_lista'])
                print('[5] Voltar ao menu principal')
                num3 = int(input('Digite o numero: '))
                if num3 == 5:
                    break

                if num3 == 1:
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')
                    num4 = int(input('Digite o numero: '))
                    if num4 == 1:
                        ver_tarefa(tarefas_na_lista, ordenada_por_data)

                    elif num3 == 2:
                        ver_tarefa(tarefas_na_lista, ordena_por_prioridade)


                elif num3 == 2:
                    tarefas_nao_concluidas = filtrar_tarefas_nao_concluidas(tarefas_na_lista)
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')
                    num3 = int(input('Digite o numero: '))
                    if num3 == 1:
                        ver_tarefa(tarefas_nao_concluidas, ordenada_por_data)

                    elif num3 == 2:
                        ver_tarefa(tarefas_nao_concluidas, ordena_por_prioridade) 



                elif num2 == 3:
                    tarefas_ate_hoje = filtrar_tarefas_ate_hoje(tarefas_na_lista)
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')                   
                    num3 = int(input('Digite o numero: '))
                    if num3 == 1:
                        ver_tarefa(tarefas_ate_hoje, ordenada_por_data)

                    elif num3 == 2:
                        ver_tarefa(tarefas_ate_hoje, ordena_por_prioridade)


                elif num2 == 4:
                    tarefas_ate_7_dias = filtrar_data_ate_7_dias(tarefas_na_lista)
                    print('Como você deseja ordena-las')
                    print('[1] Ordenar por data')
                    print('[2] Ordenar por prioridade')
                    if num3 == 1:
                        ver_tarefa(tarefas_ate_7_dias, ordenada_por_data)
                        
                    elif num3 == 2:
                        ver_tarefa(tarefas_ate_7_dias, ordena_por_prioridade)



desenhar_layout()