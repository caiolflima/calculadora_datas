meses = {'01':31, '02':28, '03':31, '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}
ano = 0
bissexto = False

def verificar_bissexto():
    if (ano%4==0) and (ano%100!=0):
        bissexto = True
        fev = {'02':29}
        return meses.update(fev)
    else:
        bissexto = False
        fev = {'02':28}
        return meses.update(fev)

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
        dias = int(input('Quantidade de dias a somar: '))
        data1[0] = int(data1[0])
        data1[0] += dias
        print(f'{data1} + {dias} = {data1[0]}/{data1[1]}/{data1[2]}')
    elif operacao == 3:
        print('Sair')
        break