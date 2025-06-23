import os
import sys
import datetime as dt



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

def ler_codigo_de_arquivo(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        return "Arquivo não encontrado."
    
while True:
    opcoes_do_menu = ["Criar nova tarefa", "Modificar tarefas", "Visualizar tarefas", "Sair"]
    opcao = 0

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
                elif ch1 == '\r':
                    return 'enter'
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
            return None

    def limpar():
        """ Limpa o terminal após cada print
            
            """
        os.system('cls' if IS_WINDOWS else 'clear')

    def mostrar_menu():
        limpar()
        largura = 40
        print(NEGRITO + "-"* 57 + RESET)
        print(WBLUE + " "* 20 + WBLUE + " MENU PRINCIPAL " + WBLUE + " "* 21 + WNEGRITO )
        print(NEGRITO + "-"* 57 + RESET)
        dia = dt.date.today()           
        dia_formatado = dia.strftime("%d/%m/%Y")
        print(
            GREEN
            + f" {' '*43} |{dia_formatado}|"
            + WNEGRITO
            + RESET 
    )
        for i, item in enumerate(opcoes_do_menu):
            if i == opcao and opcao != 3:
                print( " "* 2 + SUBLINHADO + " "* 3 + f" ⟶ {item}     " + RESET)
            elif i == opcao and opcao == 3:
                print( " "* 2 + SUBLINHADO_VERMELHO + " "* 3 + f" ⟶ {item}     " + RESET)

            else:
                print(f"    {item}" )
        print()
        print(NEGRITO + "-"* 57 + RESET)
    

    while True:
        mostrar_menu()
        tecla = tecla_apertada()
        if tecla == 'cima':
            opcao = (opcao - 1) % len(opcoes_do_menu)
            if opcao == -1:
                opcao = 3
                continue
        elif tecla == 'baixo':
            opcao = (opcao + 1) % len(opcoes_do_menu)
            if opcao == 4:
                opcao = 0
                continue
        elif tecla == 'enter':
            limpar()
            if "Criar nova tarefa" in opcoes_do_menu[opcao]:
                    exec(open("criar_tarefas.py").read())
                    limpar()
                    
            if "Sair" in opcoes_do_menu[opcao]:
                input("\nPressione Enter para sair...")
                if tecla == 'enter':
                    break



