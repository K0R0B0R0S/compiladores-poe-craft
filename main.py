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
    comandos_teste = f"""
        usar ORBE DE ALQUIMIA em arma
        usar ORBE DE EXALTADO em arma
        usar ORBE DE EXALTADO em arma
    """

    print(f"Executando comando: {comandos_teste}")
    executar_comando(comandos_teste, itens)
    print(itens["arma"])
    print(itens["armadura"])
    print("-" * 40)