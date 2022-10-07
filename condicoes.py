# Comentarios
'''
Comentarios is a Python package for working with Comentarios.

'''
idade = 16

if idade <= 15:
    print('Acesso nao permitido!')
elif idade > 15 or idade < 18:
    print('Necessita autorizacao')
else:
    print('Acesso liberado!')

#VETOR
materias = ['Web2','00 I','BD']
print(type(materias))
print(materias)

#Tamanho da lista/vetor/array
print(f' \nTamanho da lista: {len(materias)}\n')

#FOR mostrando os valores do vetor
for i in range(0,len(materias)):
    print(materias[i])

# lista com 5 precos de produtos, clacular o total

preco = [10,15,20,25]
soma = 0

for i in range(0,len(preco)):
    soma += preco[i]

print(f'O valor total dos produtos: {soma}')

print(max(preco))
print(min(preco))
print(sum(preco))