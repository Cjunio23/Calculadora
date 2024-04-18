import math

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    else:
        return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: não é possível calcular a raiz quadrada de um número negativo!"
    else:
        return math.sqrt(a)

def calculadora():
    print("=== CALCULADORA ===")
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")

    opcao = input("Digite o número da operação desejada: ")

    if opcao in ('1', '2', '3', '4', '5', '6'):
        if opcao in ('1', '2', '3', '4', '5'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                print("Resultado:", adicao(num1, num2))
            elif opcao == '2':
                print("Resultado:", subtracao(num1, num2))
            elif opcao == '3':
                print("Resultado:", multiplicacao(num1, num2))
            elif opcao == '4':
                print("Resultado:", divisao(num1, num2))
            elif opcao == '5':
                print("Resultado:", potencia(num1, num2))
        else:
            num = float(input("Digite o número: "))
            if opcao == '6':
                print("Resultado:", raiz_quadrada(num))
    else:
        print("Opção inválida. Por favor, escolha uma das opções de 1 a 6.")

# Executando a calculadora
calculadora()
