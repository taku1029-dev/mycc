import sys
import os
import string
from enum import Enum, auto

class MyPreprocessor: 
    class DirectiveType(Enum):
        INCLUDE = auto()
        DEFINE = auto()
        IFDEF = auto()
        IFNDEF = auto()
        IF = auto()
        ELSE = auto()
        ENDIF = auto()
        UNDEF = auto()

    skipped_chars: tuple = (
        ' ', '\t', '\n', '\r', '\v', '\f'
    )


    def __init__(self, file_path: str):
        
        self.current_index = 0
        self.file_size = 0
        self.current_line: int = 0
        self.source_text: str = ""
        self.lf_split_source: list[str] = []
        
        with open(file_path) as f:
            self.source_text = f.read()
        
        self.file_size = len(self.source_text)
        self.lf_split_source = self.source_text.split('\n')
        for line in self.lf_split_source:
            print(line)
    # def removeBlanks(self):
    # # Check if the first letter is #
    # def isDirective(self, line_num):
    #
    # def process_define(self):
    # def process_undef(self):
    # def process_include(self):
    # def process_else(self):
    # def process_eliff(self):
    # def process_endif(self):
    # def process_line_comment(self):
    # def process_block_comment(self):
    # def preprocess(lines: list[str]) -> str:

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
        preprocessor = MyPreprocessor(sys.argv[1])
        # preprocessed: str = preprocessor.preprocess()
        # print(preprocessed)

if __name__ == "__main__":
    main()
