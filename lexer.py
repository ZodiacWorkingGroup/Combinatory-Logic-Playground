from UtopiaLexer import *

COMBINATOR = 'COMB'
PAREN = 'PAREN'

def lexscript(script):
    lex = lexer()

    lex.add_token_expr(r"^[\s]", None)
    lex.add_token_expr(r"[()]", PAREN)
    lex.add_token_expr(r"[A-Z][a-z0-9_*]*", COMBINATOR)

    return lex.lex(script)

if __name__ == '__main__':
    print(lexscript(input()))
    input()
