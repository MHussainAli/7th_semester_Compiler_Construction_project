def pretty(tree, indent=0):
    if not isinstance(tree,tuple): return ' '*indent+str(tree)
    label,children=tree; lines=[' '*indent+label]
    for c in children: lines.append(pretty(c,indent+2))
    return '\n'.join(lines)
