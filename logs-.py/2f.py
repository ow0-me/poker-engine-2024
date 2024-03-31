import sys
first, second = sys.argv[1:3]
#xprint = print
xprint = lambda *args: None
#if sys.argv[3:] == ['noxp']:
    #xprint = lambda *args: None

import os

def print_last_two_lines(directory):
    sumbank = 0
    ct = 0
    tt = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 2 and lines[-2].startswith(first) and lines[-1].startswith(second):
                # and int(filename[11:13]) == 13 and int(filename[14:16]) >= 24:
                    xprint(f"{filename}:")
                    xprint(lines[-2].strip())
                    xprint(lines[-1].strip())
                    *_, l2 = lines[-2].strip().split()
                    sumbank += int(l2)
                    if int(l2) < 0:
                        xprint('-')
                    else:
                        xprint('+')
                        ct += 1
                    tt += 1
                    xprint()
                    
    print(f'{first} against {second}:')
    print(first, 'wins', sumbank)
    print(ct, 'out of', tt)

# Provide the directory path here
directory_path = "."
print_last_two_lines(directory_path)
