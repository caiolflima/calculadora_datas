meses = {'01':31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}
ano = 0
bissexto = False

def verificar_bissexto():
    if (ano%4==0) and (ano%100!=0):
        bissexto = True
        meses['02'] = 29
    else:
        bissexto = False
        meses['02'] = 28

while True:
    print('-='*31)
    print(f'{'Calculadora de Datas':^61}')
    print('Qual operação deseja realizar? ')
    operacao = int(input('(1) Calcular quantos dias há entre duas datas\n(2) Somar uma quantidade de dias a uma data\n(3) Sair\n>'))
    while operacao not in (1,2,3):
        operacao = int(input('(1) Calcular quantos dias há entre duas datas\n(2) Somar uma quantidade de dias a uma data\n(3) Sair\n>'))
    if operacao == 1:
        data1 = int(input('Escreva a primeira data (DD/MM/AAAA): '))
        data2 = int(input('Escreva a segunda data (DD/MM/AAAA): '))
        diferenca = data2 - data1
        print(f'{data1} + {data2} = {diferenca}')
    elif operacao == 2:
        data1 = int(input('Escreva a data (DD/MM/AAAA): '))
        dias = int(input('Quantidade de dias a somar: '))
        data_soma = data1 + dias
        print(f'{data1} + {dias} = {data_soma}')
    elif operacao == 3:
        print('Sair')
        break