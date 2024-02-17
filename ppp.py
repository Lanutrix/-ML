import pandas as pd
import numpy as np


file = pd.read_csv('apple_quality.csv')

# file.columns
# file.Acidity
# file.Quality

x_train = np.transpose(np.array([    np.array(file.Size,dtype= np.float32)[:3200],
                        np.array(file.Weight,dtype= np.float32)[:3200],
                        np.array(file.Sweetness,dtype= np.float32)[:3200],
                        np.array(file.Crunchiness,dtype= np.float32)[:3200],
                        np.array(file.Juiciness,dtype= np.float32)[:3200],
                        np.array(file.Ripeness,dtype=np.float32)[:3200],
                        np.array(file.Acidity,dtype= np.float32)[:3200]], dtype="object"))

y_train = np.array(file.Quality,dtype= "object")[:3200]
y_train = np.where(y_train == 'bad', 0, np.where(y_train == 'good', 1, y_train)).astype(np.float32)


x_test = np.transpose(np.array([     np.array(file.Size,dtype= np.float32)[3200:],
                        np.array(file.Weight,dtype= np.float32)[3200:],
                        np.array(file.Sweetness,dtype= np.float32)[3200:],
                        np.array(file.Crunchiness,dtype= np.float32)[3200:],
                        np.array(file.Juiciness,dtype= np.float32)[3200:],
                        np.array(file.Ripeness,dtype= np.float32)[3200:],
                        np.array(file.Acidity,dtype= np.float32)[3200:]], dtype="object"))

y_test = np.array(file.Quality,dtype= "object")[3200:]
y_test = np.where(y_test == 'bad', 0.0, np.where(y_test == 'good', 1.0, y_test)).astype(np.float32)

from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l1, l2
from keras.layers import Dropout
from keras.layers import BatchNormalization


model = Sequential()
model.add(Dense(128, input_shape=(7,), activation='relu'))

model.add(Dense(64, activation='relu',kernel_regularizer=l2(0.01)))

model.add(Dense(1, activation='sigmoid',kernel_regularizer=l2(0.01)))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

from keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(monitor = "val_loss", patience=3, restore_best_weights=True)
hist = model.fit(x_train, y_train, epochs=10, batch_size=4, validation_split=0.2, callbacks=[early_stopping])