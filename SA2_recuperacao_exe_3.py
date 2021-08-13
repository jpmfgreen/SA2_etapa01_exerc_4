lista = [ ]
for Z in range(0, 20):
  lista.append(int(input('Digite número para ordenar: ')))

print(f'lista: {lista}')

#média dos números da lista
soma = 0
for N in range(0, len(lista)):
   soma = soma + lista[N]

media = soma/4              
print(f'A média de todos os números da lista é {media}.')  

#maior número da lista
maior_n = 1 
for num in range(0, len(lista)):
  if lista[num]>maior_n:
    maior_n = lista[num]
print(f'O MAIOR valor da lista é o {maior_n}.')       

#menor número da lista
menor_n = 100 
for num in range(0, len(lista)):
  if lista[num]<menor_n:
    menor_n = lista[num]
print(f'O MENOR valor da lista é o {menor_n}.') 