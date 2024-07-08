import matplotlib.image as mpimg
import numpy as np


'''Câu hỏi 12: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào
phương pháp Lightness:'''
def gray_scale_lightness(arr):
    result = np.ones((arr.shape[0], arr.shape[1]))
    for row in range(arr.shape[0]):
        for col in range(arr.shape[1]):
            result[row, col] = round((arr[row, col].max() + arr[row, col].min()) / 2, 1)
    return result

img = mpimg.imread('dog.jpeg')
gray_img_01 = gray_scale_lightness(img)
print(gray_img_01[0, 0])

'''Câu hỏi 13: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào
phương pháp Average:'''
def gray_scale_average(arr):
    result = np.ones((arr.shape[0], arr.shape[1]))
    for row in range(arr.shape[0]):
        for col in range(arr.shape[1]):
            result[row, col] = round(arr[row, col].mean(), 1)
    return result

img = mpimg.imread('dog.jpeg')
gray_img_02 = gray_scale_average(img)
print(gray_img_02[0, 0])

'''Câu hỏi 14: Hoàn thành đoạn code sau đây để chuyển ảnh màu sang ảnh xám dựa vào
phương pháp Luminosity:'''
def gray_scale_luminosity(arr):
    result = np.ones((arr.shape[0], arr.shape[1]))
    for row in range(arr.shape[0]):
        for col in range(arr.shape[1]):
            result[row, col] = arr[row, col, 0] * 0.21 + arr[row, col, 1] * 0.72 + arr[row, col, 2] * 0.07
            result[row, col] = round(result[row, col], 1)
    return result

img = mpimg.imread('dog.jpeg')
gray_img_03 = gray_scale_luminosity(img)
print(gray_img_03[0, 0])


'''
12A
13A
14C
'''

