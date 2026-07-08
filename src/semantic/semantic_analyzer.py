class SemanticAnalyzer:
    def __init__(self): self.symbols={}
    def analyze(self,tokens):
        i=0
        while i<len(tokens):
            t=tokens[i]
            if t.type=="KEYWORD" and t.lexeme in {"int","float"}:
                if i+1>=len(tokens) or tokens[i+1].type!="ID": raise SyntaxError("Expected identifier after type")
                name=tokens[i+1].lexeme
                if name in self.symbols: raise TypeError(f"Duplicate declaration: {name}")
                self.symbols[name]={"type":t.lexeme,"line":t.line,"initialized":False}; i+=2
                if i<len(tokens) and tokens[i].lexeme=="=": self.symbols[name]["initialized"]=True
            elif t.type=="ID" and t.lexeme not in self.symbols: raise NameError(f"Undeclared variable '{t.lexeme}' at line {t.line}")
            i+=1
        return self.symbols
