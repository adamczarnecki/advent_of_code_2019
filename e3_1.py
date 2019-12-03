with open('inputs/3.in') as f:
    A, B = f.readlines()
    A, B = [x.split(',') for x in [A, B]]

print(A, B)
