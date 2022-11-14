from MensagemDiaDosNamorados import MensagemDiaDosNamorados as Namorados
from MensagemAniversario import MensagemAniversario as Aniversario
from MensagemNatal import MensagemNatal as Natal

m1 = Namorados('Fulano', 'Ciclana')
m2 = Natal('John dee', 'Foo bar')
m3 = Aniversario('Augustinho Carrara', 'Lineu')

m4 = Aniversario('Pedro', 'Augusto')
m5 = Aniversario('Cleber', 'Junior')
m6 = Natal('Laura', 'Joana')

m6.printMsgs()