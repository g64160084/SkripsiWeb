import rasterio
from rasterio.fill import fillnodata
import numpy as np
import glob

path = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\clipped"
listBand4 = glob.glob(path + "/*B4_Clipped.tif")
listBand5 = glob.glob(path + "/*B5_Clipped.tif")
listBQA = glob.glob(path + "/*BQA_Clipped.tif")
output = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\cloudremoved"

for x in range(len(listBQA)):
    b4 = rasterio.open(listBand4[x])
    band4 = b4.read(1).astype('float64')
    b4prof=b4.profile
    b4.close()
    b5 = rasterio.open(listBand5[x])
    band5 = b5.read(1).astype('float64')
    b5prof = b5.profile
    b5.close()
    bqa = rasterio.open(listBQA[x])
    bqas = bqa.read(1).astype('float64')
    bqa.close()

    condition = [((bqas == 2800.) | (bqas == 2804.) | (bqas == 2808.) | (bqas == 2812.) | (bqas == 6896.) |
                  (bqas == 6900.) | (bqas == 6904.) | (bqas == 6908.) | (bqas == 2976.) | (bqas == 2980.) |
                  (bqas == 2984.) | (bqas == 2988.) | (bqas == 3008.) | (bqas == 3012.) | (bqas == 3016.) |
                  (bqas == 3020.) | (bqas == 7072.) | (bqas == 7076.) | (bqas == 7080.) | (bqas == 7084.) |
                  (bqas == 7104.) | (bqas == 7108.) | (bqas == 7112.) | (bqas == 7116.))]
    maskBolong = np.where(
        condition,0,1
    )
    bolongin4 = np.where(
        maskBolong==1,band4,0
    )

    with rasterio.Env():
        profile = b4prof
        profile.update(
            dtype=rasterio.float64,
            count=1,
            compress='lzw')

        with rasterio.open(output + "/" + listBand4[x].split("\\")[-1][:-4]+"_Comp"+".tif" , 'w', **profile) as dst:
            dst.write(bolongin4.astype(rasterio.float64))
            dst.close()

    bolongin5 = np.where(
        maskBolong==1,band5,0
    )

    with rasterio.Env():
        profile = b5prof
        profile.update(
            dtype=rasterio.float64,
            count=1,
            compress='lzw')

        with rasterio.open(output + "/" + listBand5[x].split("\\")[-1][:-4]+"_Comp"+".tif", 'w', **profile) as dst:
            dst.write(bolongin5.astype(rasterio.float64))
            dst.close()

    print("{} SUCESS",x)