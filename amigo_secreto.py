prompt_entrada = "Digite o nome do participante seguido por 3 sugestões de presentes. (Ex: Fulano Bicicleta Playstation5 PcGamer): "
amigos_presentes = {}
print("BEM VINDO AO AMIGO SECRETO")
quantidade_amigos = int(input("Quantos amigos vão participar do jogo? "))
for i in range(quantidade_amigos):
    print(f"\nEntre com os dados do {i + 1}° participante:")
    entrada = input(prompt_entrada).lower()
    nome, presentes = entrada.split()[0], entrada.split()[1:]
    amigos_presentes.update({nome:presentes})
print(amigos_presentes)
print("\nVamos verificar se os participantes acertaram nos presentes:")
while True:
    nome_presente = input("Digite o nome do ganhador do presente e do presente ganhado (Ex.: Fulano tênis) ou 's' para sair: ").lower()
    if nome_presente == 's':
        break
    if nome_presente.split()[1] in amigos_presentes[nome_presente.split()[0]]:
        print("Uhul! Seu amigo secreto vai adorar o/")
    else:
        print("Tente novamente!")
