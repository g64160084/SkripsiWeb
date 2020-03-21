import rasterio
from rasterio.fill import fillnodata
import numpy as np
import glob

path = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\raw"
listBand4 = glob.glob(path + "/*B4.tif")
listBand5 = glob.glob(path + "/*B5.tif")
listBQA = glob.glob(path + "/*BQA.tif")
output = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output"

for x in range(len(listBQA)):
    b4 = rasterio.open(listBand4[0])
    b5 = rasterio.open(listBand5[x])
    bqa = rasterio.open(listBQA[0])
    bqas = bqa.read(1).astype('float64')
    band4 = b4.read(1).astype('float64')
    band5 = b5.read(1).astype('float64')
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
        profile = b4.profile
        profile.update(
            dtype=rasterio.float64,
            count=1,
            compress='lzw')

        with rasterio.open(output + "/" + listBand4[x].split("\\")[-1][:-4]+"_Comp"+".tif" , 'w', **profile) as dst:
            dst.write(bolongin4.astype(rasterio.float64))

    bolongin5 = np.where(
        maskBolong==1,band5,0
    )

    with rasterio.Env():
        profile = b5.profile
        profile.update(
            dtype=rasterio.float64,
            count=1,
            compress='lzw')

        with rasterio.open(output + "/" + listBand5[x].split("\\")[-1][:-4]+"_Comp"+".tif", 'w', **profile) as dst:
            dst.write(bolongin5.astype(rasterio.float64))

    filled4 = rasterio.fill.fillnodata(bolongin4, mask=maskBolong, max_search_distance=100.0, smoothing_iterations=0)
    filled5 = rasterio.fill.fillnodata(bolongin5, mask=maskBolong, max_search_distance=100.0, smoothing_iterations=0)

    with rasterio.open(output + "/" + listBand4[x].split("\\")[-1][:-4]+"_InPol"+".tif" , 'w', **profile) as dst:
        dst.write(filled4.astype(rasterio.float64))

    with rasterio.open(output + "/" + listBand5[x].split("\\")[-1][:-4]+"_InPol"+".tif", 'w', **profile) as dst:
         dst.write(filled5.astype(rasterio.float64))

    print("{} SUCESS",x)