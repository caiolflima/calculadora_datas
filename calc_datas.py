'''
Projeto 6 - Nível Médio
Calculadora de Datas

autor: Caio Lima
formato: arquivo python

link: https://github.com/caiolflima/calculadora_datas

Funções criadas:
-def verificar_bissexto(data1):
-def diferenca_data(data1, data2, meses):
-def soma_dias(data1, dias, meses):

'''
meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
meses_nome = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
bissexto = False

def verificar_bissexto(data1):
    if ((data1[2]%4==0) and not (data1[2]%100==0)) or (data1[2]%400==0):
        bissexto = True
        meses[1] = 29
        return meses[1], bissexto
    else:
        bissexto = False
        meses[1] = 28
        return meses[1], bissexto

def diferenca_data(data1, data2, meses):
    dias = 0
    verificar_bissexto(data1)
    verificar_bissexto(data2)
    while data1 != data2:
        data1[0] += 1
        if data1[0] > meses[((data1[1])-1)]:
            data1[0] = 1
            data1[1] += 1
            if data1[1] > 12:
                data1[1] = 1
                data1[2] += 1
                verificar_bissexto(data1)
        dias += 1
    return dias

def soma_dias(data1, dias, meses):
    verificar_bissexto(data1)
    while dias + data1[0] > meses[((data1[1])-1)]:
        dias_sobrando = meses[((data1[1])-1)] - data1[0]
        dias -= dias_sobrando
        data1[0] = 0
        data1[1] += 1
        if data1[1] > 12:
            data1[1] = 1
            data1[2] += 1
            verificar_bissexto(data1)
    data1[0] += dias 
    return data1, bissexto

def inserir_data():
    data = input('Escreva a data (DD/MM/AAAA): ').strip().split('/')
    data = [int(item) for item in data]
    return data

def validar_data(data):
    while data[1] > 12:
        print(f'Erro: Mês inexistente.')
        data = inserir_data()
    if data[1] <= 12:
        while data[0] > meses[(data[1])-1]:
            print(f'Erro: Data inválida. {meses_nome[(data[1])-1]} tem {meses[(data[1])-1]} dias')
            data = inserir_data()

    data = [str(item) for item in data]
    while len(data[2]) < 4:
        print(f'Erro: use o formato DD/MM/AAAA')
        data = inserir_data()
        
    while len(data[0]) > 2:
        print(f'Erro: use o formato DD/MM/AAAA')
        data = inserir_data()

    while len(data[1]) > 2:
        print(f'Erro: use o formato DD/MM/AAAA')
        data = inserir_data()

    data = [int(item) for item in data]
    verificar_bissexto(data)
    if bissexto==False:
        while (data[0]==29) and (data[1]==2):
            print(f'Erro: {data[0]}/{data[1]}/{data[2]} não existe. ({data[2]} não é bissexto).')
            data = inserir_data()
    return data

while True:
    print('-='*31)
    print(f'{'Calculadora de Datas':^61}')
    print('Qual operação deseja realizar? ')
    operacao = int(input('(1) Calcular quantos dias há entre duas datas\n(2) Somar uma quantidade de dias a uma data\n(3) Sair\n>'))
    while operacao not in (1,2,3):
        operacao = int(input('(1) Calcular quantos dias há entre duas datas\n(2) Somar uma quantidade de dias a uma data\n(3) Sair\n>'))
    if operacao == 1:
        print('Data 1: ')
        data1 = inserir_data()
        data1 = validar_data(data1)
        print('Data 2:')
        data2 = inserir_data()
        data2 = validar_data(data2)
        print(f'Entre {data1[0]}/{data1[1]}/{data1[2]} e {data2[0]}/{data2[1]}/{data2[2]} = ',end='')
        diferenca = diferenca_data(data1, data2, meses)
        print(f'{diferenca}')
    elif operacao == 2:
        data1 = input('Escreva a data (DD/MM/AAAA): ').strip().split('/')
        data1 = [int(item) for item in data1]
        dias = int(input('Quantidade de dias a somar: '))
        print(f'{data1[0]}/{data1[1]}/{data1[2]} + {dias} = ',end='') 
        data1, bissexto = soma_dias(data1, dias, meses)
        print(f'{data1[0]}/{data1[1]}/{data1[2]}')
    elif operacao == 3:
        print('Sair')
        break