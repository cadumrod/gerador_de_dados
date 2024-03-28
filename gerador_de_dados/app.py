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
    print()

    opcoes = input('Digite o número respectivo à escolha ou "parar" \npara sair do sistema: ')
    print()

    if opcoes.lower() == 'parar':
            print('Você está saindo do sistema...')
            break

    dados = []


    for opcao in opcoes:
        if opcao == '1':
            dados.append(random.choice(nomes))
        elif opcao == '2':
            dados.append(random.choice(emails))
        elif opcao == '3':
            dados.append(random.choice(telefones))
        elif opcao == '4':
            dados.append(random.choice(cidades))
        elif opcao == '5':
            dados.append(random.choice(estados))
        else:
            print('Por favor, digite um número entre 1 e 5.')
            print()

    print("Dados gerados: \n")
    for dado in dados:
        print(dado)
    print()

    while opcoes != 'parar':
        if opcao == '1' or '2' or '3' or '4' or '5':
            salvar = input('Você deseja salvar os dados em um arquivo .txt? [s]im ou [n]ao: ')
            if salvar.lower() == 's':
                with open("arquivo.txt", "a") as arquivo:
                    for dado in dados:
                        arquivo.write(opcao + '\n')
                    print(f'Os dados foram salvos em "arquivo.txt". ')
                print()
                break
            elif salvar.lower() == 'n':
                break