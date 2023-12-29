from os import path as op

file = 'submission.txt'

file = op.join(op.dirname(op.realpath(__file__)), file)
open(file, 'w').close()
file = open(file, 'r+')

n = 23
for i in range(1, n+1):
    file.write(f'[{i}]\n')