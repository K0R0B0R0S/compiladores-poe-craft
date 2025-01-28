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
    '''comando : USAR ORBE EM ITEM'''
    p[0] = (p[2], p[4]) 

def p_error(p):
    print("Comando inválido!")

# Construir o parser
parser = yacc.yacc()