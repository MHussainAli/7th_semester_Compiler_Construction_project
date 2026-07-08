def left_factor(productions):
    """One-pass left factoring. Productions use lists of symbols."""
    result={}; counter=1
    for A,alts in productions.items():
        groups={}
        for alt in alts: groups.setdefault(alt[0] if alt else 'ε',[]).append(alt)
        result[A]=[]
        for first,group in groups.items():
            if len(group)==1: result[A].append(group[0])
            else:
                name=f"{A}'{counter}"; counter+=1; result[A].append([first,name])
                result[name]=[g[1:] if len(g)>1 else ['ε'] for g in group]
    return result
