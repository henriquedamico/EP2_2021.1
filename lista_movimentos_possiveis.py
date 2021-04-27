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
