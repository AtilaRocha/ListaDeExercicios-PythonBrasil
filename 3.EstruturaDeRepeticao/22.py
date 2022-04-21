# 22 Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

def primo():
    while True:
        
        # Criando acumulador
        lista = []
        
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
            if numero % 2 != 0 or numero == 2:
                print(f"\nO número {numero} é PRIMO!")
            else:
                    for i in range(numero):
                            if numero % (i + 1) == 0:
                                    lista.append(i + 1)
                    print(f"\nOs números divisiveis por {numero} são:\n{lista}")
                
        # Saindo do programa
        else:
            print('Até logo!')
            break
primo()