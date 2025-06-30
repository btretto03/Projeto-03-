import os
from Tarefa import Tarefa


if __name__ == "__main__":

    EH_WINDOWS = os.name == 'nt'
    
    #Cores de texto usadas
    WHITE = "\033[0;37m"
    NEGRITO = "\033[1m"
    RESET = "\033[0m"

    #Cores de fundo usadas
    WBLUE = "\033[1;44m"
    WWHITE = "\033[0;47m"
 



    def menu_criar(titulo = "", descricao = '', tags = "",prioridade = "",repetição = "",data = ""):
        ''' Menu para criar novas tarefas
        
        '''
        print(NEGRITO+"="*42+RESET )
        print(WBLUE + f"{"Criar tarefa":^42}" + RESET)
        print(NEGRITO+"="*42+RESET )
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
        print(NEGRITO+ ("-"*42) + RESET)
        print()
        
    # Inicial
    titulo = ""
    descricao = ''
    tags = ""
    prioridade = ""
    repetição = ""
    data = ""

    menu_criar(titulo, descricao, tags, prioridade, repetição, data)

    tarefa = Tarefa()
    
    # Input Nome
    titulo = tarefa.escolher_titulo()
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
    
    # Input descricao
    descricao = tarefa.criar_descricao()
    menu_criar(titulo = titulo, descricao = descricao ,tags = "",prioridade = "",repetição = "",data = "") 


    # Input tags
    tags = tarefa.escolher_tag()
    menu_criar(titulo = titulo, descricao = descricao ,tags = tags,prioridade = "",repetição = "",data = "")

    
    # Input prioridade 
    prioridades = tarefa.escolher_prioridades()
    menu_criar(titulo = titulo, descricao = descricao ,tags = tags,prioridade = prioridades,repetição = "",data = "")


    # Input repeticao
    repetição = tarefa.escolher_repeticao()
    menu_criar(titulo = titulo, descricao = descricao ,tags = tags,prioridade = prioridades,repetição = repetição,data = "")

    # Input data
    data = tarefa.escolher_data()
    menu_criar(titulo = titulo, descricao = descricao ,tags = tags,prioridade = prioridades,repetição = repetição,data = data)
    
    
    with open("dados_tarefas.txt", "a", encoding = 'utf-8') as escrever:
        escrever.write(f"-  {titulo:20} | {tags:20} | {prioridade:20} | {data:20} | {"Não concluida":20} " "\n")
    with open("Nomes_tarefas.txt", "a", encoding = 'utf-8') as escrever:
        escrever.write(f"{titulo} - {id}" "\n")
            
            
            