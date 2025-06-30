import os
import sys
import re
from datetime import datetime
from Tarefa import Tarefa



if __name__ == "__main__":

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



    def limpar_tela():
        """ Limpa o terminal após cada print
            
            """
        os.system('cls' if EH_WINDOWS else 'clear')



    def menu_criar(titulo = "",tags = "",prioridade = "",repetição = "",data = ""):
        ''' Menu para criar novas tarefas
        
        '''
        print(NEGRITO+"="*42+RESET )
        print(WBLUE + f"{"Criar tarefa":^42}" + RESET)
        print(NEGRITO+"="*42+RESET )
        print(f"| Título:{titulo:32}|")
        print("-"*42)
        print(f"| Tags: {tags:33}|")
        print("-"*42)
        print(f"| Prioridade: {prioridade:27}|")
        print("-"*42)
        print(f"| Repetição: {repetição:28}|")
        print("-"*42)
        print(f"| Data: {data:33}|")
        print(NEGRITO+ ("-"*42) + RESET)
        print()
        

    # Inicial
    titulo = ""
    tags = ""
    prioridade = ""
    repetição = ""
    data = ""

    menu_criar(titulo, tags, prioridade, repetição, data)

    # Input Nome
    def escolher_titulo():
        titulo = input("Titulo: ")
        limpar_tela()
        return titulo
    titulo = escolher_titulo()
    menu_criar(titulo = titulo,tags = "",prioridade = "",repetição = "",data = "")

    
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


    # Input tags
    def escolher_tag(): 
        tags = input("Escolha a tag:")
        limpar_tela()
        return tags
    tags = escolher_tag()
    menu_criar(titulo = titulo,tags = tags,prioridade = "",repetição = "",data = "")

    
    # Input prioridade 
    def escolher_prioridades(): 
        prioridades = input("Defina a prioridade:")
        limpar_tela()
        return prioridades
    prioridades = escolher_prioridades()
    menu_criar(titulo = titulo,tags = tags,prioridade = prioridades,repetição = "",data = "")


    # Input repeticao
    def escolher_repeticao(): 
        print(f"{1} Semanal \n {2} Baixa")
        repetição = int(input("Escolha a frêquencia:"))
        limpar_tela() 
        return repetição

    repetição = escolher_repeticao()
    menu_criar(titulo = titulo,tags = tags,prioridade = prioridades,repetição = repetição,data = "")

   
    def escolher_data():
        '''
        Solicita uma data para o usuário no formato dd/mm/aaaa
        Continua pedindo até que seja inserida no formato válido
        '''
        while True:
            data = input('data (dd/mm/aaaa): ')
            limpar_tela()
            
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
    menu_criar(titulo = titulo,tags = tags,prioridade = prioridades,repetição = repetição,data = data)
    
    
    with open("dados_tarefas.txt", "a", encoding = 'utf-8') as escrever:
        escrever.write(f"-  {titulo:20} | {tags:20} | {prioridade:20} | {data:20} | {"Não concluida":20} " "\n")
    with open("Nomes_tarefas.txt", "a", encoding = 'utf-8') as escrever:
        escrever.write(f"{titulo} - {id}" "\n")
            
            
            
            




    
    


        
