import os
import sys


EH_WINDOWS = os.name == 'nt'
def limpar():
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
