meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
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

while True:
    print('-='*31)
    print(f'{'Calculadora de Datas':^61}')
    print('Qual operação deseja realizar? ')
    operacao = int(input('(1) Calcular quantos dias há entre duas datas\n(2) Somar uma quantidade de dias a uma data\n(3) Sair\n>'))
    while operacao not in (1,2,3):
        operacao = int(input('(1) Calcular quantos dias há entre duas datas\n(2) Somar uma quantidade de dias a uma data\n(3) Sair\n>'))
    if operacao == 1:
        data1 = int(input('Escreva a primeira data (DD/MM/AAAA): ').strip().split('/'))
        data2 = int(input('Escreva a segunda data (DD/MM/AAAA): ').strip().split('/'))
        #diferenca = data2 - data1
        print(f'{data1} + {data2} = diferenca')
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