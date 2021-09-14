#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras import datasets, layers, models


# In[2]:


class CNN(object):
    def __init__(self):
        model = models.Sequential()
        
        model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28,28,1)))
        model.add(layers.MaxPooling2D((2,2)))
        
        model.add(layers.Conv2D(64,(3,3), activation='relu'))
        model.add(layers.MaxPooling2D((2,2)))
        
        model.add(layers.Conv2D(64,(3,3), activation='relu'))
        
        model.add(layers.Flatten())
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(34, activation='softmax'))

        model.summary()

        self.model = model


# In[ ]:




