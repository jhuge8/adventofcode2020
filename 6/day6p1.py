import fileinput

L = "".join([l for l in fileinput.input()]).split("\n\n")
L = [list(filter(bool,l.split("\n"))) for l in L]
L = [list(map(list,l)) for l in L]
L = [ [y for x in l for y in x] for l in L]

print(sum([len(set(l)) for l in L]))
