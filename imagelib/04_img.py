import os
from PIL import Image
from PIL import ImageEnhance

def ImageAugument():
     path = r'D:\demo'
     files = os.listdir(path)
     prefix = path + '/'
     for file in files:
           image = Image.open(prefix + file)
           # image.show()
           #亮度增强
           enh_bri = ImageEnhance.Brightness(image)
           brightness = 1.5
           image_brightened = enh_bri.enhance(brightness)
           image_brightened.save(prefix + file[0:6] + 'lightup' + '.jpg')
           #色度增强
           enh_col = ImageEnhance.Color(image)
           color = 1.5
           image_colored = enh_col.enhance(color)
           image_colored.save(prefix + file[0:6] + 'colorup' + '.jpg')
           #对比度增强
           enh_con = ImageEnhance.Contrast(image)
           contrast = 1.3
           image_contrasted = enh_con.enhance(contrast)
           image_contrasted.save(prefix + file[0:6] + 'contrastup' + '.jpg')
           #锐度增强
           enh_sha = ImageEnhance.Sharpness(image)
           sharpness = 2.8
           image_sharped = enh_sha.enhance(sharpness)
           image_sharped.save(prefix + file[0:6] + 'moreSharp' + '.jpg')

# 1、祛痘
def demo01():
    import cv2
    level = 5  # 降噪等级
    img = cv2.imread('D:/demo/study.moreSharp.jpg')  # 读取原图
    img = cv2.bilateralFilter(img, level, level * 2, level / 2)  # 美颜
    cv2.imwrite('D:/demo/study.result.jpg', img)


def demo2():
    import os
    from PIL import Image
    from PIL import ImageEnhance

    """
    1、对比度：白色画面(最亮时)下的亮度除以黑色画面(最暗时)下的亮度；
    2、色彩饱和度：：彩度除以明度，指色彩的鲜艳程度，也称色彩的纯度；
    3、色调：向负方向调节会显现红色，正方向调节则增加黄色。适合对肤色对象进行微调；
    4、锐度：是反映图像平面清晰度和图像边缘锐利程度的一个指标。
    """

    def augument(image_path, parent):
        # 读取图片
        image = Image.open(image_path)

        image_name = os.path.split(image_path)[1]
        name = os.path.splitext(image_name)[0]

        # 变亮
        # 亮度增强,增强因子为0.0将产生黑色图像；为1.0将保持原始图像。
        enh_bri = ImageEnhance.Brightness(image)
        brightness = 1.5
        image_brightened1 = enh_bri.enhance(brightness)
        image_brightened1.save(os.path.join(parent, '{}_bri1.jpg'.format(name)))

        # 变暗
        enh_bri = ImageEnhance.Brightness(image)
        brightness = 0.8
        image_brightened2 = enh_bri.enhance(brightness)
        image_brightened2.save(os.path.join(parent, '{}_bri2.jpg'.format(name)))

        # 色度,增强因子为1.0是原始图像
        # 色度增强
        enh_col = ImageEnhance.Color(image)
        color = 1.5
        image_colored1 = enh_col.enhance(color)
        image_colored1.save(os.path.join(parent, '{}_col1.jpg'.format(name)))

        # 色度减弱
        enh_col = ImageEnhance.Color(image)
        color = 0.8
        image_colored1 = enh_col.enhance(color)
        image_colored1.save(os.path.join(parent, '{}_col2.jpg'.format(name)))

        # 对比度，增强因子为1.0是原始图片
        # 对比度增强
        enh_con = ImageEnhance.Contrast(image)
        contrast = 1.5
        image_contrasted1 = enh_con.enhance(contrast)
        image_contrasted1.save(os.path.join(parent, '{}_con1.jpg'.format(name)))

        # 对比度减弱
        enh_con = ImageEnhance.Contrast(image)
        contrast = 0.8
        image_contrasted2 = enh_con.enhance(contrast)
        image_contrasted2.save(os.path.join(parent, '{}_con2.jpg'.format(name)))

        # 锐度，增强因子为1.0是原始图片
        # 锐度增强
        enh_sha = ImageEnhance.Sharpness(image)
        sharpness = 3.0
        image_sharped1 = enh_sha.enhance(sharpness)
        image_sharped1.save(os.path.join(parent, '{}_sha1.jpg'.format(name)))

        # 锐度减弱
        enh_sha = ImageEnhance.Sharpness(image)
        sharpness = 0.8
        image_sharped2 = enh_sha.enhance(sharpness)
        image_sharped2.save(os.path.join(parent, '{}_sha2.jpg'.format(name)))

    dir = 'E:/4/'
    for parent, dirnames, filenames in os.walk(dir):
        for filename in filenames:
            fullpath = os.path.join(parent + '/', filename)
            if 'jpg' in fullpath:
                print(fullpath, parent)
                augument(fullpath, parent)


if __name__ == '__main__':
     ImageAugument()
     #demo01()