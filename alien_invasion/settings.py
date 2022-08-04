import pygame


class Settings(): 
    """Uma classe para armazenar todas as configurações da Invasão Alienígena.""" 
    def __init__(self):
        """Inicializa as configurações do jogo.""" 
        # Configurações da tela 
        self.screen_width = 1350
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        #velocidade da espaçonave
        self.ship_speed_factor = 1.5
        self.ship_limit=3
        # Configurações dos projéteis 
        self.bullet_speed_factor = 3
        self.bullet_width = 3 
        self.bullet_height = 15 
        self.bullet_color = 60, 60, 60
        self.bullets_allowed=3
        self.alien_speed_factor=1
        self.fleet_drop_speed = 10  
        # fleet_direction igual a 1 representa a direita; -1 representa a esquerda 
        self.fleet_direction = 1
        





 

