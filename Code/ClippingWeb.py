def clipweb(input):
    import os
    import rasterio
    from rasterio.mask import mask
    import geopandas as gpd

    def getFeatures(gdf):
        import json
        return [json.loads(gdf.to_json())['features'][0]['geometry']]

    clipupload = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\clipupload"
    #cutline = gpd.read_file(r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\kebunfix.gpkg")
    cutline = gpd.read_file('../flasks/kebunfix.gpkg')
    data = rasterio.open(input)
    nama = os.path.basename(input)[:-4]
    geo = cutline.to_crs(crs=data.crs.data)
    coords = getFeatures(geo)
    out_img, out_transform = mask(dataset=data, shapes=coords, crop=True)
    out_meta = data.meta.copy()
    epsg_code = int(data.crs.data['init'][5:])
    out_meta.update({"driver": "GTiff",
                     "height": out_img.shape[1],
                     "width": out_img.shape[2],
                     "transform": out_transform})

    with rasterio.open(os.path.join(clipupload,nama) + "_Clipped" + ".tif", "w",
                       **out_meta) as dest:
        dest.write(out_img)
        outputclip = os.path.join(clipupload,nama) + "_Clipped" + ".tif"
    return outputclip