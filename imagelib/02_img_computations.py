# 运算
def computation01():
    """
    Numpy 加法

    Numpy 的运算方法是： img = img1 + img2 ，然后再对最终的运算结果取模。
    当最终的像素值 <= 255 时，则运算结果直接为 img1 + img2 。
    当最终的像素值 > 255 时，则运算的结果需对 255 进行取模运算。

    OpenCV 加法

    OpenCV 的运算方式是直接调用 add() 函数进行的，这时的运算方式是饱和运算。
    当最终的像素值 <= 255 时，则运算结果直接为 img1 + img2 。
    当最终的像素值 > 255 时，这时则是饱和运算，结果固定为 255 。

    x = np.uint8([250])
    y = np.uint8([10])
    print( cv.add(x,y) ) # 250+10 = 260 => 255
    [[255]]
    print( x+y )          # 250+10 = 260 % 256 = 4
    [4]
    """
    import cv2
    # 读取图像 cv.IMREAD_UNCHANGED：加载图像，包括alpha通道
    img = cv2.imread('./img/lena.jpg', cv2.IMREAD_UNCHANGED)
    print(img.shape)
    test = img
    # Numpy 加法
    result1 = img + test
    # OpenCV 加法
    result2 = cv2.add(img, test)
    # 显示图像
    cv2.imshow("orig_img", img)
    cv2.imshow("Numpy + result1", result1)
    cv2.imshow("OpenCV add result2", result2)
    cv2.imshow("Numpy * result1", img * img)
    cv2.imshow("OpenCV multiply result2", cv2.multiply(img, img))
    # 等待显示
    cv2.waitKey()
    cv2.destroyAllWindows()

# 图像融合（Image Blending）
def mix01():
    # 图像融合： img = img1 * alpha + img2 * beta + gamma
    # 这里的 alpha 和 beta 都是系数，而 gamma 则是一个亮度调节量，不可省略。
    import cv2
    # 读取图像 cv.IMREAD_UNCHANGED：加载图像，包括alpha通道
    img1 = cv2.imread('./img/lena.jpg', cv2.IMREAD_UNCHANGED)
    img2 = cv2.imread('./img/bg.jpg', cv2.IMREAD_UNCHANGED)
    # 图像融合
    img = cv2.addWeighted(img1, 0.8, img2, 0.6, 10)
    # dst = cv.addWeighter(img1, alpha, img2, beta, gamma)
    # dst = img1 * alpha + img2 * beta + gamma

    # 显示图像
    # cv2.imshow("img1", img1)
    # cv2.imshow("img2", img2)
    cv2.imshow("addWeighter img", img)
    # 等待显示
    cv2.waitKey()
    cv2.destroyAllWindows()

# 位运算(添加logo)
def Bitwise01():
    import cv2 as cv
    # Load two images
    img1 = cv.imread('./img/lena.jpg')
    img2 = cv.imread('./img/logo.jpg')
    height, width = img2.shape[:2]
    img2 = cv.resize(img2, (int(width / 2), int(height / 2)), interpolation=cv.INTER_CUBIC)
    # I want to put logo on top-left corner, So I create a ROI
    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    # 二值化
    ret, mask = cv.threshold(img2gray, 20, 255, cv.THRESH_BINARY)
    cv.imshow('mask', mask)

    # 位操作 取反
    mask_inv = cv.bitwise_not(mask)
    cv.imshow('mask_inv', mask_inv)

    # Now black-out the area of logo in ROI
    img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
    cv.imshow('img1_bg', img1_bg)
    # Take only region of logo from logo image.
    img2_fg = cv.bitwise_and(img2, img2, mask=mask)
    cv.imshow('img2_fg', img2_fg)

    # Put logo in ROI and modify the main image
    dst = cv.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols] = dst
    cv.imshow('res', img1)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 性能衡量
def Performance01():
    import cv2 as cv
    # print(cv.useOptimized()) # 是否开启优化
    # cv.setUseOptimized(False)
    # print(cv.useOptimized())  # 是否开启优化
    img1 = cv.imread('./img/lena.jpg')
    e1 = cv.getTickCount()
    for i in range(5, 49, 2):
        img1 = cv.medianBlur(img1, i)
        # MedianBlur(中值滤波/百分比滤波器)
        # ksize:滤波模板的尺寸大小，必须是大于1的奇数，如3、5、7……
        cv.imshow('img1', img1)
        cv.waitKey(100)
    e2 = cv.getTickCount()
    t = (e2 - e1) / cv.getTickFrequency()
    print(t)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    #computation01()
    Performance01()

    import cv2
    flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    print(flags)
    # HSV 的色相范围为 [0,179] ，饱和度范围为 [0,255] ，值范围为 [0,255] 。不同的软件使用不同的范围。因此，如果需要将 OpenCV 值和它们比较，则需要将这些范围标准化。






