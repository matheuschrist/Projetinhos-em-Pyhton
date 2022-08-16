from random import choice 


class RandomWalk(): 
    """Uma classe para gerar passeios aleatórios.""" 
    def __init__(self, num_points=5000): 
        """Inicializa os atributos de um passeio.""" 
        self.num_points = num_points 
        # Todos os passeios começam em (0, 0) 
        self.x_values = [0] 
        self.y_values = [0]


    def fill_walk(self): 
        """Calcula todos os pontos do passeio.""" 
        # Continua dando passos até que o passeio alcance o tamanho desejado 
        while len(self.x_values) < self.num_points:
        # Rejeita movimentos que não vão a lugar nenhum
            if self.get_step_x() == 0 and self.get_step_y() == 0: 
                continue # Calcula os próximos valores de x e de y 
            next_x = self.x_values[-1] + self.get_step_x()
            next_y = self.y_values[-1] + self.get_step_y()
            self.x_values.append(next_x) 
            self.y_values.append(next_y)
            
    def get_step_x(self):
         # Decide direção a ser seguida e distância a ser percorrida nessa direção 
        x_direction = choice([1, -1]) 
        x_distance = choice([0, 1, 2, 3, 4]) 
        x_step = x_direction * x_distance 
        
        return x_step
    
    def get_step_y(self):
         # Decide direção a ser seguida e distância a ser percorrida nessa direção
        y_direction = choice([1, -1]) 
        y_distance = choice([0, 1, 2, 3, 4]) 
        y_step = y_direction * y_distance
        
        return y_step
            




