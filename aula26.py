''' Formatação básica de strings
 s - string
 d - int
 f - float
 .< números de digitos>f
 x ou X - Hexadecimal 
 (Caractere)(><^)(quantidade)
 > - esquerda
 < - Direita
 ^ - centro
 Sinal - + ou -
 Ex. : 0>-100, 1f
 Conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')
print (f'{variavel: >10}')
print (f'{variavel: <10}.')
print (f'{variavel: ^10}.')
print (f'{1000.081083927392:.1f}')