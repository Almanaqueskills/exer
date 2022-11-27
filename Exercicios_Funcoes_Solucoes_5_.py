Exercícios com Funções: Proposta de Soluções
Esta página contém algumas propostas de soluções para os exercícios da Lista 6: Funções.

Exercício 1
Esconder número das linhas
   1 def exercicio_1(n):
   2     for i in range(n):
   3         i += 1
   4         print str(i) * i
Proposta por ThiagoSeixas

Exercício 1
Esconder número das linhas
   1  def exercicio1(n):
   2      for i in range(1, n+1):
   3          for j in range(i):
   4              print i,         # print j times the number i in the same line 
   5          print                # print a new line
Proposta por HenriqueBaggio

Exercício 1
Esconder número das linhas
   1  def exercicio_1(n):
   2      x=1
   3      while x<=n:
   4         y=0
   5         while y<x:
   6             print '%i' %x,
   7             y+=1
   8         x+=1
   9         print 
Proposta por Lhzefe

Exercício 1
Esconder número das linhas
   1  def ex1(n):
   2      for i in range(1, n+1): 
   3          print((str(i)+" ")*i)
Proposta por RogerioDuarte

* Exercício 2 valor = []

def nesima(n):

for i in range(1,10): #para 9 elementos
if i < 10:

valor.append(n+i) print(valor)
Por Diel Jr

Exercício 2

Esconder número das linhas
   1 def imprimeLinha(numero):
   2     for n in range(1, numero + 1):
   3         print(('  {} ').format(n), end='')
   4     print()
   5 
   6 def imprimeSequencia(numero):
   7     for numero in range(numero + 1):
   8         imprimeLinha(numero)
   9 
  10 
  11 numero = input('Digite um número: ')
  12 imprimeSequencia(int(numero))
Proposta por Vinicius Almeida
Exercício 3
Esconder número das linhas
   1  def exercicio3(a, b, c):
   2      return a + b + c
Proposta por IuriSilvio

Exercício 4
Esconder número das linhas
   1  def pn(x):
   2      if x<0:
   3          return "N"
   4      elif x>0:
   5          return "P"
   6      else:
   7         return "ZERO"
by Jorge
Exercício 5
Esconder número das linhas
   1  def somaimposto(taxaimposto,custo):
   2     return (0.01*taxaimposto)*custo + custo
   3  
by Jorge
Exercício 6.

Esconder número das linhas
   1 def hora(h, m):
   2     b = h / 12
   3     if b <= 1:
   4         hh = str(h)
   5         print('Sua hora: '+ hh + ':', end='')
   6     elif b > 1 and b < 2:
   7         hhh = str(h - 12)
   8         print('Sua hora: '+ hhh + ':', end='')
   9     else:
  10         print('Formato de hora invalido')
  11     if b <= 1 and m <= 60:
  12         print(m, 'a.m')
  13     elif b > 1 and m <= 60:
  14         print(m, 'p.m')
  15     else:
  16         print('Formato de minutos invalidos')
  17 
  18 while True:
  19     print('digite 666 para sair')
  20     h = int(input('Informe a hora:'))
  21     if h == 666:
  22         break
  23     m = int(input('Informe os minutos: '))
  24     hora(h, m)
Proposta por Leo Araujo

Exercício 7

Esconder número das linhas
   1 qtPrest = []
   2 listaVc = []
   3 ct = 0
   4 def funcVP(VP, NumDias):
   5     Vpm = VP * 1.03
   6     valorC = round(Vpm *((1 + 0.001) ** NumDias), 2)
   7     listaVc.append(valorC)
   8     print('Valor corrigido:', valorC)
   9     global ct
  10     ct += 1
  11     qtPrest.append(ct)
  12 
  13 while True:
  14     VP = float(input('Digitr o valor da prestação: (0 para sair) '))
  15     if VP == 0:
  16         break
  17     NumDias = int(input('Quantos dias que está em atraso: '))
  18     funcVP(VP, NumDias)
  19 print('Quantidade de prestações pagas: ', ct)
  20 print('Valor total de prestações pagas no dia: R$', round(sum(listaVc)), 2)
Proposta por Leo Araujo

Exercício 7. Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
Esconder número das linhas
   1  __author__ = 'JonasAlves'
   2 
   3  def valorPagamento(vp, da):
   4         if da < 1:
   5                 valor = vp
   6                 print(valor)
   7                 return valor
   8         else:
   9                 valor = (vp + vp * 0.03 + 0.01 * da)
  10                 print(valor)
  11                 return valor
  12 
  13  valor = []
  14  vp = 0
  15  da = 0
  16  qp = 0
  17  valortotal = 0
  18 
  19  while True:
  20         qp += 1
  21         vp = float(input('Qual o valor da prestacao? '))
  22         da = int(input('Quantos dias esta em atraso? '))
  23         if vp == 0:
  24                 break
  25         valor.append(valorPagamento(vp, da))
  26 
  27  qp -= 1
  28  for i in range(qp):
  29     valortotal += valor[i]
  30 
  31  print('Relatorio do dia, foram pagas %d prestacoes no valor: ' %qp, valor)
  32  print('Valor total de prestacoes pagas: ', valortotal)
Exercício 8
Esconder número das linhas
   1  def exercicio8(n):
   2      s = str(n)
   3      return len(s)
Exercício 9:Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

Esconder número das linhas
   1 def exercicio_9(n):
   2     inverte=str(n)
   3     print inverte[::-1]
Proposta por ThiagoSeixas

Exercício 9: A ideia nesse exercicio é que, para um dado digito numa posição i do número de entrada, ele terá o seu valor multiplicado por 10**i no número de saída.
Esconder número das linhas
   1  def reverso(n):
   2      s = str(n)       # converte o numero para uma string
   3      l = 0
   4      for x in range(len(s)):
   5          l += int(s[x]) * (10**x)
   6      return l
Exercício 10

Esconder número das linhas
   1 from random import randint
   2 k = 0
   3 
   4 def craps():
   5     k = randint(2,13)
   6     if k == 7 or k == 11:
   7         print('Você é o mestre!! Ganhou!!', k)
   8     elif k == 2 or k == 3 or k == 12:
   9         print('Craps!!! Você perdeu!', k)
  10     elif k in range(4,6) or k in range(8,10):
  11         print('Esse é o seu numero vamos jogar!! Numero:', k)
  12         print('Digite D para jogar o dado: ')
  13         z = 0
  14         while k != z:
  15             print('Digite D para jogar o dado:')
  16             s = input()
  17             if s == 'D':
  18                 z = randint(2,13)
  19                 print('Seu numero foi: ', z)
  20                 if z == 7:
  21                     print('Voce Perdeu!!!')
  22                     break
  23         if  z != 7:
  24             print('Voce Ganhou!!!')
  25 craps()
Proposta por Leo Araujo

Exercício 10 - Foi criado uma função interna para jogar os dados e no final apresenta a quantidade de vezes que ganhou e perdeu.

Esconder número das linhas
   1 from random import randint
   2 def craps():
   3     #Função para jogar os dados 
   4     def jogar():
   5         dado1 = randint(1, 6)
   6         dado2 = randint(1, 6)
   7         print(f'DADO AMARELO {dado1} e DADO AZUL {dado2} e SOMA {dado2 + dado1}')
   8         return dado1 + dado2
   9 
  10     cont = ganho = perda = 0
  11     while True:
  12         a = input('jogar: ')
  13         if a in "nN": break
  14         valor = jogar()
  15         
  16         if cont == 0 and valor == 7 or valor == 11:
  17             print('come-out roll GANHOOOOUUU')
  18             ganho += 1
  19             cont = 0
  20         elif cont == 0 and valor == 2 or valor == 3 or valor == 12:
  21             print('come-out roll PERDEEEEUUUU')
  22             cont = 0
  23             perda += 1
  24         elif cont == 0:
  25             passLine = valor
  26             cont = 1
  27             print('jogue mais uma vez')
  28             continue
  29         elif cont == 1:
  30             if passLine == valor:
  31                 print('Pass line  GANHOOOOUUU')
  32                 ganho += 1
  33                 
  34             else:
  35                 print('PERDEEEEUUUU \nTenta novamente')
  36                 perda += 1
  37             cont = passLine = 0
  38         print('-*' * 15)
  39     print('OBRIGADO POR SE DIVERTIR COM CRAPS EM NOSSO CASSINO')
  40     print(f'você ganhou {ganho} e perdeu {perda}')
  41 
  42 craps()
Proposta por JeandroBrito

Exercício 11:
Esconder número das linhas
   1 def dma(d,m,a):
   2     dia = d
   3     mes = m
   4     ano = a
   5     
   6     if dia <=31:
   7     meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outrubro','Novembro','Dezembro']
   8         mesPorextenso = meses[m-1]
   9         if mesPorextenso == 'Fevereiro' and dia > 28 and ano%4==1:
  10             print("Fevereiro só tem 28 dias em anos não bissextos!")
  11         elif mesPorextenso == 'Fevereiro' and dia>=30:
  12             print("Fevereiro só tem 29 ou 28 dias!")
  13 
  14         else:
  15             print("%d de %s de %i"%(d,mesPorextenso,ano))
  16 
  17     else:
  18         print("Dia inválido")

Esconder número das linhas
   1 def dataExtenso(data):
   2     meses = [(), ['janeiro', 31], ['fevereiro', 29], ['março', 31], ['abril', 30],
   3              ['maio', 31], ['junho', 30], ['julho', 31], ['agosto', 31], ['setembro', 30],
   4              ['outubro', 31], ['novembro', 30], ['dezembro', 31]]
   5 
   6     data = data.split('/')
   7     dia, mes, ano = int(data[0]), int(data[1]), int(data[2])
   8     if mes == 2:
   9         meses[mes][1] = anoBissexto(ano)
  10     if 0 < mes < 13 and 0 < dia <= meses[mes][1]:
  11         print(f'{dia} de {meses[mes][0]} de {ano}')
  12     else:
  13         print('NULL')
  14 
  15 #verifica se ano é bissexto
  16 def anoBissexto(ano):
  17     if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
  18         return 29
  19     else:
  20         return 28
  21 
  22 dataExtenso('29/2/2020')
  23 dataExtenso('29/2/2021')
Proposta por JeandroBrito

Exercício 12: Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
Esconder número das linhas
   1  import random
   2 
   3  def exercicio_12(s):
   4      embaralha = random.sample(s, len(s)) # String vira lista
   5      a = ''.join(embaralha) # lista vira string
   6      print (a)
Proposta por ThiagoSeixas

Exercício 13
Esconder número das linhas
   1  def valor_por_omissao(valor):
   2      if valor=='':
   3          return int(1)
   4      else:
   5          return faixa_minima_maxima(int(valor))
   6 
   7  def faixa_minima_maxima(valor):
   8      if valor<1:
   9          return 1
  10      elif valor>20:
  11          return 20
  12      else:
  13          return valor
  14 
  15  def cria_linha(linha):
  16      l='+'
  17      for x in range(linha):
  18          l+='-'
  19      l+='+'
  20      print l
  21 
  22  def cria_coluna(linha, coluna):
  23      for y in range(coluna):
  24          c='|'
  25          c+= ' '*linha
  26          c+='|'
  27          print c
  28 
  29  def desenha_moldura(linha, coluna):
  30      cria_linha(linha)
  31      cria_coluna(linha, coluna)
  32      cria_linha(linha)
  33 
  34  linha=raw_input('Diga quantos +----+, entre 1 e 20: ')
  35  coluna=raw_input('Diga quantos |    |, entre 1 e 20: ')
  36  desenha_moldura(valor_por_omissao(linha), valor_por_omissao(coluna))
Proposta por Lhzefe

* Exercício 13

Esconder número das linhas
   1 def primeria_linha_coluna(linha, coluna):
   2     contC = 0
   3     contL = 0
   4     c = ''
   5     l = ''
   6     while (contL < linha) and (contC < coluna):
   7         if contL == 0:
   8             l = '+'
   9             for i in range(coluna):
  10                 c += '-'
  11             l = '+'
  12         contL += 1
  13         contC += 1
  14     print(l+c+l)
  15     
  16 def outras_linhas(linha, coluna):
  17     contC = 0
  18     contL = 0
  19     c = ''
  20     l = ''
  21     while contL < linha:
  22         if contL == 0:
  23             l = '|'
  24             for i in range(linha):
  25                 c += ' '
  26             l = '|'
  27         contL += 1
  28         contC += 1
  29         print(l+c+l)
  30 
  31 def ultima_linha(linha, coluna):
  32     contL = 0
  33     contC = 0
  34     l = ''
  35     c = ''
  36     while (contL < linha) and (contC < coluna):
  37         if contL == 0:
  38             l = '+'
  39             for i in range(coluna):
  40                 c += '-'
  41             l = '+'
  42         contL += 1
  43         contC += 1
  44     print(l+c+l)
  45         
  46     
  47     
  48 linha = int(input('Informe o número de linhas: '))
  49 coluna = int(input('Informe o número de colunas: '))
  50 
  51 primeria_linha_coluna(linha, coluna)
  52 outras_linhas(linha, coluna)
  53 ultima_linha(linha, coluna)
Proposto por Diel Junior

* Exercício 14. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada

posição e no qual a soma das linhas, colunas e diagonais é a mesma. Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
Esconder número das linhas
   1  def gera_combinacoes(lista, n):    
   2     #  gera tupla com todas as combinações possíveis da soma de três números da lista 
   3     #  que seja iguais a 15.
   4     for i in lista:
   5         for j in lista:            
   6             if n + i + j == 15 and (n != i and n != j and i != j):
   7                 combinacoes.append((n, i, j))
   8 
   9  
  10  def gera_quadro(comb, L1):
  11     linha1 = L1    
  12     for i in range(len(comb)):
  13         linha2 = comb[i]
  14         for j in range(len(comb)):
  15             linha3 = comb[j]
  16             
  17                     
  18             if (linha1[0] + linha2[0] + linha3[0] == 15) and\
  19                (linha1[1] + linha2[1] + linha3[1] == 15) and\
  20                (linha1[2] + linha2[2] + linha3[2] == 15) and\
  21                (linha1[0] + linha2[1] + linha3[2] == 15) and\
  22                (linha1[2] + linha2[1] + linha3[0] == 15):     
  23 
  24                 if (linha1[0] not in linha2) and\
  25                    (linha1[1] not in linha2) and\
  26                    (linha1[2] not in linha2):
  27 
  28                     print(linha1)
  29                     print(linha2)
  30                     print(linha3)
  31                     print()
  32                 
  33 
  34  lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  35  combinacoes = []
  36 
  37  for n in range(1,10):    
  38     gera_combinacoes(lista, n)
  39 
  40  print()
  41 
  42  for L1 in combinacoes:
  43     gera_quadro(combinacoes, L1)
Proposta por JoelNogueira

* Exercício 14.

Esconder número das linhas
   1 from itertools import combinations, permutations
   2 
   3 
   4 def validaTabela(tabela): # Verifica se a tabela é válida
   5     if sum(tabela[:3]) == sum(tabela[3:6]) == sum(tabela[6:10]):
   6         if sum(tabela[::3]) == sum(tabela[1::3]) == sum(tabela[2::3]):
   7             if sum(tabela[::4]) == sum(tabela[2:8:2]):
   8                 print(tabela, ' valida ')
   9                 return 1
  10             else: return 0
  11         else: return 0
  12     else:
  13         return 0
  14 
  15 
  16 def gera(tab): #gerar as matrizes possíveis
  17     cont = 0
  18     validos = 0
  19     for i in permutations(tab,9):
  20         cont += 1
  21         validos += validaTabela(i)
  22     print(f'total de verificações {cont} e matriz válidas {validos}')
  23 
  24 tabela = [1,2,3,4,5,6,7,8,9]
  25 
  26 gera(tabela)