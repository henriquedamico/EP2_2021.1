from random import shuffle

def cria_baralho():
    naipes = ['♠', '♥', '♣', '♦']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    l = [valor + naipe for naipe in naipes for valor in valores]
    shuffle(l)
    return l
