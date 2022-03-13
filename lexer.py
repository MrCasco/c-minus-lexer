def reset(lexem, token):
    print(lexem, token)
    return '', 0

def getToken(imprime=True):
    table = [
        [1, 3, 12, 18, 13, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 19, 0],
        [1]+[2]*17,
        [0]*18,
        [4, 3]+[4]*16,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18,
        [0]*18
    ]
    s = 'int gcd (int u ,int v ){ }$'
    blank = ' \n\t$'
    digit = '0123456789'
    letter = 'acbdefghijklmnopqrstuvwxyz'+'acbdefghijklmnopqrstuvwxyz'.upper()

    state = 0
    p = 0
    lexem = ''
    token = ''
    # import ipdb; ipdb.set_trace()
    while (s[p] != '$' or (s[p] == '$' and state != 0)):
        char = s[p]
        if char in letter:
            col = 0
        elif char in blank:
            col = 17
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

        state = table[state][col]

        if state == 2:
            token = 'ID'
            lexem, state = reset(lexem, token)
        elif state == 4:
            token = 'NUM'
            lexem, state = reset(lexem, token)
        elif state == 5:
            token = 'PLUS'
            lexem = '+'
            lexem, state = reset(lexem, token)
        elif state == 6:
            token = 'MINUS'
            lexem = '-'
            lexem, state = reset(lexem, token)
        elif state == 7:
            token = 'PLUS'
            lexem = '*'
            lexem, state = reset(lexem, token)
        elif state == 8:
            token = 'DIV'
            lexem = '/'
            lexem, state = reset(lexem, token)
        elif state == 9:
            token = 'LESSTHAN'
            lexem = '<'
            lexem, state = reset(lexem, token)
        elif state == 10:
            token = 'GREATERTHAN'
            lexem += '>'
            lexem, state = reset(lexem, token)
        elif state == 11:
            token = 'EQUALS'
            lexem += '='
            lexem, state = reset(lexem, token)
        elif state == 12:
            token = 'OPENBRACKET'
            lexem += '['
            lexem, state = reset(lexem, token)
        elif state == 13:
            token = 'CLOSEBRACKET'
            lexem = ']'
            lexem, state = reset(lexem, token)
        elif state == 14:
            token = 'OPENPAR'
            lexem = '('
            lexem, state = reset(lexem, token)
        elif state == 15:
            token = 'CLOSEPAR'
            lexem = ')'
            lexem, state = reset(lexem, token)
        elif state == 16:
            token = 'OPENCURLY'
            lexem = '{'
            lexem, state = reset(lexem, token)
        elif state == 17:
            token = 'CLOSECURLY'
            lexem = '}'
            lexem, state = reset(lexem, token)
        elif state == 18:
            token = 'COMA'
            lexem = ','
            lexem, state = reset(lexem, token)
        elif state == 19:
            token = 'SEMICOLON'
            lexem = ';'
            lexem, state = reset(lexem, token)
        p += 1

        if char == '$':
            p -= 1
        if state != 0:
            lexem += char

getToken()
