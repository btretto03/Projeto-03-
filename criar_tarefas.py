import os
import sys
import re
from datetime import datetime
from Tarefa import Tarefa

lista_titulos = []
lista_tags = []
lista_prioridades = []
lista_repeticao = []
lista_data = []
lista_geral = []


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

    if EH_WINDOWS: #Caso o sistema operacional seja windows, usamos esse codigo para capturar a tecla
        import msvcrt

        def tecla_apertada():
            """ Reconhece se o usuario aperta alguma tecla(nesse caso, as setas para navegar pelo menu)
            
            """
            key = msvcrt.getch()
            if key == b'\xe0':
                key = msvcrt.getch()
                if key == b'H': 
                    return 'cima'
                elif key == b'P': 
                    return 'baixo'
            elif key in [b'\r', b'\n']:
                return 'enter'
            elif key == b'\x1b':
                return "Esc"
            return None
        
    else: #Caso o sistema operacional seja linux ou macOS, usamos esse codigo para capturar a tecla
        import termios
        import tty

        def tecla_apertada():
            """ Reconhece se o usuario aperta alguma tecla(nesse caso, as setas para navegar pelo menu)
            
            """
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch1 = sys.stdin.read(1)
                if ch1 == '\x1b':
                    ch2 = sys.stdin.read(1)
                    ch3 = sys.stdin.read(1)
                    if ch2 == '[':
                        if ch3 == 'A': return 'cima'
                        elif ch3 == 'B': return 'baixo'
                    else:
                        return "Esc"
                elif ch1 == '\r':
                    return 'enter'
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
            return None


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

    tags = ["Nenhuma tag disponivel"]
    opcao_tags = 0
    def escolher_tag(): 
        print("Escolha a tag:")
        global opcao_tags  
        for i, item in enumerate(tags):
            if i == opcao_tags :
                print( " "* 2 + SUBLINHADO + " "* 1 + f"  {item}     " + RESET)
            else:
                print(f"    {item}" )
        
    while True:  
            escolher_tag()
            tecla = tecla_apertada()
            if tecla == 'cima':
                limpar_tela()
                menu_criar(titulo = titulo,tags = "",prioridade = "",repetição = "",data = "")
                opcao_tags = (opcao_tags - 1) % len(tags)
            elif tecla == 'baixo':
                limpar_tela()
                menu_criar(titulo = titulo,tags = "",prioridade = "",repetição = "",data = "")
                opcao_tags = (opcao_tags + 1) % len(tags)
            elif tecla == 'enter':
                tags = "Indisponivel"
                limpar_tela()
                break      
    menu_criar(titulo, tags, prioridade, repetição, data)


    # Input prioridade
    prioridades = ["Baixa", "Media", "Alta"]
    opcao_prioridades = 0
    def escolher_prioridades(): 
        print("Defina a prioridade:")
        global opcao_prioridades  
        for i, item in enumerate(prioridades):
            if i == opcao_prioridades :
                print( " "* 2 + SUBLINHADO + " "* 1 + f"  {item}     " + RESET)
            else:

                print(f"    {item}" )

    while True:
            escolher_prioridades()
            tecla = tecla_apertada()
            if tecla == 'cima':
                limpar_tela()
                opcao_prioridades = (opcao_prioridades - 1) % len(prioridades)
                menu_criar(titulo = titulo,tags = tags,prioridade = "",repetição = "",data = "")
            elif tecla == 'baixo':
                limpar_tela()
                opcao_prioridades = (opcao_prioridades + 1) % len(prioridades)
                menu_criar(titulo = titulo,tags = tags,prioridade = "",repetição = "",data = "")
            elif tecla == 'enter':
                prioridade = prioridades[opcao_prioridades]
                limpar_tela()
                break
    menu_criar(titulo, tags, prioridade, repetição, data)


    # Input repeticao
    repeticao = ["Nenhuma","Diária", "Semanal","Mensal","Anual"]
    opcao_repeticao = 0
    def escolher_repeticao(): 
        print("Escolha a frêquencia:")
        global opcao_repeticao  
        for i, item in enumerate(repeticao):
            if i == opcao_repeticao :
                print( " "* 2 + SUBLINHADO + " "* 1 + f"  {item}     " + RESET)
            else:
                print(f"    {item}" )

    while True:
            escolher_repeticao()
            tecla = tecla_apertada()
            if tecla == 'cima':
                limpar_tela()
                opcao_repeticao = (opcao_repeticao - 1) % len(repeticao)
                menu_criar(titulo = titulo,tags = tags,prioridade = prioridade,repetição = "",data = "")
            elif tecla == 'baixo':
                limpar_tela()
                opcao_repeticao = (opcao_repeticao + 1) % len(repeticao)
                menu_criar(titulo = titulo,tags = tags,prioridade = prioridade,repetição = "",data = "")
            elif tecla == 'enter':
                repetição = repeticao[opcao_repeticao]
                limpar_tela()
                break
    menu_criar(titulo, tags, prioridade, repetição, data)

   
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
    menu_criar(titulo, tags, prioridade, repetição, data)
    
    nova_tarefa = Tarefa(titulo = titulo, id=id, tags = tags, prioridade = prioridade, repetição = repetição, data = data)
    
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
    
    with open("dados_tarefas.txt", "a") as escrever:
        escrever.write(f"-  {titulo:20} | {tags:20} | {prioridade:20} | {data:20} | {"Não concluida":20} " "\n")
    with open("Nomes_tarefas.txt", "a") as escrever:
        escrever.write(f"{titulo} - {id}" "\n")
            
            
            
            




    
    


        
