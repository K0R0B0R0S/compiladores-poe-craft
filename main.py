from parser import parser
from items import Item, Orbe

def inicializar_sistema():
    """Inicializa o sistema, criando um dicionário vazio para armazenar os itens."""
    return {}

def processar_comando(comando, itens):
    """Processa o comando do usuário e executa a ação correspondente."""
    resultados = parser.parse(comando)
    if resultados:
        for acao, lista_itens in resultados:
            if acao == "listar":
                listar_itens(lista_itens, itens)
            elif acao == "criar":
                criar_item(lista_itens, itens)
            else:
                usar_orbe(acao, lista_itens, itens)
    else:
        print("Comando inválido!")

def listar_itens(lista_itens, itens):
    """Lista os itens conforme solicitado pelo usuário."""
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

def criar_item(tipo_item, itens):
    """Cria um novo item e o adiciona ao dicionário de itens."""
    novo_item = Item(tipo_item)
    itens[novo_item.uuid[:5]] = novo_item
    print(f"Item {novo_item.tipo} criado com UUID: {novo_item.uuid[:5]}")

def usar_orbe(orbe, uuid_item, itens):
    """Aplica um orbe no item correspondente ao UUID fornecido."""
    item = itens.get(uuid_item)
    if item:
        Orbe.usar(orbe, item)
    else:
        print(f"Item com UUID {uuid_item} não encontrado.")

def exibir_ajuda():
    """Exibe as instruções de uso para o usuário."""
    print("\n=== Ajuda ===")
    print("Comandos disponíveis:")
    print("- criar arma: Cria uma nova arma.")
    print("- criar armadura: Cria uma nova armadura.")
    print("- criar acessório: Cria um novo acessório.")
    print("- usar ORBE DE <tipo> em <uuid>: Aplica um orbe no item com o UUID fornecido.")
    print("- listar todos: Lista todos os itens criados.")
    print("- listar <tipo>: Lista itens de um tipo específico.")
    print("- sair: Encerra o programa.")
    print("=============\n")

def encerrar_programa():
    """Encerra o programa com uma mensagem de despedida."""
    print("Encerrando o programa...")
    exit()

def main():
    """Função principal que gerencia o loop de interação com o usuário."""
    itens = inicializar_sistema()
    print("Bem-vindo ao sistema de criação de itens! Digite 'ajuda' para ver os comandos disponíveis.")
    
    while True:
        comando = input("> ").strip()
        if comando == 'sair':
            encerrar_programa()
        elif comando == 'ajuda':
            exibir_ajuda()
        elif comando:
            processar_comando(comando, itens)
        else:
            print("Por favor, insira um comando válido.")

if __name__ == "__main__":
    main()