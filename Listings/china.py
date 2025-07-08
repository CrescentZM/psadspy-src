from osgeo import gdal

# 打开地图tiff文件
dataset = gdal.Open('D:\StudyFiles\Figure\\taiwan.tif')

# 获取地图投影信息
projection = dataset.GetProjection()

# 获取地图地理坐标信息
geotransform = dataset.GetGeoTransform()

# 分别获取地图左上角经度、纬度和地图像素大小
left_top_lon = geotransform[0]
left_top_lat = geotransform[3]
pixel_size_x = geotransform[1]
pixel_size_y = geotransform[5]

print('Left top longitude:', left_top_lon)
print('Left top latitude:', left_top_lat)
print('Pixel size X:', pixel_size_x)
print('Pixel size Y:', pixel_size_y)

# 假设要获取第10行20列像素点的经纬度信息
row = 10
col = 20

lon = left_top_lon + col * pixel_size_x
lat = left_top_lat + row * pixel_size_y

print('Longitude:', lon)
print('Latitude:', lat)
