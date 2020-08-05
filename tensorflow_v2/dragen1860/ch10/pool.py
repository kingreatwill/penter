from tensorflow.keras import layers

"""
缩小图像（或称为下采样（subsampled）或降采样（downsampled））的主要目的有两个：1、使得图像符合显示区域的大小；2、生成对应图像的缩略图。

放大图像（或称为上采样（upsampling）或图像插值（interpolating））的主要目的是放大原图像,从而可以显示在更高分辨率的显示设备上。
对图像的缩放操作并不能带来更多关于该图像的信息, 因此图像的质量将不可避免地受到影响。然而，确实有一些缩放方法能够增加图像的信息，从而使得缩放后的图像质量超过原图质量的。

常用的插值方法 
1、最邻近元法 interpolation='nearest'
    这是最简单的一种插值方法，不需要计算，在待求象素的四邻象素中，将距离待求象素最近的邻象素灰度赋给待求象素。
    最邻近元法计算量较小，但可能会造成插值生成的图像灰度上的不连续，在灰度变化的地方可能出现明显的锯齿状。
2、双线性内插法 interpolation='bilinear'
    双线性内插法是利用待求象素四个邻象素的灰度在两个方向上作线性内插
    双线性内插法的计算比最邻近点法复杂，计算量较大，但没有灰度不连续的缺点，结果基本令人满意。它具有低通滤波性质，使高频分量受损，图像轮廓可能会有一点模糊。

插值方法总结：
“Inverse Distance to a Power（反距离加权插值法）”、
“Kriging（克里金插值法）”、
“Minimum Curvature（最小曲率)”、
“Modified Shepard's Method（改进谢别德法）”、
“Natural Neighbor（自然邻点插值法）”、
“Nearest Neighbor（最近邻点插值法）”、
“Polynomial Regression（多元回归法）”、
“Radial Basis Function（径向基函数法）”、
“Triangulation with Linear Interpolation（线性插值三角网法）”、
“Moving Average（移动平均法）”、
“Local Polynomial（局部多项式法）”
"""

layers.UpSampling2D(size=(2, 2))  # 放大两倍
layers.MaxPool2D(pool_size=[2, 2], strides=2, padding="same"),  # 下采样 - > 池化层->降维
