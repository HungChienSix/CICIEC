# -*- coding: utf-8 -*-

import cv2
import numpy as np
# from matplotlib import pyplot as plt

lower_blue = np.array([100, 100, 100])  # 蓝色下限
upper_blue = np.array([130, 255, 255])  # 蓝色上限

lower_red1 = np.array([0, 100, 100])    # 红色下限
upper_red1 = np.array([20, 255, 255])   # 红色上限
lower_red2 = np.array([160, 100, 100])  # 红色下限
upper_red2 = np.array([180, 255, 255])  # 红色上限

lower_yellow = np.array([25, 100, 100])  # 黄色下限
upper_yellow = np.array([35, 255, 255])  # 黄色上限

lower_black = np.array([  0,   0,   0])  # 黑色下限
upper_black = np.array([179, 255,  120])  # 黑色上限

Color = "NULL"

cap = cv2.VideoCapture(0)

while cap.isOpened() :
    _, image = cap.read()
    image_blue = image.copy()
    image_red = image.copy()
    image_yellow = image.copy()
    image_black = image.copy()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 蓝色
    mask_blue = cv2.inRange(image_hsv, lower_blue, upper_blue)
    mask_open_blue = cv2.morphologyEx(mask_blue,cv2.MORPH_OPEN,(3,3))
    contours, _ = cv2.findContours(mask_open_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected_blue = []
    for cnt in contours:
        area = cv2.contourArea(cnt) # 计算轮廓面积
        if area > 400:  # 忽略小面积噪声
            detected_blue.append(cnt)
            perimeter = cv2.arcLength(cnt, True)  # 计算轮廓周长
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)  # 获取轮廓角点坐标
            x, y, w, h = cv2.boundingRect(approx)  # 获取坐标值和宽度、高度
            objType = "NULL"
            if len(approx) == 3:
                objType = "Three"
            elif len(approx) == 4:
                objType = "Four"
            elif len(approx) == 6:
                objType = "Six"
            elif len(approx) > 6:
                objType = "Zero"
            Color = "Blue"
            # print(Color,x,y,objType,perimeter*perimeter//area,len(approx))

    # 红色
    mask1_red = cv2.inRange(image_hsv, lower_red1, upper_red1)
    mask2_red = cv2.inRange(image_hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask1_red,mask2_red)
    mask_open_red = cv2.morphologyEx(mask_red,cv2.MORPH_OPEN,(3,3))
    contours, _ = cv2.findContours(mask_open_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected_red = []
    for cnt in contours:
        area = cv2.contourArea(cnt) # 计算轮廓面积
        if area > 400:  # 忽略小面积噪声
            detected_red.append(cnt)
            perimeter = cv2.arcLength(cnt, True)  # 计算轮廓周长
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)  # 获取轮廓角点坐标
            x, y, w, h = cv2.boundingRect(approx)  # 获取坐标值和宽度、高度
            objType = "NULL"
            if perimeter*perimeter//area >19:
                objType = "Three"
            elif len(approx) == 3:
                objType = "Three"
            elif len(approx) == 4:
                objType = "Four"
            elif len(approx) == 6:
                objType = "Six"
            elif len(approx) > 6:
                objType = "Zero"
            Color = "Red"
            # print(Color, x, y, objType, perimeter*perimeter//area, len(approx))

    # 黄色
    mask_yellow = cv2.inRange(image_hsv, lower_yellow, upper_yellow)
    mask_open_yellow = cv2.morphologyEx(mask_yellow,cv2.MORPH_OPEN,(3,3))
    contours, _ = cv2.findContours(mask_open_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected_yellow = []
    for cnt in contours:
        area = cv2.contourArea(cnt) # 计算轮廓面积
        if area > 400:  # 忽略小面积噪声
            detected_yellow.append(cnt)
            perimeter = cv2.arcLength(cnt, True)  # 计算轮廓周长
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)  # 获取轮廓角点坐标
            x, y, w, h = cv2.boundingRect(approx)  # 获取坐标值和宽度、高度
            objType = "NULL"
            if len(approx) == 3:
                objType = "Three"
            elif len(approx) == 4:
                objType = "Four"
            elif len(approx) == 6:
                objType = "Six"
            elif len(approx) > 6:
                objType = "Zero"
            Color = "Yellow"
            # print(Color,x,y,objType,perimeter*perimeter//area,len(approx))

    # 黑色
    mask_black = cv2.inRange(image_hsv, lower_black, upper_black)
    mask_open_black = cv2.morphologyEx(mask_black, cv2.MORPH_OPEN, (3, 3))
    contours, _ = cv2.findContours(mask_open_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    detected_black = []
    for cnt in contours:
        area = cv2.contourArea(cnt)  # 计算轮廓面积
        if  5000> area > 400:  # 忽略大小面积噪声
            detected_black.append(cnt)
            perimeter = cv2.arcLength(cnt, True)  # 计算轮廓周长
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)  # 获取轮廓角点坐标
            x, y, w, h = cv2.boundingRect(approx)  # 获取坐标值和宽度、高度
            objType = "NULL"
            if perimeter * perimeter // area > 19:
                objType = "Three"
            elif len(approx) == 3:
                objType = "Three"
            elif len(approx) == 4:
                objType = "Four"
            elif len(approx) == 6:
               objType = "Six"
            elif len(approx) > 6:
                objType = "Zero"
                Color = "Black"
                print(Color, x, y, objType, perimeter*perimeter//area, len(approx))

    print(len(detected_blue))
    print(len(detected_red))
    print(len(detected_yellow))
    print(len(detected_black))

    image_red = cv2.drawContours(image_red, detected_red, -1, (0, 255, 0), 2)
    image_blue = cv2.drawContours(image_blue, detected_blue, -1, (0, 255, 0), 2)
    image_yellow = cv2.drawContours(image_yellow, detected_yellow, -1, (0, 255, 0), 2)
    image_black = cv2.drawContours(image_black, detected_black, -1, (0, 255, 0), 2)

    cv2.imshow("Orin",image)

    cv2.imshow("Mask_open_blue", mask_open_blue)
    cv2.imshow("Mask_open_red", mask_open_red)
    cv2.imshow("Mask_open_yellow", mask_open_yellow)
    cv2.imshow("Mask_open_black", mask_open_black)

    cv2.imshow("Blue", image_blue)
    cv2.imshow("Red", image_red)
    cv2.imshow("Yellow", image_yellow)
    cv2.imshow("Black", image_black)
    cv2.waitKey(10)

cv2.destroyAllWindows()

