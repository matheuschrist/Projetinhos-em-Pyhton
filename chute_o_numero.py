#Objetivo:acertar o Número
import random

class ChuteONumero:
    def __init__(self):
        self.numero=0
        self.valor_minimo=1
        self.valor_maximo=100
        self.tentar_novamente=True
    
        
        
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.Pergunta()
        try:
            while self.tentar_novamente==True:
                if self.valor_do_chute > self.numero:
                    print('Você errou ! ')
                    print(' Chute um numero mais baixo !')
                    self.Pergunta()
                elif self.valor_do_chute < self.numero:
                    print('Você errou !')
                    print(' Chute um numero mais alto !')
                    self.Pergunta()
                print('PARABÉNS VOCÊ ACERTOU!')
                self.tentar_novamente=False
        except:
            print('Favor inserir apenas números!')    
            self.Iniciar()
    def Pergunta(self):
         print('Chute um Número de 1 a 100')
         self.valor_do_chute = int(input(''))
    
    def GerarNumeroAleatorio(self):
         self.numero=random.randint(self.valor_minimo,self.valor_maximo)
         return self.numero

    
aceter_o_numero= ChuteONumero()
aceter_o_numero.Iniciar()