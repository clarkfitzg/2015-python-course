'''
make_graph.py

Generates dot file for directed graph from simple Makefile

command line usage:

    $ python make_graph.py > make_graph.dot

'''


def printdot(line):
    '''
    Prints dot graph output for a single line in Makefile
    '''
    targets, depends = line.split(':')
    targets = targets.split()
    depends = depends.split()
    
    for t in targets:
        for d in depends:
            print(' -> '.join((t, d)), ';')


print('digraph {')

with open('Makefile') as makefile:
    for line in makefile:
        # Skips comments and commands
        if line[0].isalpha():
            printdot(line)

print('}')
