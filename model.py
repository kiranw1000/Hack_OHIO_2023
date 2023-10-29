import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import statistics as stats
import matplotlib as mp
img_height = 480
img_width = 640

model = tf.keras.models.load_model(f"model")

def make_ds(dir,labels, val, batch_size):
    ret = tf.keras.utils.image_dataset_from_directory(
  dir,
  # labels=list([classify(x) for x in labels]),
  labels=list(labels),
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)
    return ret

def predict(images):
    return model.predict(images)

def show_image(images,image):
    plt.imshow(images[image])
