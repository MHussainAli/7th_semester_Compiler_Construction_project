EPSILON="ε"
class Grammar:
    def __init__(self,productions,start):
        self.productions=productions; self.start=start; self.nonterminals=set(productions)
        self.terminals={x for rhs in productions.values() for prod in rhs for x in prod if x not in self.nonterminals and x!=EPSILON}
    def first(self):
        first={n:set() for n in self.nonterminals}; changed=True
        while changed:
            changed=False
            for A,prods in self.productions.items():
                for prod in prods:
                    nullable=True
                    for x in prod:
                        if x==EPSILON: first[A].add(EPSILON); nullable=False; break
                        if x not in self.nonterminals: first[A].add(x); nullable=False; break
                        before=len(first[A]); first[A]|=first[x]-{EPSILON}; changed|=len(first[A])>before
                        if EPSILON not in first[x]: nullable=False; break
                    if nullable: before=len(first[A]); first[A].add(EPSILON); changed|=len(first[A])>before
        return first
    def follow(self):
        first=self.first(); follow={n:set() for n in self.nonterminals}; follow[self.start].add("$"); changed=True
        while changed:
            changed=False
            for A,prods in self.productions.items():
                for prod in prods:
                    trailer=set(follow[A])
                    for x in reversed(prod):
                        if x in self.nonterminals:
                            before=len(follow[x]); follow[x]|=trailer; changed|=len(follow[x])>before
                            trailer=(trailer|first[x]-{EPSILON}) if EPSILON in first[x] else set(first[x])
                        elif x!=EPSILON: trailer={x}
        return follow
