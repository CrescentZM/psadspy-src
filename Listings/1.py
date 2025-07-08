from osgeo import gdal, osr

dataset = gdal.Open("D:/StudyFiles/Figure/taiwan.tif")
proj_wkt = dataset.GetProjection()

srs = osr.SpatialReference()
srs.ImportFromWkt(proj_wkt)

# 尝试获取 EPSG 编号
epsg_code = srs.GetAttrValue("AUTHORITY", 1)
print("EPSG 编号:", epsg_code)
