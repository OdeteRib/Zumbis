def foo(l):
    return l in "snrbg"

def bar(l):
    return not foo(l)

def preposicao(p):
    return len(p) == 5 and bar(p[-1]) and 'q' not in p
def verbo(p):
    return len(p) >= 6 and bar(p[-1])

def verbo_primeira_pessoa(p):
    return verbo(p) and bar(p[0])

def cmp_googlon(p1, p2):
    v = 'jgptzmqskbclrhdfnvwx'
    for l1, l2 in zip(p1, p2):
        if v.index(l1) != v.index(l2):
            return v.index(l1) - v.index(l2)
    return len(p1) - len(p2)

def valor_numerico(p):
    v = 'jgptzmqskbclrhdfnvwx'
    vn = 0
    i = 0
    for c in p:
        vn += v.index(c) * (20 ** i)
        i += 1
    return vn
