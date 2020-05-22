"""
准备数据集
首当其冲地就是数据集，这里提供一个很方便的工具imglab。
dlib官方源码中提供了这个工具，想要的可以去下载。
1. 在从github上下载的源码中，文件路径为：dlib/tools/imglab。
2. 这里我再提供一个下载链接，提取出了这个工具包供下载。http://download.csdn.net/download/hongbin_xu/10103900
（推荐到官网自行下载）
默认已经下载好了这个文件。
进入目录，输入以下指令：

mkdir build
cd build
cmake ..
cmake --build . --config Release
"""


"""
进入到当前准备的训练数据图片的目录下：

imglab -c cat.xml ./

cat.xml：这个是xml文件的名字，随便取一个就是了
./：这个是你的数据集的目录，我是直接在数据集文件夹中创建的，所以直接指定当前文件夹
之后文件夹中会生成两个文件：一个xml文件，一个xsl文件。

接下来，打开这个xml文件：
imglab cat.xml
随后会启动工具软件。

接下来一张一张图片打标签吧。
操作很简单，按下shift键后，鼠标左键拖动就会画出框；先松开左键，就会记录这个框，若先松开shift键，则不记录操作。

cat.xml 只是标记而已，接下来开始训练模型
"""
# 训练模型
def training_cat():
    import os
    import sys
    import glob
    import dlib
    import cv2

    # options用于设置训练的参数和模式
    options = dlib.simple_object_detector_training_options()
    # Since faces are left/right symmetric we can tell the trainer to train a
    # symmetric detector.  This helps it get the most value out of the training
    # data.
    options.add_left_right_image_flips = True
    # 支持向量机的C参数，通常默认取为5.自己适当更改参数以达到最好的效果
    options.C = 5
    # 线程数，你电脑有4核的话就填4
    options.num_threads = 4
    options.be_verbose = True

    # 获取路径
    current_path = os.getcwd()
    train_xml_path = r'E:\bigdata\ai\cat\cat.xml'
    print("training file path:" + train_xml_path)
    # print(train_xml_path)

    # 开始训练
    print("start training:")
    dlib.train_simple_object_detector(train_xml_path, r'E:\bigdata\ai\cat\detector.svm', options)

    print("---------")
    # 测试训练模型
    print("Training accuracy（准确性）: {}".format(
        dlib.test_simple_object_detector(train_xml_path, r'E:\bigdata\ai\cat\detector.svm')))
    # 测试非训练模型
    # print("Testing accuracy（准确性）: {}".format(
    #     dlib.test_simple_object_detector(r'E:\bigdata\ai\cat2\cat.xml', r'E:\bigdata\ai\cat\detector.svm')))

# training_cat()
# 可以看到准确率差不多100%

def demo1():
    import os
    import sys
    import dlib
    import cv2
    import glob

    detector = dlib.simple_object_detector(r'E:\bigdata\ai\cat\detector.svm')

    current_path = os.getcwd()
    test_folder = current_path + '/cats_test/'

    for f in [r"E:\openjw\penter\third\imagelib\dog1.png",r"E:\openjw\penter\third\imagelib\cat1.jpg"]: # glob.glob(test_folder + '*.jpg'):
        print("Processing file: {}".format(f))
        img = cv2.imread(f, cv2.IMREAD_COLOR)
        b, g, r = cv2.split(img)
        img2 = cv2.merge([r, g, b])
        dets = detector(img2)
        print("Number of faces detected: {}".format(len(dets)))
        for index, face in enumerate(dets):
            print('face {}; left {}; top {}; right {}; bottom {}'.format(index, face.left(), face.top(), face.right(),
                                                                         face.bottom()))

            left = face.left()
            top = face.top()
            right = face.right()
            bottom = face.bottom()
            cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 3)
            cv2.namedWindow(f, cv2.WINDOW_AUTOSIZE)
            cv2.imshow(f, img)

    k = cv2.waitKey(0)
    cv2.destroyAllWindows()

demo1()

