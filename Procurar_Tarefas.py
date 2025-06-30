import padrao as pd


def interface():

  print(pd.NEGRITO + "="* 90 + pd.RESET)
  print(pd.WBLUE + " "* 35 + pd.WBLUE + " Buscar tarefas" + pd.WBLUE + " "* 40 + pd.WNEGRITO )
  print(pd.NEGRITO + "="* 90 + pd.RESET)

def encontrar_tarefa():
  
  while True:
    
    lista = []
    pesquisar = input("Para sair digite enter\nDigite o nome da tarefa\n")
    if pesquisar == "":
      break
    else:
      with open("Nomes_tarefas.txt", "r") as leitura:
          for linha in leitura:
            if pesquisar in linha:
              with open("dados_tarefas.txt", "r") as lendo:
                for linha in lendo:
                  if pesquisar in linha:
                    lista.append(linha)
                    pd.limpar()
                    interface()
                    break 
                   
            else:
              pd.limpar()
              interface()
              print("Nenhuma tarefa encontrada")
              break   
    print()  
    for i in range(len(lista)):
      print(lista[i])

    
interface()    
encontrar_tarefa()
