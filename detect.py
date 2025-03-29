# -*- coding: utf-8 -*-

import cv2
import numpy as np
from matplotlib import pyplot as plt

lower_blue = np.array([100, 100, 100])  # 蓝色下限
upper_blue = np.array([130, 255, 255])  # 蓝色上限

lower_red1 = np.array([0, 100, 100])    # 红色下限
upper_red1 = np.array([20, 255, 255])   # 红色上限
lower_red2 = np.array([160, 100, 100])  # 红色下限
upper_red2 = np.array([180, 255, 255])  # 红色上限

lower_yellow = np.array([25, 100, 100])  # 黄色下限
upper_yellow = np.array([35, 255, 255])  # 黄色上限

cap = cv2.VideoCapture(0)

# while cap.isOpened() :
#     _, image = cap.read()
#     image_orin = image.copy()
#     image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)                           # 转灰度
#     # image_gray = 0.299*image[:,:,2] + 0.4*image[:,:,1] + 0.114*image[:,:,0]
#     # image_gauss = cv2.GaussianBlur(image_gray,(3,3),3,0)        # 高斯滤波
#     # image_bil = cv2.bilateralFilter(image_gray, 5, 100, 100)
#     sobelx = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=3)
#     sobely = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=3)
#     sobelx = cv2.convertScaleAbs(sobelx)
#     sobely = cv2.convertScaleAbs(sobely)
#     image_sobel = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)    # sobel边缘检测
#
#     # image_dil = cv2.dilate(image_sobel, (3,3))    # 膨胀操作
#     _, image_bin = cv2.threshold(image_sobel, 75, 255, cv2.THRESH_BINARY)  # 二值化处理
#     # image_canny = cv2.Canny(image_gauss, 20, 200)  # canny检测
#
#     contours, _ = cv2.findContours(image_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # 检索边框
#
#     big_contours = [] # 大小符合
#     Rectangle_contours = []# 矩形
#
#     for obj in contours:
#         area = cv2.contourArea(obj)  # 计算轮廓内区域的面积
#         if 50<area<3500:
#             big_contours.append(obj)
#             # print(len(contours))
#             perimeter = cv2.arcLength(obj, True)  # 计算轮廓周长
#             approx = cv2.approxPolyDP(obj, 0.02 * perimeter, True)  # 获取轮廓角点坐标
#             CornerNum = len(approx)  # 轮廓角点的数量
#             x, y, w, h = cv2.boundingRect(approx)  # 获取坐标值和宽度、高度
#
#
#
#             cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)  # 绘制边界框
#             cv2.putText(image, objT, (x + (w // 2), y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0),1)  # 绘制文字
#
#     cv2.imshow("image",image)
#     cv2.imshow("image_gray", image_gray)
#     # cv2.imshow("image_gauss", image_gauss)
#     # cv2.imshow("image_bil", image_bil)
#     cv2.imshow("image_sobel", image_sobel)
#     # cv2.imshow("image_dil", image_dil)
#     # cv2.imshow("image_canny", image_canny)
#     cv2.imshow("image_bin", image_bin)
#     # cv2.imshow("image_con", image_con)
#     # cv2.imshow("image_canny", image_canny)
#     cv2.waitKey(3)
#
# cv2.destroyAllWindows()

while cap.isOpened() :
    _, image = cap.read()
    # image_ori = image.copy()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 红色
    mask1_red = cv2.inRange(image_hsv, lower_red1, upper_red1)
    mask2_red = cv2.inRange(image_hsv, lower_red2, upper_red2)
    mask_blue = cv2.inRange(image_hsv, lower_blue, upper_blue)
    mask_yellow = cv2.inRange(image_hsv, lower_yellow, upper_yellow)
    mask_1 = cv2.bitwise_or(mask1_red,mask2_red)
    mask_2 = cv2.bitwise_or(mask_blue,mask_yellow)
    mask = cv2.bitwise_or(mask_1, mask_2)
    mask_open_red = cv2.morphologyEx(mask,cv2.MORPH_OPEN,(3,3))
    contours, _ = cv2.findContours(mask_open_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("mask",mask)
    # detected_ = []
    # for cnt in contours:
    #     area = cv2.contourArea(cnt) # 计算轮廓面积
    #     if area > 400:  # 忽略小面积噪声
    #         detected_.append(cnt)
    #         perimeter = cv2.arcLength(cnt, True)  # 计算轮廓周长
    #         approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)  # 获取轮廓角点坐标
    #         x, y, w, h = cv2.boundingRect(approx)  # 获取坐标值和宽度、高度
    #         objType = "NULL"
    #         if perimeter*perimeter//area >19:
    #             objType = "Three"
    #         elif len(approx) == 3:
    #             objType = "Three"
    #         elif len(approx) == 4:
    #             objType = "Four"
    #         elif len(approx) == 6:
    #             objType = "Six"
    #         elif len(approx) > 6:
    #             objType = "Zero"
    #         Color = "Red"
    #         # print(Color, x, y, objType, perimeter*perimeter//area, len(approx))

    cv2.waitKey(10)

cv2.destroyAllWindows()

