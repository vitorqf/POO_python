from blog import Blog
from postagem import Postagem
from usuario import Usuario

import datetime
from uuid import uuid4


usuario = Usuario(uuid4().int, "Administrador", "admin", "admin")

print('Para continuar entre na sua conta\n')

login = input('Login: ')
password = input('Senha: ')

if login != usuario.login:
    print('\n* Usuario invalido')
    exit()

if password != usuario.senha:
    print('\n* Senha invalida')
    exit()

print(f'Ola, {usuario.nome}. Seja bem-vindo(a)!')

postagem1 = Postagem(uuid4().int, 'Embranquecimento de Corais', 'A exploracao nao regrada dos corais...', datetime.datetime.now())
postagem2 = Postagem(uuid4().int, 'Impacto das Fake News', 'As fake news impactam na sociedade...', datetime.datetime(2023, 3, 3))
postagem3 = Postagem(uuid4().int, 'Lorem ipsum dolor', 'Lorem ipsum dolor sit amet...', datetime.datetime(2023, 3, 10))

blog1 = Blog()

blog1.adicionarPostagem(postagem1)
blog1.adicionarPostagem(postagem2)
blog1.adicionarPostagem(postagem3)

blog1.publicarPostagem(postagem2)

publicadas = blog1.listarPostagensPublicadas()
postagens = blog1.listarTodasAsPostagens()

if postagens:
    print('\n-- Todas as postagens --')
    for postagem in postagens:
        print(postagem)

else:
    print('Nenhuma postagem encontrada')

if publicadas:
    print('\n-- Todas as postagens publicadas --')
    for publicada in publicadas:
        print(publicada)

else:
    print('Nenhuma postagem publicada')

blog1.apagarPostagem(postagem1)

publicadas = blog1.listarPostagensPublicadas()

print('\n** Lista de publicadas após apagar uma postagem que foi anteriormente publicada: ')

if publicadas:
    print('\n-- Todas as postagens publicadas --')
    for publicada in publicadas:
        print(publicada)

else:
    print('Nenhuma postagem publicada')