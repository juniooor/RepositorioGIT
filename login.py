email = str(input('EMAIL: '))
senha = str(input('SENHA: '))
invalid = str(input("Esqueceu a senha?: [S/N]"))

if email == 'emailteste@hotmail.com' and senha == '1a2b3c45':
    print('LOGIN EFETUADO COM SUCESSO')
else:
    print('EMAIL OU SENHA INVALIDOS')
    