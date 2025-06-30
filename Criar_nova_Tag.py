import padrao
def escolher_tag():
    tag = input("Escolha o nome da tag\n")
    padrao.limpar()
    return tag
tag = escolher_tag()

with open("dados_tag.txt", "a", encoding = 'utf-8') as escrever:
    escrever.write(f" {tag}" "\n")