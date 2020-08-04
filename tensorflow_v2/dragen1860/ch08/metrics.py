import tensorflow as tf
from tensorflow.keras import datasets, layers, optimizers, Sequential, metrics


def preprocess(x, y):
    x = tf.cast(x, dtype=tf.float32) / 255.
    y = tf.cast(y, dtype=tf.int32)

    return x, y


batchsz = 128
(x, y), (x_val, y_val) = datasets.mnist.load_data()
print('datasets:', x.shape, y.shape, x.min(), x.max())

db = tf.data.Dataset.from_tensor_slices((x, y))
db = db.map(preprocess).shuffle(60000).batch(batchsz).repeat(10)

ds_val = tf.data.Dataset.from_tensor_slices((x_val, y_val))
ds_val = ds_val.map(preprocess).batch(batchsz)

network = Sequential([layers.Dense(256, activation='relu'),
                      layers.Dense(128, activation='relu'),
                      layers.Dense(64, activation='relu'),
                      layers.Dense(32, activation='relu'),
                      layers.Dense(10)])
network.build(input_shape=(None, 28 * 28))
network.summary()

optimizer = optimizers.Adam(lr=0.01)

# 1. 实例
acc_meter = metrics.Accuracy()
loss_meter = metrics.Mean()
"""
https://www.cnblogs.com/xiximayou/p/12689915.html
一，常用的内置评估指标
MeanSquaredError（平方差误差，用于回归，可以简写为MSE，函数形式为mse）
MeanAbsoluteError (绝对值误差，用于回归，可以简写为MAE，函数形式为mae)
MeanAbsolutePercentageError (平均百分比误差，用于回归，可以简写为MAPE，函数形式为mape)
RootMeanSquaredError (均方根误差，用于回归)
Accuracy (准确率，用于分类，可以用字符串"Accuracy"表示，Accuracy=(TP+TN)/(TP+TN+FP+FN)，要求y_true和y_pred都为类别序号编码)
Precision (精确率，用于二分类，Precision = TP/(TP+FP))
Recall (召回率，用于二分类，Recall = TP/(TP+FN))
TruePositives (真正例，用于二分类)
TrueNegatives (真负例，用于二分类)
FalsePositives (假正例，用于二分类)
FalseNegatives (假负例，用于二分类)
AUC(ROC曲线(TPR vs FPR)下的面积，用于二分类，直观解释为随机抽取一个正样本和一个负样本，正样本的预测值大于负样本的概率)
CategoricalAccuracy（分类准确率，与Accuracy含义相同，要求y_true(label)为onehot编码形式）
SparseCategoricalAccuracy (稀疏分类准确率，与Accuracy含义相同，要求y_true(label)为序号编码形式)
MeanIoU (Intersection-Over-Union，常用于图像分割)
TopKCategoricalAccuracy (多分类TopK准确率，要求y_true(label)为onehot编码形式)
SparseTopKCategoricalAccuracy (稀疏多分类TopK准确率，要求y_true(label)为序号编码形式)
Mean (平均值)
Sum (求和)
"""

for step, (x, y) in enumerate(db):

    with tf.GradientTape() as tape:
        # [b, 28, 28] => [b, 784]
        x = tf.reshape(x, (-1, 28 * 28))
        # [b, 784] => [b, 10]
        out = network(x)
        # [b] => [b, 10]
        y_onehot = tf.one_hot(y, depth=10)
        # [b]
        loss = tf.reduce_mean(tf.losses.categorical_crossentropy(y_onehot, out, from_logits=True))
        # 2. 更新数值
        loss_meter.update_state(loss)

    grads = tape.gradient(loss, network.trainable_variables)
    optimizer.apply_gradients(zip(grads, network.trainable_variables))

    if step % 100 == 0:
        # 3. 显示数值
        print(step, 'loss:', loss_meter.result().numpy())
        # 4. 清空
        loss_meter.reset_states()

    # evaluate
    if step % 500 == 0:
        total, total_correct = 0., 0
        acc_meter.reset_states()

        for step, (x, y) in enumerate(ds_val):
            # [b, 28, 28] => [b, 784]
            x = tf.reshape(x, (-1, 28 * 28))
            # [b, 784] => [b, 10]
            out = network(x)

            # [b, 10] => [b] 
            pred = tf.argmax(out, axis=1)
            pred = tf.cast(pred, dtype=tf.int32)
            # bool type 
            correct = tf.equal(pred, y)
            # bool tensor => int tensor => numpy
            total_correct += tf.reduce_sum(tf.cast(correct, dtype=tf.int32)).numpy()
            total += x.shape[0]

            acc_meter.update_state(y, pred)

        print(step, 'Evaluate Acc:', total_correct / total, acc_meter.result().numpy())
