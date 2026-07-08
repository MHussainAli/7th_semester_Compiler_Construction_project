def minimize_dfa(dfa):
    states=set(dfa['states']); accepts=set(dfa['accepts']); alphabet={s for _,s in dfa['transitions']}
    partitions=[p for p in (accepts,states-accepts) if p]
    changed=True
    while changed:
        changed=False; new=[]
        for group in partitions:
            buckets={}
            for q in group:
                sig=tuple(next((i for i,p in enumerate(partitions) if dfa['transitions'].get((q,a),-1) in p),-1) for a in sorted(alphabet))
                buckets.setdefault(sig,set()).add(q)
            new.extend(buckets.values()); changed |= len(buckets)>1
        partitions=new
    mapping={q:i for i,p in enumerate(partitions) for q in p}
    return {'start':mapping[dfa['start']], 'states':set(range(len(partitions))), 'accepts':{mapping[q] for q in accepts},
            'transitions':{(mapping[q],a):mapping[r] for (q,a),r in dfa['transitions'].items()}}
