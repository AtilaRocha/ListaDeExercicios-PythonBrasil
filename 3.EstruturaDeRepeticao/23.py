# 23 Faça um programa que mostre todos os primos entre 1 e N, sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

def primo():
    while True:
        
        # Criando acumulador
        lista = []
        divisoes = 0
        
        # Menu Principal
        print(42*'-')
        print('MENU PRINCIPAL'.center(42))
        print(42*'-')
        print('A - Digitar um número\nB - Sair do programa')
        opcao = str(input('\n')).upper()
        print(42*'-')
        
        # Analisando número
        if opcao == 'A':
            numero = int(input("\nDigite um número: "))
            for i in range(numero +1):
                if i % 2 == 1 and i != 2:    
                    lista.append(i)
                    divisoes += 1
                else:
                    divisoes += 1
            print(f'Números Primos: {lista}')
            print(f'Números de divisões:{divisoes}')
                    
        # Saindo do programa
        else:
            print('Até logo!')
            break
primo()