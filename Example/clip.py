import os
from os import system
# from osgeo import gdal
import glob

path = r"C:\Users\DELL\Documents\LANDSAT\DATA_NEW\RAW"
listRaster = glob.glob(path + "/*.tif")
cutline = r"C:\Users\DELL\Documents\LANDSAT\DATA_NEW\masking_new.shp"
output = r"C:\Users\DELL\Documents\LANDSAT\DATA_NEW\output"
# RootDir1 = r"D:\FORESTS2020\SHARING\ILKOM\DATA\DATA_NEW"
# listRaster = list()
# for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
#         for name in files:
#             if name.endswith('.tif'):
#                 print(name)
#                 listRaster.append(os.path.join(root,name))

for x in listRaster:
    print(x)
    filename =output+ "/" + x.split("\\")[-1]
    print(filename)
    os.system('gdalwarp -cutline {} -crop_to_cutline -dstalpha {} {}'.format(cutline, x, filename))
# fig, (axr, axg, axb) = pyplot.subplots(1,3, figsize=(21,7))
# show(band4, ax=axr, cmap='Blues_r', title='Original Band4')
# show(bolong4, ax=axg, cmap='Blues_r', title='Mask')
# show(filled, ax=axb, cmap='Blues_r', title='Masked(polarization)')
# pyplot.show()