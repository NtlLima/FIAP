''' numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
    '''


'''idade = int(input("Digite a sua idade: "))
if idade in range(0, 10):
    print("É criança.")
elif  idade in range(13,18):
     print("É adolescente.")
elif idade >= 18: 
    print("É adulto")'''

import re

# Função para verificar a senha
def verificar_senha(senha):
    # Verifica se a senha contém pelo menos um caractere especial, um número e uma letra maiúscula
    if re.match(r'^(?=.*[!@#$%^&*()_+{}|:"<>?])[A-Za-z0-9!@#$%^&*()_+{}|:"<>?]{8,}$', senha):
        return True
    else:
        return False

# Solicita a senha ao usuário
senha = input("Digite sua senha: ")

# Verifica a senha
if verificar_senha(senha):
    print("Senha registrada")
else:
    print("Senha inválida. A senha deve conter pelo menos 8 caracteres, incluindo pelo menos um caractere especial, um número e uma letra maiúscula.")