import ply.lex as lex

# Lista de tokens
tokens = (
    'USAR',
    'ORBE',
    'EM',
    'ITEM'
)

# Palavras-chave
t_USAR = r'usar'
t_EM = r'em'

# Expressões regulares para os orbes e itens
def t_ORBE(t):
    r'ORBE\s+DE\s+(TRANSMUTAÇÃO|AMPLIAÇÃO|RÉGIO|EXALTADO|ANULAÇÃO|ALQUIMIA)'
    t.value = t.value.split(" ", 2)[-1].lower()
    return t

def t_ITEM(t):
    r'\b(arma|armadura|acessório)\b'
    t.value = t.value.lower()
    return t

# Ignorar espaços e tabs
t_ignore = ' \t\n'

# Gerenciar erros léxicos
def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()