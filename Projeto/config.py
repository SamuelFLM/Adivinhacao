import os
import random
import time


def limpar_terminal():
    os.system('cls')


# Estrutura para colocar titulo
def interface_titulo_jogo(titulo, qtd):
    print(qtd * "*")
    print(f"    {titulo}    ")
    print(qtd * "*")


# Estrutura switch case
def opcao_jogo(pergunta_para_usuario):
    opcao_usuario = int(input(pergunta_para_usuario))
    match opcao_usuario:
        case 1:
            estrutura_jogo_sigle()
        case 2:
            estrutura_jogo_multiplayer()


def estrutura_jogo_sigle():
    limpar_terminal()
    interface_titulo_jogo("JOGO ADIVINHAÇÃO", 30)
    nome = input("\nINFORME SEU NOME: ")
    sorteia_numeros(nome)



#Estrutura de 2 ou mais jogadores.
def estrutura_jogo_multiplayer():
    nomes = []

    interface_titulo_jogo("JOGO ADIVINHAÇÃO MULTIPLAYER", 30)
    interface_titulo_jogo("\nQUANTIDADE JOGADORES", 0)

    # Loop com tratamento para impedir número limite
    while True:
        try:
            qtd_jogadores = int(input("\nDigite a quantidade de jogadores: "))
            if not (2 <= qtd_jogadores <= 4):
                raise ValueError("Número maximo ultrapassado \n[Mínimo 2] - [Maximo 4]")
            break
        except ValueError as erro:
            print(erro)

    limpar_terminal()

    # Loop para armazenar nome dos jogadores
    for indice in range(0, qtd_jogadores):
        interface_titulo_jogo("\nNOMES JOGADORES", 0)
        nome_jogador = input(f"\nINFORME O NOME DO JOGADOR {indice}: ")
        nomes.append(nome_jogador)

#Funcao responsavel por limitar o laço de repeticao
def rodadas():
    interface_titulo_jogo("INFORME QUANTIDADE RODADAS", 0)
    while True:
        try:
            opcao_rodadas = int(input("""
            1 - EASY [ 10 RODADAS ]
            2 - INTERMEDIARY [ 5 RODADAS ]
            3 - HARD [ 3 RODADAS ]
            \nDIGITE: """))

            if not (1 <= opcao_rodadas <= 3):
                raise ValueError("Erro - Digite um número entre [1] - [3]")

            match opcao_rodadas:
                case 1:
                    return 10
                    break
                case 2:
                    return 5
                    break
                case 3:
                    return 3
                    break
        except ValueError as erro:
            print(erro)

#Retorna valor limite de dificuldade.
def dificuldade_adivinhacao():
    interface_titulo_jogo("DIFICULDADE ADIVINHACÃO", 0)
    while True:
        try:
            dificuldade = int(input("""
            RECOMENDAÇÃO:
            Easy  [0, 10]
            Intermediario [0, 50] 
            Hard [0, 100]
            OBS: DIGITE VALOR MAX
            \nDIGITE: """))

            if not (10 <= dificuldade <= 100):
                raise ValueError("Erro - Valor min[10] - max[100]")
            break
        except ValueError as erro:
            print(erro)

    return dificuldade

#Tela final de pontuacao. Placar listado para o jogador
def placar(nome, pontos):
    limpar_terminal()
    interface_titulo_jogo("PLACAR FINAL" , 30)
    print("""
    10 pts - Win [ Venceu a maquina ] 
    5 pts - Médiano [ perdeu mais falta pouco ] 
    3 pts - Está no caminho [ perdeu de lavada ]
    """)
    print("Pontuacão Final:")
    if( pontos >= 10):
        print("Parabéns você venceu!!!!!!")
        print(f"\nJOGADOR {nome}: {pontos} pontos")
    elif ( pontos >= 4 or pontos <= 7):
        print("Você Foi Quase!!!!")
        print(f"\nJOGADOR {nome}: {pontos} pontos")
    else:
        print("Você Perdeu!!!!")
        print(f"\nJOGADOR {nome}: {pontos} pontos")



#Reune funcoes de rodadas, dificuldade, pontuacao e placar.
def sorteia_numeros(nome):

    contagem = 0
    pontos = 0
    qtd_rodadas = rodadas()
    num_max = dificuldade_adivinhacao()
    while contagem <= qtd_rodadas:
            limpar_terminal()
            interface_titulo_jogo("VOCE VS MAQUINA", 30)
            print("\nTENTE VENCER")

            contagem += 1
            valor_sortido = random.randrange(1, num_max)
            user = int(input(f"\n{nome} \nINFORME UM NÚMERO: "))
            if(user == valor_sortido):
                print(f"Acertou - Valor sortido: {valor_sortido}")
                pontos += 2
                print(f"Seus pontos: {pontos}")
                time.sleep(1)
            elif(abs(user - valor_sortido) <= 3):
                print(f"Valor passou perto {valor_sortido}")
                pontos += 1
                time.sleep(1)
            else:
                print(f"Errou - Valor sortido: {valor_sortido}")
                time.sleep(1)
    placar_final = placar(nome, pontos)
