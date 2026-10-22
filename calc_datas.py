'''
Projeto 6 - Nível Médio\n
Calculadora de Datas\n

autor: Caio Lima\n
formato: arquivo python\n

link: https://github.com/caiolflima/calculadora_datas\n

Funções criadas:\n
-def verificar_bissexto(data1): - 
Verifica se o ano informado é bissexto e altera a quantidade de dias de Fevereiro\n
-def segunda_data_post(data1,data2): -
Verifica se a segunda data é posterior à primeira\n
-def diferenca_data(data1, data2, meses):
Calcula a diferença de dias entre as datas informadas\n
-def soma_dias(data1, dias, meses):
Soma a quantidade de dias informada à data\n
-def inserir_data():
Coleta a data desejada\n
-def validar_data(data):
Verifica se a data está no formato DD/MM/AAAA e se a quantidade de dias e meses está coerente com o calendário.\n
def dia_semana(data1):\n
Retorna o dia da semana da data no resultado de soma.
'''
meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
meses_nome = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
dias_semana = ['segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sábado','domingo']
bissexto = False
data_segunda_feira = [12,10,2026]

def verificar_bissexto(data1):
    if ((data1[2]%4==0) and not (data1[2]%100==0)) or (data1[2]%400==0):
        bissexto = True
        meses[1] = 29
        return meses[1], bissexto
    else:
        bissexto = False
        meses[1] = 28
        return meses[1], bissexto

def segunda_data_post(data1,data2):
    while True:
        if data1[2] > data2[2]:
            print('Segunda Data inválida. Escreva uma data posterior à data 1:')
            data2 = inserir_data()
            segunda_data_post(data1,data2)
            break
        elif (data1[1]>data2[1]) and (data1[2]>=data2[2]):
            print('Segunda Data inválida. Escreva uma data posterior à data 1:')
            data2 = inserir_data()
            segunda_data_post(data1,data2)
            break
        elif (data1[0]>data2[0]) and (data1[1]>=data2[1]) and (data1[2]>=data2[2]):
            print('Segunda Data inválida. Escreva uma data posterior à data 1:')
            data2 = inserir_data()
            segunda_data_post(data1,data2)
            break
        else:
            break
    return data2

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

def dia_semana(data1):
    if data_segunda_feira[2] > data1[2]:
        cont_semana = diferenca_data(data1,data_segunda_feira,meses)
    elif (data_segunda_feira[1] > data1[1]) and (data_segunda_feira[2] >= data1[2]):
        cont_semana = diferenca_data(data1,data_segunda_feira,meses)
    elif (data_segunda_feira[0] > data1[0]) and (data_segunda_feira[1] >= data1[1]) and (data_segunda_feira[2] >= data1[2]):
        cont_semana = diferenca_data(data1,data_segunda_feira,meses)
    else:
        cont_semana = diferenca_data(data_segunda_feira,data1,meses)
    if (cont_semana==0) or (cont_semana%7==0):
        nome_dia = dias_semana[0]
    else:
        indice = (cont_semana-((cont_semana//7)*7))
        nome_dia = dias_semana[indice]
    return nome_dia

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
        data2 = segunda_data_post(data1,data2)
        print(f'Entre {data1[0]}/{data1[1]}/{data1[2]} e {data2[0]}/{data2[1]}/{data2[2]} = ',end='')
        diferenca = diferenca_data(data1, data2, meses)
        print(f'{diferenca}')
    elif operacao == 2:
        data1 = input('Escreva a data (DD/MM/AAAA): ').strip().split('/')
        data1 = [int(item) for item in data1]
        dias = int(input('Quantidade de dias a somar: '))
        print(f'{data1[0]}/{data1[1]}/{data1[2]} + {dias} = ',end='') 
        data1, bissexto = soma_dias(data1, dias, meses)
        print(f'{data1[0]}/{data1[1]}/{data1[2]}',end='')
        print(f' ({(dia_semana(data1))}).')
    elif operacao == 3:
        print('Sair')
        break