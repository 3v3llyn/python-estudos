#Desafio 004: Crie um script Python que leia dois números e tente mostrar a soma entre eles.
print('===== DESAFIO 004 =====')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
s = n1 + n2
#print('A soma entre', n1, 'e', n2, 'é:', s)
print('A soma entre {} e {} vale: {}'.format(n1,n2,s))
