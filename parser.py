import ply.yacc as yacc
from lexer import tokens

# Regras da gramática

def p_comandos(p):
    '''comandos : comando comandos
                | comando'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_comando(p):
    '''comando : USAR ORBE EM lista_itens
               | LISTAR lista_itens
               | LISTAR TODOS'''
    if len(p) == 3 and p[1] == "listar":
        p[0] = ("listar", p[2])
    elif len(p) == 2 and p[1] == "listar":
        p[0] = ("listar", "todos")
    else:
        p[0] = (p[2], p[4])

def p_lista_itens(p):
    '''lista_itens : ITEM lista_itens_aux'''
    p[0] = [p[1]] + p[2]

def p_lista_itens_aux(p):
    '''lista_itens_aux : VIRGULA ITEM lista_itens_aux
                       | empty'''
    if len(p) == 4:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []

def p_empty(p):
    '''empty :'''
    p[0] = []

def p_error(p):
    print("Comando inválido!")

# Construir o parser
parser = yacc.yacc()