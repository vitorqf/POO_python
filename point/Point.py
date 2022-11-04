from math import sqrt, pow

"Observe que ao usar a classe, o docstring fica disponível para o usuário da classe"
class Point:
    "Representa coordenadas geométricas de um ponto no espaço bidimensional"
    "Construto iniciando com x=0 e y=0 por padrāo"
    def __init__(self, x=0, y=0):
        """Inicializa a posição de um novo ponto. x e y podem
           ser especificados. Se eles não forem, as coordenadas
           serão inicializadas na origem."""
        self.x = x
        self.y = y
        
    def move(self, x, y):
        "Move um ponto para uma nova coordenada no espaço 2D." 
        self.x = x
        self.y = y
    
    def reset(self):
        "Reposiciona um ponto na origem geométrica: (0, 0)" 
        self.x = 0
        self.y = 0

    def calculate_distance(self, other_point):
        """Calcula a distância euclidiana entre esse ponto e um segundo
        ponto passado como parâmetro. Depois, a distância é 
        retorna como um float."""
        distance = (sqrt(
            pow((other_point.x - self.x), 2) +
            pow((other_point.y - self.y), 2)
        ))   

        return distance
    
    def __add__(self, other):
        '''soma x e y de dois pontos distintos
        other é um objeto "do tipo Point"
        '''
        return Point((self.x + other.x), (self.y + other.y))

    def __str__(self):
        return "Point: x %d, y %d" % (self.x , self.y)

p1 = Point(1,1)
p2 = Point(2,2)
p3 = Point()
p4 = p1+p2

print("A distancia de p1 e p2 eh ",p1.calculate_distance(p2))
print("A soma de p1 e p2 eh: ",p4)
print("p3 inicializado na origem:",p3)
'''
Os prints devem ser:
A distancia de p1 e p2 eh  1.4142135623730951
A soma de p1 e p2 eh:  Point: x 3, y 3
p3 inicializado na origem: Point: x 0, y 0
'''
p3.move(6,7)
p4.reset()

print("p3 foi movido para os pontos: ",p3)
print("p4 reseteado para os pontos na origem: ",p4)
'''
Os prints devem ser:
p3 foi movido para os pontos:  Point: x 6, y 7
p4 reseteado para os pontos na origem:  Point: x 0, y 0
'''