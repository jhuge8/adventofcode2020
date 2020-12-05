import fileinput

L = ("".join([l.replace('\n',' ') for l in fileinput.input()])).split('  ')
L[-1]=L[-1][:-1]
L = [eval("{'%s'}" % (l.replace(":","':'").replace(" ","','"))) for l in L]

def test(l,v,f):
    if v not in l:
        return False
    try:
        return f(l[v])
    except:
        return False

print(sum([(test(l,'byr',lambda x: (len(x) == 4) and (1920 <= int(x) <= 2002)) and
    test(l,'iyr',lambda x: (len(x) == 4) and (2010 <= int(x) <= 2020)) and
    test(l,'eyr',lambda x: (len(x) == 4) and (2020 <= int(x) <= 2030)) and
    test(l,'hgt',lambda x: (150 <= int(x[:-2]) <= 193) if 'cm' in x else ((59 <= int(x[:-2]) <= 76) and 'in' in x)) and
    test(l,'hcl',lambda x: (x[0] == '#') and (len(x) == 7) and x[1:].isalnum()) and
    test(l,'ecl',lambda x: x in "amb blu brn gry grn hzl oth".split()) and
    test(l,'pid',lambda x: (len(x) == 9) and x.isnumeric())) for l in L]))
