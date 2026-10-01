import sys

R = ["Norte", "Sur", "Centro", "Occidente"]


def f(a):
    d = open(a).read().split("\n")
    r = []
    for x in d[1:]:
        if x == "":
            continue
        r.append(x.split(","))
    t = {}
    g = {k: [0, 0] for k in R}
    for i in range(len(r) - 1):
        k = r[i][1]
        if k not in t:
            t[k] = [0, 0]
        m = float(r[i][5])
        t[k][0] += m
        t[k][1] += 1
        g[r[i][2]][0] += m
        g[r[i][2]][1] += 1
    s = sorted(t.items(), key=lambda z: str(z[1][0]), reverse=True)
    print("TOP VENDEDORES")
    n = 1
    for k, v in s[:3]:
        print(n, k, v[0], v[1])
        n += 1
    print("TICKET PROMEDIO POR REGION")
    for k in R:
        print(k, g[k][0] / g[k][1])
    print("TOTAL", sum(v[0] for v in t.values()))


if __name__ == "__main__":
    f(sys.argv[1])
