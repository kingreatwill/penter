# 图像越清晰度
# 图像清晰度的评价指标 https://blog.csdn.net/charlene_bo/article/details/72673490
import cv2
import numpy as np
import math
# Brenner 梯度函数
def brenner(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    shape = np.shape(img)
    out = 0
    for x in range(0, shape[0]-2):
        for y in range(0, shape[1]):
            out+=(int(img[x+2,y])-int(img[x,y]))**2
    return out
# Laplacian梯度函数
def Laplacian(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    return cv2.Laplacian(img,cv2.CV_64F).var()
# SMD（灰度方差）
def SMD(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    shape = np.shape(img)
    out = 0
    for x in range(1, shape[0]-1):
        for y in range(0, shape[1]):
            out+=math.fabs(int(img[x,y])-int(img[x,y-1]))
            out+=math.fabs(int(img[x,y]-int(img[x+1,y])))
    return out
# SMD2（灰度方差乘积）
def SMD2(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    shape = np.shape(img)
    out = 0
    for x in range(0, shape[0]-1):
        for y in range(0, shape[1]-1):
            out+=math.fabs(int(img[x,y])-int(img[x+1,y]))*math.fabs(int(img[x,y]-int(img[x,y+1])))
    return out
# 方差函数
def variance(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    out = 0
    u = np.mean(img)
    shape = np.shape(img)
    for x in range(0,shape[0]):
        for y in range(0,shape[1]):
            out+=(img[x,y]-u)**2
    return out
# 能量梯度函数
def energy(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    shape = np.shape(img)
    out = 0
    for x in range(0, shape[0]-1):
        for y in range(0, shape[1]-1):
            out+=((int(img[x+1,y])-int(img[x,y]))**2)*((int(img[x,y+1]-int(img[x,y])))**2)
    return out
# Vollath函数
def Vollath(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    shape = np.shape(img)
    u = np.mean(img)
    out = -shape[0]*shape[1]*(u**2)
    for x in range(0, shape[0]-1):
        for y in range(0, shape[1]):
            out+=int(img[x,y])*int(img[x+1,y])
    return out
# 熵函数
def entropy(img):
    '''
    :param img:narray 二维灰度图像
    :return: float 图像越清晰越大
    '''
    out = 0
    count = np.shape(img)[0]*np.shape(img)[1]
    p = np.bincount(np.array(img).flatten())
    for i in range(0, len(p)):
        if p[i]!=0:
            out-=p[i]*math.log(p[i]/count)/count
    return out

def main(img1, img2):
    print('Brenner',brenner(img1),brenner(img2))
    print('Laplacian',Laplacian(img1),Laplacian(img2))
    print('SMD',SMD(img1), SMD(img2))
    print('SMD2',SMD2(img1), SMD2(img2))
    print('Variance',variance(img1),variance(img2))
    print('Energy',energy(img1),energy(img2))
    print('Vollath',Vollath(img1),Vollath(img2))
    print('Entropy',entropy(img1),entropy(img2))

if __name__ == '__main__':
    #读入原始图像
    img1 = cv2.imread('1.png')
    img2 = cv2.imread('2.png')
    #灰度化处理
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    main(img1,img2)