# mycc
This custom C compiler is inspired by ["**Writing a C Compiler**"](https://www.amazon.co.jp/-/en/Writing-Compiler-Programming-Language-Scratch/dp/1718500424) by NORA SANDLER

## Overview
This C compiler (toolchain) could be broken down into several stages as explained individually below:

### Preprocessor
It's designed to find directives for the preprocessor by reading file contents char by char to detect **'#'**, the beginning of each instruction, counting the current index number. There are several proprocess instructions are supported, following **include**, **define**.

### Lexer
Responsible for tokenization process, classified into multiple token types such as **ID**, **KEYWORD** for later stage of compilation, the **Parser**. Only a list of tokens are produced during the processs;

For example:

`
int main(){
  return 0;
}
`

[KEYWORD, ID, OPEN_PARENTHESIS, CLOSE_PARENTHESIS, OPEN_BRACKET, KEYWORD, CONSTANT, SEMICOLON, CLOSE_BRACKET]

### Parser
Verifies the grammer of the given tokens according to a list of **Production Rules** (Haven't impled yet)
### 
