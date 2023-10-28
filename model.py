import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import statistics as stats
import matplotlib as mp

model = tf.keras.models.load_model(f"model")

def predict(images):
    return model.predict(images)

def show_image(images,image):
    plt.imshow(images[image])