from collections import defaultdict
import sys
path = sys.argv[1]

xprint = lambda *args: None

import os
l=['bipot','birai','og','ogcp','player','j','ezwin','bp2-old']

def print_last_two_lines(directory):
    mat = defaultdict(lambda: defaultdict(int))
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    *p1, _, c1 = lines[0].strip().split()
                    *p2, _, c2 = lines[1].strip().split()
                    p1 = ' '.join(p1)
                    p2 = ' '.join(p2)
                    if 0 and not (p1 in l and p2 in l):
                        continue
                    if mat[p1][p2] != 0:
                        print('bad')
                    mat[p1][p2] = int(c1)
                    mat[p2][p1] = int(c2)

    #print(mat)

    weight = defaultdict(float)
    for k in mat:
        weight[k] = 1.0/len(mat)

    for _ in range(1):
        ranking = []
        for j, nei in mat.items():
            pwr = 0.0
            for k, v in nei.items():
                pwr += v * weight[k]
            ranking.append((pwr, j))

        ranking.sort()


        x = []
        for i, (_, j) in enumerate(ranking):
            weight[j] = 0.95 ** (-i)
            x.append(j)

    print(ranking)
    print(x)

    return mat

# Provide the directory path here
directory_path = f"shorts/{path}"
print_last_two_lines(directory_path)
