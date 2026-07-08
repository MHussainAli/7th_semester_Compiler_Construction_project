import re
from .token import Token
class Lexer:
    KEYWORDS={"int","float","if","else","while","return","print"}
    SPEC=[("COMMENT",r"//[^\n]*"),("FLOAT",r"\d+\.\d+"),("INTEGER",r"\d+"),("ID",r"[A-Za-z_][A-Za-z0-9_]*"),("STRING",r'"[^"\n]*"'),("OP",r"==|!=|<=|>=|[+\-*/%=<>]"),("SEP",r"[;,(){}]"),("SKIP",r"[ \t\r]+"),("NEWLINE",r"\n"),("MISMATCH",r".")]
    MASTER=re.compile("|".join(f"(?P<{n}>{p})" for n,p in SPEC))
    def __init__(self,source): self.source=source
    def tokenize(self):
        out=[]; line=1; col=1
        for m in self.MASTER.finditer(self.source):
            kind,text=m.lastgroup,m.group()
            if kind=="NEWLINE": line+=1; col=1; continue
            if kind in {"SKIP","COMMENT"}: col+=len(text); continue
            if kind=="ID": kind="KEYWORD" if text in self.KEYWORDS else "ID"
            if kind=="MISMATCH": raise SyntaxError(f"Unexpected character {text!r} at {line}:{col}")
            out.append(Token(kind,text,line,col)); col+=len(text)
        out.append(Token("EOF","",line,col)); return out
