import random
from time import sleep
naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
faces = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
sorted_naipe = random.randint(0,3)
sorted_face = random.randint(0,12)
cont_played = 0
print("Bem vindo ao meu jogo de adivinhação de cartas!")
sleep(0.5)
print("""As regras são as seguintes:
Você pode tentar até conseguir acertar.
Escreva os nomes de faces e naipes corretamente.
E principalmente, se divirta e boa sorte!""")
sleep(1)
answer = input("Está pronto pra jogar??? S | N \n").upper()
while answer == "S" or answer == "SIM":
    if cont_played >= 1:
        print("Bem vindo novamente ao meu jogo de adivinhação de cartas!")
        print("Para você não esquecer irei repetir as regras!")
        sleep(1)
        print("""As regras são as seguintes:
        Você pode tentar até conseguir acertar.
        Escreva os nomes de faces e naipes corretamente.
        E principalmente, se divirta e boa sorte!""")
        sleep(1)
    print(f"Os naipes usados aqui são: {naipes}")
    print(f"As faces usadas aqui são: {faces}")
    guess_naipe = input("Informe o naipe da carta que você acha que é: ")
    guess_face = input("Informe a face da carta que você acha que é: ")
    cont_plays = 1
    while True:
        if guess_naipe == naipes[sorted_naipe] and guess_face == faces[sorted_face]:
            print(f"Parabéns você acertou com {cont_plays} tentativas!")
            answer = input("Deseja jogar novamente??? S | N \n").upper()
            cont_played = 1
            break
        else:
            if guess_face == faces[sorted_face]:
                print("Você acertou a face da carta sorteada!")
            else:
                for i in range(0,12):
                    if guess_face == faces[i]:
                        if i > sorted_face:
                            print("A face sorteada é menor que o seu chute!")
                        else:
                            print("A face sorteada é maior que o seu chute!")
            if guess_naipe == naipes[sorted_naipe]:
                print("Você acertou o naipe da carta sorteada!")
            else:
                print("A carta sorteada tem naipe diferente do seu chute!")
            print("Outra chance!")
            cont_plays += 1
            if guess_naipe == naipes[sorted_naipe]:
                pass
            else:
                guess_naipe = input("Informe o naipe da carta que você acha que é: ")
            if guess_face == faces[sorted_face]:
                pass
            else:
                guess_face = input("Informe a face da carta que você acha que é: ")

            
        
    
