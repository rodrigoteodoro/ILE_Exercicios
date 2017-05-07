def e22():
    #Atencao: raw_input nao existe no python3 entao modifiquei
    nome = input("Digite seu nome: ")
    print("Ola %s" % nome)


def e23():
    horas = int(input("Horas: "))
    valor = float(input("Valor/Hora: "))
    bruto = (horas * valor)
    print("Salario bruto: %s" % bruto)


def e24():
    largura = 17
    altura = 12.0
    r = largura / 2
    print(type(r),'-', r)
    r = largura / 2.0
    print(type(r), '-', r)
    r = altura / 3
    print(type(r), '-', r)
    r = 1 + 2 * 5
    print(type(r),'-', r)


def e25():
    t = float(input("Celsius: "))
    r = t * 9/5 + 32
    print('Fahrenheit = %s' % r)


def e31():
    horas = int(input("Horas: "))
    valor = float(input("Valor/Hora: "))
    if horas > 40:
        total = (40 * valor) + (((horas - 40) * 1.5) * valor)
    else:
        total = (horas * valor)
    print("Salario bruto: %s" % total)


def e32():
    while True:
        try:
            horas = int(input("Horas: "))
            break
        except Exception as e:
            print('Erro! Por favor, digite uma entrada numérica.')
    while True:
        try:
            valor = float(input("Valor/Hora: "))
            break
        except Exception as e:
            print('Erro! Por favor, digite uma entrada numérica.')

    if horas > 40:
        total = (40 * valor) + (((horas - 40) * 1.5) * valor)
    else:
        total = (horas * valor)
    print("Salario bruto: %s" % total)


def e33():
    try:
        p = float(input("Digite uma pontuação: "))
        if p< 0.0 or p > 1.0:
            raise Exception('Pontuação Ruim')
        elif p >= 0.9:
            print('A')
        elif p >= 0.8:
            print('B')
        elif p >= 0.7:
            print('C')
        elif p >= 0.6:
            print('D')
        elif p < 0.6:
            print('F')
    except Exception as e:
        print('Pontuação Ruim')


def e45():
    def fred():
        print('Zap')
    def jane():
        print('ABC')
    jane()
    fred()
    jane()


def e46():
    def computepagamento(horas, valor):
        if horas > 40:
            total = (40 * valor) + (((horas - 40) * 1.5) * valor)
        else:
            total = (horas * valor)
        return total

    while True:
        try:
            horas = int(input("Horas: "))
            break
        except Exception as e:
            print('Erro! Por favor, digite uma entrada numérica.')
    while True:
        try:
            valor = float(input("Valor/Hora: "))
            break
        except Exception as e:
            print('Erro! Por favor, digite uma entrada numérica.')

    total = computepagamento(horas, valor)
    print("Salario bruto: %s" % total)


def e47():
    def computegrau(p):
        if p< 0.0 or p > 1.0:
            raise Exception('Pontuação Ruim')
        elif p >= 0.9:
            return 'A'
        elif p >= 0.8:
            return 'B'
        elif p >= 0.7:
            return 'C'
        elif p >= 0.6:
            return 'D'
        elif p < 0.6:
            return 'F'
    try:
        p = float(input("Digite uma pontuação: "))
        print(computegrau(p))
    except Exception as e:
        print('Pontuação Ruim')


def e51():
    qtd = 0
    soma = 0
    while True:
        try:
            v = input('Digite um numero: ')
            if v == 'done':
                break
            else:
                qtd += 1
                soma += float(v)
        except Exception as e:
            print('Invalid input')
    if qtd > 0:
        media = soma/qtd
        print('Soma: %s, quantidade: %s, media :%s' %(soma, qtd, media))


def e52():
    a = []
    while True:
        try:
            v = input('Digite um numero: ')
            if v == 'done':
                break
            else:
                a.append(float(v))
        except Exception as e:
            print('Invalid input')
    if a:
        print('Maior valor: %s, menor valor: %s' %(max(a), min(a)))


def e61():
    str = 'X - DSPAM - Confidence: 0.8475'
    v = float(str[str.find(':')+1:].replace(' ',''))
    print(type(v),'-', v)


def e71():
    arq = input('Enter a file name: ')
    if arq:
        f = open(arq, 'r')
        for l in f:
            print(l.upper())
        f.close()


def e72():
    import re
    soma = 0
    qtd = 0
    arq = input('Enter a file name: ')
    if arq:
        f = open(arq, 'r')
        for l in f:
            if l.startswith('X-DSPAM-Confidence'):
                x = re.findall(r'[\d\.]+', l)
                if x:
                    soma += float(x[0])
                    qtd += 1
        f.close()
        if qtd > 0:
            media = soma/qtd
            print('Average spam confidence: %s' % media)


def e73():
    try:
        arq = input('Enter a file name: ')
        if arq and arq == 'na na boo boo':
            print('NA NA BOO BOO TO YOU - You have been punk’d!')
        elif arq:
            f = open(arq, 'r')
            x = 0
            for l in f:
                x += 1
            print('There were %s subject lines in %s' % (x, arq))
    except Exception as e:
        print('File cannot be opened: %s' % arq)


def e84():
    v = []
    try:
        arq = input('Informe o arquivo: ')
        f = open(arq, 'r')
        for l in f:
            s = l.split(' ')
            if s:
                for p in s:
                    p = p.replace('\n', '')
                    if p not in v:
                        v.append(p)
        if v:
            print(sorted(v))
    except Exception as e:
        print('File cannot be opened: %s' % arq)


def e85():
    v = []
    try:
        arq = input('Informe o arquivo: ')
        f = open(arq, 'r')
        for l in f:
            if l.startswith('From'):
                s = l.split(' ')
                if s:
                    v.append(s[1].replace('\n',''))

        print('\n'.join(v))
        print('%s linhas no arquivo possuem From como a primeira palavra' % (len(v)))
    except Exception as e:
        print('File cannot be opened: %s' % arq)


def e86():
    a = []
    while True:
        try:
            v = input('Insira um numero: ')
            if v == 'pronto':
                break
            else:
                a.append(float(v))
        except Exception as e:
            print('Invalid input')
    if a:
        print('Maior valor: %s, menor valor: %s' % (max(a), min(a)))
        f = open('numeros.txt', 'w')
        for n in a:
            f.write('%s\n' % str(n))
            f.flush()
        f.close()


def e92():
    v = dict()
    try:
        arq = input('Digite o nome do arquivo: ')
        #arq = 'mbox-short.txt'
        f = open(arq, 'r')
        for l in f:
            if l.startswith('From'):
                s = l.split(' ')
                if s and len(s) > 3:
                    if v.get(s[2]):
                        v[s[2]] += 1
                    else:
                        v[s[2]] = 1
        if v:
            print('%s' % v)
    except Exception as e:
        print('File cannot be opened: %s' % arq)


def e93():
    v = dict()
    try:
        arq = input('Digite o nome do arquivo: ')
        #arq = 'mbox-short.txt'
        f = open(arq, 'r')
        for l in f:
            if l.startswith('From'):
                s = l.split(' ')
                if s and len(s) >= 2:
                    if v.get(s[1]):
                        v[s[1]] += 1
                    else:
                        v[s[1]] = 1
        if v:
            print('%s' % v)

    except Exception as e:
        print('File cannot be opened: %s' % arq)


def e94():
    v = dict()
    try:
        arq = input('Digite o nome do arquivo: ')
        arq = 'mbox-short.txt'
        f = open(arq, 'r')
        for l in f:
            if l.startswith('From'):
                s = l.split(' ')
                if s and len(s) >= 2:
                    if v.get(s[1]):
                        v[s[1]] += 1
                    else:
                        v[s[1]] = 1
        if v:
            import operator
            m = max(v.items(), key=operator.itemgetter(1))
            print(m[0], m[1])

    except Exception as e:
        print('File cannot be opened: %s' % arq)


def e95():
    v = dict()
    try:
        arq = input('Digite o nome do arquivo: ')
        arq = 'mbox-short.txt'
        f = open(arq, 'r')
        for l in f:
            if l.startswith('From'):
                s = l.split(' ')
                if s and len(s) >= 2:
                    d = s[1][s[1].index('@')+1:].replace('\n','')
                    if v.get(d):
                        v[d] += 1
                    else:
                        v[d] = 1
        if v:
            print('%s' %v)

    except Exception as e:
        print('File cannot be opened: %s' % arq)


def e101():
    v = dict()
    try:
        arq = input('Digite o nome do arquivo: ')
        #arq = 'mbox-short.txt'
        f = open(arq, 'r')
        for l in f:
            if l.startswith('From'):
                s = l.split(' ')
                if s and len(s) >= 2:
                    u = s[1].replace('\n', '')
                    if v.get(u):
                        v[u] += 1
                    else:
                        v[u] = 1
        if v:
            t = v.items()
            t = sorted(t, reverse=True)
            print(t[0])

    except Exception as e:
        print('File cannot be opened: %s' % arq)


def e102():
    v = dict()
    try:
        arq = input('Digite o nome do arquivo: ')
        # arq = 'mbox-short.txt'
        f = open(arq, 'r')
        for l in f:
            if l.startswith('From'):
                s = l.replace('  ',  ' ').split(' ')
                if s and len(s) >= 6:
                    h = s[5].split(':')[0]
                    if v.get(h):
                        v[h] += 1
                    else:
                        v[h] = 1
        if v:
            t = v.items()
            for x in sorted(t):
                print(x[0],x[1])

    except Exception as e:
        print('File cannot be opened: %s' % arq)


def e103():
    import re
    v = dict()
    x = []
    y = []
    try:
        # arq = input('Digite o nome do arquivo: ')
        #arq = 'mbox-short.txt'
        #arq = 'livro.txt'
        f = open(arq, 'r')
        for l in f:
            for lt in l:
                lt = lt.lower()
                if re.match(r'[a-z]', lt):
                    if v.get(lt):
                        v[lt] += 1
                    else:
                        v[lt] = 1
        if v:
            import operator
            m = sorted(v.items(), key=operator.itemgetter(1), reverse=True)
            for l in m:
                print(l[0], l[1])
                x.append(l[0])
                y.append(l[1])

    except Exception as e:
        print('File cannot be opened: %s' % arq)

    # Exibe o histograma das letras vs frequencia do texto
    if x and y:
        # http://stackoverflow.com/questions/18973404/setting-different-bar-color-in-matplotlib-python
        import pandas as pd
        import matplotlib.pyplot as plt
        s = pd.Series(
            y,
            index=x
        )
        plt.title("Frequencia das letras")
        plt.ylabel('Frequencia')
        plt.xlabel('Letra')
        s.plot(
            kind='bar'
        )
        plt.show()

e103()