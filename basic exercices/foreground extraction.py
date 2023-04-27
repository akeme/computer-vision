#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[6]:


#img = cv2.imread('data/opencv-python-foreground-extraction-tutorial.jpg')
img = cv2.imread('data/menina.jpeg')
plt.imshow(img)


# In[7]:


mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

#rect = (161,79,150,150) #rectangle with the foreground image #change the image change the rectangle
rect = (0,0,750,1200)


# In[ ]:


cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()


# In[ ]:




