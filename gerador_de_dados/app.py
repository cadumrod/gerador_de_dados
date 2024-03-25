import random




nomes = ['Ana Silva',
'Pedro Santos',
'Maria Oliveira',
'João Souza',
'Carolina Costa']

emails = ['ana.silva@example.com',
'pedro.santos@example.com',
'maria.oliveira@example.com',
'joao.souza@example.com',
'carolina.costa@example.com']

telefones = ['(11) 98765-4321',
'(21) 12345-6789',
'(31) 87654-3210',
'(41) 56789-1234',
'(51) 23456-7890']

cidades = ['São Paulo',
'Rio de Janeiro',
'Belo Horizonte',
'Curitiba',
'Porto Alegre']

estados = ['São Paulo (SP)',
'Rio de Janeiro (RJ)',
'Minas Gerais (MG)',
'Paraná (PR)',
'Rio Grande do Sul (RS)']


while True:
    print('###### Bem-vindo ao gerador de dados ######')
    print()
    print('Escolha quais dados devem ser gerados entre: ')
    print('Nome(1), E-mail(2), telefone(3), cidade(4) e/ou estado(5).')

    opcao = int(input('Digite o número respectivo à escolha: '))
    print()

    if opcao == 1:
        print(random.choice(nomes))
        print()
    elif opcao == 2:
        print(random.choice(emails))
        print()
    elif opcao == 3:
        print(random.choice(telefones))
        print()
    elif opcao == 4:
        print(random.choice(cidades))
        print()
    elif opcao == 5:
        print(random.choice(estados))
        print()

    elif opcao == 'parar':
        print('Você está saindo do sistema...')
        break

    else:
        print('Por favor, digite um número entre 1 e 5.')
        print()