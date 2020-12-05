import fileinput, functools

R="byr ecl eyr hcl hgt iyr pid".split()
L = ("".join([l.replace('\n',' ') for l in fileinput.input()])).split('  ')
L[-1]=L[-1][:-1]
L = [eval("{'%s'}" % (l.replace(":","':'").replace(" ","','"))) for l in L]

print(sum([functools.reduce(lambda a,b: (a in l) and b, R + [True]) for l in L]))
    
