def possui_movimentos_possiveis(baralho):
    for i in baralho:
        if baralho.index(i) < 3 and baralho.index(i) > 0:
            if extrai_valor(i) == extrai_valor(baralho[baralho.index(i) - 1]) or extrai_naipe(i) == extrai_naipe(baralho[baralho.index(i) - 1]):
                return True
        elif baralho.index(i) >= 3:
             if extrai_valor(i) == extrai_valor(baralho[baralho.index(i) - 1]) or extrai_naipe(i) == extrai_naipe(baralho[baralho.index(i) - 1]):
                True
             if extrai_valor(i) == extrai_valor(baralho[baralho.index(i) - 3]) or extrai_naipe(i) == extrai_naipe(baralho[baralho.index(i) - 3]):
                True
    return False
