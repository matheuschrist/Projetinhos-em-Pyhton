


import random
import PySimpleGUI 


class DecidaPorMim():
    def __init__(self):
        self.respostas=[
            'Com certeza,Você deve fazer isso',
            'Você que sabe',
            'Não faz isso não!',
            'Acho que está na hora certa!']
    def Iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.respostas))
        
        
decida =DecidaPorMim()

decida.Iniciar()