
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    #Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasio")
    # Cria o botão Play 
    play_button = Button(ai_settings, screen, "Play")


    # Cria uma instância para armazenar dados estatísticos do jogo 
    stats = GameStats(ai_settings)
    #cria uma espaçonave
    ship=Ship(ai_settings,screen)
    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    # Cria um grupo no qual serão armazenados a frota de aliens
    aliens=Group()
    #Cria a frota de aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    #inicializa o laço principal do jogo
    while True:
        #observa os eventos de reclado e mouse
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        
        
        #verifica se o jogo está ativo
        if stats.game_active:
            ship.update()
            #atualiza a posição dos projéteis 
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
           
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)  


run_game()        
    


