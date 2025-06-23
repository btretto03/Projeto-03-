import os
import sys
IS_WINDOWS = os.name == 'nt'
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
    os.system('cls' if IS_WINDOWS else 'clear')  # Limpa o terminal no Unix/Linux/Mac. Para Windows, use os.system("cls")

if IS_WINDOWS: #Caso o sistema operacional seja windows, usamos esse codigo para capturar a tecla
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


def desenhar_layout(titulo = "",tags = "",prioridade = "",repetição = "",data = ""):
    print("┌"+"─"*40+"┐" )
    print(WBLUE + f"{"Criar tarefa":^42}" + RESET)
    print("─"*42)
    print(f"│ Título:{titulo:32}│")
    print("─"*42)
    print(f"│ Tags: {tags:33}│")
    print("─"*42)
    print(f"│ Prioridade: {prioridade:27}│")
    print("─"*42)
    print(f"│ Repetição: {repetição:28}│")
    print("─"*42)
    print(f"│ Data: {data:33}│")
    print("└"+ ("─"*40) + "┘")
    print()
    

# Inicial
titulo = ""
tags = ""
prioridade = ""
repetição = ""
data = ""

desenhar_layout(titulo, tags, prioridade, repetição, data)

# Input Nome
def titulo():
    titulo = input("Titulo: ")
    limpar_tela()
    return titulo
titulo = titulo()
desenhar_layout(titulo = titulo,tags = "",prioridade = "",repetição = "",data = "")

# Input tags

tags = ["Nenhuma tag disponivel"]
opcao_tags = 0
def escolher_tag(): 
    print("Escolha a tag:")
    global opcao_tags  
    for i, item in enumerate(tags):
        if i == opcao_tags :
            print( " "* 2 + SUBLINHADO + " "* 1 + f" ⟶ {item}     " + RESET)
        else:
            print(f"    {item}" )
    
while True:  
        escolher_tag()
        tecla = tecla_apertada()
        if tecla == 'cima':
            limpar_tela()
            desenhar_layout(titulo = titulo,tags = "",prioridade = "",repetição = "",data = "")
            opcao_tags = (opcao_tags - 1) % len(tags)
        elif tecla == 'baixo':
            limpar_tela()
            desenhar_layout(titulo = titulo,tags = "",prioridade = "",repetição = "",data = "")
            opcao_tags = (opcao_tags + 1) % len(tags)
        elif tecla == 'enter':
            tags = "Indisponivel"
            limpar_tela()
            break      
desenhar_layout(titulo, tags, prioridade, repetição, data)


# Input prioridade
prioridades = ["Baixa", "Media", "Alta"]
opcao_prioridades = 0
def escolher_prioridades(): 
    print("Defina a prioridade:")
    global opcao_prioridades  
    for i, item in enumerate(prioridades):
        if i == opcao_prioridades :
            print( " "* 2 + SUBLINHADO + " "* 1 + f" ⟶ {item}     " + RESET)
        else:

            print(f"    {item}" )

while True:
        escolher_prioridades()
        tecla = tecla_apertada()
        if tecla == 'cima':
            limpar_tela()
            opcao_prioridades = (opcao_prioridades - 1) % len(prioridades)
            desenhar_layout(titulo = titulo,tags = tags,prioridade = "",repetição = "",data = "")
        elif tecla == 'baixo':
            limpar_tela()
            opcao_prioridades = (opcao_prioridades + 1) % len(prioridades)
            desenhar_layout(titulo = titulo,tags = tags,prioridade = "",repetição = "",data = "")
        elif tecla == 'enter':
            prioridade = prioridades[opcao_prioridades]
            limpar_tela()
            break
desenhar_layout(titulo, tags, prioridade, repetição, data)


# Input repeticao
repeticao = ["Nenhuma","Diária", "Semanal","Mensal","Anual"]
opcao_repeticao = 0
def escolher_repeticao(): 
    print("Escolha a frêquencia:")
    global opcao_repeticao  
    for i, item in enumerate(repeticao):
        if i == opcao_repeticao :
            print( " "* 2 + SUBLINHADO + " "* 1 + f" ⟶ {item}     " + RESET)
        else:
            print(f"    {item}" )

while True:
        escolher_repeticao()
        tecla = tecla_apertada()
        if tecla == 'cima':
            limpar_tela()
            opcao_repeticao = (opcao_repeticao - 1) % len(repeticao)
            desenhar_layout(titulo = titulo,tags = tags,prioridade = "prioriodade",repetição = "",data = "")
        elif tecla == 'baixo':
            limpar_tela()
            opcao_repeticao = (opcao_repeticao + 1) % len(repeticao)
            desenhar_layout(titulo = titulo,tags = tags,prioridade = "prioridade",repetição = "",data = "")
        elif tecla == 'enter':
            repetição = repeticao[opcao_repeticao]
            limpar_tela()
            break
desenhar_layout(titulo, tags, prioridade, repetição, data)

def data():
    data= input("data: ")
    limpar_tela()
    return data
data = data()
desenhar_layout(titulo, tags, prioridade, repetição, data)


        
