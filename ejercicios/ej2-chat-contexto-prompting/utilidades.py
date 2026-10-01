import re


def f1(l):
    r = {}
    for x in l:
        k = x["categoria"]
        r[k] = r.get(k, 0) + x["precio"] * x["stock"]
    return r


def f2(s):
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    return re.sub(r"\s+", "-", s)


def f3(l, n):
    # promedio móvil de ventana n
    out = []
    for i in range(len(l)):
        v = l[i : i + n]
        out.append(sum(v) / n)
    return out


def f4(precio, pct):
    return precio - precio * pct / 100
