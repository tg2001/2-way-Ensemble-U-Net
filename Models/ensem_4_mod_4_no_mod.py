from tensorflow.keras import models, layers
from Models.layer_4_mod import *
from Models.layer_4_no_mod import *

def ensem_4_4():

  # 4 layer mod
  model1 = mod_4(1)

  # 4 layer no mod
  model2 = no_mod_4(1)

  # 4 mod 4 no mod ensemble

  inp = layers.Input(shape=(256, 256, 1))

  out1 = model1(inp)
  out2 = model2(inp)

  conc1 = layers.concatenate([out2, out1])

  conv2 = layers.Conv2D(16, 3, activation='relu', padding='same')(conc1)
  outp1 = layers.Conv2D(8, 1, name='output1', activation='sigmoid', padding='same')(conv2)

  model = models.Model(inputs=inp, outputs=outp1)

  return model
