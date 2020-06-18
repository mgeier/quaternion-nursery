def canonicalize_quaternion_sequence(seq):
    seq = iter(seq)
    for p in seq:
        if p.scalar < 0:
            p = -p
        break
    else:
        return
    yield p
    for q in seq:
        if p.dot(q) < 0:
            q = -q
        yield q
        p = q
