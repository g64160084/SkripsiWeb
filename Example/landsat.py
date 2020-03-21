#import required libraries
import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
import os
import csv

#os.listdir('../Landsat8/')
#import bands as separate 1 band raster
#band4 = rasterio.open('../Landsat8/LC08_L1TP_042035_20180603_20180615_01_T1_B4_clip.tif') #red
#band5 = rasterio.open('../Landsat8/LC08_L1TP_042035_20180603_20180615_01_T1_B5_clip.tif') #nir
bqa = rasterio.open(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\raw\LC08_L1TP_119065_20180428_20180502_01_T1\LC08_L1TP_119065_20180428_20180502_01_T1_BQA.TIF")
#band4 = rasterio.open('../Landsat8/New folder/B42.tif') #red
#band5 = rasterio.open('../Landsat8/New folder/B52.tif') #nir
#number of raster rows
bqa.height
#number of raster columns
bqa.width
#plot band
plot.show(bqa)
#type of raster byte
bqa.dtypes[0]
#raster sytem of reference
bqa.crs
#raster transform parameters
bqa.transform
#raster values as matrix array
bqa.read(1)

#multiple band representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plot.show(bqa, ax=ax1, cmap='Reds') #red
fig.tight_layout()

#plot.show(band5, ax=ax2, cmap='Reds') #nir

#generate nir and red objects as arrays in float64 format
bqas = bqa.read(1).astype('float64')
bqas.med()
#nir = band5.read(1).astype('float64')
#red = band4.read(1).astype('float64')
#nir = band5.read(1).astype('float64')
#ndvi calculation, empty cells or nodata cells are reported as 0
#ndvi=np.where(
#    (nir+red)==0.,
#    0,
#    (nir-red)/(nir+red))
#ndvi[:5,:5]

#print(bqa.shape)
#export ndvi image
#ndviImage = rasterio.open('../Output/ndviImage.tiff','w',driver='Gtiff',
#                          width=band4.width,
#                          height = band4.height,
#                          count=1, crs=band4.crs,
#                          transform=band4.transform,
#                         dtype='float64')
#ndviImage.write(ndvi,1)
#ndviImage.close()
#plot ndvi
#ndvi = rasterio.open('../Output/ndviImage.tiff')
#fig = plt.figure(figsize=(18,12))
#plot.show(ndvi)
#NDVI = ndvi.read(1).astype('float64')
#with open('ndvi.csv','w',newline='') as file:
#    writer = csv.writer(file)
#    writer.writerows(NDVI)

