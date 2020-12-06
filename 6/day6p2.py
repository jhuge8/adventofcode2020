import fileinput

L = "".join([l for l in fileinput.input()]).split("\n\n")
L = [list(filter(bool,l.split("\n"))) for l in L]
L = [list(map(list,l)) for l in L]
L = [ (len(l),[y for x in l for y in x]) for l in L]
L = [ (n, l, set(l)) for (n,l) in L]
L = [ [(l.count(x) == n) for x in s] for (n,l,s) in L]
print(sum([sum(l) for l in L]))
