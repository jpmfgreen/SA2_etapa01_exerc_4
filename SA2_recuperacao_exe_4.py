def linha(tam_linha):
  lin = '_'
  for J in range(tam_linha):
    print(lin, end='')

tam_linha = int(input('Digite o tamanho da linha: '))
linha(tam_linha)