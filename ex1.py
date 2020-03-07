repetir = 's'
fatura = []
total = 0

while repetir == 's':
    produto = input('digite o nome do prod')
    preco = float(input('digite o preco dele'))
    fatura.append([produto, preco])
    total += preco
    repetir = input('quer continuar? (s/n)').lower()
for i in fatura:
    print(i[0], '-', i[1])
print('total da fatura e: ', total)

#nesse codigo, da ruim se alguem digitar 10,00 como preco. o input nao consegue converter pra float
repetir = 's'
fatura = []
total = 0
valid_preco = False
while repetir == 's':
    produto = input('digite o nome do prod')
    preco = float(input('digite o preco dele'))
    while valid_preco == False:
      Try:
        preco = float(preco)
        valid_preco
    fatura.append([produto, preco])
    total += preco
    repetir = input('quer continuar? (s/n)').lower()
for i in fatura:
    print(i[0], '-', i[1])
print('total da fatura e: ', total)


