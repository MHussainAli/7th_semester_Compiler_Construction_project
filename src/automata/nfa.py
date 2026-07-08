from dataclasses import dataclass, field
from collections import deque

@dataclass
class NFA:
    start: int
    accepts: set
    transitions: dict = field(default_factory=dict)
    def add(self, src, symbol, dst):
        self.transitions.setdefault((src, symbol), set()).add(dst)

def epsilon_closure(nfa, states):
    result=set(states); q=deque(states)
    while q:
        s=q.popleft()
        for dst in nfa.transitions.get((s,'ε'), set()):
            if dst not in result:
                result.add(dst); q.append(dst)
    return frozenset(result)

def regex_to_nfa(pattern):
    """Thompson construction for literals, |, concatenation, *, and parentheses."""
    def postfix(regex):
        out=[]; ops=[]; prev=None
        prec={'|':1,'.':2,'*':3}
        def atom(c): return c not in '|*().'
        for c in regex:
            if atom(c) or c=='(':
                if prev is not None and (atom(prev) or prev in ')*'):
                    while ops and ops[-1]!='(' and prec[ops[-1]]>=2: out.append(ops.pop())
                    ops.append('.')
                if c=='(': ops.append(c)
                else: out.append(c)
            elif c==')':
                while ops and ops[-1]!='(': out.append(ops.pop())
                if ops: ops.pop()
            elif c=='*': out.append(c)
            elif c=='|':
                while ops and ops[-1]!='(' and prec[ops[-1]]>=1: out.append(ops.pop())
                ops.append(c)
            prev=c
        while ops: out.append(ops.pop())
        return out
    nfa=NFA(0,set()); counter=0
    def new():
        nonlocal counter; x=counter; counter+=1; return x
    stack=[]
    for c in postfix(pattern):
        if c not in '|.*':
            a,b=new(),new(); nfa.add(a,c,b); stack.append((a,{b}))
        elif c=='.':
            b=stack.pop(); a=stack.pop()
            for e in a[1]: nfa.add(e,'ε',b[0])
            stack.append((a[0],b[1]))
        elif c=='|':
            b=stack.pop(); a=stack.pop(); s,e=new(),new()
            nfa.add(s,'ε',a[0]); nfa.add(s,'ε',b[0])
            for x in a[1]: nfa.add(x,'ε',e)
            for x in b[1]: nfa.add(x,'ε',e)
            stack.append((s,{e}))
        else:
            a=stack.pop(); s,e=new(),new(); nfa.add(s,'ε',a[0]); nfa.add(s,'ε',e)
            for x in a[1]: nfa.add(x,'ε',a[0]); nfa.add(x,'ε',e)
            stack.append((s,{e}))
    start,accepts=stack.pop(); nfa.start=start; nfa.accepts=accepts; return nfa

def nfa_to_dfa(nfa):
    alphabet={sym for (_,sym) in nfa.transitions if sym!='ε'}
    start=epsilon_closure(nfa,{nfa.start}); states=[start]; ids={start:0}; trans={}
    for current in states:
        cid=ids[current]
        for sym in sorted(alphabet):
            moved=set()
            for s in current: moved |= nfa.transitions.get((s,sym),set())
            if not moved: continue
            target=epsilon_closure(nfa,moved)
            if target not in ids: ids[target]=len(ids); states.append(target)
            trans[(cid,sym)]=ids[target]
    accepts={ids[s] for s in states if s & nfa.accepts}
    return {'start':0,'states':set(range(len(states))),'accepts':accepts,'transitions':trans}
