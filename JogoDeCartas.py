import random
from time import sleep
naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
faces = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cont_played = 0
already_sorted = []

def ask_face():
    guess_face = input("Informe a face da carta que você acha que é: ").title()
    if guess_face not in faces:
        while guess_face not in faces:
            print(f"Faces: {faces}")
            guess_face = input("Informe a face do baralho que você acha que é: ").title()
    return guess_face

def ask_naipe():
    guess_naipe = input("Informe o naipe da carta que você acha que é: ").title()
    if guess_naipe not in naipes:
        while guess_naipe not in naipes:
            print(f"Naipes: {naipes}")
            guess_naipe = input("Informe o naipe do baralho que você acha que é: ").title()
    return guess_naipe

print("Bem vindo ao meu jogo de adivinhação de cartas!")
sleep(0.5)
print("""As regras são as seguintes:
Você pode tentar até conseguir acertar.
Escreva os nomes de faces e naipes corretamente.
E principalmente, se divirta e boa sorte!\n\n\n""")
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
E principalmente, se divirta e boa sorte!\n\n\n""")
        sleep(1)
    sorted_naipe = random.randint(0,3)
    sorted_face = random.randint(0,12)
    while faces[sorted_face] + naipes[sorted_naipe] in already_sorted:
        sorted_naipe = random.randint(0,3)
        sorted_face = random.randint(0,12)
    print(f"Os naipes usados aqui são: {naipes}")
    print(f"As faces usadas aqui são: {faces}")
    guess_naipe = ask_naipe()
    guess_face = ask_face()
    cont_plays = 1
    while True:
        if guess_naipe == naipes[sorted_naipe] and guess_face == faces[sorted_face]:
            print(f"A carta sorteada é {faces[sorted_face]} de {naipes[sorted_naipe]}!")
            print(f"Parabéns você acertou com {cont_plays} tentativas!")
            already_sorted.append(faces[sorted_face] + naipes[sorted_naipe])
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
            print("Outra chance!\n\n\n")
            cont_plays += 1
            if guess_naipe != naipes[sorted_naipe]:
                guess_naipe = ask_naipe()
            if guess_face != faces[sorted_face]:
                guess_face = ask_face()
                

            
        
    
