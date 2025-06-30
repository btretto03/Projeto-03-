from dataclasses import dataclass



@dataclass
class Tarefa():
    def __init__(self):
        self.titulo = str 
        self.tags = str  
        self.prioridade = str
        self.repetição = str 
        self.data = int 
        self.id = int 
    
    def escolher_titulo(self):
      self.titulo = input("Título: ")
      self.limpar_tela()
      return self.titulo
  
    def criar_descricao(self):
        '''Possibilita ao usuario dar uma descrição para sua tarefa'''
        self.descricao = input('Descrição: ')

        while len(self.descricao) > 38:
            print('Sua descrição é muito grande, favor alterar')
            self.descricao = input('Descrição: ')
        self.limpar_tela()
        return self.descricao  
    
    def escolher_tag(self): 
        self.tags = input("Escolha a tag: ")
        self.limpar_tela()
        return self.tags
    
    def escolher_prioridades(self): 
        prioridades = ["Baixa", "Media", "Alta"]
        for i in range(len(prioridades)):
            print(f"{i + 1}. {prioridades[i]}")
        self.prioridade = int(input("Defina a prioridade: "))
        self.limpar_tela()
        return prioridades[self.prioridade - 1]
    
    def escolher_repeticao(self): 
        repeticao = ["Nenhuma","Diária", "Semanal","Mensal","Anual"]
        for i in range(len(repeticao)):
            print(f"{i + 1}. {repeticao[i]}")
        self.repetição = int(input("Escolha a frêquencia: "))
        self.limpar_tela() 
        return repeticao[self.repetição - 1]
    
    def escolher_data(self):
        '''
        Solicita uma data para o usuário no formato dd/mm/aaaa
        Continua pedindo até que seja inserida no formato válido
        '''
        import re
        from datetime import datetime
        
        while True:
            self.data = input('data (dd/mm/aaaa): ')
            self.limpar_tela()
            
            #Verifica o formato dd/mm/aaaa
            if re.match(r'^\d{2}\/\d{2}\/\d{4}$', self.data):
                
                # Verifica se a data é real
                try:
                    datetime.strptime(self.data, '%d/%m/%Y')

                    return self.data
                except ValueError:
                    print('Data inválida. Por favor, insira uma data real no formato dd/mm/aaaa.')
            else:
                print('Formato Inválido. Por favor, insira a data no formato dd/mm/aaaa.')
                print('Exemplo: 01/01/2025')
                
    def limpar_tela(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')


        

  
            
  

  
  
  
  


  
  
  
  
  
  
  
  
  
  
  
  