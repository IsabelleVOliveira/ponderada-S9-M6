import cv2
import numpy as np
# Carrega o modelo
from tensorflow.keras.models import load_model

modelo_2 = load_model('modelo_mnist.h5')

def predict():
    # Usa o modelo para realizar uma predição
    img = cv2.imread('./images/7.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # predicao = modelo_2.predict(img.reshape(1, 28, 28, 1))
    img = cv2.resize(img, (28,28))
    img = img / img.max()

    img = img.reshape(1,28,28,1)
    predicao = modelo_2.predict(img)
    print(predicao)
    # Exibe a classe com a maior probabilidade de ser a correta da predição
    print(np.argmax(predicao))
