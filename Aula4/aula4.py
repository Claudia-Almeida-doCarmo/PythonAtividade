#  30/07/22 Tipos de dados
"""
TIPOS DE DADOS
str - string - textos entre '' ou ""
int - inteiro - 123456 (números com pontos)
float - real/ponto flutuante 10.50 1.5 Todos com pontos em todas linguagens de programação.
bool - booleano/lógico - true / false 0 ou 1 sim ou não
Python  linguagem interpretada e de tipagem dinâmica !!! Ele interpreta de acordo com o códico q tem no código.
ou seja quando é uma string ele sabe e assim sucessivamente.
*** NÚMEROS NÃO USAM ASPAS !!!!! SE USAR VIRA UMA STRING !!!!
"""
print('Luiz', type('Luiz'))
print(10, type(10))
print(25.23, type(25.23))
print(10==10, type(10==10)) # == SIGNIFICA PERGUNTAR SE É IGUAL ..
print('l'=='l', type('l'== 'l'))
print('C'=='l', type('c'== 'l'))
print('1.10', type('1.10'))
print(1.10, type(1.10))
print(100, type(100))
print('Luiz', type('Luiz'), bool('Luiz'))
print('', type(''))
print(bool('')) # sempre q estiver vazio, sem valor dará falso !!!
print('10', type('10'), type(int('10'))) #  dadam a ordem de transformar p número inteiro Type Quest
print('10',type('10'), type(10)) # mas nem sempre é possível.
print('10'+'10') #  junta os valores !!!
#  print('10'+10) NÃO PODE !!!!! DAR ERROR !!!!!
#  ATIVIDADE:
# string: NOme
print('Claudia Almeida', type('Claudia Almeida'))
# Idade: int
print(41, type(41))
#Altura:Float
print(1.60, type(1.60))
#  É maior de idade
print(41>18, type(41>18))

