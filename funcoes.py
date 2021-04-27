def cria_baralho():
    naipes = ['♠', '♥', '♣', '♦']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    l = [valor + naipe for naipe in naipes for valor in valores]
    shuffle(l)
 

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
