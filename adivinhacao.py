print("********************************")
print("Bem vindo ao jogo da adivinhação")
print("********************************")

numero_secreto = 42

chute = input("Digite o seu numero: ")

print("Você digitou", chute)

if numero_secreto == int(chute):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do jogo")
