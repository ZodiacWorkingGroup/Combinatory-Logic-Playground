from UtopiaLexer import *

COMBINATOR = 'COMB'
PAREN = 'PAREN'
RESERVED = 'RES'


def lexline(line):
    lex = lexer()

    lex.add_token_expr(r"^[\s]", None)
    lex.add_token_expr(r"import", RESERVED)
    lex.add_token_expr(r"=", RESERVED)
    lex.add_token_expr(r"[()]", PAREN)
    lex.add_token_expr(r"[A-Z][a-z0-9_*]*", COMBINATOR)

    return lex.lex(line)


def lexscript(script):
    return [lexline(x) for x in script.split('\n')]

if __name__ == '__main__':
    print(lexscript(input()))
    input()
