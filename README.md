# Compiler Construction Studio

Educational Mini Compiler aligned with the supplied Compiler Construction outline.

## Pipeline
Source Code -> Lexical Analysis -> Syntax/Grammar Tools -> Semantic Analysis -> Three Address Code -> Optimization -> Target Code

## Covered Topics
- Compiler phases and passes
- Lexical analysis and tokenization
- Regular-expression concepts
- NFA -> DFA conversion
- DFA minimization
- Context-free grammar
- FIRST and FOLLOW
- Left factoring
- LL(1) predictive parsing
- Recursive-descent parsing
- Parse-tree representation
- Symbol table and semantic checks
- Three-address code and quadruples
- Constant folding and algebraic simplification
- Dead-code analysis scaffold
- Simple target-code generation

## Google Colab
Open `notebooks/Compiler_Construction_Studio.ipynb`. In Colab, upload/clone the repository and run the cells.

## Local
```bash
pip install -r requirements.txt
python demo.py
```

Example source:
```text
int a = 10;
int b = 20;
int c = a + b * 2;
print(c);
```
