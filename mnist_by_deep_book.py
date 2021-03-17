import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import utils, layers, models
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

print(tf.__version__)

EPOCHS = 50
BATCH_SIZE = 128
VERBOSE = 1
NB_CLASSES = 10  # output의 demension
N_HIDDEN = 128
VALIDATION_SPLIT = 0.2  # 검증
DROPOUT = 0.3

# MNIST 데이터셋 로드
# 검증

mnist = keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
RESHAPED = 784

x_train = x_train.reshape(60000, RESHAPED)
x_test = x_test.reshape(10000, RESHAPED)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

print(x_train.shape)
plt.imshow(x_train[5].reshape(28, 28))

# 입력을 [0, 1] 사이로 정규화
# 파이썬의 타입
# int, float
# int = 0, 1, 2, 3
# float = 0.0, 1.0, 2.0, 3.0
x_train = x_train / 255.
x_test = x_test / 255.
# 0 => 0.0
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# 레이블을 원핫 인코딩
y_train = keras.utils.to_categorical(y_train, NB_CLASSES)
y_test = keras.utils.to_categorical(y_test, NB_CLASSES)

# 모델 구축
model = models.Sequential()

model.add(layers.Dense(N_HIDDEN, input_shape=(RESHAPED,),
                       name='dense_layer', activation='relu'))
model.add(layers.Dropout(DROPOUT))
model.add(layers.Dense(N_HIDDEN,
                       name='dense_layer_2', activation='relu'))
model.add(layers.Dropout(DROPOUT))
model.add(layers.Dense(NB_CLASSES,
                       name='dense_layer_3',
                       activation='softmax'))
plt.imshow(x_train[0].reshape(28, 28))
plt.show()

# 모델 컴파일
model.compile(optimizer="SGD",
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train,
          y_train,
          batch_size=BATCH_SIZE,
          epochs=EPOCHS,
          verbose=VERBOSE,
          validation_split=VALIDATION_SPLIT)
# 모델 평가
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

model.summary()
