#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from PIL import Image


# In[2]:


# img as np array
def convert2gray(img):
    if len(img.shape) > 2:
        img = np.mean(img, -1)
    return img


# In[3]:


# Image object
def convert2binaryimg(img, threshold = 200):
    table = [0 for i in range(threshold)] + [1 for i in range(threshold, 256)]
    img = img.point(table, '1')
    return img


# In[4]:


class CharArea(object):
    def __init__(self):
        self.area = set()
        
    
    # point format: (row, col)
    def add_point(self, point):
        self.area.add(point)
        if len(self.area) == 1:
            self.top = point[0]
            self.bottom = point[0]
            self.left = point[1]
            self.right = point[1]
        else:
            self.top = min(self.top, point[0])
            self.bottom = max(self.bottom, point[0])
            self.left = min(self.left, point[1])
            self.right = max(self.right, point[1])
    
    def has_point(self, point):
        return point in self.area
    
    def get_border(self):
        return (self.left, self.right, self.top, self.bottom)
    
    def size(self):
        return len(self.area)
    
    def get_area(self):
        return self.area
        



# img as np array
def noise_elimination(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j]>200:
                continue
            num = 0
            num_white = 0
            if i -1 >= 0:
                if j - 1 >= 0:
                    num += 1
                    if img[i-1][j-1] > 200:
                        num_white += 1
                if j + 1 < len(img[i]):
                    num += 1
                    if img[i-1][j+1] > 200:
                        num_white += 1
                if img[i-1][j] > 200:
                    num_white += 1
                num += 1
            if i + 1 < len(img):
                if j - 1 >= 0:
                    num += 1
                    if img[i+1][j-1] > 200:
                        num_white += 1
                if j + 1 < len(img[i]):
                    num += 1
                    if img[i+1][j+1] > 200:
                        num_white += 1
                if img[i+1][j] > 200:
                    num_white += 1
            if j - 1 >= 0:
                num += 1
                if img[i][j-1] > 200:
                    num_white += 1
            if j + 1 < len(img[i]):
                num += 1
                if img[i][j+1] > 200:
                        num_white += 1
            num += 1
            if num_white * 2 > num:
                img[i][j] = 255
                
    return img


# In[5]:


def comp(e):
    return e.get_border()[0]


# In[6]:


def img_segmentation(img):
    matrix = img.copy()
    matrix = np.where(matrix > 200, False, True)
    
    area_list = []
    for i in range(len(img)):
        for j in range(len(img[0])):
            if matrix[i][j]:
                root = (i, j)
                l = []
                l.append(root)
                matrix[i][j] = False
                area = CharArea()

                while len(l) != 0:
                    point = l.pop()
                    x, y = point[0], point[1]
                    area.add_point((x, y))
                    
                    if x + 1 < len(img) and matrix[x+1][y]:
                        l.append((x+1, y))
                        matrix[x+1][y] = False
                    if y +1 < len(img[0]) and matrix[x][y+1]:
                        l.append((x, y+1))
                        matrix[x][y+1] = False
                    if x - 1 >= 0  and matrix[x-1][y]:
                        l.append((x - 1, y))
                        matrix[x-1][y] = False
                    if y - 1 >= 0 and matrix[x][y-1]:
                        l.append((x, y - 1))
                        matrix[x][y-1] = False
                
                if area.size() > 1:
                    area_list.append(area)
    
    rate = 0.015
    i = 0
    while i < len(area_list):
        if area_list[i].size() < len(img) * len(img[0]) * rate:
            area_list.pop(i)
        else:
            i += 1
                        
    area_list.sort(key=comp)
    
    subImg_list = []
    for a in area_list:
        (left, right, top, bottom) = a.get_border()
        img = np.full((bottom - top +1, right - left + 1), 255)
        area_set = a.get_area()
        
        for x, y in area_set:
            img[x-top, y-left] = 0
        subImg_list.append(img)
    return subImg_list
            

# ---
