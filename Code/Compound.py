import rasterio
from rasterio.fill import fillnodata
import numpy as np
import glob
from rasterio import plot
import matplotlib.pyplot as plt
from numpy import array

path = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\cloudremoved"
listBand4 = glob.glob(path + "/*B4_Clipped_Comp.tif")
listBand5 = glob.glob(path + "/*B5_Clipped_Comp.tif")
compOutput = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\compound"


b40 = rasterio.open(listBand4[0])
band40 = b40.read(1).astype('float64')
b4prof = b40.profile
b40.close()
b41 = rasterio.open(listBand4[1])
band41 = b41.read(1).astype('float64')
b41.close()
b42 = rasterio.open(listBand4[2])
band42 = b42.read(1).astype('float64')
b42.close()
b43 = rasterio.open(listBand4[3])
band43 = b43.read(1).astype('float64')
b43.close()
b44 = rasterio.open(listBand4[4])
band44 = b44.read(1).astype('float64')
b44.close()
b45 = rasterio.open(listBand4[5])
band45 = b45.read(1).astype('float64')
b45.close()
b46 = rasterio.open(listBand4[6])
band46 = b46.read(1).astype('float64')
b46.close()
b47 = rasterio.open(listBand4[7])
band47 = b47.read(1).astype('float64')
b47.close()
b48 = rasterio.open(listBand4[8])
band48 = b48.read(1).astype('float64')
b48.close()
b49 = rasterio.open(listBand4[9])
band49 = b49.read(1).astype('float64')
b49.close()
b410 = rasterio.open(listBand4[10])
band410 = b410.read(1).astype('float64')
b410.close()
b411 = rasterio.open(listBand4[11])
band411 = b411.read(1).astype('float64')
b411.close()
b412 = rasterio.open(listBand4[12])
band412 = b412.read(1).astype('float64')
b412.close()
b413 = rasterio.open(listBand4[13])
band413 = b413.read(1).astype('float64')
b413.close()
b414 = rasterio.open(listBand4[14])
band414 = b414.read(1).astype('float64')
b414.close()
b415 = rasterio.open(listBand4[15])
band415 = b415.read(1).astype('float64')
b415.close()
b416 = rasterio.open(listBand4[16])
band416 = b416.read(1).astype('float64')
b416.close()
b417 = rasterio.open(listBand4[17])
band417 = b417.read(1).astype('float64')
b417.close()
b418 = rasterio.open(listBand4[18])
band418 = b418.read(1).astype('float64')
b418.close()
b419 = rasterio.open(listBand4[19])
band419 = b419.read(1).astype('float64')
b419.close()
b420 = rasterio.open(listBand4[20])
band420 = b420.read(1).astype('float64')
b420.close()
b421 = rasterio.open(listBand4[21])
band421 = b421.read(1).astype('float64')
b421.close()
b422 = rasterio.open(listBand4[22])
band422 = b422.read(1).astype('float64')
b422.close()
b423 = rasterio.open(listBand4[23])
band423 = b423.read(1).astype('float64')
b423.close()




b50 = rasterio.open(listBand5[0])
band50 = b50.read(1).astype('float64')
b5prof = b50.profile
b51 = rasterio.open(listBand5[1])
band51 = b51.read(1).astype('float64')
b51.close()
b52 = rasterio.open(listBand5[2])
band52 = b52.read(1).astype('float64')
b52.close()
b53 = rasterio.open(listBand5[3])
band53 = b53.read(1).astype('float64')
b53.close()
b54 = rasterio.open(listBand5[4])
band54 = b54.read(1).astype('float64')
b54.close()
b55 = rasterio.open(listBand5[5])
band55 = b55.read(1).astype('float64')
b55.close()
b56 = rasterio.open(listBand5[6])
band56 = b56.read(1).astype('float64')
b56.close()
b57 = rasterio.open(listBand5[7])
band57 = b57.read(1).astype('float64')
b57.close()
b58 = rasterio.open(listBand5[8])
band58 = b58.read(1).astype('float64')
b58.close()
b59 = rasterio.open(listBand5[9])
band59 = b59.read(1).astype('float64')
b59.close()
b510 = rasterio.open(listBand5[10])
band510 = b510.read(1).astype('float64')
b510.close()
b511 = rasterio.open(listBand5[11])
band511 = b511.read(1).astype('float64')
b511.close()
b512 = rasterio.open(listBand5[12])
band512 = b512.read(1).astype('float64')
b512.close()
b513 = rasterio.open(listBand5[13])
band513 = b513.read(1).astype('float64')
b513.close()
b514 = rasterio.open(listBand5[14])
band514 = b514.read(1).astype('float64')
b514.close()
b515 = rasterio.open(listBand5[15])
band515 = b515.read(1).astype('float64')
b515.close()
b516 = rasterio.open(listBand5[16])
band516 = b516.read(1).astype('float64')
b516.close()
b517 = rasterio.open(listBand5[17])
band517 = b517.read(1).astype('float64')
b517.close()
b518 = rasterio.open(listBand5[18])
band518 = b518.read(1).astype('float64')
b518.close()
b519 = rasterio.open(listBand5[19])
band519 = b519.read(1).astype('float64')
b519.close()
b520 = rasterio.open(listBand5[20])
band520 = b520.read(1).astype('float64')
b520.close()
b521 = rasterio.open(listBand5[21])
band521 = b521.read(1).astype('float64')
b521.close()
b522 = rasterio.open(listBand5[22])
band522 = b522.read(1).astype('float64')
b522.close()
b523 = rasterio.open(listBand5[23])
band523 = b523.read(1).astype('float64')
b523.close()


twod_list = []
for i in range (0, 300):
    new = []
    for j in range (0, 235):
        hero = np.median([band423[i,j],band422[i,j],band421[i,j],band420[i,j],band419[i,j],band418[i,j],band417[i,j],band416[i,j],band415[i,j],band414[i,j],band413[i,j],band412[i,j],band411[i,j],band410[i,j],band49[i,j],band48[i,j],band47[i,j],band46[i,j],band45[i,j],band44[i,j],band43[i,j],band42[i,j],band41[i,j],band40[i,j]])
        new.append(hero)
    twod_list.append(new)

twod_list5 = []
for i in range (0, 300):
    new5 = []
    for j in range (0, 235):
        hero = np.median([band523[i,j],band522[i,j],band521[i,j],band520[i,j],band519[i,j],band518[i,j],band517[i,j],band516[i,j],band516[i,j],band514[i,j],band513[i,j],band512[i,j],band511[i,j],band510[i,j],band59[i,j],band58[i,j],band57[i,j],band56[i,j],band55[i,j],band54[i,j],band53[i,j],band52[i,j],band51[i,j],band50[i,j]])
        new5.append(hero)
    twod_list5.append(new5)

compound4 = np.asarray(twod_list)
compound5 = np.asarray(twod_list5)

with rasterio.Env():
    profile = b4prof
    profile.update(
        dtype=rasterio.uint32,
        count=1,
        compress='lzw')

    with rasterio.open(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\compound\compound4.tif", 'w', **profile) as dst:
        dst.write(compound4.astype(rasterio.uint32),1)
        dst.close()

    with rasterio.Env():
        profile = b5prof
        profile.update(
            dtype=rasterio.uint32,
            count=1,
            compress='lzw')

        with rasterio.open(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\compound\compound5.tif", 'w', **profile) as dst:
            dst.write(compound5.astype(rasterio.uint32),1)
            dst.close