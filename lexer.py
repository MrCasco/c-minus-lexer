from globalTypes import *

def globales(programa, posicion, progLong):
    global s
    global p
    global lng

    s = programa
    p = posicion
    lng = progLong

def reset(lexem, token):
    print(lexem, token)
    return '', 0

def getToken(imprime=True):
    table = [
        [1, 3, 12, 18, 13, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 19, 20, 0],
        [1]+[2]*19,
        [0]*20,
        [4, 3]+[4]*18,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [21]*11+[22]+[21]*8,
        [23]*11+[24]+[23]*8,
        [25]*11+[26]+[25]*8,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [27]*19+[28],
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20,
        [0]*20
    ]
    reserved = {
        'else': TokenType.ELSE,
        'if': TokenType.IF,
        'int': TokenType.INT,
        'return': TokenType.RETURN,
        'void': TokenType.VOID,
        'while': TokenType.WHILE
    }
    # s = '1+1$'
    # s = 'int gcd(int u, int v){ <=,,,, }$'
    s = ' >=== >= hh 7 void !=$'

    # s = open('test.c', 'r')
    # s = s.read() + '$'     # lee todo el archivo a compilar

    blank = ' \n\t$'
    digit = '0123456789'
    letter = 'acbdefghijklmnopqrstuvwxyz'+'acbdefghijklmnopqrstuvwxyz'.upper()

    state = 0
    p = 0
    lexem = ''
    token = ''

    tokens = []
    # import ipdb; ipdb.set_trace()
    while (s[p] != '$' or (s[p] == '$' and state != 0)):
        char = s[p]
        if char in letter:
            col = 0
        elif char in blank:
            col = 18
        elif char in digit:
            col = 1
        elif char == '[':
            col = 2
        elif char == ',':
            col = 3
        elif char == ']':
            col = 4
        elif char == '+':
            col = 5
        elif char == '-':
            col = 6
        elif char == '*':
            col = 7
        elif char == '/':
            col = 8
        elif char == '<':
            col = 9
        elif char == '>':
            col = 10
        elif char == '=':
            col = 11
        elif char == '(':
            col = 12
        elif char == ')':
            col = 13
        elif char == '{':
            col = 14
        elif char == '}':
            col = 15
        elif char == ';':
            col = 16
        elif char == '!':
            col = 17

        state = table[state][col]

        if state == 2:
            p -= 1
            if lexem in reserved:
                token = reserved[lexem]
            else:
                token = TokenType.ID
            lexem, state = reset(lexem, token)
        elif state == 4:
            p -= 1
            token = TokenType.NUM
            lexem, state = reset(lexem, token)
        elif state == 5:
            token = TokenType.PLUS
            lexem = '+'
            lexem, state = reset(lexem, token)
        elif state == 6:
            token = TokenType.MINUS
            lexem = '-'
            lexem, state = reset(lexem, token)
        elif state == 7:
            token = TokenType.TIMES
            lexem = '*'
            lexem, state = reset(lexem, token)
        elif state == 8:
            token = TokenType.DIV
            lexem = '/'
            lexem, state = reset(lexem, token)
        elif state == 12:
            token = TokenType.OPENBRACKET
            lexem += '['
            lexem, state = reset(lexem, token)
        elif state == 13:
            token = TokenType.CLOSEBRACKET
            lexem = ']'
            lexem, state = reset(lexem, token)
        elif state == 14:
            token = TokenType.OPENPAR
            lexem = '('
            lexem, state = reset(lexem, token)
        elif state == 15:
            token = TokenType.CLOSEBRACKET
            lexem = ')'
            lexem, state = reset(lexem, token)
        elif state == 16:
            token = TokenType.OPENCURLY
            lexem = '{'
            lexem, state = reset(lexem, token)
        elif state == 17:
            token = TokenType.CLOSECURLY
            lexem = '}'
            lexem, state = reset(lexem, token)
        elif state == 18:
            token = TokenType.COMMA
            lexem = ','
            lexem, state = reset(lexem, token)
        elif state == 19:
            token = TokenType.SEMICOLON
            lexem = ';'
            lexem, state = reset(lexem, token)
        elif state == 21:
            token = TokenType.LESSTHAN
            lexem = '<'
            lexem, state = reset(lexem, token)
        elif state == 22:
            token = TokenType.LEQ
            lexem = '<='
            lexem, state = reset(lexem, token)
        elif state == 23:
            token = TokenType.GREATERTHAN
            lexem = '>'
            lexem, state = reset(lexem, token)
        elif state == 24:
            token = TokenType.GEQ
            lexem = '>='
            lexem, state = reset(lexem, token)
        elif state == 25:
            token = TokenType.EQUALS
            lexem = '='
            lexem, state = reset(lexem, token)
        elif state == 26:
            token = TokenType.EQEQ
            lexem = '=='
            lexem, state = reset(lexem, token)
        elif state == 27:
            token = TokenType.ERROR
            lexem = '!'
            lexem, state = reset(lexem, token)
        elif state == 28:
            token = TokenType.DIFF
            lexem = '!='
            lexem, state = reset(lexem, token)
        else:
            token = TokenType.ERROR
            lexem, state = reset(lexem, token)
        p += 1

        if state != 0:
            lexem += char
        else:
            tokens.append(token)
    return tokens + [TokenType.ENDFILE]

getToken()
