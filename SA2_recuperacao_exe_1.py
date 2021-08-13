L = [5,7,2,9,4,1,3]

#contador sem o uso da função len
cont = 0
for i in L:
  cont = cont + 1

print(f'A lista tem {cont} posições.')

#maior número da lista
maior_n = 1 
for num in range(0, len(L)):
  if L[num]>maior_n:
    maior_n = L[num]
print(f'O MAIOR número da lista é o {maior_n}.')       

#menor número da lista
menor_n = 100 
for num in range(0, len(L)):
  if L[num]<menor_n:
    menor_n = L[num]
print(f'O MENOR número da lista é o {menor_n}.') 

#soma de todos os elementos da lista
soma = 0
for num in range(0, len(L)):
   soma = soma + L[num]
              
print(f'A soma de todos os números da lista é {soma}.') 
            
#ordenar a lista em ordem crescente
for num in range (len(L)-1,0,-1):
  for i in range(num):
    if L[i]>L[i+1]:
      aux = L[i]
      L[i] = L[i+1]
      L[i+1] = aux

print(L)

#ordenar a lista em ordem descrente
for num in range (len(L)-1,0,-1):
  for i in range(num):
    if L[i]<L[i+1]:
      aux = L[i]
      L[i] = L[i+1]
      L[i+1] = aux

print(L)
