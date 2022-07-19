import os
from flask import Flask, request, jsonify, send_from_directory,render_template
from imgToCartoon import ImgToCartoon

DIRETORIO = "C:\\uploads\\"

api = Flask(__name__)

@api.route("/")
def index():
    return render_template('index.html')
    
    
@api.route("/arquivos", methods=["POST"])
def post_arquivo():
    #Recebe o arquivo via form
    arquivo = request.files.get("meuArquivo")
    nome_do_arquivo = arquivo.filename
    arquivo.save(os.path.join(DIRETORIO, nome_do_arquivo))
    #recebe o caminho do arquiv original 
    caminho=str(nome_do_arquivo)
    #recebe o caminho da imagem
    imgCartoon=ImgToCartoon(caminho)
    

    return  render_template('cartoon.html',ImgCartoon=imgCartoon)


    

if __name__ == "__main__":
    api.run(debug=True, port=8000)