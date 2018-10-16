#Function:将RGB图像转换为灰度值图像
#Author：worthurlove
#Date：2018.10.15
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import numpy as np

img = mpimg.imread('123.jpg')  #读取图片以Numpy.arry的形式存储


def rgb2gray(rgb):  #定义转换函数
    rgbgray = rgb.copy()  #复制图片副本
    arr_1 = rgb.shape[0]  #数组第一维的长度
    arr_2 = rgb.shape[1]  #数组第二维的长度
    for i in range(arr_1):
        for j in range(arr_2):
            A = np.array([
                float(rgb[i, j, 0]),
                float(rgb[i, j, 1]),
                float(rgb[i, j, 2])
            ])  #记录每一个像素点的RGB值
            '''
            双重循环遍历每一个像素点
            '''
            B = np.array([0.299, 0.587, 0.114])  #灰度转换系数
            GRAY = np.dot(A, B)  #转换后的灰度值
            rgbgray[i, j, :3] = [GRAY, GRAY, GRAY]  #赋值
    return rgbgray


gray = rgb2gray(img)#将选中的图片转换为灰度值

plt.subplot(1, 2, 1)
plt.imshow(img)
#显示原图

plt.subplot(1, 2, 2)
plt.imshow(gray)
#显示转换后的灰度值图片
plt.show()