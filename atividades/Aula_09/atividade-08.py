senhaCorreta = 1234
contador = 0

senha = int(input("Insira a senha numerica para efetuar o login: "))

if(senha != 1234):
    while (senha != 1234):
        contador+=1
        print("SENHA INCORRETA!")
        senha = int(input("Insira a senha novamente:"))

print("SENHA CORRETA!")
print("Login efetuado com sucesso")
print("Tentativas necessárias: ", contador)