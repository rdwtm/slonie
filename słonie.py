from cmath import inf

n = int(input())
m = [int(x) for x in input().split()]
# Odejmuję 1 ze względu na indeksowanie w zadaniu od 1
a = [int(x) - 1 for x in input().split()]
b = [int(x) - 1 for x in input().split()]
p = [None] * n
# konstrukcja permutacji
for i in range(n):
    p[b[i]] = a[i]

# rozkład p na cykle proste
odw = [False for x in range(n)]
c = 0
C = []
for i in range(n):
    if not odw[i]:
        x = i
        d=[]
        while not odw[x]:
            odw[x] = True
            d.append(x) #składam listę cykli
            x = p[x]
        c += 1
        C.append(d[:]) # składam wszystkie cykle do listy

# wyznaczenie parametrów cykli
min_glob = inf
sumac = [None] * c
minc = [None] * c
for i in range(c):
    sumac[i] = 0
    minc[i] = inf
    for e in C[i]:
        sumac[i] = sumac[i] + m[e]
        minc[i] = min([minc[i],m[e]])
    min_glob = min([min_glob,minc[i]])

# Obliczanie wyniku
w = 0
for i in range(c):
    met1 = sumac[i] + (len(C[i]) - 2) * minc[i]
    met2 = sumac[i] + minc[i] + (len(C[i]) + 1) * min_glob
    w = w + min([met1, met2])
print(w)


     
