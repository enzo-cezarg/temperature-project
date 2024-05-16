import os

# Inicialização das variáveis que armazenarão valores-chave
contMeses = 0
maiorTemp = 0
menorTemp = 50
mesMenorTemp = 0
mesMaiorTemp = 0
somaTemperaturas = 0
qMesesEsc = 0

# Declaração de um array contendo os meses do ano
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Inicialização do laço de repetição que irá garantir que serão inseridos valores válidos
while contMeses != 12:
    # Output formatado adequadamente para o usuário
    print('===='*20)
    temperatura = float(input(f'Digite a temperatura para o mês de {meses[contMeses]} ({contMeses+1}) em graus Celsius: '))

    # Verificação do intervalo da temperatura
    if not(temperatura >= -60 and temperatura <= 50):
        print('Inválido! Temperatura deve estar entre -60 °C e 50 °C')
        continue
    else:
        print('Registrado!')
        # Soma das temperaturas
        somaTemperaturas += temperatura

        # Verificação de meses escaldantes
        if temperatura > 33:
            qMesesEsc += 1

        # Verificação da maior e da menor temperatura
        if temperatura > maiorTemp:
            maiorTemp = temperatura
            mesMaiorTemp = contMeses
        elif temperatura < menorTemp:
            menorTemp = temperatura
            mesMenorTemp = contMeses
        contMeses += 1
        
# Output final do programa
print('===='*20)
print(f'Temperatura média máxima anual: {somaTemperaturas/12:.2f} °C')
print(f'Quantidade de meses escaldantes (acima de 33 °C): {qMesesEsc}')
print(f'Maior temperatura lida: {maiorTemp:.1f} °C no mês de {meses[mesMaiorTemp]}')
print(f'Menor temperatura lida: {menorTemp:.1f} °C no mês de {meses[mesMenorTemp]}')