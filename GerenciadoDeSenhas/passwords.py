import sqlite3


MASTER_PASSWORD='12345678'

senha= input("Insira sua senha Master:")
if senha != MASTER_PASSWORD:
    print("Senha Inválida  Ecerrando...")
    exit()
    
conn =sqlite3.connect('passwords.db')


cursor=conn.cursor()

cursor.execute('''
           CREATE TABLE IF NOT EXISTS  users(
           service TEXT NOT NULL,
           username TEXT NOT NULL,
           password    
           
           )  ;
               ''')



def menu():
    print("***********************")
    print("*I :inserir nova senha")
    print("*L :Listar serviçoes Salvos")
    print("*R :Recuperar senha")
    print("*S :sair")
    print("***********************")
    
    
while True:
    menu()
    op = input("O que deseja Fazer? ")
    if op not in ['L','I','R','S']:
        print("Opção inválida")
        continue
    if op=='S':
        break
    
    
conn.close()