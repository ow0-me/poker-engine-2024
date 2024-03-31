first = 'j'
#second = 'k'

import os

def print_last_two_lines(directory):
    sumbank = 0
    ct = 0
    tt = 0
    z=0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 2 and lines[-2].startswith(first):
                # and int(filename[11:13]) == 13 and int(filename[14:16]) >= 24:
                    print(f"{filename}:")
                    print(lines[-2].strip())
                    print(lines[-1].strip())
                    *_, l2 = lines[-2].strip().split()
                    sumbank += int(l2)
                    if int(l2) < 0:
                        print('-')
                    elif int(l2) == 0:
                        print('0')
                        z+=1
                    else:
                        print('+')
                        ct += 1
                    tt += 1
                    print()
                    
    print(first,'wins', sumbank)
    print(ct, 'out of', tt)
    if z != 0:
        print(z,'ties (zer0s)')

# Provide the directory path here
directory_path = "."
print_last_two_lines(directory_path)
