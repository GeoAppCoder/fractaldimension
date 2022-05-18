#-------------------------------------------------------------------------------
# Name:        Fractal final
# Purpose:     Estimate the fractal dimension of a curve in an jpg image
#
# Author:      GIS-group
#
# Created:     16/04/2022
# Copyright:   (c) GIS-group 2022
# Licence:     <open for use after reference>
#-------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import PIL
from scipy import stats
from PIL import Image
from numpy import asarray
Image.MAX_IMAGE_PIXELS = None


# ===============================================================


image = Image.open(r'1_500.jpg')
im3d=asarray(image)
map=im3d[:,:,0].copy()
print('Image loaded')


# ===============================================================
map[map<=50]=1
map[map>50]=0
# ===============================================================


# ===============================================================
print(map.shape)

map_col = np.array([])
map_row = np.array([])

ratio = np.array([])
boxes = np.array([])
# ===============================================================


# ===============================================================
# set of r sizes

sizes = [10, 30, 50, 93, 155, 200, 600, 775, 2325, 3720, 4650, 9300] #1-500


for r in sizes:

   sqr_size=map[0,:].size/r
   boxcount=0
   # ===============================================================

   
   # ===============================================================
   map_col = np.array_split(map, r, axis=1)

   # counting box interecting with shorelines
   for x in map_col:
      map_row = np.array_split(x, r, axis=0)
      for y in map_row:
         
          if (1 in y):
             boxcount+=1
            

   # ===============================================================

   # 
   ratio = np.append(ratio, sqr_size)
   boxes = np.append(boxes, boxcount)
   print('finished phase of size r=', r)

print(ratio)
print(boxes)


