from random import shuffle

def cria_baralho():
    naipes = ['♠', '♥', '♣', '♦']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    l = [valor + naipe for naipe in naipes for valor in valores]
    shuffle(l)
    return l

def extrai_naipe(carta):
    return carta[-1]

def extrai_valor(carta):
    return carta[:-1]

def lista_movimentos_possiveis(baralho, i):
    mov = []
    if i < 3 and i > 0:
        if extrai_valor(baralho[i]) == extrai_valor(baralho[i - 1]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i - 1]):
            mov.append(1)
    elif i >= 3:
         if extrai_valor(baralho[i]) == extrai_valor(baralho[i - 1]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i - 1]):
            mov.append(1)
         if extrai_valor(baralho[i]) == extrai_valor(baralho[i - 3]) or extrai_naipe(baralho[i]) == extrai_naipe(baralho[i - 3]):
            mov.append(3)
    return mov

def empilha(baralho, o, d):
    baralho[d] = baralho.pop(o)
    return baralho

def possui_movimentos_possiveis(baralho):
    for i in baralho:
        if baralho.index(i) < 3 and baralho.index(i) > 0:
            if extrai_valor(i) == extrai_valor(baralho[baralho.index(i) - 1]) or extrai_naipe(i) == extrai_naipe(baralho[baralho.index(i) - 1]):
                return True
        elif baralho.index(i) >= 3:
             if extrai_valor(i) == extrai_valor(baralho[baralho.index(i) - 1]) or extrai_naipe(i) == extrai_naipe(baralho[baralho.index(i) - 1]):
                return True
             if extrai_valor(i) == extrai_valor(baralho[baralho.index(i) - 3]) or extrai_naipe(i) == extrai_naipe(baralho[baralho.index(i) - 3]):
                return True
    return False

def loop_cartas(baralho):
    cartas = ''
    print('O estado atual das cartas é: ')
    for i in baralho:
        cartas += '{}. {} \n'.format(baralho.index(i) + 1, i)
    print(cartas)


def inteiro(n):
    try:
        int(n)
        return True
    except:
        return False

def comeca():
    comeca = 'x'
    while comeca != '':
        comeca = input('Aperte [Enter] para iniciar o jogo...')
    
    baralho = cria_baralho()
    cartas = ''
    for i in baralho:
        cartas += '{}. {} \n'.format(baralho.index(i) + 1, i)
    print(cartas)
    programa(baralho)


def programa(baralho):
    if possui_movimentos_possiveis(baralho):
        escolha = input('Escolha uma carta (digite um número entre 1 e {}): '.format(len(baralho)))
        if inteiro(escolha) and int(escolha) <= len(baralho):
            escolha = int(escolha) - 1
            movimentos_possiveis = (lista_movimentos_possiveis(baralho, escolha))
            if len(movimentos_possiveis) == 1:
                baralho = empilha(baralho, escolha, escolha - movimentos_possiveis[0])
                loop_cartas(baralho)
                programa(baralho)
            elif len(movimentos_possiveis) == 2:
                escolha2 = int(input('Sobre qual carta você quer empilhar o {} ? \n 1. {}\n 2. {}\nDigite o número da sua escolha: '.format(baralho[escolha], baralho[escolha - 1], baralho[escolha - 3])))
                if escolha2 == 1:
                    baralho = empilha(baralho, escolha, escolha - 1)
                    loop_cartas(baralho)
                    programa(baralho)
                elif escolha2 == 2:
                    baralho = empilha(baralho, escolha, escolha - 3)
                    loop_cartas(baralho)
                    programa(baralho)
            elif len(movimentos_possiveis) == 0:
                print('A carta {} não pode ser movida.'.format(baralho[escolha], len(baralho)))
                programa(baralho)
        else:
            print('Insira um número válido')
            programa(baralho)
    else:
        if len(baralho) == 1:
            print('Parabéns!!! Você venceu!!!')
        else:
            print('Não há mais nenhum movimento possível. Você perdeu :(')
    novamente = input('Deseja jogar novamente (s/n)? ')
    if novamente == 's':
        comeca()

comeca()
