secretnumer = 42
chute = input("Digite o seu número: ") #funçao input devolve string
print("vc digitou", chute)
if(secretnumer == chute):
    print("Vc acertou")
else:
    print("Vc errou")
                           #esse codigo nao pode
chute_str = input..
print...
chute2 = int(chute_str)  #funçaõ int converte o valor para inteiro
if(secretnumer == chute):
    ..
///////////////////////////////////////////////////////////////////
idade1 = 10
idade2 = "20"
print(idade1 + idade2) #nao funfa

idade1 = 10
idade2 = int("20")
print(idade1 + idade2) # acertou

#o + tem a funçao de concatenar e nao somar(apenas para variaveis int)

////////////////////////////////////////////////////////
numero1 = 10
numero2 = "20"
produto = numero1 * numero2
print(produto)
>>>20202020202020202020
#isso é a syntax sugar do Python. O código acima é equivalente
# a : 10*"20".

/////////////////////////////////////////////////////////////
if (numero_secreto == chute):
    print("Você acertou!")
else:
    if (chute > numero_secreto):
        print("Você errou! O seu chute foi maior")
    else:
        print("Você errou! O seu chute foi menor")
# este codigo e a msm coisa desse:
if (numero_secreto == chute):
    print("Você acertou!")
else:                                 #else nao aceita condiçao!
    if (chute > numero_secreto):      #por isso o else if existe
        print("Você errou! O seu chute foi maior")
    elif (chute < numero_secreto):
        print("Você errou! O seu chute foi menor")
#para ficar mais top:
acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto
if (acertou):
    print("Você acertou!")
else:
    if (maior):
        print("Você errou! O seu chute foi maior")
    elif (menor):
        print("Você errou! O seu chute foi menor")

//////////////////////////////////////////////////////////////
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade  = idade > 18
crianca      = idade < 12
adolescente  = idade > 12

print(maior_idade,crianca,adolescente)
# resultado sera false,false,True
///////////////////////////////////////////////////////////////
while == msm coisa de c
-----------------------
print("Tentativa", rodada, "de", total_de_tentativas)
# rodada e total_de_tentativas sao variaveis mutavies.
# mas vamos fazer de um modo mais elegante
# podemos escrever strings q eventualmente podem mudar. onde ela mudar,
#usaremos {}
print("Tentativa {} de {}", rodada, total_de_tentativas)
>>> Tentativa {} de {} 1 3
#deu ruim né? para funfar vamos usar a funçao format!
print("Tentativa {} de {}".format(rodada, total_de_tentativas))
#isso se chama INTERPOLAÇAO DE STRINGS
dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017
"Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim)
#usando no while
numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")

    rodada = rodada + 1

print("Fim do jogo")
//////////////////////////////////////////////////////////////////
for rodada in range(1,10) #rodada foi declarada no for.
#roda de 1 ate 9
ou for rodada in [1,2,3,4,5,6,7,8,9,10]
# a funcao range tem o seguinte parametro range(start, stop[, step])
# o step é opcional, e nele nos podemos pular
contador = 1;
while(contador <= 10):
    print(contador)
    contador = contador + 3
>>> 1 4 7 10
# esse codigo em for fica
for contador in range(1,11,3):
    print(contador)
/////////////////////////////////////////////////////////////////////
#break, que acaba, encerra o laço;
#continue, que acaba, encerra a iteração, continuando para a próxima instruçao
for i in range(1,8):
    if(i == 5):
        continue
    print(i)
>>> 1 2 3 4 6 7
/////////////////////////////////////////////////////////////////////////////////
concatenaçao = nome + nome2 = 'stringstring2'
concatenaçao = nome + ' ' + nome2 = 'string string2'
nome= 'hualian' nome[0:2] >>> 'hu'
num1 **5 >>> num1⁵
5 + 2 / 2 >>> 6.0
(5+2) / 2 >>> 3.5
import math
math.sqrt(16) >>> 4
///////////////////////////////////////////////////////////////////////////////////
tgcf = ('hua cheng', 'xie lian', 'yushi hang', 'pei ming')
type(tgcf) >>> tuple
tgcf = ['hua cheng', 'xie lian', 'yushi hang', 'pei ming'] >>> list
tgcf.append('shi qingxuan')   tgcf.insert(5, 'ming yi')
tgcf.pop(4) ou tgcf.remove('pei ming')
tgcf2 = ['bai wuxiang'] tgcf + tgcf 2 = concatenaçao das 2
///////////////////////////////////////////////////////////////////////////////////
danmei = {'tgcf': 'hualian', 'erha': ['ranwan','shuangmeimeng'], 'spl':'changgu'}
del danmei['spl'] for x in danmei print(x) >>> printa tds as chaves 
for x in danmei print(x + '' + danmei[x])
danmei.get('tgcf', 'nao consta') >>> hualian # danmei.get('sv', 'nao consta') >>> 'nao consta'
danmei['erha'].append('WANNING')
danmei.clear() >>> {}  danmei['sv'] = 'liushen'

//////////////////////////////////////////////////////////////////////////////////
s1 = input(''wtv).lower() -> recebe a string em caracteres minusculos
for i in tgcf: #o for pode percorrer listas, strings(printa cd letra da string)
    print(i)   >>> hua cheng, xie lian....
for i in danmei:
    print(danmei[i]) >>> printa tds os valores associados as chaves
    print(i, ' ', danmei[i]) >>> printa as chaves e os valores
    
danmei2 = [['HC', 'XL', 'SQX'], ['LBH','SQQ','LQG'], ['CWN','MR']]
    for i in danmei2:
        #print(i) >>> printa as 3 listas
        for j in i:
            print(j)
///////////////////////////////////////////////////////////////////////////////////////

        
   
    














