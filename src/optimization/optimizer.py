import re
class Optimizer:
    def optimize(self,instructions):
        out=[]
        for ins in instructions:
            if ins.op in {"+","-","*","/"} and re.fullmatch(r"-?\d+(\.\d+)?",ins.arg1 or "") and re.fullmatch(r"-?\d+(\.\d+)?",ins.arg2 or ""):
                a=float(ins.arg1); b=float(ins.arg2); value={"+":a+b,"-":a-b,"*":a*b,"/":a/b}[ins.op]
                value=int(value) if value.is_integer() else value; out.append(type(ins)("=",str(value),result=ins.result))
            elif ins.op=="+" and ins.arg2=="0": out.append(type(ins)("=",ins.arg1,result=ins.result))
            elif ins.op=="*" and ins.arg2=="1": out.append(type(ins)("=",ins.arg1,result=ins.result))
            else: out.append(ins)
        return out
