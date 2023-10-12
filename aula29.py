"""
Introdução ao try/excpet
try -> tentar executar um codigo
except -> ocorreu algum erro  ao tentar executar

"""

numero_str = input(
    'vou dobrar o numero que você digitar: '
)

try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print ('float', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um numero..')