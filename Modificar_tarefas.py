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
    
    
  limpar()
  def desenhar_layout():
    nova_lista = [] 
    with open("dados_tarefas.txt", "r") as dados: #Visualizar as tarefas no arquivo e adiciona-las a uma lista
      for lista in dados:
        nova_lista.append(lista.strip())
  
    while True:
        if len(nova_lista) == 0:
            print("Nenhuma tarefa adicionada")
            sair = input("Pressione qualquer tecla para sair \n")
            return "s"
        else:
            print(NEGRITO+"="*114+RESET )
            print(f"{"        Tarefas":25} | {"       Tag":20} | {"    Prioridade":20} | {"     Data":20} | {"     Concluida"} ")
            print(NEGRITO+"-"*114+RESET )
            print(f"     {"":20} | {"":20} | {"":20} | {"":20} | {"":20} ")
            for i in range(len(nova_lista)):
                print(i+1, nova_lista[i])
                print(f"     {"":20} | {"":20} | {"":20} | {"":20} | {"":20} ")
                print(NEGRITO+"-"*114+RESET )
            modificar = input("Digite o numero da tarefa que deseja modificar. Para sair digite s\n")

            return modificar


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
  sim = True
  while sim:
    modificar = desenhar_layout()
    if modificar == "s":
      sim = False
      break
    else:
      def menu_criar(titulo = "",tags = "",prioridade = "",repetição = "",data = ""):
        ''' Menu para criar novas tarefas
          
          '''
        limpar()
        nova_lista = [] 
        with open("dados_tarefas.txt", "r") as dados: #Visualizar as tarefas no arquivo e adiciona-las a uma lista
            for lista in dados:
                nova_lista.append(lista.strip())
        print(NEGRITO+"="*114+RESET )
        print(f"{"        Tarefas":25} | {"       Tag":20} | {"    Prioridade":20} | {"     Data":20} | {"     Concluida"} ")
        print(NEGRITO+"-"*114+RESET )
        print(f"     {"":20} | {"":20} | {"":20} | {"":20} | {"":20} ")
        print(int(modificar)-1, nova_lista[int(modificar)-1])
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
          limpar()
          return titulo
      titulo = escolher_titulo()
      menu_criar(titulo = titulo,tags = "",prioridade = "",repetição = "",data = "")

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
                  limpar()
                  menu_criar(titulo = titulo,tags = "",prioridade = "",repetição = "",data = "")
                  opcao_tags = (opcao_tags - 1) % len(tags)
              elif tecla == 'baixo':
                  limpar()
                  menu_criar(titulo = titulo,tags = "",prioridade = "",repetição = "",data = "")
                  opcao_tags = (opcao_tags + 1) % len(tags)
              elif tecla == 'enter':
                  tags = "Indisponivel"
                  limpar()
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
                  limpar()
                  opcao_prioridades = (opcao_prioridades - 1) % len(prioridades)
                  menu_criar(titulo = titulo,tags = tags,prioridade = "",repetição = "",data = "")
              elif tecla == 'baixo':
                  limpar()
                  opcao_prioridades = (opcao_prioridades + 1) % len(prioridades)
                  menu_criar(titulo = titulo,tags = tags,prioridade = "",repetição = "",data = "")
              elif tecla == 'enter':
                  prioridade = prioridades[opcao_prioridades]
                  limpar()
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
                  limpar()
                  opcao_repeticao = (opcao_repeticao - 1) % len(repeticao)
                  menu_criar(titulo = titulo,tags = tags,prioridade = prioridade,repetição = "",data = "")
              elif tecla == 'baixo':
                  limpar()
                  opcao_repeticao = (opcao_repeticao + 1) % len(repeticao)
                  menu_criar(titulo = titulo,tags = tags,prioridade = prioridade,repetição = "",data = "")
              elif tecla == 'enter':
                  repetição = repeticao[opcao_repeticao]
                  limpar()
                  break
      menu_criar(titulo, tags, prioridade, repetição, data)

      def escolher_data():
          data= input("data: ")
          limpar()
          return data
      data = escolher_data()
      menu_criar(titulo, tags, prioridade, repetição, data)
      
      nova_tarefa = Tarefa(titulo = titulo, tags = tags, prioridade = prioridade, repetição = repetição, data = data)
      
      with open("Nomes_tarefas.txt", "a") as escrever:
          escrever.write(f"{titulo}" "\n")
              
      with open("dados_tarefas.txt", "r") as arquivo:
          linhas = arquivo.readlines()
          
      try:
        linhas[int(modificar)-1] = f"-  {titulo:20} | {tags:20} | {prioridade:20} | {data:20} | {"Não concluida":20} " "\n"
        with open("dados_tarefas.txt", "w") as arquivo:
            arquivo.writelines(linhas)   
      except:
        print("Nenhuma tarefa com esse numero")  
    limpar()