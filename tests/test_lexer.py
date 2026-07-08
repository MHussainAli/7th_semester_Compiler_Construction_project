from src.lexer.lexer import Lexer
def test_basic_tokens():
    t=Lexer('int x = 10;').tokenize()
    assert t[0].type=='KEYWORD' and t[1].type=='ID' and t[3].type=='INTEGER'
