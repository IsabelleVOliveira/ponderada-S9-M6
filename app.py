from flask import Flask, request, jsonify, render_template
import time
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='keras')

modelo_normal = load_model('models/modelo_mnist.h5')
modelo_linear = load_model('models/linear_modelo_mnist.h5')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload_and_compare', methods=['POST'])
def upload_and_compare():
    file = request.files['file']
    
    img = Image.open(file)
    img = img.resize((28, 28))
    img = img.convert('L')
    img_array = np.array(img) / 255.0  
    img_array_cnn = img_array.reshape(1, 28, 28, 1)
    img_array_linear = img_array.reshape(1, 28 * 28)
    
    # Predição com modelo CNN
    start_time = time.time()
    predict_normal = modelo_normal.predict(img_array_cnn)
    end_time = time.time()
    predict_normal_time = end_time - start_time
    predict_normal = np.argmax(predict_normal, axis=1)[0]
    
    # Predição com modelo Linear
    start_time = time.time()
    predict_linear = modelo_linear.predict(img_array_linear)
    end_time = time.time()
    predict_linear_time = end_time - start_time
    predict_linear = np.argmax(predict_linear, axis=1)[0]

    return jsonify({
        'predict_normal': int(predict_normal),
        'predict_normal_time': predict_normal_time,
        'predict_linear': int(predict_linear),
        'predict_linear_time': predict_linear_time
    })

if __name__ == '__main__':
    app.run(debug=True)
