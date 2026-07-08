def to_quadruples(instructions):
    return [(i.op,i.arg1,i.arg2,i.result) for i in instructions]
