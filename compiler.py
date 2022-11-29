"""
    Luis Bodart A01635000
    Compiler using Lex-Yacc
"""

import sys

import ply.lex as lex
import ply.yacc as yacc
from ply.lex import LexToken
from ply.yacc import YaccProduction

from Node import Node

sys.path.insert(0, "..")

# Reserved words
reserved = {
    "int": "INTDCL",
    "float": "FLOATDCL",
    "boolean": "BOOLDCL",
    "print": "PRINT",
    "true": "BOOLVAL",
    "false": "BOOLVAL",
    "if": "IF",
    "elif": "ELIF",
    "else": "ELSE",
    "while": "WHILE",
    "for": "FOR",
    "and": "AND",
    "or": "OR"
}

# All valid tokens (terminal)
tokens = ('NAME', 'INUMBER', 'FNUMBER', 'LPAREN', 'RPAREN',
          'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POW',
          'EQ', 'NE', 'LT', 'LE', 'GT', 'GE'
          ) + tuple(set(reserved.values()))

# Literal words
literals = ('=', ';', '{', '}')

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POW = r'\^'

# Comparisons
t_EQ = r'=='  # Equal
t_NE = r'!='  # Not equal
t_LT = r'<'  # Less than
t_LE = r'<='  # Less equal
t_GT = r'>'  # Greater than
t_GE = r'>='  # Greater equal

# Ignored chars (spaces and tabs)
t_ignore = ' \t'


# LEX #

# Tokens Rules
# ID
def t_NAME(t: LexToken):
    r'[a-zA-Z_]+[a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'NAME')
    return t


# Float
def t_FNUMBER(t: LexToken):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


# Integer
def t_INUMBER(t: LexToken):
    r'\d+'
    t.value = int(t.value)
    return t


# Line numbers
def t_newline(t: LexToken):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Token error
def t_error(t: LexToken):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Lexer
lexer = lex.lex()


# YACC #
# Parsing rules
# Program (root)
def p_prog(p: YaccProduction):
    'prog : stmts'
    global abstractTree
    abstractTree = Node()
    abstractTree.type = 'root'
    abstractTree.childrens.extend(p[1])


# Recursion
def p_statements_recursion(p: YaccProduction):
    '''stmts : statement stmts
            | statement '''
    stmts = [p[1]]
    if len(p) == 3:
        stmts.extend(p[2])
    p[0] = stmts


# Declarations
def p_statement_declare_int(p: YaccProduction):
    '''statement : INTDCL NAME ";"
                | INTDCL NAME "=" expression ";" '''
    symbolsTable['table'][p[2]] = {'type': 'INT', 'value': 0}
    n = Node()
    n.type = 'INT_DLC'
    n.val = p[2]
    if len(p) == 6:
        symbolsTable['table'][p[2]]['value'] = p[4].val
        n.childrens.append(p[4])
    p[0] = n


def p_statement_declare_float(p: YaccProduction):
    '''statement : FLOATDCL NAME ";"
                | FLOATDCL NAME "=" expression ";" '''
    symbolsTable['table'][p[2]] = {'type': 'FLOAT', 'value': 0.0}
    n = Node()
    n.type = 'FLOAT_DLC'
    n.val = p[2]
    if len(p) == 6:
        symbolsTable['table'][p[2]]['value'] = p[4].val
        n.childrens.append(p[4])
    p[0] = n


def p_statement_declare_bool(p: YaccProduction):
    '''statement : BOOLDCL NAME ";"
                | BOOLDCL NAME "=" boolean_expression ";" '''
    symbolsTable['table'][p[2]] = {'type': 'BOOLEAN', 'value': False}
    n = Node()
    n.type = 'BOOL_DLC'
    n.val = p[2]
    if len(p) == 6:
        symbolsTable['table'][p[2]]['value'] = p[4].val
        n.childrens.append(p[4])
    p[0] = n


# Print
def p_statement_print(p: YaccProduction):
    'statement : PRINT expression ";"'
    n = Node()
    n.type = 'PRINT'
    n.childrens.append(p[2])
    p[0] = n


# Conditions
def p_statement_if(p: YaccProduction):
    '''statement : IF LPAREN boolean_expression RPAREN "{" stmts "}" elifs else '''
    n = Node()
    n.type = "IF"
    c = Node()
    c.type = 'CONDITION'
    c.childrens.append(p[3])
    b = Node()
    b.type = 'BLOCK'
    b.childrens.extend(p[6])
    n.childrens.append(c)
    n.childrens.append(b)
    if p[8]:
        n.childrens.extend(p[8])
    if p[9]:
        n.childrens.append(p[9])
    p[0] = n


# ELIF recursion
def p_elif_recursion(p: YaccProduction):
    '''elifs : elif elifs
            | elif '''
    if p[1]:
        elif_rec = [p[1]]
        if len(p) == 3:
            elif_rec.extend(p[2])
        p[0] = elif_rec


def p_elif(p: YaccProduction):
    '''elif : ELIF LPAREN boolean_expression RPAREN "{" stmts "}"
            | empty '''
    if len(p) == 8:
        n = Node()
        n.type = "ELIF"
        c = Node()
        c.type = 'CONDITION'
        c.childrens.append(p[3])
        b = Node()
        b.type = 'BLOCK'
        b.childrens.extend(p[6])
        n.childrens.append(c)
        n.childrens.append(b)
        p[0] = n


def p_else(p: YaccProduction):
    '''else : ELSE "{" stmts "}"
            | empty '''
    if len(p) == 5:
        n = Node()
        n.type = "ELSE"
        b = Node()
        b.type = 'BLOCK'
        b.childrens.extend(p[3])
        n.childrens.append(b)
        p[0] = n


# LOOPS
def p_statement_while(p: YaccProduction):
    '''statement : WHILE LPAREN boolean_expression RPAREN "{" stmts "}" '''
    n = Node()
    n.type = 'WHILE'
    c = Node()
    c.type = 'CONDITION'
    c.childrens.append(p[3])
    b = Node()
    b.type = 'BLOCK'
    b.childrens.extend(p[6])
    n.childrens.append(c)
    n.childrens.append(b)
    p[0] = n


def p_statement_for(p: YaccProduction):
    'statement : FOR LPAREN statement boolean_expression ";" step RPAREN "{" stmts "}"'
    n = Node()
    n.type = 'FOR'
    v = Node()
    v.type = 'VARIABLE'
    v.childrens.append(p[3])
    c = Node()
    c.type = 'CONDITION'
    c.childrens.append(p[4])
    s = Node()
    s.type = 'STEP'
    s.childrens.append(p[6])
    b = Node()
    b.type = 'BLOCK'
    b.childrens.extend(p[9])
    n.childrens.append(v)
    n.childrens.append(c)
    n.childrens.append(s)
    n.childrens.append(b)
    p[0] = n


# FOR step
def p_expression_step(p: YaccProduction):
    '''step : NAME PLUS "=" expression
            | NAME MINUS "=" expression
            | NAME TIMES "=" expression
            | NAME DIVIDE "=" expression
            | NAME PLUS PLUS
            | NAME MINUS MINUS
            | PLUS PLUS NAME
            | MINUS MINUS NAME'''
    n = Node()
    s = Node()
    s.type = 'ID'
    n.childrens.append(s)
    if len(p) == 4:
        if p[1] in ['+', '-']:
            n.type = p[1] * 2
            s.val = p[3]
        else:
            n.type = p[2] * 2
            s.val = p[1]
    elif len(p) == 5:
        n.type = p[2] + p[3]
        s.val = p[1]
        n.childrens.append(p[4])
    p[0] = n


# Assignment
def p_statement_assign(p: YaccProduction):
    'statement : NAME "=" expression ";"'
    if p[1] not in symbolsTable["table"]:
        print("You must declare a variable before using it")
    n = Node()
    n.type = 'ASSIGN'
    if p[1] in symbolsTable["table"]:
        n1 = Node()
        n1.type = 'ID'
        n1.val = p[1]
        n.childrens.append(n1)
    else:
        print("Error undeclared variable")
    n.childrens.append(p[3])
    p[0] = n


# Expressions
# Group expressions ()
def p_expression_group(p: YaccProduction):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]


# Operations
def p_expression_binop(p: YaccProduction):
    '''expression : expression PLUS expression
                | expression MINUS expression
                | expression TIMES expression
                | expression DIVIDE expression
                | expression POW expression '''
    n = Node()
    n.type = 'OP'
    n.val = p[2]
    n.childrens.append(p[1])
    n.childrens.append(p[3])
    p[0] = n


# Int
def p_expression_inumber(p: YaccProduction):
    "expression : INUMBER"
    n = Node()
    n.type = 'INUMBER'
    n.val = int(p[1])
    p[0] = n


# Float
def p_expression_fnumber(p: YaccProduction):
    "expression : FNUMBER"
    n = Node()
    n.type = 'FNUMBER'
    n.val = float(p[1])
    p[0] = n


# Boolean
def p_expression_boolean(p: YaccProduction):
    "expression : boolean_expression"
    p[0] = p[1]


# Group boolean expressions ()
def p_boolean_expression_group(p: YaccProduction):
    'boolean_expression : LPAREN boolean_expression RPAREN'
    p[0] = p[2]


# Boolean expressions
def p_boolean_expression(p: YaccProduction):
    '''boolean_expression : boolean_expression AND boolean_expression
                        | boolean_expression OR boolean_expression
                        | comparison
                        | boolean_val '''
    if len(p) == 4:
        if p[2] in ['and', 'or']:
            n = Node()
            n.type = 'LOGICAL_OP'
            n.val = p[2]
            n.childrens.append(p[1])
            n.childrens.append(p[3])
            p[0] = n
        else:
            p[0] = p[2]
    else:
        p[0] = p[1]


# Boolean comparisons
def p_comparison(p: YaccProduction):
    '''comparison : expression EQ expression
                | expression NE expression
                | expression LT expression
                | expression LE expression
                | expression GT expression
                | expression GE expression '''
    n = Node()
    n.type = 'COMPARISON'
    n.val = p[2]
    n.childrens.append(p[1])
    n.childrens.append(p[3])
    p[0] = n


# Boolean value
def p_boolean_val(p: YaccProduction):
    '''boolean_val : boolexp
                    | NAME '''
    if isinstance(p[1], str):
        n = Node()
        n.type = 'ID'
        n.val = p[1]
        p[0] = n
    else:
        p[0] = p[1]


# Boolean
def p_bool_expression(p: YaccProduction):
    'boolexp : BOOLVAL'
    n = Node()
    n.type = 'BOOLVAL'
    n.val = (p[1] == 'true')
    p[0] = n


# ID
def p_expression_name(p: YaccProduction):
    "expression : NAME"
    if p[1] in symbolsTable["table"]:
        n = Node()
        n.type = 'ID'
        n.val = p[1]
        p[0] = n


# Lambda
def p_empty(p: YaccProduction):
    'empty :'
    pass


# Parser Errors
def p_error(p: LexToken):
    if p:
        print(p)
        print(f"Syntax error at line {p.lineno}, character '{p.type}'")
    else:
        print("Syntax error at EOF")


# Parser
parser = yacc.yacc(start="prog")

# Node Tree
abstractTree = None
# dictionary of names
symbolsTable = {
    "table": {},
    "parent": None
}

precedence = (
    ('left', 'AND', 'OR'),
    ('left', 'EQ', 'NE'),
    ('nonassoc', 'LT', 'LE', 'GT', 'GE'),  # Nonassociative operators
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'POW'),
    ('right', 'UMINUS'),  # Unary minus operator + -2
)

if __name__ == '__main__':
    f = open("input.txt")
    content = f.read()
    yacc.parse(content)
    if abstractTree:
        abstractTree.printTree()
    print(symbolsTable['table'])
