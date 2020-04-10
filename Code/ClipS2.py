import glob
import rasterio
from rasterio.mask import mask
import geopandas as gpd

def getFeatures(gdf):
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

path = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data"
listRaster = glob.glob(path + "/*.tif")
cutline = gpd.read_file(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\Kebunfix.gpkg")
output = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\Data\clipped"

for x in range(len(listRaster)):
    data = rasterio.open(listRaster[x])
    geo = cutline.to_crs(crs=data.crs.data)
    coords = getFeatures(geo)
    out_img, out_transform = mask(dataset=data, shapes=coords, crop=True)
    out_meta = data.meta.copy()
    epsg_code = int(data.crs.data['init'][5:])
    out_meta.update({"driver": "GTiff",
                     "height": out_img.shape[1],
                     "width": out_img.shape[2],
                     "transform": out_transform})
    data.close()
    with rasterio.open(output + "/" + listRaster[x].split("\\")[-1][:-4]+"_Clipped" + ".tif", "w", **out_meta) as dest:
        dest.write(out_img)
        dest.close()
    print("Succes",x)