from datetime import date, timedelta

class Data:
    def __init__(self, dia = date.today().day, 
                        mes = date.today().month, 
                        ano = date.today().year):


        if (mes <= 12 and mes > 0):
            self.__mes = mes

        else:
            raise ValueError("--< Mes nao pode ser maior que 12 ou menor que 0 >--")


        if (ano > 0):
            self.__ano = ano
        
        else:
            raise ValueError("--< Ano nao pode ser menor que 0 >--")


        if (dia <= 31 and dia > 0):

            if (dia == 31 and self.__mes % 2 == 0):
                raise ValueError("--< O mes nao possui 31 dias >--")

            if (not self.bissexto()):
                if (self.__mes == 2 and self.__dia == 29):
                    raise ValueError("--< Nesse ano, o mes de Fevereiro nao possui 29 dias >--")

            self.__dia = dia

        
        else:
            raise ValueError("--< Dia nao pode ser maior que 31 ou menor que 0 >--")

    def __str__(self):
        return (f'Data: {self.tipoData().strftime("%d/%m/%Y")}')

    def __add__(self, dado):
        if isinstance(dado, Data):
            tempo = dado.__dia + dado.__ano * 365

            for i in range(0, self.__mes - 1):
                if (self.__mes == 2):
                    if (self.bissexto()):
                        tempo += 29
                    else:
                        tempo += 28

                elif (self.__mes % 2 == 0):
                    tempo += 31

                elif (self.__mes % 2 != 0):
                    tempo += 30

            novaData = (self.tipoData() + timedelta(days=tempo))
            return Data(novaData.day, novaData.month, novaData.year)

        elif isinstance(dado, int):
            novaData = (self.tipoData() + timedelta(days=dado))
            return Data(novaData.day, novaData.month, novaData.year)
        
    def __radd__(self, dado):
        return self.__add__(dado)

    def tipoData(self):
        return date(day=self.__dia, month=self.__mes, year=self.__ano)

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
        if (((self.__dia == 31 or self.__dia + dias == 31) and self.__mes == 12)):
            self.__ano += 1
            self.__dia = 1
            self.__mes = 1

        elif(self.__mes == 2):
            if (self.bissexto() and (self.__dia == 29 or self.__dia + dias == 29)):
                self.__mes += 1
                self.__dia = 1

            elif (not self.bissexto() and (self.__dia == 28 or self.__dia + dias == 28)):
                self.__mes += 1
                self.__dia = 1

            else:
                self.__dia += 1

        elif (((self.__dia == 31 or self.__dia + dias == 31) and self.__mes < 12 and self.__mes % 2 != 0)):
            self.__mes += 1
            self.__dia = 1

        elif (((self.__dia == 30 or self.__dia + dias == 30) and self.__mes < 12 and self.__mes % 2 == 0)):
            self.__mes += 1
            self.__dia = 1

        else:
            self.__dia += 1

    def bissexto(self):
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
            raise ValueError("--< Dia nao pode ser maior que 31 ou menor que 0 >--")

    def get_mes(self):
        return self.__mes
    
    def set_mes(self, mes):
        if (mes <= 12 and mes > 0):
            self.__mes = mes

        else:
            raise ValueError("--< Mes nao pode ser maior que 12 ou menor que 0 >--")

    def get_dia(self):
        return self.__dia
    
    def set_ano(self, ano):
        if (ano > 0):
            self.__ano = ano
        
        else:
            raise ValueError("--< Ano nao pode ser menor que 0 >--")

hoje = Data(30, 4, 2000)
hoje1 = Data(20, 5, 2000)
hoje2 = hoje + 9
print(hoje2)