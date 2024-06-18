import os 
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from implementModel import predict  # Supondo que implementModel contém a função predict

app = Flask(__name__)
img_folder = os.path.join(os.getcwd(), 'images')  

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict_image():
    try:
        file = request.files['imagem']
        savePath = os.path.join(img_folder, secure_filename(file.filename))
        file.save(savePath)

        # Passa o caminho da imagem para a função predict
        result = predict(savePath)  # Passa o caminho correto aqui

        return render_template('predict.html', resultado=result)
    except Exception as e:
        return render_template('predict.html', resultado=f"Erro ao processar imagem: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)