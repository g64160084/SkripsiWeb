import rasterio
import numpy as np
import glob
from rasterio.plot import show

path = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\clipped2"
listRaster4 = glob.glob(path + "/*B4_Comp_Clipped.tif")
listRaster5 = glob.glob(path + "/*B5_Comp_Clipped.tif")
compoundb4 = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\compound\compound4.tif"
compoundb5 = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\compound\compound5.tif"
output = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\filledcompound"
c4 = rasterio.open(compoundb4)
c4 = c4.read(1).astype('float64')
c5 = rasterio.open(compoundb5)
c5 = c5.read(1).astype('float64')


for x in range(len(listRaster4)):
    b4 = rasterio.open(listRaster4[x])
    b5 = rasterio.open(listRaster5[x])
    band4 = b4.read(1).astype('float64')
    band5 = b5.read(1).astype('float64')

    fillingcompound4 = np.where(
        band4==0,c4,band4
    )

    with rasterio.Env():
        profile = b4.profile
        profile.update(
            dtype=rasterio.float64,
            count=1,
            compress='lzw')

        with rasterio.open(output + "/" + listRaster4[x].split("\\")[-1][:-4]+"_Filled" + ".tif", 'w',
                           **profile) as dst:
            dst.write(fillingcompound4.astype(rasterio.float64), 1)

    fillingcompound5 = np.where(
        band5 == 0, c5, band5
    )

    with rasterio.Env():
        profile = b5.profile
        profile.update(
            dtype=rasterio.float64,
            count=1,
            compress='lzw')

        with rasterio.open(output + "/" + listRaster5[x].split("\\")[-1][:-4]+"_Filled" + ".tif", 'w',
                           **profile) as dst:
            dst.write(fillingcompound5.astype(rasterio.float64), 1)