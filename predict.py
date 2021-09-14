#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
from preprocess import noise_elimination, img_segmentation, convert2binaryimg
import matplotlib.pyplot as plt
from cnn import CNN


# In[4]:


class Predict(object):
    def __init__(self):
        latest = tf.train.latest_checkpoint('./ckpt')
        self.cnn = CNN()
        self.cnn.model.load_weights(latest).expect_partial()
        self.map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'J': 8, 'K': 9, 'L': 10, 'M': 11, 'N': 12, 'P': 13, 'Q': 14, 'R': 15, 'S': 16, 'T': 17, 'U': 18, 'V': 19, 'W': 20, 'X': 21, 'Y': 22, 'Z': 23, '0': 24, '1': 25, '2': 26, '3': 27, '4': 28, '5': 29, '6': 30, '7': 31, '8': 32, '9': 33}
    
    # mode: test or predict
    def predict(self, img_path, mode="predict"): 
        image = Image.open(img_path)
        image = image.convert('L')
        image = convert2binaryimg(image)
        img_array = np.where(np.array(image), 255, 0)
        noise_elimination(img_array)
        
        subImg_list = img_segmentation(img_array)
        
        res = ""
        for img in subImg_list:
            img = np.pad(img, ((10,10),(10,10)),'constant',constant_values=(255, 255))
            im = Image.fromarray(img.astype(np.uint8))
            im = im.resize((28,28),Image.ANTIALIAS)
            img = np.array(im)
            img = np.reshape(img,(-1,28,28,1))/255.0
            img = 1 - img
            
            y = self.cnn.model.predict(img)
            for k in self.map:
                if self.map[k] == np.argmax(y[0]):
                    res += k
        
        if mode == 'predict':
            plt.imshow(img_array)
            plt.figure()
            print('The predicted result of the given captcha image is: {}'.format(res))
        return res


# In[ ]:




