#uestão super digito

def super_digito(x:int) ->int:
    x=str(x)
    if len(x)==1:
        return int(x)
    else:
        soma = 0
        for digito in list(x):
            soma+= int(digito)
        if len(str(soma)) == 1:
            return soma
        else:
             return super_digito(soma)

def main(n:int, k:int) -> int :
    numero = int(str(n)*k)
    return super_digito(numero)