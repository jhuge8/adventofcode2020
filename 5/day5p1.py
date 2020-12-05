import fileinput
L = [l.replace('B','1').replace('F','0').replace('L','0').replace('R','1') for l in fileinput.input()]
print(max([(int(l[:7],2)*8 + int(l[7:],2)) for l in L]))
