from src.parser.grammar import Grammar
def test_first_follow():
    g=Grammar({'E':[['T','E\'']],"E'":[['+','T',"E'"],['ε']], 'T':[['id']]},'E')
    assert 'id' in g.first()['E'] and '$' in g.follow()['E']
