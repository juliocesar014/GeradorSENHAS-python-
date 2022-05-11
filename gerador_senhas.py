import random

print('Bem vindo ao Gerador de senhas!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$% ^ &*()., ?0123456789'

number = input('Quantas senhas gerar?')
number = int(number)

lenght = input('Informe o tamanho da sua senha:')
lenght = int(lenght)

print('\nResultado da senha criada:')

for pwd in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)
