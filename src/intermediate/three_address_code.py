class TAC:
    def __init__(self,op,arg1="",arg2="",result=""): self.op,self.arg1,self.arg2,self.result=op,arg1,arg2,result
    def __str__(self):
        if self.op=="=": return f"{self.result} = {self.arg1}"
        if self.op=="print": return f"print {self.arg1}"
        return f"{self.result} = {self.arg1} {self.op} {self.arg2}"
class TACGenerator:
    def __init__(self,tokens): self.tokens=[t for t in tokens if t.type!="EOF"]; self.temp=0; self.instructions=[]
    def new_temp(self): self.temp+=1; return f"t{self.temp}"
    def generate(self):
        i=0
        while i<len(self.tokens):
            if self.tokens[i].lexeme=="print":
                if i+2<len(self.tokens): self.instructions.append(TAC("print",self.tokens[i+2].lexeme)); i+=4; continue
            if self.tokens[i].lexeme in {"int","float"} and i+3<len(self.tokens):
                target=self.tokens[i+1].lexeme; j=i+3; vals=[]
                while j<len(self.tokens) and self.tokens[j].lexeme!=";": vals.append(self.tokens[j].lexeme); j+=1
                while len(vals)>=3 and "*" in vals:
                    k=vals.index("*"); temp=self.new_temp(); self.instructions.append(TAC("*",vals[k-1],vals[k+1],temp)); vals[k-1:k+2]=[temp]
                while len(vals)>=3 and "+" in vals:
                    k=vals.index("+"); temp=self.new_temp(); self.instructions.append(TAC("+",vals[k-1],vals[k+1],temp)); vals[k-1:k+2]=[temp]
                if vals: self.instructions.append(TAC("=",vals[0],result=target))
                i=j+1; continue
            i+=1
        return self.instructions
