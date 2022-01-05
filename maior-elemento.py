# Desenvolva uma função recursiva que calcule e mostre o maior elemento de um array de tamanho N. Os elementos consistem em números inteiros.
# ----
def max_list(lista:list):
    if len(lista)==1:
        return lista[0]
    else:
        maximo = max_list(lista[1:])
        #print(maximo)
        return maximo if maximo > lista[0] else lista[0]