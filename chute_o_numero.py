#Objetivo:acertar o Número
import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.numero=0
        self.valor_minimo=1
        self.valor_maximo=100
        self.tentar_novamente=True
    
        
        
    def Iniciar(self):
        #layout
        self.layout=[
            [sg.Text("Seu Chute",size=(35,0))],
            [sg.Input(size=(20,0),key='ValorDoChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(20,20),key='saidaErro')]
        ]
        
        self.layout2=[
            [sg.Text("Você venceu",size=(35,0))]
        ]
       
        self.GerarNumeroAleatorio()
         #Criar uma window
        self.janela=sg.Window("Chute o Número",layout=self.layout)
        
        #receber valores
        self.Pergunta()
        try:
            while self.tentar_novamente==True:
                if self.valor_do_chute > self.numero:
                    print('Você errou !Chute um numero mais baixo ! ')
                    self.Pergunta()
                elif self.valor_do_chute < self.numero:
                    print('Você errou !Chute um numero mais alto !')
                    self.Pergunta()
                else:
                    print('PARABÉNS VOCÊ ACERTOU!')
                    self.tentar_novamente=False
                    self.janela.Close()
                    self.janelaVitoria=sg.Window("voce venceu",layout=self.layout2)
                    self.evento=self.janelaVitoria.Read()
                    
                    
        except:
            print('Favor inserir apenas números!')    
            self.Iniciar()
    def Pergunta(self):
        self.evento,self.valores = self.janela.Read()
        if self.evento=='Chutar':
            self.valor_do_chute=int(self.valores['ValorDoChute'])
    
    def GerarNumeroAleatorio(self):
         self.numero=random.randint(self.valor_minimo,self.valor_maximo)
         return self.numero

    
aceter_o_numero= ChuteONumero()
aceter_o_numero.Iniciar()