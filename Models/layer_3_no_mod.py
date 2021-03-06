from tensorflow.keras import models, layers

def create_model():

    inp = layers.Input(shape=(256, 256, 1))

    conv2 = layers.Conv2D(32, 3, activation='relu', padding='same')(inp)
    conv2 = layers.Conv2D(32, 3, activation='relu', padding='same')(conv2)
    pool2 = layers.MaxPool2D(2)(conv2)
        
    conv3 = layers.Conv2D(64, 3, activation='relu', padding='same')(pool2)
    conv3 = layers.Conv2D(64, 3, activation='relu', padding='same')(conv3)
    pool3 = layers.MaxPool2D(2)(conv3)

    conv8 = layers.Conv2D(128, 3, activation='relu', padding='same')(pool3)
    conv8 = layers.Conv2D(128, 3, activation='relu', padding='same')(conv8)
    pool4 = layers.MaxPool2D(2)(conv8)

    conv4_ = layers.Conv2D(256, 3, activation='relu', padding='same')(pool4)
    conv4 = layers.Conv2D(256, 3, activation='relu', padding='same')(conv4_)

    dconv4 = layers.Conv2DTranspose(128, 3, strides=2, activation='relu', padding='same')(conv4)
    conc4 = layers.concatenate([dconv4, conv8])
    conv9 = layers.Conv2D(128, 3, activation='relu', padding='same')(conc4)
    conv9 = layers.Conv2D(128, 3, activation='relu', padding='same')(conv9)

    dconv3 = layers.Conv2DTranspose(64, 3, strides=2, activation='relu', padding='same')(conv9)
    conc3 = layers.concatenate([dconv3, conv3])
    conv5 = layers.Conv2D(64, 3, activation='relu', padding='same')(conc3)
    conv5 = layers.Conv2D(64, 3, activation='relu', padding='same')(conv5)

    dconv2 = layers.Conv2DTranspose(32, 3, strides=2, activation='relu', padding='same')(conv5)
    conc2 = layers.concatenate([dconv2, conv2])
    conv6 = layers.Conv2D(32, 3, activation='relu', padding='same')(conc2)
    conv6 = layers.Conv2D(32, 3, activation='relu', padding='same')(conv6)

    outp1 = layers.Conv2D(8, 1, name='output1', activation='sigmoid', padding='same')(conv6)

    model = models.Model(inputs=inp, outputs=outp1)
    
    return model
