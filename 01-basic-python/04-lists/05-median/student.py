def median(ns):
    ns = sorted(ns)
    if len(ns) % 2 == 0:
        return (ns[len(ns) // 2 - 1] + ns[len(ns) // 2]) / 2        
    else:
        return ns[len(ns) // 2]