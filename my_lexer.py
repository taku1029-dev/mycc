import sys
import os
import string
from enum import Enum


# ID: [a-zA-Z_]\w*\b
# Constant: [0-9]+\b
# Keywords: i.g) int keyword-> int\b
# Parenthesis/Braces: \(, \), {, }
# Semicolon: ;
class MyLexer: 
    class TokenType(Enum):
        ID = 1
        CONSTANT = 2
        KEYWORD = 3
        OPEN_PARENTHESIS = 4
        CLOSE_PARENTHESIS = 5
        OPEN_BRACKET = 6
        CLOSE_BRACKET = 7
        SEMICOLON = 8
        OPERATOR = 9

    keywords: tuple = (
        "char", "int", "long", "float", "double",
        "for", "while", "return", "break", "continue"
    )
    operators: tuple = (
        "+", "-", "*", "/", "%",
        "++", "--",
        "==", "!=", "<", ">", ">=", "<=",
        "&&", "||", "!",
        "&", "|", "^", "~", "<<", ">>",
        "=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>="
    )
    operator_chars: tuple = (
        "+", "-", "*", "/", "%",
        "<", ">",
        "!",
        "&", "|", "^", "~",
        "="
    )
    skipped_chars: tuple = (
        ' ', '\t', '\n', '\r', '\v', '\f'
    )
    current_index: int = 0
    source: str = ""
    file_size: int = 0
    tokens: list = []

    def __init__(self, file_path: str):
        self.current_index = 0
        with open(file_path) as f:
            self.source = f.read()
        self.file_size = len(self.source)
       
    def peek(self) -> str:
        # Boundary check
        if(self.current_index >= self.file_size-1):
            print("Reached EOF")
            return ""

        print(f"At index {self.current_index+1}: {self.source[self.current_index+1]}")
        return self.source[self.current_index+1]

    # Unecessary chars must be skipped beforehand
    def isKeyword(self, token: str) -> bool:
        if token in self.keywords:
            return True
        return False

    def readConstant(self) -> str:
        token: str = ""
        current: str = self.source[self.current_index]

        while current in string.digits:
            token += current
            self.advance()
            current = self.source[self.current_index]
        return token

    def readIdentifier(self) -> str:
        token: str = ""
        current: str = self.source[self.current_index]

        while current in string.digits+string.ascii_letters+"_":
            token += current
            self.advance()
            current = self.source[self.current_index]
        return token

    def readOperator(self) -> str:
        token: str = ""
        current: str = self.source[self.current_index]

        while current in self.operator_chars:
            token += current
            self.advance()
            current = self.source[self.current_index]
        return token

    def advance(self):
        if self.current_index < self.file_size:
            self.current_index += 1
        else:
            print("File reached EOF while self.advance()")

    def printTokenList(self):
        for token in self.tokens:
            print(token)
        
    def tokenize(self) -> list:
        # When empty file is processed
        if(self.source == ""):
            return []
        current: str = self.source[0]
        current_token: str

        while self.current_index < self.file_size:

            current_token = ""
            if(current in string.digits):
                current_token = self.readConstant()
                self.tokens.append(self.TokenType.CONSTANT)
            elif(current in string.ascii_letters+"_"):
                current_token = self.readIdentifier()
                if(self.isKeyword(current_token) == True):
                   self.tokens.append(self.TokenType.KEYWORD)
                else:
                    self.tokens.append(self.TokenType.ID)
            elif(current == "("):
                self.tokens.append(self.TokenType.OPEN_PARENTHESIS)
                self.advance()
            elif(current == ")"):
                self.tokens.append(self.TokenType.CLOSE_PARENTHESIS)
                self.advance()
            elif(current == "{"):
                self.tokens.append(self.TokenType.OPEN_BRACKET)
                self.advance()
            elif(current == "}"):
                self.tokens.append(self.TokenType.CLOSE_BRACKET)
                self.advance()
            elif(current == ";"):
                self.tokens.append(self.TokenType.SEMICOLON)
                self.advance()
            elif(current in self.operator_chars):
                current_token = self.readOperator()
                self.tokens.append(self.TokenType.OPERATOR)
            elif(current in self.skipped_chars):
                self.advance()
            else:
                print(f"Invalid Char: {current} found at {self.current_index}")
                self.advance()
            if(self.current_index < self.file_size):
                current = self.source[self.current_index]
            else:
                break
        return self.tokens

# Command line args
# argv[0]: file Path
# argv[1]: option1
# argv[2]: option2
def main():
    if os.path.exists(sys.argv[1]):
        print("File exists")
    else:
        print("File doesn't exist!")
    if(len(sys.argv) < 2):
        print("C program path not given!")
    else:
        print(f"Given file path: {sys.argv[1]}")
        lexer = MyLexer(sys.argv[1])
        tokens: list = lexer.tokenize()
        for token in tokens:
            print(token)

if __name__ == "__main__":
    main()
