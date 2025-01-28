import random

# Lista de modificadores possíveis
PREFIXOS = ["Afiado", "Destruidor", "Devoto", "Refinado", "Gélido", "Volátil"]
SUFIXOS = ["da Fúria", "do Poder", "da Resistência", "do Vigor", "do Gelo", "da Chama"]


class Item:
    def __init__(self, tipo):
        self.tipo = tipo
        self.raridade = "normal"
        self.prefixos = []
        self.sufixos = []

    def __str__(self):
        total_mods = len(self.prefixos) + len(self.sufixos)
        mods = ", ".join(self.prefixos + self.sufixos)
        return f"{self.tipo} ({self.raridade}) com {total_mods}/6 mods: {mods}"

    def adicionar_modificador(self):
        """Adiciona um modificador aleatório, respeitando os limites de prefixos e sufixos, e evita duplicação."""
        opcoes_validas = []
        if len(self.prefixos) < 3:
            opcoes_validas.append("prefixo")
        if len(self.sufixos) < 3:
            opcoes_validas.append("sufixo")

        if not opcoes_validas:
            print("Não é possível adicionar mais modificadores.")
            return False

        tipo_modificador = random.choice(opcoes_validas)
        if tipo_modificador == "prefixo":
            prefixos_disponiveis = [mod for mod in PREFIXOS if mod not in self.prefixos]
            if prefixos_disponiveis:
                mod = random.choice(prefixos_disponiveis)
                self.prefixos.append(mod)
                return True
        elif tipo_modificador == "sufixo":
            sufixos_disponiveis = [mod for mod in SUFIXOS if mod not in self.sufixos]
            if sufixos_disponiveis:
                mod = random.choice(sufixos_disponiveis)
                self.sufixos.append(mod)
                return True

        print("Não foi possível adicionar um modificador válido.")
        return False

    def remover_modificador(self):
        """Remove um modificador aleatório, se houver algum."""
        if not self.prefixos and not self.sufixos:
            print("Não há modificadores para remover.")
            return False

        if self.prefixos and (not self.sufixos or random.choice(["prefixo", "sufixo"]) == "prefixo"):
            removido = self.prefixos.pop()
        else:
            removido = self.sufixos.pop()

        print(f"Modificador '{removido}' foi removido.")
        return True


class Orbe:
    @staticmethod
    def usar(orbe, item):
        if orbe == "transmutação":
            if item.raridade == "normal":
                item.raridade = "mágico"
                item.adicionar_modificador()
            else:
                print("Orbe de transmutação só funciona em itens normais.")
        elif orbe == "ampliação":
            if item.raridade == "mágico":
                item.adicionar_modificador()
            else:
                print("Orbe de ampliação só funciona em itens mágicos com espaço para mods.")
        elif orbe == "régio":
            if item.raridade == "mágico":
                item.raridade = "raro"
                item.adicionar_modificador()
            else:
                print("Orbe régio só funciona em itens mágicos.")
        elif orbe == "exaltado":
            if item.raridade == "raro":
                item.adicionar_modificador()
            else:
                print("Orbe exaltado só funciona em itens raros")
        elif orbe == "anulação":
            if item.prefixos or item.sufixos:
                item.remover_modificador()
            else:
                print("Não há modificadores para remover.")
        elif orbe == "alquimia":
            if item.raridade == "normal":
                item.raridade = "raro"
                for _ in range(4):
                    item.adicionar_modificador()
            else:
                print("Orbe de alquimia só funciona em itens normais.")
        else:
            print("Orbe inválido ou não implementado.")