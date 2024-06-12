# # ====================================================================================== # #
# | Segunda fase do projeto avaliativo da cadeira de Lógica e Programação de Computadores  | #
# | Escrito por Enzo Cezar Garcia Rocha com início em 07/06/2024                           | #
# # ====================================================================================== # #

import matplotlib.pyplot as plt

# O arquivo fornecido teve seu nome alterado para "dados.csv" apenas por 
# motivos de praticidade, seu conteúdo não foi modificado
def carregarDados(arq):
    """Carrega os dados do arquivo fornecido"""
    with open(arq, 'r') as arquivo:
        # Pula o cabeçalho
        arquivo.readline()
        # Separa os valores
        dados = [linha[:-1].split(',') for linha in arquivo]
        val = []
        # Percorre as linhas do arquivo e gera tuplas com os valores já convertidos
        for lin in range(len(dados)):
            val.append((str(dados[lin][0]), float(dados[lin][1]), float(dados[lin][2]), float(dados[lin][3]), float(dados[lin][4]), float(dados[lin][5]), float(dados[lin][6]), float(dados[lin][7])))
        # Fechando o arquivo para evitar vazamentos de memória
        arquivo.close()
    return val

def salvarCabecalho(arq):
    """Retorna apenas o cabeçalho do arquivo"""
    with open(arq, 'r') as arquivo:
        cabecalho = arquivo.readline()
    return cabecalho[:-1].split(',')

def gerarMenu():
    """Gera o menu interativo"""
    print('===='*12)
    print('> Selecione a opção desejada:\n')
    print('  1. Visualizar todos os dados\n  2. Visualizar dados de precipitação\n  3. Visualizar dados de temperatura\n  4. Visualizar dados de umidade e vento\n')
    print('  0. Sair\n')
    print('===='*12)
    print()

def validaMes(mes):
    if mes >= 1 and mes <= 12:
        return True
    else:
        print('Mês inválido! Tente novamente.\n')
        return False
    
def validaAno(ano, mes):
    """Valida se o ano está no intervalo permitido"""
    if ano >= 1961 and ano <= 2016:
        # Registros de 2016 vão somente até julho, por isso essa providência
        if ano == 2016 and mes > 7:
            print('Mês inexistente na base de dados! Tente novamente.\n')
            return False
        else:
            return True
    else:
        print('Ano inválido! Tente novamente.\n')
        return False

def validaEntrada():
    """Valida cada mês e ano digitados pelo usuário, permitindo a redigitação caso necessário"""
    validaMesI = False
    while validaMesI == False:
        mesI = int(input('Digite o mês inicial (1 a 12): '))
        validaMesI = validaMes(mesI)
        if validaMesI == True:
            validaAnoI = False
            while validaAnoI == False:
                anoI = int(input('Digite o ano inicial (1961 a 7/2016): '))
                validaAnoI = validaAno(anoI, mesI)
                if validaAnoI == True:
                    validaMesF = False
                    while validaMesF == False:
                        mesF = int(input('Digite o mês final (1 a 12): '))
                        validaMesF = validaMes(mesF)
                        if validaMesF == True:
                            validaAnoF = False
                            while validaAnoF == False:
                                anoF = int(input('Digite o ano final (1961 a 7/2016): '))
                                validaAnoF = validaAno(anoF, mesF)
                                if validaAnoF == True:
                                    return [mesI, anoI, mesF, anoF]

def ordenarAnos(mesI, anoI, mesF, anoF):
    """Ordena de forma que os anos menores fiquem sempre como iniciais"""
    if anoI > anoF:
        aux = anoF
        anoF = anoI
        anoI = aux

        aux = mesI
        mesI = mesF
        mesF = aux
    elif anoF == anoI:
        # Caso o ano seja o mesmo, verifica os meses e põe em ordem
        if mesI > mesF:
            aux = mesI
            mesI = mesF
            mesF = aux

    return [mesI, anoI, mesF, anoF]


def setarIntervalo(arquivo, datas, posI, posF, cont):
    """Define a posição inicial e posição final do intervalo desejado no arquivo"""

    # Se o mês final for 12 ele é substituído pelo primeiro mês do ano seguinte
    if datas[2] == 12:
        datas[2] = '1'
        datas[3] = f'{int(datas[3] + 1)}'
    else:
        datas[2] = f'{int(datas[2] + 1)}'

    # Percorre o arquivo para pegar as posições do intervalo
    for linha in arquivo:
        if (f'01/0{datas[0]}/{datas[1]}') in linha or (f'01/{datas[0]}/{datas[1]}') in linha:
            if posI == 0:
                posI = cont
            else:
                continue

        if (f'01/0{datas[2]}/{datas[3]}') in linha or (f'01/{datas[2]}/{datas[3]}') in linha:
            if posF == 0:
                posF = cont
            else:
                continue
        cont += 1
    return posI,posF

def visualizarTodos(mesI, anoI, mesF, anoF, arquivo, cab):
    """Exibe todos os dados no intervalo determinado"""
    datas = ordenarAnos(mesI, anoI, mesF, anoF)

    posI = 0
    posF = 0
    cont = 0
        
    posI, posF = setarIntervalo(arquivo, datas, posI, posF, cont)

    print('===='*12)
    print(f'{cab[0]} | {cab[1]} | {cab[2]} | {cab[3]} | {cab[4]} | {cab[5]} | {cab[6]} | {cab[7]}')
    print()
    for i in range(posI, posF):
        print(arquivo[i])
    print()
        
def visualizarPrec(mesI, anoI, mesF, anoF, arquivo):
    """Exibe apenas a precipitação no intervalo determinado"""
    datas = ordenarAnos(mesI, anoI, mesF, anoF)

    posI = 0
    posF = 0
    cont = 0
        
    posI, posF = setarIntervalo(arquivo, datas, posI, posF, cont)

    print('===='*12)
    print('> Precipitação:')
    print()
    for i in range(posI, posF):
        print(f'{arquivo[i][0]}: {arquivo[i][1]}')
    print()

def visualizarTemp(mesI, anoI, mesF, anoF, arquivo):
    """Exibe apenas os dados de temperatura no intervalo determinado"""
    datas = ordenarAnos(mesI, anoI, mesF, anoF)

    posI = 0
    posF = 0
    cont = 0
        
    posI, posF = setarIntervalo(arquivo, datas, posI, posF, cont)

    print('===='*12)
    print('> Temperaturas:')
    print()
    for i in range(posI, posF):
        print(f'{arquivo[i][0]}: Máx.: {arquivo[i][2]} °C | Mín.: {arquivo[i][3]} °C')
    print()

def visualizarUmiVen(mesI, anoI, mesF, anoF, arquivo):
    """Exibe apenas os dados de umidade e vento no intervalo determinado"""
    datas = ordenarAnos(mesI, anoI, mesF, anoF)

    posI = 0
    posF = 0
    cont = 0
        
    posI, posF = setarIntervalo(arquivo, datas, posI, posF, cont)

    print('===='*12)
    print('> Umidade relativa e Velocidade do vento:')
    print()
    for i in range(posI, posF):
        print(f'{arquivo[i][0]}: Um. Rel.: {arquivo[i][6]:.2f} | Vel. Vento: {arquivo[i][7]:.2f}')
    print()

def mesMaisChuvoso(arquivo):
    """Pega o mês mais chuvoso de cada ano"""
    maisChuvoso = {}
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    # Anos que não constam no arquivo de dados
    # 1979, 1980, 1981, 1982, 2001 geram resultados errados
    anosInvalidos = [1985, 1986, 1987]
    for i in range(1961, 2017):
        maiorPre = 0
        mesMaiorPre = ''
        soma = 0
        if i in anosInvalidos:
            continue
        for j in range(1,13):
            if i == 2016 and j == 7:
                break
            soma = 0
            posI, posF = setarIntervalo(arquivo, [j,i,j,i], 0, 0, 0)

            for dias in range(posI, posF):
                # Faz a soma das precipitações do mês
                soma += arquivo[dias][1]
            # Compara com os maiores dados lidos naquele ano
            if soma > maiorPre:
                maiorPre = soma
                mesMaiorPre = meses[j-1]
        maisChuvoso[i] = (f'{i}: {mesMaiorPre} > {maiorPre:.2f}')

    # Retorna um dicionário com os meses mais chuvosos por ano e sua precipitação
    return maisChuvoso

def mediaMes(arquivo, meses, mes):
    media = {}

    cont = 1
    numMes = contaMeses(meses, mes, cont)

    for i in range(2006,2017):
        cont = 0
        mediaMin = 0 
        somaMin = 0

        if i == 2016 and numMes >= 7:
            break

        posI, posF = setarIntervalo(arquivo, [numMes, i, numMes, i], 0, 0, 0)

        for dias in range(posI, posF):
            somaMin += arquivo[dias][3]
            cont += 1

        mediaMin = somaMin/cont
        media[(f'{mes}{i}')] = (f'{mediaMin:.2f}')

    return media

def contaMeses(meses, mes, cont):
    """Pega o mês digitado e retorna seu número equivalente"""
    for elem in meses:
        if mes == elem:
            numMes = cont
            break
        cont += 1
    return numMes

def gerarGrafico(mes, numMes, dicionario):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    valores = []
    for i in range(2006,2017):
        if i == 2016 and numMes >= 7:
            break

        chave = f'{mes}{i}'
        valores.append(float(dicionario[chave]))
    
    anos = [a for a in range(2006, 2017)]

    plt.bar(anos, valores)
    plt.title(f'Médias mínimas para o mês de {meses[numMes-1]}')
    plt.show()

    return

# ====================================== Programa principal ======================================

# Carga dos dados nas variáveis
dados = carregarDados('dados.csv')
cab = salvarCabecalho('dados.csv')

mesesInput = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

while True:
    gerarMenu()
    op = int(input('Digite o número da opção: '))
    if op == 0:
        print('Fim do programa!')
        break
    elif op == 1:
        intervalo = validaEntrada()
        visualizarTodos(intervalo[0], intervalo[1], intervalo[2], intervalo[3], dados, cab)
        
    elif op == 2:
        intervalo = validaEntrada()
        visualizarPrec(intervalo[0], intervalo[1], intervalo[2], intervalo[3], dados)

    elif op == 3:
        intervalo = validaEntrada()
        visualizarTemp(intervalo[0], intervalo[1], intervalo[2], intervalo[3], dados)

    elif op == 4:
        intervalo = validaEntrada()
        visualizarUmiVen(intervalo[0], intervalo[1], intervalo[2], intervalo[3], dados)

    else:
        print('Opção inválida!')

#    print()
#    print('> Mês/ano mais chuvosos:\n')
#    maisChuvoso = mesMaisChuvoso(dados)
#    for i in range(1961, 2017):
#        if i in maisChuvoso:
#            print(maisChuvoso[i])
#    print()

    mes = input('Digite um mês para exibir dados (ou 0 para sair): ').lower()
    print()
    if mes == '0':
        print('Fim do programa!')
        break
    while not(mes in mesesInput):
        print('Mês inválido! Tente novamente.\n')
        mes = input('Digite um mês para exibir dados: ').lower()
    
    medias = mediaMes(dados, mesesInput, mes)
    numMes = contaMeses(mesesInput, mes, 1)
    somaMin = 0
    cont = 0
    for i in range(2006, 2017):
        if i == 2016 and numMes >= 7:
            break
        chave = f'{mes}{i}'
        print(f'{mes}/{i}: {medias[chave]} °C')
        somaMin += float(medias[chave])
        cont += 1
    print() 
    
    print(f'> Média mín. geral do período no mês de {mes}: {somaMin/cont:.2f} °C\n')

    gerarGrafico(mes, numMes, medias)