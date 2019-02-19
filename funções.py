# from datetime import datetime, timedelta

# pessoa = {
#     'ano' : '',
#     'mes' : '',
#     'dia' : '',
# }

# for chave in pessoa:
#     pessoa [chave] = int(input('digite o ' +chave))
# print(pessoa)


# data_nascimento= timedelta(days=pessoa['dia'])
# data_hoje= datetime.now()
# delta_data_hoje = timedelta(days=data_hoje.day)

# diferenca_de_dias= data_nascimento - delta_data_hoje
# print(diferenca_de_dias)


# def soma(a,b):
#     soma= a+b
#     return soma

# banana=soma(2, 10)
# print(banana)

def numero(x):
    if (x % 2 == 0):
        print('verdadeiro')
    else:
         print('falso')
parametro= int(input('Esse parâmetro é par?'))
numero(x=parametro)
