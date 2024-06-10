# # ====================================================================================== # #
# | Segunda fase do projeto avaliativo da cadeira de Lógica e Programação de Computadores  | #
# | Escrito por Enzo Cezar Garcia Rocha em 07/06/2024                                      | #
# # ====================================================================================== # #

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
    if ano >= 1961 and ano <= 2016:
        if ano == 2016 and mes > 7:
            print('Mês inexistente na base de dados! Tente novamente.\n')
            return False
        else:
            return True
    else:
        print('Ano inválido! Tente novamente.\n')
        return False

def validaEntrada():
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
    if anoI > anoF:
        aux = anoF
        anoF = anoI
        anoI = aux

        aux = mesI
        mesI = mesF
        mesF = aux
    elif anoF == anoI:
        if mesI > mesF:
            aux = mesI
            mesI = mesF
            mesF = aux

    return [mesI, anoI, mesF, anoF]


def setarIntervalo(arquivo, datas, posI, posF, cont):
    datas[2] = f'{int(datas[2] + 1)}'

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


# ====================================== Programa principal ======================================

# Carga dos dados nas variáveis
dados = carregarDados('dados.csv')
cab = salvarCabecalho('dados.csv')

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
        print('temperaturas')

    elif op == 4:
        intervalo = validaEntrada()
        print('vento e umidade')

    else:
        print('Opção inválida!')
