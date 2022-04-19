# 24 Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

def jogo(): 
    # Coletando Número
    n = float(input('Informe um Número: '))
    
    while True:
        # Mostrando Opções
        print(' 1 - Par ou Impar')
        print(' 2 - Positivo ou Negativo')
        print(' 3 - Inteiro ou Decimal')
        print(' 4 - Escolher novo Número')      
        print(' 5 - Sair do jogo')
        opcao = input('>> Escolha uma opção: ')
        print()
        
        
        # Analisando número escolhido e outras opções
        if opcao == '1':
            if n % 2 == 0:
                print('O número é par')
            else:
                print('O número é impar')        
        elif opcao == '2':
            if n < 0:
                print('O número é negativo')
            elif n > 0:
                print('O número é positivo')
            else:
                print('O número é igual a zero')          
        elif opcao == '3':
            if n == int(n):
                print('O número é inteiro')
            else:
                print('O número é decimal')          
        elif opcao == '4':
            opcao = input('>> Escolha uma opção: ')
        elif opcao == '5':
            print('Saindo do Jogo... Até logo!')
            break
        else:
            print('Opção Inválida')
            
        print()

jogo() 