import cv2 as cv2
import numpy as np
import os



def ImgToCartoon(caminho):    
    path=r'C:\\uploads\\'+caminho
    #carregar imagem
    img = cv2.imread(path)
    #passa os parametros para a lib
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)
    edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,9)
    #CARTONIZA A IMAGEM
    color=cv2.bilateralFilter(img,9,250,250)
    cartoon=cv2.bitwise_and(color,color,mask=edges)
    #especificando o Diretório
    directory='C:\\Users\\mathe\\OneDrive\\Documentos\\Python\\imgToCartoon\\images\\'
    os.chdir(directory)
    #Salvando o arquivo 
    cv2.imwrite(caminho,cartoon)
    #img_pronta=directory+caminho
    return caminho


