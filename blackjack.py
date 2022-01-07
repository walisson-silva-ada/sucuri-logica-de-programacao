import random 

def criar_baralho():
    return (list(range(2, 11)) + list('AVDR')) * 4

def jogada(nome_jogador, jogadores, baralho):
    jogador = jogadores[nome_jogador]
    if jogador['pontos'] < 21 and jogador['ativo']:
        if input(f"{nome_jogador}, deseja comprar uma carta? [s/n]: ").lower() == 's':
            jogador['pontos'] += sorteio(baralho)
            if jogador['pontos'] >= 21:
                jogador['ativo'] = False
        else:
            jogador['ativo'] = False

def sorteio(baralho):
    carta = baralho.pop(random.randint(0, len(baralho)-1))
    if carta == "A":
        pontos = 1
    else:
        pontos = carta if type(carta) == int else 10
    print("Carta sorteada:", carta)
    print("Pontos:", pontos)
    return pontos

def verificacao(jogadores):
    print(jogadores)
    classificados = {jogador:jogadores[jogador]['pontos'] for jogador in jogadores if jogadores[jogador]['pontos']<=21}
    ganhadores = {jogador:pontuacao for jogador, pontuacao in classificados.items() if pontuacao == max(classificados.values())}
    print(ganhadores)           
           
def iniciar_jogo():
    num_jogadores = int(input("Informe o número de jogadores: "))
    jogadores = {input(f"Informe o nome do {i+1}° jogador: "):{'pontos':0, 'ativo':True} for i in range(num_jogadores)}
    baralho = criar_baralho()
    jogadores_ativos = [jogador for jogador in jogadores if jogadores[jogador]['ativo']] 
    while jogadores_ativos:
        print(len(baralho))
        for nome_jogador in jogadores_ativos:
            jogada(nome_jogador, jogadores, baralho)
            print("Total de pontos:", jogadores[nome_jogador]['pontos'])
        jogadores_ativos = [jogador for jogador in jogadores if jogadores[jogador]['ativo']] 
    verificacao(jogadores)
