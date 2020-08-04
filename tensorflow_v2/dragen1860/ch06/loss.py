import tensorflow as tf

y = tf.constant([1, 2, 3, 0, 2])
y = tf.one_hot(y, depth=4)
y = tf.cast(y, dtype=tf.float32)

out = tf.random.normal([5, 4])

# MSE loss
loss1 = tf.reduce_mean(tf.square(y - out))
loss2 = tf.square(tf.norm(y - out)) / (5 * 4)
loss3 = tf.reduce_mean(tf.losses.MSE(y, out))

print(loss1)
print(loss2)
print(loss3)


# 多类损失函数categorical_crossentropy  分类_交叉熵  loss    第一个参数是label  第二个参数是概率（ 如果不是概率，或者没有经过softmax，那么 需要增加参数，from_logits = True）
print(tf.losses.categorical_crossentropy([0, 1, 0, 0], [0.25, 0.25, 0.25, 0.25]))
print(tf.losses.categorical_crossentropy([0, 1, 0, 0], [0.1, 0.1, 0.7, 0.1]))
print(tf.losses.categorical_crossentropy([0, 1, 0, 0], [0.1, 0.7, 0.1, 0.1]))
print(tf.losses.categorical_crossentropy([0, 1, 0, 0], [0.01, 0.97, 0.01, 0.01]))
"""
tf.Tensor(1.3862944, shape=(), dtype=float32)
tf.Tensor(2.3025851, shape=(), dtype=float32)
tf.Tensor(0.35667497, shape=(), dtype=float32)
tf.Tensor(0.030459179, shape=(), dtype=float32)  
准确率越高越小
"""

# 二分类_交叉熵 loss
print(tf.losses.binary_crossentropy([1], [0.25]))


