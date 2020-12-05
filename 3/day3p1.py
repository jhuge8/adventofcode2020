import fileinput

L = [l for l in fileinput.input()]
f = lambda a,b: sum([(x == '#') for x in
                    [L[b*i][(a*i) % (len(L[0])-1)] for i in range(len(L) // b)]])

print(f(1,1)*f(3,1)*f(5,1)*f(7,1)*f(1,2))
