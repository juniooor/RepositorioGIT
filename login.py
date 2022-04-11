email = str(input('EMAIL: '))
senha = str(input('SENHA: '))
password = int(input('qual sua idade?: '))

if email == 'emailteste@hotmail.com' and senha == '1a2b3c45':
    print('LOGIN EFETUADO COM SUCESSO')
else:
    print('EMAIL OU SENHA INVALIDOS')