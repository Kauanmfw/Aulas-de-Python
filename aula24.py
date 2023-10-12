# Operadores in e not in 
# Strings são interáveis    
# 0 1 2 3 4 5
# O T Á V I O
#-6-5-6-7-8-9
#nome = 'Ótavio'
#print(nome[2])
#print(nomd[-4])
'''print('a' in nome)
print ('z' in nome)
print (10 * '-')
print('vio' not in nome)
print('zero' in nome)
'''

nome = input('Digite seu nome:')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')