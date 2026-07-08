class RecursiveDescentParser:
    """Parser for E -> T {+ T}, T -> F {* F}, F -> (E) | id | number."""
    def __init__(self,tokens): self.tokens=tokens; self.i=0
    def peek(self): return self.tokens[self.i] if self.i<len(self.tokens) else '$'
    def eat(self,x):
        if self.peek()!=x: raise SyntaxError(f'Expected {x}, got {self.peek()}')
        self.i+=1
    def expression(self):
        children=[self.term()]
        while self.peek()=='+': self.eat('+'); children += ['+',self.term()]
        return ('E',children)
    def term(self):
        children=[self.factor()]
        while self.peek()=='*': self.eat('*'); children += ['*',self.factor()]
        return ('T',children)
    def factor(self):
        if self.peek()=='(':
            self.eat('('); x=self.expression(); self.eat(')'); return ('F',['(',x,')'])
        x=self.peek(); self.i+=1; return ('F',[x])
    def parse(self):
        tree=self.expression()
        if self.peek()!='$': raise SyntaxError(f'Unexpected token {self.peek()}')
        return tree
