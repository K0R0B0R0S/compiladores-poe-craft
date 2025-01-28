from parser import parser
from items import Item, Orbe

def executar_comando(comando, itens):
    resultados = parser.parse(comando)
    print(resultados)
    if resultados:
        for orbe, tipo_item in resultados:
            item = itens.get(tipo_item)
            if item:
                Orbe.usar(orbe, item)
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
            for item in itens.values():
                print(item)
        else:
            print("Por favor, insira um comando válido.")