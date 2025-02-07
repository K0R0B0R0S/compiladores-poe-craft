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
        return

    if not isinstance(lista_itens, list):
        lista_itens = [lista_itens]

    for item_ref in lista_itens:
        if len(item_ref) == 5 and all(c in "0123456789abcdef" for c in item_ref):
            item = itens.get(item_ref)
            if item:
                print(item)
            else:
                print(f"Item com UUID {item_ref} não encontrado.")
        else:
            itens_filtrados = [item for item in itens.values() if item.tipo == item_ref]
            if itens_filtrados:
                for item in itens_filtrados:
                    print(item)
            else:
                print(f"Nenhum item do tipo {item_ref} encontrado.")

def criar_item(lista_itens, itens):
    """Cria um ou mais itens e os adiciona ao dicionário de itens."""
    for tipo_item in lista_itens:
        if tipo_item in ["arma", "armadura", "acessório"]:
            novo_item = Item(tipo_item)
            itens[novo_item.uuid[:5]] = novo_item
            print(f"Item {novo_item.tipo} criado com UUID: {novo_item.uuid[:5]}")
        else:
            print(f"Tipo de item inválido: {tipo_item}")

def usar_orbe(orbe, lista_uuid, itens):
    """Aplica um orbe em cada item correspondente aos UUIDs fornecidos."""
    for uuid_item in lista_uuid:
        item = itens.get(uuid_item)
        if item:
            print(f"Aplicando orbe {orbe} no item {item.tipo} (UUID: {uuid_item})...")
            Orbe.usar(orbe, item)
        else:
            print(f"Item com UUID {uuid_item} não encontrado.")

def exibir_ajuda():
    """Exibe as instruções de uso para o usuário."""
    print("\n=== Ajuda ===")
    print("Comandos disponíveis:")
    print("\n1. Criar itens:")
    print("   - criar arma: Cria uma nova arma.")
    print("   - criar armadura: Cria uma nova armadura.")
    print("   - criar acessório: Cria um novo acessório.")
    print("   - criar arma, armadura, acessório: Cria múltiplos itens de uma vez.")
    
    print("\n2. Listar itens:")
    print("   - listar todos: Lista todos os itens criados.")
    print("   - listar arma: Lista todas as armas criadas.")
    print("   - listar armadura: Lista todas as armaduras criadas.")
    print("   - listar acessório: Lista todos os acessórios criados.")
    print("   - listar <uuid>: Lista o item com o UUID especificado.")
    
    print("\n3. Usar orbes:")
    print("   - usar ORBE DE TRANSMUTAÇÃO em <uuid>: Transforma um item normal em mágico e adiciona um modificador.")
    print("   - usar ORBE DE AMPLIAÇÃO em <uuid>: Adiciona um modificador a um item mágico.")
    print("   - usar ORBE DE RÉGIO em <uuid>: Transforma um item mágico em raro e adiciona um modificador.")
    print("   - usar ORBE DE EXALTADO em <uuid>: Adiciona um modificador a um item raro.")
    print("   - usar ORBE DE ANULAÇÃO em <uuid>: Remove um modificador de um item.")
    print("   - usar ORBE DE ALQUIMIA em <uuid>: Transforma um item normal em raro e adiciona quatro modificadores.")
    
    print("\n4. Outros comandos:")
    print("   - ajuda: Exibe esta mensagem de ajuda.")
    print("   - sair: Encerra o programa.")
    print("\n=== Fim da Ajuda ===\n")

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