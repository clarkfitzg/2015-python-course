'''
make_graph.py

Generates dot file for directed graph from simple Makefile

command line usage:

    $ python make_graph.py > make_graph.dot

'''


# accumulate the nodes here so that we can write the labels
nodeset = set()


def printdot(line):
    '''
    Prints dot graph output for a single line in Makefile
    '''
    # dot language doesn't like . character in nodenames
    targets, depends = line.replace('.', '_').split(':')
    targets = targets.split()
    depends = depends.split()
    
    for t in targets:
        nodeset.add(t)
        for d in depends:
            nodeset.add(d)
            print(' -> '.join((d, t)))


print('digraph {\nrankdir = BT')
#print('digraph {')

# Graph structure
with open('Makefile') as makefile:
    for line in makefile:
        # Skips comments and commands
        if line[0].isalpha():
            printdot(line)

# Node labels

print()

for node in nodeset:
    index = node.rfind('_')
    if index != -1:
        label = '.'.join([node[:index], node[index + 1:]])
        label = ''.join(['[label="', label, '"]'])
        print(node, label)

print('}')
