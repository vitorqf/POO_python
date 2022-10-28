class Veiculo:
    __velocidade = 0

    def __init__(self, modelo, ano, potencia, peso, consumo, tanqueMax, tanqueAtual, velocidadeMax):
        self.__modelo = modelo
        self.__ano = ano
        self.__potencia = potencia
        self.__peso = peso
        self.__consumo = consumo
        self.__tanqueMax = tanqueMax
        self.__tanqueAtual = tanqueAtual
        self.__velocidadeMax = velocidadeMax

    def acelerar(self, tempo):
        gasto = (self.__velocidade/tempo)/self.__consumo

        if (gasto < self.__tanqueAtual):

            for segundo in range(tempo):

                #DISCLAIMER: A formula nao tem qualquer representacao realista (que eu tenha encontrado kkkk), apenas peguei a proporcao de potencia por peso e multipliquei por 100, porque dessa maneira, ao considerar o 0 a 100 de um veiculo qualquer, o tempo necessario chegou a ser proximo
                if (self.__velocidade + (self.__potencia/self.__peso) * 100 < self.__velocidadeMax):
                    self.__velocidade += (self.__potencia/self.__peso) * 100

                else:
                    self.__velocidade = self.__velocidadeMax

                self.queimarCombustivel(gasto)

        else:
                self.__velocidade = 0
                print("\n*** Veiculo sem combustivel!")

        return self.get_velocidade()

    def frear(self, tempo):
        for segundo in range(tempo):
            # mesma coisa da primeira formula, so muda que considerei potencia * 3, pois o sistema de frenagem tem mais ou menos isso a mais de potencia
            if ((self.__velocidade - (self.__potencia * 3 * segundo)/self.__peso * 100) >= 0):
                self.__velocidade -= (self.__potencia * 3 * segundo)/self.__peso * 100

            else:
                self.__velocidade = 0

        return int(self.__velocidade)

    def abastecer(self, litragem):
        if(self.__tanqueAtual + litragem <= self.__tanqueMax):
            self.__tanqueAtual += litragem
            return True
        
        else:
            return False

    def queimarCombustivel(self, consumo):
        self.__tanqueAtual -= consumo
        return self.__tanqueAtual

    def set_ano(self, novo):
        self.__ano = novo

    def set_potencia(self, novo):
        self.__potencia = novo

    def set_tanqueMax(self, novo):
        self.__tanqueMax = novo

    def set_tanqueAtual(self, novo):
        self.__tanqueAtual = novo

    def set_modelo(self, novo):
        self.__modelo = novo

    def set_peso(self, novo):
        self.__peso = novo

    def set_velocidadeMax(self, novo):
        self.__velocidadeMax = novo

    def set_consumo(self, novo):
        self.__consumo = novo

    def get_ano(self):
        return self.__ano

    def get_peso(self):
        return self.__peso

    def get_modelo(self):
        return self.__modelo
    
    def get_potencia(self):
        return self.__potencia

    def get_velocidadeMax(self):
        return self.__velocidadeMax

    def get_tanqueMax(self):
        return self.__tanqueMax
    
    def get_tanqueAtual(self):
        return self.__tanqueAtual

    def get_consumo(self):
        return self.__consumo
    
    def get_velocidade(self):
        return int(self.__velocidade)