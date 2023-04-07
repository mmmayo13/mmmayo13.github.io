import sly

class DataLangLexer(sly.Lexer):

    # Define the token names for your language
    tokens = { 
        ID, INTEGER, FLOAT, STRING,
        PLUS, MINUS, TIMES, DIVIDE, ASSIGN,
        EQ, NE, LT, LE, GT, GE,
        LPAREN, RPAREN, LBRACE, RBRACE, LBRACK, RBRACK, COMMA, SEMI,
        IF, ELSE, WHILE, FOR, RETURN, FUNC, CLASS, LET, CONST, IMPORT,
        AND, OR, NOT
    }

    # Define literals that don't need a token name
    literals = {'(', ')', '[', ']', '{', '}', ',', ';'}

    # Define regular expressions for each token
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['for'] = FOR
    ID['return'] = RETURN
    ID['func'] = FUNC
    ID['class'] = CLASS
    ID['let'] = LET
    ID['const'] = CONST
    ID['import'] = IMPORT
    ID['and'] = AND
    ID['or'] = OR
    ID['not'] = NOT

    INTEGER = r'\d+'
    FLOAT = r'\d+\.\d+'
    STRING = r'\".*?\"'

    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r':='

    EQ = r'=='
    NE = r'!='
    LT = r'<'
    LE = r'<='
    GT = r'>'
    GE = r'>='

    # Define whitespace and comments to be ignored by the lexer
    ignore = ' \t'
    ignore_comment = r'\#.*'

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print(f"Illegal character '{t.value[0]}' at line {self.lineno}")
        self.index += 1

