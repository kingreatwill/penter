import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, optimizers, datasets

# 返回60k训练数据集和10k测试集
(x, y), (x_test, y_test) = datasets.mnist.load_data()
# x (60000, 28, 28)   y是label：(60000,)
print("Datasets Shape :", x.shape, y.shape)

# 数据集打乱
# idx = tf.range(len(x))
# tf.random.shuffle(idx)
# x = tf.gather(x,idx)
# y = tf.gather(y, idx)


x = tf.convert_to_tensor(x, dtype=tf.float32) / 255.
y = tf.convert_to_tensor(y, dtype=tf.int32)
y = tf.one_hot(y, depth=10)
print("Datasets Y one_hot Shape :", x.shape, y.shape)

# 创建数据集
train_dataset = tf.data.Dataset.from_tensor_slices((x, y))
# 每次200
train_dataset = train_dataset.batch(200)

# tensorflow_v2\mnist_cnn\train.py
# tensorflow_v2\dragen1860\ch04\4.10-forward-prop.py
# dense ：全连接层  相当于添加一个层
model = keras.Sequential([
    layers.Dense(512, activation='relu', activity_regularizer="l2"),  # 512 输出维度
    layers.Dense(256, activation='relu', activity_regularizer="l2"),  # 256 输出维度
    layers.Dense(10)])  # 10 输出维度

# optimizer：优化器； learning_rate 学习速率(步长)
# SGD->Stochastic随机的 Gradient Descent 梯度下降
optimizer = optimizers.SGD(learning_rate=0.001, momentum=0.9)


# momentum 动力，

# 如何选择优化算法?
#
# 如果数据是稀疏的，就用自适用方法，即 Adagrad, Adadelta, RMSprop, Adam。
# RMSprop, Adadelta, Adam 在很多情况下的效果是相似的。
# Adam 就是在 RMSprop 的基础上加了 bias-correction 和 momentum，
# 随着梯度变的稀疏，Adam 比 RMSprop 效果会好。
# 整体来讲，Adam 是最好的选择。
# 很多论文里都会用 SGD，没有 momentum 等。SGD 虽然能达到极小值，但是比其它算法用的时间长，而且可能会被困在鞍点，这时就需要momentum参数了，一般0.9。

# 深度学习——优化器算法Optimizer详解（BGD、SGD、MBGD、Momentum、NAG、Adagrad、Adadelta、RMSprop、Adam）
# https://www.cnblogs.com/guoyaohua/p/8542554.html

def train_epoch(epoch):
    # Step4.loop （每次取200，上面有设置，会循环300次）
    for step, (x, y) in enumerate(train_dataset):

        with tf.GradientTape() as tape:
            # [b, 28, 28] => [b, 784] 打平(如果在model添加layers.Flatten(),下面的打平操作可以不要)
            x = tf.reshape(x, (-1, 28 * 28))
            # Step1. compute output
            # [b, 784] => [b, 10] ;x输入 经过 各种神经元，输出
            out = model(x)
            # Step2. compute loss；计算欧氏距离：reduce_sum 求和，square平方
            loss = tf.reduce_sum(tf.square(out - y)) / x.shape[0]
        # gradient 梯度，求导，对loss求导，model.trainable_variables：参数w和b
        # Step3. optimize and update w1, w2, w3, b1, b2, b3
        grads = tape.gradient(loss, model.trainable_variables)

        # 自动更新，反馈
        # w' = w - lr * grad
        optimizer.apply_gradients(zip(grads, model.trainable_variables))

        if step % 100 == 0:
            print(epoch, step, 'loss:', loss.numpy())


def train():
    # 训练30次
    for epoch in range(30):
        train_epoch(epoch)


def predict(image_path):
    from PIL import Image
    import numpy as np
    img = Image.open(image_path).convert('L')
    # img = img.resize((168, 168))
    # img = np.asarray(img)
    # print(img.shape)
    flatten_img = np.reshape(img, (28, 28, 1))
    x = np.array([1 - flatten_img])
    # 打平
    # x = tf.reshape(x, (-1, 28 * 28))
    x = np.reshape(x, (-1, 28 * 28))
    y = model.predict(x)
    print(y)
    print(np.argmax(y[0]))


if __name__ == '__main__':
    train()
    predict(r"E:\openjw\penter\tensorflow_v2\mnist_cnn\test_images\0.png")
    predict(r"E:\openjw\penter\tensorflow_v2\mnist_cnn\test_images\1.png")
    predict(r"E:\openjw\penter\tensorflow_v2\mnist_cnn\test_images\4.png")
