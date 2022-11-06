from datetime import date, timedelta

class Data:
    "Método para criação de um objeto Data"

    """
        Em caso de não ser inserido dados da data, é utilizado o dado referente a data atual. Caso sejam informados, é criado um objeto com os dados do usuário         
    """
    def __init__(self, dia = date.today().day, 
                        mes = date.today().month, 
                        ano = date.today().year):


        """
            >> Validação de data

            Se o mes for menor que 12 e maior que 0, então, é válido
                Se não, o mes não é válido

            Se o ano for maior que 0, então é valido, caso contrário, não.

            Se o dia for menor ou igual a 31 e maior que 0,
                Verifique se ele faz parte de um mês par(30 dias) ou impar(31 dias), se caso for dia 31 e o mês for par, então a data é inválida

                Verifique se o ano é bissexto, se não for e o mês for fevereiro e dia 29, então a data é inválida        
        """
        if (mes <= 12 and mes > 0):
            self.__mes = mes

        else:
            raise ValueError("Mes nao pode ser maior que 12 ou menor que 0 >--")


        if (ano > 0):
            self.__ano = ano
        
        else:
            raise ValueError("Ano nao pode ser menor que 0 >--")


        if (dia <= 31 and dia > 0):

            if (dia == 31 and self.__mes % 2 == 0):
                raise ValueError("O mes nao possui 31 dias >--")

            if (not self.bissexto()):
                if (self.__mes == 2 and self.__dia == 29):
                    raise ValueError("Nesse ano, o mes de Fevereiro nao possui 29 dias >--")

            self.__dia = dia

        
        else:
            raise ValueError("Dia nao pode ser maior que 31 ou menor que 0 >--")

    "Método retorna uma string da data informada pelo usuário"
    def __str__(self):
        return (f'Data: {self.tipoData().strftime("%d/%m/%Y")}')

    "Método retorna ou uma nova data pela soma de duas datas ou uma nova data pela soma de dias"
    def __add__(self, dado):
        """
            Se caso o dado informado for do tipo Data()
                então, primeiramente, some a quantidade de dias com 365 * quantidade de anos para obter um total de dias

                e para complementar, para cada mês de diferença entre as datas - 1, verifique se ele é par ou impar
                    se for impar, o total de dias é acrescido de 31 dias

                    se for par, o total de dias é acrescido de 30 dias        

                por fim, é criado um objeto do tipo Date com a soma da primeira data + a quantidade de dias até a próxima e é retornado para o usuário um objeto do tipo Data

            
            Já se o dado for uma instância do tipo inteiro
                então, apenas é somado a primeira data com o dado e retornado um objeto do tipo Data conforme a soma
        """
        if isinstance(dado, Data):
            tempo = dado.__dia + dado.__ano * 365

            for i in range(0, self.__mes - 1):
                if (i == 2):
                    if (self.bissexto()):
                        tempo += 29
                    else:
                        tempo += 28

                elif (i % 2 == 0):
                    tempo += 31

                elif (i % 2 != 0):
                    tempo += 30

            novaData = (self.tipoData() + timedelta(days=tempo))
            return Data(novaData.day, novaData.month, novaData.year)

        elif isinstance(dado, int):
            novaData = (self.tipoData() + timedelta(days=dado))
            return Data(novaData.day, novaData.month, novaData.year)

    "Caso o usuário use, por exemplo, 10 + data1, o programa poderia quebrar, então, é adicionado o método __radd__ que chama o __add__ passando o dado à esquerda"  
    def __radd__(self, dado):
        return self.__add__(dado)

    "O método retorna um objeto do tipo Date"
    def tipoData(self):
        return date(day=self.__dia, month=self.__mes, year=self.__ano)

    "O método faz com que a data atual avance 1 dia"
    def avanca(self):
        """
            Se for dia 31/12/YYYY, então,
                aumente o ano e vá para 01/janeiro;

            Se não, se o mes for fevereiro, 
                for um ano bissexto e for dia 29, 
                    va para o 01/proximo_mes, 

                se não for um ano bissexto mas for dia 28, 
                    va para o 01/proximo_mes, 
                
                se não for dia 29 de um ano bissexto nem dia 28 de um ano não bissexto, 
                    avance um dia
            
            Se não, se o dia for 31 e o mes for impar, 
                avance para o dia 01 do proximo mes

            se não, se o dia for 30 e o mes for par, 
                avance para o dia 01 do proximo mes

            se não for nada anterior,
                avance um dia
        """
        if ((self.__dia == 30 and self.__mes == 12)):
            self.__ano += 1
            self.__dia = 1
            self.__mes = 1

        elif(self.__mes == 2):
            if (self.bissexto() and self.__dia == 29):
                self.__mes += 1
                self.__dia = 1

            elif (not self.bissexto() and self.__dia == 28):
                self.__mes += 1
                self.__dia = 1

            else:
                self.__dia += 1

        elif ((self.__dia == 31 and self.__mes < 12 and self.__mes % 2 != 0)):
            self.__mes += 1
            self.__dia = 1

        elif ((self.__dia == 30 and self.__mes < 12 and self.__mes % 2 == 0)):
            self.__mes += 1
            self.__dia = 1

        else:
            self.__dia += 1

    "O método verifica se o ano é bissexto"
    def bissexto(self):
        """
            Caso o ano seja divisível por 4,
                verifique se é também divisível por 100,
                    caso seja divisível por 100, verifique se é também divisível por 400

                        caso seja divisível por 4, por 100 e por 400, então é um ano bissexto

                    caso seja divisível por 4 e por 100, mas não seja divisível por 400, então, não é um ano bissexto
                caso seja divisível por 4 mas não seja por 100, então, é um ano bissexto
            caso não seja divisível por 4, não é um ano bissexto  
        """
        if (self.__ano % 4 == 0):
            if (self.__ano % 100 == 0):
                if (self.__ano % 400 == 0):
                    return True

                else:
                    return False

            else:
                return True

        else:
            return False

    def get_dia(self):
        return self.__dia
    
    def set_dia(self, dia):
        if (dia <= 31 and dia > 0):
            self.__dia = dia  

        else:
            raise ValueError("Dia nao pode ser maior que 31 ou menor que 0 >--")

    def get_mes(self):
        return self.__mes
    
    def set_mes(self, mes):
        if (mes <= 12 and mes > 0):
            self.__mes = mes

        else:
            raise ValueError("Mes nao pode ser maior que 12 ou menor que 0 >--")

    def get_dia(self):
        return self.__dia
    
    def set_ano(self, ano):
        if (ano > 0):
            self.__ano = ano
        
        else:
            raise ValueError("Ano nao pode ser menor que 0 >--")
