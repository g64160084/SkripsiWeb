def cloudremove(stacked,nama4,nama5):
    import rasterio
    import os
    import rasterio
    import contextlib
    import numpy as np

    loc = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\static\img"


    cloudremoval = r"C:\Users\DELL\Documents\SKRIPSI\PYCHARM\Code\flasks\cloudremoval"
    c4 = r"D:\Feterachman\DATA SKRIPSI\26-2-2020\output\compound\compound4.tif"
    c5 = r"D:\Feterachman\DATA SKRIPSI\26-2-2020\output\compound\compound5.tif"
    c4 = rasterio.open(c4)
    c4 = c4.read(1).astype('float64')
    c5 = rasterio.open(c5)
    c5 = c5.read(1).astype('float64')
    bqa = rasterio.open(stacked)
    bqas = bqa.read(1).astype('float64')
    band4 = bqa.read(2).astype('float64')
    band5 = bqa.read(3).astype('float64')
    condition = [((bqas == 2800.) | (bqas == 2804.) | (bqas == 2808.) | (bqas == 2812.) | (bqas == 6896.) |
                  (bqas == 6900.) | (bqas == 6904.) | (bqas == 6908.) | (bqas == 2976.) | (bqas == 2980.) |
                  (bqas == 2984.) | (bqas == 2988.) | (bqas == 3008.) | (bqas == 3012.) | (bqas == 3016.) |
                  (bqas == 3020.) | (bqas == 7072.) | (bqas == 7076.) | (bqas == 7080.) | (bqas == 7084.) |
                  (bqas == 7104.) | (bqas == 7108.) | (bqas == 7112.) | (bqas == 7116.))]
    maskBolong = np.where(
        condition, 0, 1
    )
    bolongin4 = np.where(
        maskBolong == 1, band4, 0
    )
    bolongin5 = np.where(
        maskBolong == 1, band5, 0
    )
    fillingcompound4 = np.where(
        band4 == 0, c4, band4
    )
    fillingcompound5 = np.where(
        band5 == 0, c5, band5
    )

    with rasterio.Env():
        profile = bqa.profile
        profile.update(
            dtype=rasterio.float64,
            count=1,
            compress='lzw')
        with rasterio.open(os.path.join(cloudremoval,nama4) + "_filled" + ".tif", "w",
                           **profile) as dst:
            dst.write(bolongin4.astype(rasterio.float64))
            dst.close()


    with rasterio.Env():
        profile = bqa.profile
        profile.update(
            dtype=rasterio.float64,
            count=1,
            compress='lzw')

        with rasterio.open(os.path.join(cloudremoval,nama5) + "_filled" + ".tif", "w",
                           **profile) as dst:
            dst.write(bolongin5.astype(rasterio.float64))
            dst.close()

    outputclip4 = os.path.join(cloudremoval, nama4) + "_filled" + ".tif"
    outputclip5 = os.path.join(cloudremoval, nama5) + "_filled" + ".tif"
    return outputclip4,outputclip5