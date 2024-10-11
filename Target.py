#1)
def achaFibo(n):
  fiboList = [1, 1]
  fibo = 0
  while fibo <= n:
    fibo = fiboList[-1] + fiboList[-2]
    fiboList.append(fibo)
  return print(f'{n} pertence a sequência de fibonacci.') if n in fiboList else print(f'{n} não pertence à sequencia de fibonacci.')

achaFibo(int(input('Digite n: ')))

#2)
def achaA(string):
  ocorrencias = []
  for letra in string:
    if letra in 'aãáâàÃÁÂÀ':
      ocorrencias.append(letra)
  if len(ocorrencias) > 0:
    return print(f"A letra 'a' ocorre {len(ocorrencias)}x na string. ")
  else: return print("A letra 'a' não ocorre na string.")
achaA(input('Digite a string: '))

#3)
i = 12
soma = 0
k = 1
while k < i:
  k = k + 1
  soma = soma + k
print('O resultado do programa do exercício três é', soma)