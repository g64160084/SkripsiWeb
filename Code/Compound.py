import rasterio
from rasterio.fill import fillnodata
import numpy as np
import glob
from rasterio import plot
import matplotlib.pyplot as plt
from numpy import array

path = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\clipped2"
listBand4 = glob.glob(path + "/*B4_Comp_Clipped.tif")
listBand5 = glob.glob(path + "/*B5_Comp_Clipped.tif")
compOutput = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\compound"

b40 = rasterio.open(listBand4[0])
b41 = rasterio.open(listBand4[1])
b42 = rasterio.open(listBand4[2])
b43 = rasterio.open(listBand4[3])
b44 = rasterio.open(listBand4[4])
b45 = rasterio.open(listBand4[5])

b50 = rasterio.open(listBand5[0])
b51 = rasterio.open(listBand5[1])
b52 = rasterio.open(listBand5[2])
b53 = rasterio.open(listBand5[3])
b54 = rasterio.open(listBand5[4])
b55 = rasterio.open(listBand5[5])

band40 = b40.read(1).astype('float64')
band41 = b41.read(1).astype('float64')
band42 = b42.read(1).astype('float64')
band43 = b43.read(1).astype('float64')
band44 = b44.read(1).astype('float64')
band45 = b45.read(1).astype('float64')

band50 = b50.read(1).astype('float64')
band51 = b51.read(1).astype('float64')
band52 = b52.read(1).astype('float64')
band53 = b53.read(1).astype('float64')
band54 = b54.read(1).astype('float64')
band55 = b55.read(1).astype('float64')

twod_list = []
for i in range (0, 110):
    new = []
    for j in range (0, 116):
        hero = np.median([band45[i, j], band44[i, j], band43[i, j], band42[i, j], band41[i, j], band40[i, j]])
        new.append(hero)
    twod_list.append(new)

twod_list5 = []
for i in range (0, 110):
    new5 = []
    for j in range (0, 116):
        hero = np.median([band45[i, j], band44[i, j], band43[i, j], band42[i, j], band41[i, j], band40[i, j]])
        new5.append(hero)
    twod_list5.append(new5)

compound4 = np.asarray(twod_list)
compound5 = np.asarray(twod_list5)

with rasterio.Env():
    profile = b40.profile
    profile.update(
        dtype=rasterio.uint32,
        count=1,
        compress='lzw')

    with rasterio.open(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\compound\compound4.tif", 'w', **profile) as dst:
        dst.write(compound4.astype(rasterio.uint32),1)

    with rasterio.Env():
        profile = b50.profile
        profile.update(
            dtype=rasterio.uint32,
            count=1,
            compress='lzw')

        with rasterio.open(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\compound\compound5.tif", 'w', **profile) as dst:
            dst.write(compound5.astype(rasterio.uint32),1)