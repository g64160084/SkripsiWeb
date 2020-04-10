import rasterio
import numpy as np
import glob
from rasterio.plot import show

path = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\cloudremoved"
listRaster4 = glob.glob(path + "/*B4_Clipped_Comp.tif")
listRaster5 = glob.glob(path + "/*B5_Clipped_Comp.tif")
compoundb4 = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\compound\compound4.tif"
compoundb5 = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\compound\compound5.tif"
output = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\filling"
c4pol = rasterio.open(compoundb4)
c4 = c4pol.read(1).astype('float64')
c4pol.close()
c5pol = rasterio.open(compoundb5)
c5 = c5pol.read(1).astype('float64')
c5pol.close()

for x in range(len(listRaster4)):
    b4 = rasterio.open(listRaster4[x])
    band4 = b4.read(1).astype('float64')
    b4prof = b4.profile
    b4.close()

    b5 = rasterio.open(listRaster5[x])
    band5 = b5.read(1).astype('float64')
    b5prof = b5.profile
    b5.close()

    fillingcompound4 = np.where(
        band4==0,c4,band4
    )

    with rasterio.Env():
        profile = b4prof
        profile.update(
            dtype=rasterio.float64,
            count=1,
            compress='lzw')

        with rasterio.open(output + "/" + listRaster4[x].split("\\")[-1][:-4]+"_Filled" + ".tif", 'w',
                           **profile) as dst:
            dst.write(fillingcompound4.astype(rasterio.float64), 1)
            dst.close()

    fillingcompound5 = np.where(
        band5 == 0, c5, band5
    )

    with rasterio.Env():
        profile = b5prof
        profile.update(
            dtype=rasterio.float64,
            count=1,
            compress='lzw')

        with rasterio.open(output + "/" + listRaster5[x].split("\\")[-1][:-4]+"_Filled" + ".tif", 'w',
                           **profile) as dst:
            dst.write(fillingcompound5.astype(rasterio.float64), 1)
            dst.close()

    print("Succes",x)