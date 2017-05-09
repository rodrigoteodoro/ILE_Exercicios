f = open('exercicio.py', 'r')
fe = None
for l in f:
    #print(l)
    if l.startswith('def'):
        path = l.split(' ')[1][:l.split(' ')[1].index('(')]
        i = 2 if len(path) == 3 else 3
        path = '%s_%s.py' % (path[1:i], path[i:])
        print(path)
        if fe:
            fe.close()
        fe = open(path, 'w')
    elif l:
        fe.write(l[4:])
        fe.flush()

if fe:
    fe.close()