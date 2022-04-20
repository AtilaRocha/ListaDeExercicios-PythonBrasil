# 3 Faça um programa que leia e valide as seguintes informações:
# a.Nome: maior que 3 caracteres;
# b.Idade: entre 0 e 150;
# c.Salário: maior que zero;
# d.Sexo: 'f' ou 'm';
# e.Estado Civil: 's', 'c', 'v', 'd';

def valid_info():
    print(42*'-')
    # Verificar nome
    nome = ''
    while len(nome) <= 3:
        nome = str(input('Informe um nome: '))
        if len(nome) <= 3:
            print('O nome deve ter mais de 3 letras!')

    # Validacao da idade
    idade = -1
    while idade < 0 or idade > 150:
        idade = int(input('Informe a idade: '))
        if idade < 0 or idade > 150:
            print('A idade deve estar entre 0 e 150')

    # Verificar salario
    salario = 0
    while salario <= 0:
        salario = int(input('Informe o salario: '))
        if salario <= 0:
            print('O salario deve ser maior que zero')

    # Verificar sexo
    sexo = ''
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Informe o sexo: ')).upper()
        if sexo != 'F' and sexo != 'M':
            print('O sexo deve ser infomado como M (masculino) ou F (feminino)')

    # Verificar estado civil
    estado_civil = 'A'
    while 'SCVD'.find(estado_civil) < 0:
        estado_civil = str(input('Informe o estado civil: ')).upper()
        if 'SCVD'.find(estado_civil) < 0:
            print('Estado civil deve ser informado como S (solteiro), C (casado), V (viuvo) ou D (divorciado)')
    
    # Quadro de informações
    print(42*'-')
    print('INFORMAÇÕES VALIDADAS'.center(42))
    print(42*'-')
    print(f' NOME: {nome}\n IDADE: {idade}\n SALARIO: {salario}\n SEXO: {sexo}\n ESTADO CIVIL: {estado_civil}')
    print(42*'-')
          
valid_info()
