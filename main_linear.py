from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten
from keras.optimizers import Adam
import time

def treinar_modelo_linear():
    (x_treino, y_treino), (x_teste, y_teste) = mnist.load_data()
    y_treino_cat = to_categorical(y_treino)
    y_teste_cat = to_categorical(y_teste)

    x_treino_norm = x_treino / 255.0
    x_teste_norm = x_teste / 255.0

    x_treino_norm = x_treino_norm.reshape(len(x_treino_norm), 28 * 28)
    x_teste_norm = x_teste_norm.reshape(len(x_teste_norm), 28 * 28)

    model = Sequential([
        Dense(128, activation='relu', input_shape=(28 * 28,)),
        Dense(10, activation='softmax')
    ])

    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer=Adam())
    inicio = time.time()
    model.fit(x_treino_norm, y_treino_cat, epochs=5, validation_split=0.2)
    fim = time.time()
    model.save('models/linear_modelo_mnist.h5')
    tempo_treinamento = fim - inicio
    loss, accuracy = model.evaluate(x_teste_norm, y_teste_cat)
    return tempo_treinamento, loss, accuracy

if __name__ == "__main__":
    
    tempo_linear, loss_linear, acc_linear = treinar_modelo_linear()
    print(f"Modelo Linear - Tempo de Treinamento: {tempo_linear:.4f}s, Loss: {loss_linear:.4f}, Acurácia: {acc_linear:.4f}")
