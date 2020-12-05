import fileinput

def valid(l):
    n,m,c,w = l.split()
    return int(n) <= w.count(c) <= int(m)

print(sum(map(valid, [l.replace('-',' ').replace(':',' ') for l in fileinput.input()])))
