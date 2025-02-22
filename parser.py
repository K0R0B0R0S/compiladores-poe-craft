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
    '''comando : USAR ORBE EM lista_uuid
               | LISTAR UUID
               | LISTAR TODOS
               | LISTAR lista_itens
               | CRIAR lista_itens'''
    if len(p) == 3 and p[1] == "listar":
        p[0] = ("listar", p[2])
    elif len(p) == 2 and p[1] == "listar":
        p[0] = ("listar", "todos")
    elif len(p) == 3 and p[1] == "criar":
        p[0] = ("criar", p[2])
    else:
        p[0] = (p[2], p[4])

def p_lista_itens(p):
    '''lista_itens : ITEM lista_itens_aux
                   | UUID lista_itens_aux'''
    p[0] = [p[1]] + p[2]

def p_lista_itens_aux(p):
    '''lista_itens_aux : VIRGULA ITEM lista_itens_aux
                       | VIRGULA UUID lista_itens_aux
                       | vazio'''
    if len(p) == 4:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []

def p_lista_uuid(p):
    '''lista_uuid : UUID lista_uuid_aux'''
    p[0] = [p[1]] + p[2]

def p_lista_uuid_aux(p):
    '''lista_uuid_aux : VIRGULA UUID lista_uuid_aux
                      | vazio'''
    if len(p) == 4:
        p[0] = [p[2]] + p[3]
    else:
        p[0] = []

def p_vazio(p):
    '''vazio :'''
    p[0] = []

def p_error(p):
    print("Comando inválido!")

parser = yacc.yacc()