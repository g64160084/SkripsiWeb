# Python
import glob
import pandas as pd
from fbprophet import Prophet
import rasterio

path = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\reflectance"
listNdvi = glob.glob(path + "/*_NDVI.tif")
output = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\extract"
base = pd.read_csv(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\bahan1.csv")
modeloutput = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\model"

for i in range (4, 13):
    for j in range (60, 70):
        listarray = base
        for k in range(len(listNdvi)):
            ndvi = rasterio.open(listNdvi[k])
            arrayndvi = ndvi.read(1).astype('float64')
            ndvi.close()
            listarray.iat[k,1] = arrayndvi[i,j]
        m = Prophet()
        m.fit(listarray)
        future = m.make_future_dataframe(periods=2, freq='M')
        forecast = m.predict(future)
        export = ("\%s-%sHasilModel.csv" % (i, j))
        export = modeloutput + export
        listarray.to_csv(('%s' % (export)), index=False)
#            export = ("\%s-%sListModel.csv" % (i, j))
#            export = output + export
#            listarray.to_csv(('%s'%(export)),index=False)


# for i in range (0, 300):
#     for j in range (0, 235):
#         target = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\extract" + ("\%s%sListModel.csv" % (i, j))
#         iniarraynya = pd.read_csv(target)
#         m = Prophet()
#         m.fit(iniarraynya)
#         future = m.make_future_dataframe(periods=2, freq='M')
#         forecast = m.predict(future)
#         export = ("\%s-%sHasilModel.csv" % (i, j))
#         export = modeloutput + export
#         listarray.to_csv(('%s' % (export)), index=False)
