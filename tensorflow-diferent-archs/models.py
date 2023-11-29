from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.optimizers import SGD

def define_model(modelNum):
    if modelNum == 0:
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
        model.add(MaxPooling2D((2, 2)))
        model.add(Flatten())
        model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(10, activation='softmax'))
        # compile model
        opt = SGD(learning_rate=0.01, momentum=0.9)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    if modelNum == 1:
        model = Sequential()
        model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
        model.add(MaxPooling2D((2, 2)))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Flatten())
        model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(32, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(10, activation='softmax'))
        # compile model
        opt = SGD(learning_rate=0.01, momentum=0.9)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    if modelNum == 2:
        model = Sequential()
        model.add(Conv2D(32, (4, 4), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Flatten())
        model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(32, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(10, activation='softmax'))
        # compile model
        opt = SGD(learning_rate=0.01, momentum=0.9)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    if modelNum == 3:
        model = Sequential()
        model.add(Conv2D(32, (4, 4), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Flatten())
        model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(32, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(10, activation='softmax'))
        # compile model
        opt = SGD(learning_rate=0.01, momentum=0.9)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    if modelNum == 4:
        model = Sequential()
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Flatten())
        model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(32, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(10, activation='softmax'))
        # compile model
        opt = SGD(learning_rate=0.01, momentum=0.9)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    if modelNum == 5:
        model = Sequential()
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Flatten())
        model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(32, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(10, activation='softmax'))
        # compile model
        opt = SGD(learning_rate=0.01, momentum=0.9)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    if modelNum == 6:
        model = Sequential()
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Flatten())
        model.add(Dense(512, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(32, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(10, activation='softmax'))
        # compile model
        opt = SGD(learning_rate=0.01, momentum=0.9)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    if modelNum == 7:
        model = Sequential()
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Flatten())
        model.add(Dense(1024, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(512, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(32, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(10, activation='softmax'))
        # compile model
        opt = SGD(learning_rate=0.01, momentum=0.9)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    if modelNum == 8:
        model = Sequential()
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(MaxPooling2D((3, 3)))
        model.add(Flatten())
        model.add(Dense(1024, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(512, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(32, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(10, activation='softmax'))
        # compile model
        opt = SGD(learning_rate=0.01, momentum=0.9)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    if modelNum == 9:
        model = Sequential()
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(Conv2D(128, (4, 4), activation='relu', kernel_initializer='he_uniform'))
        model.add(Flatten())
        model.add(Dense(1024, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(512, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(32, activation='relu', kernel_initializer='he_uniform'))
        model.add(Dense(10, activation='softmax'))
        # compile model
        opt = SGD(learning_rate=0.01, momentum=0.9)
        model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    return model
