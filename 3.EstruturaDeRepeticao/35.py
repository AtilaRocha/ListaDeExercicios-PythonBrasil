# 35 Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

def primo():
    while True:
        
        # Criando acumulador
        lista = []
        divisoes = 0
        
        # Menu Principal
        print(42*'-')
        print('MENU PRINCIPAL'.center(42))
        print('A - Digitar um número\nB - Sair do programa')
        opcao = str(input('\nSua opção: ')).upper()
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