jogadas = int(input())

for i in range(jogadas):
    escolha = input("").split(' ')
    jogador1 = escolha[0]
    jogador2 = escolha[2]
    escolha1 = escolha[1]
    escolha2 = escolha[3]
    
    if escolha1 == "PAR":
        jogadorpar = jogador1
    elif escolha2 == "PAR":
        jogadorpar = jogador2
    
    if escolha1 == "IMPAR":
        jogadorimpar = jogador1
    elif escolha2 == "IMPAR":
        jogadorimpar = jogador2
    
    jogada = input("").split(' ')
    numero1 = int(jogada[0])
    numero2 = int(jogada[1])
    soma = numero1 + numero2
    
    if soma % 2 == 0:
        print (jogadorpar)
    elif soma % 2 != 0:
        print (jogadorimpar)