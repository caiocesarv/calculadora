from func import *

while True:
    print("\n --- CALCULADORA ---")
    print("1.soma")
    print("2.subtração")
    print("3.multiplicação")
    print("4.divisão")
    print("5.sair")

    opcao = input("Escolha uma opção de 1-5: ")
    
    if opcao == "5":
        print("Encerrando a calculadora. Até logo!")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if opcao == "1":
        print(f"Resultado é: {soma(num1, num2)}")
    elif opcao == "2":
         print(f"Resultado é: {sub(num1, num2)}")
    elif opcao == "3":
         print(f"Resultado é: {mult(num1, num2)}")
    else:
        print("Opção")

#oi
#segundocomentário
#terceiro