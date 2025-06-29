import os
import sys
from Tarefa import Tarefa

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

EH_WINDOWS = os.name == 'nt'


if __name__ == "__main__":
  
  
  def limpar(): 
    '''Limpa o terminal apos cada iteracao
    
    '''
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

def menu_filtro():
    limpar()
    opcoes = ["Todas as Tarefas", "Tarefas Pendentes", "Tarefas Concluídas", "Sair para Menu Principal"]
    opcao_atual = 0
    while True:
        limpar()
        print("Como você deseja listar as tarefas?")
        for i, item in enumerate(opcoes):
            if i == opcao_atual:
                print("  " + SUBLINHADO + f"  {item}  " + RESET)
            else:
                print(f"    {item}")
        tecla = tecla_apertada()
        if tecla == 'cima':
            opcao_atual = (opcao_atual - 1) % len(opcoes)
        elif tecla == 'baixo':
            opcao_atual = (opcao_atual + 1) % len(opcoes)
        elif tecla == 'enter':
            return opcoes[opcao_atual]
        
def menu_gerenciar_acao(tarefa_selecionada):
    limpar()
    opcoes = ["Modificar Tarefa", "Marcar como Concluída", "Excluir Tarefa", "Cancelar"]
    opcao_atual = 0
    while True:
        limpar()
        print("Gerenciando a Tarefa:")
        print(f"-> {tarefa_selecionada}\n")
        print("Escolha uma ação:")
        for i, item in enumerate(opcoes):
            if i == opcao_atual:
                print("  " + SUBLINHADO + f"  {item}  " + RESET)
            else:
                print(f"    {item}")
        
        tecla = tecla_apertada()
        if tecla == 'cima':
            opcao_atual = (opcao_atual - 1) % len(opcoes)
        elif tecla == 'baixo':
            opcao_atual = (opcao_atual + 1) % len(opcoes)
        elif tecla == 'enter':
            return opcoes[opcao_atual]
               
def desenhar_layout(filtro):
    limpar()
    todas_as_tarefas = [] 
    try:
        with open("dados_tarefas.txt", "r", encoding='utf-8') as dados:
            for lista in dados:
                todas_as_tarefas.append(lista.strip())
    except FileNotFoundError:
        print("Nenhuma tarefa adicionada ainda.")
        input("Pressione qualquer tecla para sair \n")
        return "s", None
    
    lista_filtrada = []
    if filtro == "Tarefas Pendentes":
        for tarefa in todas_as_tarefas:
            if "Não concluida" in tarefa:
                lista_filtrada.append(tarefa)
    elif filtro == "Tarefas Concluídas":
        for tarefa in todas_as_tarefas:
            if "Concluida" in tarefa and "Não concluida" not in tarefa:
                lista_filtrada.append(tarefa)
    else:
        lista_filtrada = todas_as_tarefas

    if len(lista_filtrada) == 0:
        print(f"Nenhuma tarefa encontrada para o filtro: '{filtro}'")
        input("Pressione qualquer tecla para continuar...")
        return None, None
    else:
        print(NEGRITO+"="*114+RESET )
        print(f"Mostrando: {filtro}")
        print(NEGRITO+"-"*114+RESET )
        print(f"{"         Tarefas":25} | {"         Tag":20} | {"      Prioridade":20} | {"        Data":20} | {"      Concluida"} ")
        print(NEGRITO+"-"*114+RESET )
        for i in range(len(lista_filtrada)):
            print(f"{i+1}. {lista_filtrada[i]}")
            print(NEGRITO+"-"*114+RESET )
        modificar = input("Digite o numero da tarefa que deseja gerenciar. Para voltar digite s\n")
        return modificar, lista_filtrada

sim = True
while sim:
    filtro_escolhido = menu_filtro()
    if filtro_escolhido == "Sair para Menu Principal":
        sim = False
        break
    modificar, lista_de_tarefas_filtrada = desenhar_layout(filtro=filtro_escolhido)
    if modificar is None:
        continue
    if modificar.lower() == "s":
        continue
    try:
        indice_escolhido = int(modificar) - 1
        if not (0 <= indice_escolhido < len(lista_de_tarefas_filtrada)):
            print("\nNúmero da tarefa inválido.")
            input("Pressione Enter para tentar novamente...")
            continue
        
        tarefa_escolhida_str = lista_de_tarefas_filtrada[indice_escolhido]
        acao = menu_gerenciar_acao(tarefa_escolhida_str)

        if acao == "Cancelar":
            continue

        linhas_originais = []
        with open("dados_tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linhas_originais.append(linha.strip())

        indice_real_no_arquivo = linhas_originais.index(tarefa_escolhida_str)

        if acao == "Marcar como Concluída":
            partes_tarefa = linhas_originais[indice_real_no_arquivo].split('|')
            partes_tarefa[4] = f' {"Concluida":<20} '
            linhas_originais[indice_real_no_arquivo] = '|'.join(partes_tarefa)
        
        elif acao == "Excluir Tarefa":
            del linhas_originais[indice_real_no_arquivo]

        elif acao == "Modificar Tarefa":
            print("\n Falta fazer aqui")
            input("Pressione Enter para continuar...")
            continue 

        with open("dados_tarefas.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas_originais:
                arquivo.write(linha + "\n")
        
    except (ValueError, TypeError):
        print("\nEntrada inválida. Por favor, digite um número válido.")
        input("Pressione Enter para tentar novamente...")

