import matplotlib.pyplot as plt 
from random_walk import RandomWalk 


while True:
    # Cria um passeio aleatório e plota os pontos 
    rw = RandomWalk(500000) 
    rw.fill_walk() 
    # Define o tamanho da janela de plotagem 
    plt.figure(figsize=(10, 6))
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none', s=1)
    # Enfatiza o primeiro e o último ponto 
    plt.scatter(0, 0, c='green', edgecolors='none', s=50) 
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
    # Remove os eixos 
    #FALTA FAZER
    plt.show()
    keep_running = input("Make another walk? (y/n): ") 
    if keep_running == 'n':
        break

