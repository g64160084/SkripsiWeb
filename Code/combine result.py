import glob
import pandas as pd
from fbprophet import Prophet
import rasterio
import numpy


path = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\reflectance"
listNdvi = glob.glob(path + "/*_NDVI.tif")
output = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\extract"
base = pd.read_csv(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\bahan1.csv")
modeloutput = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\model"
test = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\compound\compound4.tif"
b4 = rasterio.open(test)
b4prof = b4.profile

twod_list = []
for i in range (3, 13):
    new = []
    for j in range (60, 70):
        target = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\model" + ("\%s-%sHasilModel.csv" % (i, j))
        iniarraynya = pd.read_csv(target)
        hero = iniarraynya.iat[23,1]
        new.append(hero)
    twod_list.append(new)


test = numpy.asarray(twod_list)

with rasterio.Env():
    profile = b4prof
    profile.update(
        dtype=rasterio.float64,
        count=1,
        compress='lzw')

    with rasterio.open(output + "/"+"Predict_NDVI" + ".tif", 'w',
                       **profile) as dst:
        dst.write(test.astype(rasterio.float64), 1)
        dst.close()