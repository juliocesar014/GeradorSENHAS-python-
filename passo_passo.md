# Passo a passo como foi criado esse Gerador de senhas!!

## Importamos o RANDOM, para que seja realizado de forma aleatoria:

### import random

## Criada mensagem de bem vindo->

### print('Bem vindo ao Gerador de senhas!')

## Determinamos os caracteres que serão usados para compor a senha->

### chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$% ^ &*()., ?0123456789'

## Determinamos quantas senhas gerar, atráves de um número inteiro escolhido->

### number = input('Quantas senhas gerar?')
### number = int(number)

## Definimos o tamanho de caracteres que nossa será terá ->

### lenght = input('Informe o tamanho da sua senha:')
### lenght = int(lenght)

### print('\nResultado da senha criada:')

### for pwd in range(number):
    # passwords = ''
    # for c in range(lenght):
        # passwords += random.choice(chars)
    # print(passwords)

## Senha gerada com sucesso!!