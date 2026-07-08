class TargetCodeGenerator:
    def generate(self,instructions):
        asm=[]
        for i in instructions:
            if i.op=="=": asm += [f"LOAD R1, {i.arg1}",f"STORE {i.result}, R1"]
            elif i.op in {"+","-","*","/"}:
                op={"+":"ADD","-":"SUB","*":"MUL","/":"DIV"}[i.op]; asm += [f"LOAD R1, {i.arg1}",f"{op} R1, {i.arg2}",f"STORE {i.result}, R1"]
            elif i.op=="print": asm.append(f"PRINT {i.arg1}")
        return asm
