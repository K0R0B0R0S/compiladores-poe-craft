from parser import parser
from items import Item, Orbe

def executar_comando(comando, itens):
    resultados = parser.parse(comando)
    if resultados:
        for acao, lista_itens in resultados:
            if acao == "listar":
                if lista_itens == "todos":
                    for item in itens.values():
                        print(item)
                else:
                    for tipo_item in lista_itens:
                        item = itens.get(tipo_item)
                        if item:
                            print(item)
                        else:
                            print(f"Item {tipo_item} não encontrado.")
            else:
                for tipo_item in lista_itens:
                    item = itens.get(tipo_item)
                    if item:
                        Orbe.usar(acao, item)
                    else:
                        print(f"Item {tipo_item} não encontrado.")
    else:
        print("Comando inválido!")

# Criar os itens
itens = {
    "arma": Item("arma"),
    "armadura": Item("armadura"),
    "acessório": Item("acessório")
}

# Testar comandos
if __name__ == "__main__":
    print("Bem-vindo ao sistema de criação de itens! Digite seus comandos ou 'sair' para encerrar.")
    while True:
        comando = input("> ").strip()
        if comando.lower() == 'sair':
            print("Encerrando o programa...")
            break
        if comando:
            executar_comando(comando, itens)
        else:
            print("Por favor, insira um comando válido.")