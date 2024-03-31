import sys
first = sys.argv[1]
#second = 'k'
xprint = lambda *args : None

from collections import defaultdict
import os

def print_last_two_lines(directory):
    sumbank = defaultdict(int)
    ct = defaultdict(int)
    tt = defaultdict(int)
    z= defaultdict(int)
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 2 and lines[-2].startswith(first):# and int(filename[11:13]) == 14 and int(filename[14:16]) >= 24:
                    xprint(f"{filename}:")
                    xprint(lines[-2].strip())
                    xprint(lines[-1].strip())
                    *_, l2 = lines[-2].strip().split()
                    name1 = lines[-1].split()[0][:10]
                    sumbank[name1] += int(l2)
                    if int(l2) < 0:
                        xprint('-')
                    elif int(l2) == 0:
                        xprint('0')
                        z[name1]+=1
                    else:
                        xprint('+')
                        ct[name1] += 1
                    tt[name1] += 1
                    xprint()
                    
    for k in tt:
        print(f'{first} against {k}:')
        print(first, 'wins', sumbank[k])
        print(ct[k], 'out of', tt[k])
        if z[k] != 0:
            print(z[k],'ties (zer0s)')

# Provide the directory path here
directory_path = "."
print_last_two_lines(directory_path)
