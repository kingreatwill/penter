# http://yann.lecun.com/exdb/mnist/
"""
可从此页面获得的MNIST手写数字数据库的训练集为60,000个示例，而测试集为10,000个示例。
它是NIST可提供的更大集合的子集。 这些数字已进行尺寸规格化，并在固定尺寸的图像中居中。

对于那些想在实际数据上尝试学习技术和模式识别方法而又花最少的精力进行预处理和格式化的人来说，这是一个很好的数据库。
"""
# TensorFlow——MNIST手写数据集

# Tensorflow 2.0 手写全连接MNIST数据集（理论+实战） https://blog.csdn.net/LQ_qing/article/details/99623008
# TensorFlow 2.0 (五) - mnist手写数字识别(CNN卷积神经网络)  https://geektutu.com/post/tensorflow2-mnist-cnn.html
# 大白话讲解卷积神经网络工作原理 视频 https://www.bilibili.com/video/av35087157/
# 大白话讲解卷积神经网络工作原理 https://zhuanlan.zhihu.com/p/49184702
# [3D模型可视化框架](https://tensorspace.org/html/playground/lenet.html)
# www.image-net.org
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets
import os

# 设置后台打印日志等级 避免后台打印一些无用的信息
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 利用Tensorflow2中的接口加载mnist数据集
(x, y), (x_test, y_test) = datasets.mnist.load_data()


# 对数据进行预处理 将图像的像素值都处理到[0,1]范围
def preprocess(x, y):
    x = tf.cast(x, dtype=tf.float32) / 255.
    y = tf.cast(y, dtype=tf.int32)
    return x, y


# 构建dataset对象，方便对数据的打乱，批处理等超操作
train_db = tf.data.Dataset.from_tensor_slices((x, y)).shuffle(1000).batch(128)
train_db = train_db.map(preprocess)
test_db = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(128)
test_db = test_db.map(preprocess)

# 构建模型中会用到的权重
w1 = tf.Variable(tf.random.truncated_normal([784, 256], stddev=0.1))
b1 = tf.Variable(tf.zeros([256]))
w2 = tf.Variable(tf.random.truncated_normal([256, 128], stddev=0.1))
b2 = tf.Variable(tf.zeros([128]))
w3 = tf.Variable(tf.random.truncated_normal([128, 10], stddev=0.1))
b3 = tf.Variable(tf.zeros([10]))

# 学习率
lr = 1e-3

# epoch表示整个训练集循环的次数 这里循环100次
for epoch in range(100):
    # step表示当前训练到了第几个Batch
    for step, (x, y) in enumerate(train_db):
        # 把训练集进行打平操作
        x = tf.reshape(x, [-1, 28 * 28])
        # 构建模型并计算梯度
        with tf.GradientTape() as tape:  # tf.Variable
            # 三层非线性模型搭建
            h1 = x @ w1 + tf.broadcast_to(b1, [x.shape[0], 256])
            h1 = tf.nn.relu(h1)
            h2 = h1 @ w2 + b2
            h2 = tf.nn.relu(h2)
            out = h2 @ w3 + b3

            # 把标签转化成one_hot编码
            y_onehot = tf.one_hot(y, depth=10)

            # 计算MSE
            loss = tf.square(y_onehot - out)
            loss = tf.reduce_mean(loss)

        # 计算梯度
        grads = tape.gradient(loss, [w1, b1, w2, b2, w3, b3])

        # w = w - lr * w_grad
        # 利用上述公式进行权重的更新
        w1.assign_sub(lr * grads[0])
        b1.assign_sub(lr * grads[1])
        w2.assign_sub(lr * grads[2])
        b2.assign_sub(lr * grads[3])
        w3.assign_sub(lr * grads[4])
        b3.assign_sub(lr * grads[5])

        # 每训练100个Batch 打印一下当前的loss
        if step % 100 == 0:
            print(epoch, step, 'loss:', float(loss))

    # 每训练完一次数据集 测试一下啊准确率
    total_correct, total_num = 0, 0
    for step, (x, y) in enumerate(test_db):
        x = tf.reshape(x, [-1, 28 * 28])

        h1 = tf.nn.relu(x @ w1 + b1)
        h2 = tf.nn.relu(h1 @ w2 + b2)
        out = h2 @ w3 + b3
        # 把输出值映射到[0~1]之间
        prob = tf.nn.softmax(out, axis=1)
        # 获取概率最大值得索引位置
        pred = tf.argmax(prob, axis=1)
        pred = tf.cast(pred, dtype=tf.int32)

        correct = tf.cast(tf.equal(pred, y), dtype=tf.int32)
        correct = tf.reduce_sum(correct)
        # 获取每一个batch中的正确率和batch大小
        total_correct += int(correct)
        total_num += x.shape[0]
    # 计算总的正确率
    acc = total_correct / total_num
    print('test acc:', acc)