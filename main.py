from keras.datasets import mnist # type: ignore
from keras.utils import to_categorical # type: ignore
from keras.models import Sequential # type: ignore
#Camadas que serão utilizadas
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout # type: ignore
from keras.optimizers import Adam # type: ignore
# Carrega o modelo
from tensorflow.keras.models import load_model # type: ignore
import cv2


print('Carregando o dataset')
# Carregando o dataset separando os dados de treino e de teste 
(x_treino, y_treino), (x_teste, y_teste) = mnist.load_data()

# Trazendo a função `to_categorical` para transformar os labels em one-hot encoding
y_treino_cat = to_categorical(y_treino)
y_teste_cat = to_categorical(y_teste)

# Verificação da saída one-hot encoding
print(y_treino[0]) #Valor da classe
print(y_treino_cat[0]) #Representação onehot

# Normalização dos dados de entrada
x_treino_norm = x_treino/x_treino.max()
x_teste_norm = x_teste/x_teste.max()

# Reshape dos dados de entrada para adicionar o canal de cor
x_treino = x_treino.reshape(len(x_treino), 28, 28, 1)
x_treino_norm = x_treino_norm.reshape(len(x_treino_norm), 28, 28, 1)
x_teste = x_teste.reshape(len(x_teste), 28, 28, 1)
x_teste_norm = x_teste_norm.reshape(len(x_teste_norm), 28, 28, 1)


#Modelo da rede
# Criação do modelo LeNet5
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(5,5), padding='same', activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPool2D(strides=2))
model.add(Conv2D(filters=48, kernel_size=(5,5), padding='valid', activation='relu'))
model.add(MaxPool2D(strides=2))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(84, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Constroi o modelo
model.build()
# Exibe um resumo do modelo
model.summary()

print("Modelo finalizado")

#Compila o modelo
adam = Adam()
model.compile(loss='categorical_crossentropy',
              metrics=['accuracy'], optimizer=adam)

# Realiza o treinamento do modelo
historico = model.fit(x_treino_norm, y_treino_cat, epochs=5, validation_split=0.2)

model.save('modelo_mnist.h5')


