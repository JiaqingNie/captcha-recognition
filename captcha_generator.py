#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import numpy as np
from captcha.image import ImageCaptcha
from PIL import Image
import cv2
import math
import random
from scipy import misc, ndimage
from preprocess import noise_elimination, img_segmentation, convert2gray, convert2binaryimg


# In[3]:


class Captcha(object):
    def __init__(self, captcha_string, captcha_array):
        self.captcha_string = captcha_string
        self.captcha_array = captcha_array
        
        
    def get_captcha_string(self):
        return self.captcha_string
    
    def get_captcha_array(self):
        return self.captcha_array
        
        
        


# In[4]:


class CaptchaGenerator(object):
    def __init__(self, width, height):
        self.img = ImageCaptcha(width=width, height=height)
        self.NUMBERS = [str(i) for i in range(10)]
        self.LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'j', 'm', 'n', 'p', 'q', 'r','s','t', 'u', 'v', 'w', 'x','y','z']
        self.char_list = []
    
    def __generate_random_captcha_string(self, size):
        captcha_string = ''
        for i in range(size):
            captcha_string += np.random.choice(self.char_list)
        return captcha_string
    
    def generate(self, size, charset='numbers', save=False):
        if charset == 'numbers':
            self.char_list = self.NUMBERS
        elif charset == 'letters':
            self.char_list = self.LETTERS
        elif charset == 'mixture':
            self.char_list = self.NUMBERS + self.LETTERS
        else:
            raise Exception('charset can only be numbers, letters or mixture!')
        
        captcha_string = self.__generate_random_captcha_string(size)
        if save:
            if not os.path.exists('./dataset_captcha/{}/{}'.format(size, charset)):
                os.makedirs('./dataset_captcha/{}/{}'.format(size, charset))
            self.img.write(captcha_string, './dataset_captcha/{}/{}/{}.jpg'.format(size, charset, captcha_string))
        
        captcha = self.img.generate(captcha_string)
        captcha_img = Image.open(captcha)
        captcha_array = np.array(captcha_img)
        
        return Captcha(captcha_string, captcha_array)


# In[5]:


def rotate_back(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img, 50, 150, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 0)
    rotate_angle = 0
    for rho, theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        if x1 == x2 or y1 == y2:
            continue
        t = float(y2 - y1) / (x2 - x1)
        rotate_angle = math.degrees(math.atan(t))
        if rotate_angle > 45:
            rotate_angle = -90 + rotate_angle
        elif rotate_angle < -45:
            rotate_angle = 90 + rotate_angle
    img = ndimage.rotate(img, rotate_angle)
    image = Image.fromarray(img.astype(np.uint8))
    image.save(path)
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




