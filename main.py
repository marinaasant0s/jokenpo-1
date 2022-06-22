import random

seus_pontos = 0 
pc_pontos = 0

print("Bem-vinde ao Baggins Jokenpo")
print(" JO ... KEN ... PO!\n")

print("suas opções::: pedra, papel e tesoura\nDigite 'sair' para encerrar")

jokenpo= ["pedra","papel","tesoura"]
print("-" * 20)

while True:
  you = input("sua jogada: ").lower()
  
  if you == 'sair':
    print('até logo!')
    break

  pc = random.choice(jokenpo)
  print(f"O computador escolheu {pc}")
  print(f'você escolheu {you}')

  
  if you == pc:
    print('EMPAAAATE')
    
  elif you == "pedra" and pc == "papel":
    print('PC VENCE!')
    pc_pontos = pc_pontos + 1 #acumulador
    
  elif you == "papel" and pc == "pedra":
    print('VOCÊ VENCE!')
    seus_pontos = seus_pontos + 1
  
  elif you == "papel" and pc == "tesoura":
    print('PC VENCE!')
    pc_pontos = pc_pontos + 1

  elif you == "tesoura" and pc == "papel":
    print('VOCÊ VENCE!')
    seus_pontos = seus_pontos + 1

  elif you == "pedra" and pc == "tesoura":
    print('VOCÊ VENCE!')
    seus_pontos = seus_pontos + 1

  elif you == "tesoura" and pc == "pedra":
    print('PC VENCE!')
    pc_pontos = pc_pontos + 1

  else:
    print('INVÁLIDO, escolha uma opção!')

print("-" * 20)
print("Sua pontuação: " + str(seus_pontos))
print("Pontuação do Computador: " + str(pc_pontos))
print("-" * 20)


if pc_pontos > seus_pontos:
    print("Perdeu bença!!!!")
elif pc_pontos == seus_pontos:
    print("Empatou")
else:
    print("Você venceu!!")