from data import Data
# Testes

"Criação de um objeto data com dados válidos fornecidos pelo usuário"
data = Data(30, 12, 2022)

"Utilização do método __str__"
print(f"\n<< Utilizacao do metodo __str__ >>\n{data}")


"Ao tentar gerar uma data inválida, a classe retorna uma exception de valor e não é criado o objeto"
try:
    data1 = Data(-1, 12, 2022) 

except ValueError as e:
    print(f"\n<< Utilizacao do raise exception >>\nERRO: {str(e)}")

"Criação de um objeto data sem os dados"
data2 = Data()
print(f"\n<< Criacao de data sem dados >>\n{data2}")

"Utilização do método avancar"
data.avanca()
print(f"\n<< Utilizacao do metodo avancar >>\n{data}")

"Utilização do método bissexto"
print(f"\n<< Utilizacao do metodo avancar >>Retorna True ou False dependendo se o ano é ou não bissexto: {data.bissexto()}")

"Utilização do método __add__"

"Primeiro caso: soma de duas datas"
d1 = Data()
d2 = Data()
d3 = d1 + d2

print(f"\n<< Primeiro caso: soma de duas datas >>\n{d3}")

"Segundo caso: soma de uma data e um inteiro"
d4 = d1 + 715

"A ordem dos fatores não afetará na execução"
d4 = 1 + d4

print(f"\n<< Segundo caso: soma de uma data e um inteiro >>\n{d4}")


# Fim-Testes