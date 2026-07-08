from .grammar import EPSILON
class LL1Parser:
    def __init__(self,grammar):
        self.g=grammar; self.first=grammar.first(); self.follow=grammar.follow(); self.table=self._build()
    def first_sequence(self,seq):
        result=set(); nullable=True
        for x in seq:
            if x==EPSILON: result.add(EPSILON); break
            if x not in self.g.nonterminals: result.add(x); nullable=False; break
            result|=self.first[x]-{EPSILON}
            if EPSILON not in self.first[x]: nullable=False; break
        if nullable: result.add(EPSILON)
        return result
    def _build(self):
        table={}
        for A,prods in self.g.productions.items():
            for prod in prods:
                fs=self.first_sequence(prod)
                for t in fs-{EPSILON}: table[(A,t)]=prod
                if EPSILON in fs:
                    for t in self.follow[A]: table[(A,t)]=prod
        return table
