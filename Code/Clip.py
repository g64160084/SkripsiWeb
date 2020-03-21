import glob
import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
from fiona.crs import from_epsg
import pycrs
import os


path = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output"
listRaster = glob.glob(path + "/*.tif")
cutline = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\raw\KebunBaru.gpkg"
output = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\clipped"
kiw = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\output\LC08_L1TP_119065_20180903_20180912_01_T1_B5_Comp.tif"

data = rasterio.open(kiw)
new =  gpd.read_file(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\26-2-2020\raw\KebunBaru.gpkg")

geo = new.to_crs(crs=data.crs.data)

def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

coords = getFeatures(geo)
print(coords)

out_img, out_transform = mask(dataset=data, shapes=coords, crop=True)

show(out_img)

for x in listRaster:
    print(x)
    filename =output+ "/" + x.split("\\")[-1]
    print(filename)
    os.system('gdalwarp -cutline {} -crop_to_cutline -dstalpha {} {}'.format(cutline, x, filename))
