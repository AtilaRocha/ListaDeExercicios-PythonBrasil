# 34 Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

# Exercicio igual ao #21

def primo():
    while True:
        # Menu Principal
        print(42*'-')
        print('MENU PRINCIPAL'.center(42))
        print(42*'-')
        print('1 - Digitar um número\n2 - Sair do programa')
        opcao = int(input(('\n')))
        print(42*'-')
        
        # Analisando número
        if opcao == 1:
            numero = int(input("\nDigite um número: "))
            if numero % 2 == 0 and numero != 2:
                print(f"\nO número {numero} não é PRIMO!")
            else:
                print(f"\nO número {numero} é PRIMO!")
                
        # Saindo do programa
        else:
            print('Até logo!')
            break
primo()