import fileinput
t = [[0 for i in range(8)] for j in range(128)]
L = [l.replace('B','1').replace('F','0').replace('L','0').replace('R','1') for l in fileinput.input()]
L = [(int(l[:7],2), int(l[7:],2)) for l in L]

for (r,c) in L:
    t[r][c] = 1

inlist = lambda i: t[i // 8][i % 8]

for c in range(8):
    for r in range(1,127):
        if not t[r][c]:
            i = r * 8 + c
            if inlist(i+1) and inlist(i-1):
                print((r*8+c))
