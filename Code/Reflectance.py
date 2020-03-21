import rasterio
import numpy as np
import glob
from rasterio.plot import show

path = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\filledcompound"
listRaster4 = glob.glob(path + "/*B4_Comp_Clipped_Filled.tif")
listRaster5 = glob.glob(path + "/*B5_Comp_Clipped_Filled.tif")
listRasterMTL = glob.glob(path + "/*MTL.txt")
output = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\reflectance"

for x in range(len(listRasterMTL)):
    mtl = open(listRasterMTL[x], 'r',encoding="utf-8")
    s= mtl.read()
    REFLECTANCE_Mult_= s.split("GROUP = RADIOMETRIC_RESCALING",1)
    REFLECTANCE_Mult_Band4= REFLECTANCE_Mult_[1].split("REFLECTANCE_MULT_BAND_4 = ",1)
    REFLECTANCE_Mult_Band5= REFLECTANCE_Mult_[1].split("REFLECTANCE_MULT_BAND_5 = ",1)
    REFLECTANCE_Add_Band4= REFLECTANCE_Mult_[1].split("REFLECTANCE_ADD_BAND_4 = ",1)
    REFLECTANCE_Add_Band5= REFLECTANCE_Mult_[1].split("REFLECTANCE_ADD_BAND_5 = ",1)
    REFLECTANCE_MULT_BAND_4 = REFLECTANCE_Mult_Band4[1].split("\n")
    REFLECTANCE_MULT_BAND_5 = REFLECTANCE_Mult_Band5[1].split("\n")
    REFLECTANCE_Add_BAND_4 = REFLECTANCE_Add_Band4[1].split("\n")
    REFLECTANCE_Add_BAND_5 = REFLECTANCE_Add_Band5[1].split("\n")
    RMB_4 = float(REFLECTANCE_MULT_BAND_4[0])
    RMB_5 = float(REFLECTANCE_MULT_BAND_5[0])
    RAB_4 = float(REFLECTANCE_Add_BAND_4[0])
    RAB_5 = float(REFLECTANCE_Add_BAND_5[0])
    b4 = rasterio.open(listRaster4[x])
    Band4 = b4.read(1).astype('float64')
    b5 = rasterio.open(listRaster5[x])
    Band5 = b5.read(1).astype('float64')
    REFLECTANCE_BAND4 = np.where(
        Band4!=0,((Band4*RMB_4)+RAB_4),0
    )
    REFLECTANCE_BAND5 = np.where(
        Band5!=0,((Band5*RMB_5)+RAB_5),0
    )

    NDVI = np.where(
        (REFLECTANCE_BAND5==0)|(REFLECTANCE_BAND4==0),0,(REFLECTANCE_BAND5-REFLECTANCE_BAND4)/(REFLECTANCE_BAND5+REFLECTANCE_BAND4)
    )
    show(NDVI)

    with rasterio.Env():
        profile = b4.profile
        profile.update(
            dtype=rasterio.float64,
            count=1,
            compress='lzw')

        with rasterio.open(output + "/" + listRaster5[x].split("\\")[-1][:-26]+"_NDVI" + ".tif", 'w',
                           **profile) as dst:
            dst.write(NDVI.astype(rasterio.float64), 1)
