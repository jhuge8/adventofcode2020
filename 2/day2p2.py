import fileinput

def valid(l):
    n,m,c,w = l.split()
    return (w[int(n)-1] == c) + (w[int(m)-1] == c) == 1

print(sum(map(valid, [l.replace('-',' ').replace(':',' ') for l in fileinput.input()])))

