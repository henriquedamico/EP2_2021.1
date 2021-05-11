from random import shuffle
from colorama import *

init()

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
        cartas += '{}. {} \n'.format(Style.RESET_ALL + str(baralho.index(i) + 1), cor(i))
    print(cartas)

def cor(carta):
    if extrai_naipe(carta) == '♥':
        carta = (Fore.RED + carta)
    elif extrai_naipe(carta) == '♦':
        carta = (Fore.YELLOW + carta)
    elif extrai_naipe(carta) == '♣':
        carta = (Fore.CYAN + carta)
    elif extrai_naipe(carta) == '♠':
        carta = (Fore.WHITE + carta)
    return str(carta)
  
def inteiro(n):
    try:
        int(n)
        return True
    except:
        return False

def comeca():
    comeca = 'x'
    while comeca != '':
        comeca = input('Paciência Acordeão \n seja bem vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é  colocar todas as cartas em uma mesma pilha. \n Existem apenas dois movimentos possíveis \n 1. Empilhar uma carta sobre a carta imediatamente anterior \n 2. Empilhar uma carta sobre a terceira carta anterior. \n Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: \n 1. As duas cartas possuem o mesmo valor ou \n 2. As duas cartas possuem o mesmo naipe. \n Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. \n Aperte [Enter] para iniciar o jogo...')
    
    baralho = cria_baralho()
    cartas = ''
    for i in baralho:
        cartas += '{}. {} \n'.format(Style.RESET_ALL + str(baralho.index(i) + 1), cor(i))
    print(cartas)
 
    programa(baralho)

def duas_cartas(baralho, escolha):
    escolha2 = input(Style.RESET_ALL + 'Sobre qual carta você quer empilhar o {}? \n 1. {}\n 2. {}\nDigite o número da sua escolha: '.format(baralho[escolha], baralho[escolha - 1], baralho[escolha - 3]))
    if inteiro(escolha2):
        escolha2 = int(escolha2)
        if escolha2 == 1:
            baralho = empilha(baralho, escolha, escolha - 1)
            loop_cartas(baralho)
            programa(baralho)
        elif escolha2 == 2:
            baralho = empilha(baralho, escolha, escolha - 3)
            loop_cartas(baralho)
            programa(baralho)
        else:
            print('Opção inválida')
            duas_cartas(baralho, escolha)
    else:
        print('Opção inválida')
        duas_cartas(baralho, escolha)



def programa(baralho):
    if possui_movimentos_possiveis(baralho):
        escolha = input(Style.RESET_ALL + 'Escolha uma carta (digite um número entre 1 e {}): '.format(len(baralho)))
        if inteiro(escolha) and int(escolha) <= len(baralho) and int(escolha) > 0:
            escolha = int(escolha) - 1
            movimentos_possiveis = (lista_movimentos_possiveis(baralho, escolha))
            if len(movimentos_possiveis) == 1:
                baralho = empilha(baralho, escolha, escolha - movimentos_possiveis[0])
                loop_cartas(baralho)
                programa(baralho)
            elif len(movimentos_possiveis) == 2:
                duas_cartas(baralho, escolha)
            elif len(movimentos_possiveis) == 0:
                print(Style.RESET_ALL + 'A carta {} não pode ser movida.'.format(baralho[escolha]))
                programa(baralho)
        else:
            print('Posição inválida')
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
