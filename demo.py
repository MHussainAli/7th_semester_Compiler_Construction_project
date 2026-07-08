from src.lexer.lexer import Lexer
from src.semantic.semantic_analyzer import SemanticAnalyzer
from src.intermediate.three_address_code import TACGenerator
from src.optimization.optimizer import Optimizer
from src.codegen.target_code import TargetCodeGenerator
source='''int a = 10;\nint b = 20;\nint c = a + b * 2;\nprint(c);'''
print('=== COMPILER CONSTRUCTION STUDIO ===\nSOURCE:\n',source)
tokens=Lexer(source).tokenize(); print('\n=== TOKENS ==='); [print(t) for t in tokens]
sem=SemanticAnalyzer(); print('\n=== SYMBOL TABLE ===',sem.analyze(tokens))
tac=TACGenerator(tokens).generate(); print('\n=== THREE ADDRESS CODE ==='); [print(x) for x in tac]
opt=Optimizer().optimize(tac); print('\n=== OPTIMIZED CODE ==='); [print(x) for x in opt]
print('\n=== TARGET CODE ==='); [print(x) for x in TargetCodeGenerator().generate(opt)]
