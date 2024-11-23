def computador_escolhe_partida(n, m):
    if n % (m + 1) == 0:
        return m
    else:
        return n % (m + 1)


def usuario_escolhe_partida(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if 1 <= jogada <= m and jogada <= n:
            return jogada
        else:
            print("Oops! Jogada inválida! Tente de novo.")


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("Computador começa!")
        vez_computador = True
    else:
        print("Você começa!")
        vez_computador = False

    while n > 0:
        if vez_computador:
            jogada = computador_escolhe_partida(n, m)
            print(f"O computador tirou {jogada} peça(s).")
        else:
            jogada = usuario_escolhe_partida(n, m)
            print(f"Você tirou {jogada} peça(s).")

        n -= jogada
        print(f"Agora restam {n} peças no tabuleiro.")
        vez_computador = not vez_computador

    if vez_computador:
        print("Fim do jogo! O computador ganhou!")
        return "computador"
    else:
        print("Fim do jogo! Você ganhou!")
        return "usuario"


def campeonato():
    placar_usuario = 0
    placar_computador = 0

    for rodada in range(1, 4):
        print(f"\n**** Rodada {rodada} ****")
        vencedor = partida()

        if vencedor == "computador":
            placar_computador += 1
        else:
            placar_usuario += 1

    print("\n**** Final do campeonato! ****")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")


def nim():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = int(input())

    if escolha == 1:
        print("\n**** Partida isolada ****")
        partida()
    elif escolha == 2:
        print("\n**** Campeonato ****")
        campeonato()
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")


# Inicio do jogo
nim()

