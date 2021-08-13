
def mostra_lista(lista):
    contador=0
    for valor in lista:
        contador = contador + 1
        print(contador,')',valor)


lista = [ ]
for Z in range(0, 5):
  lista.append(int(input('Digite número para ordenar: ')))


mostra_lista(lista)