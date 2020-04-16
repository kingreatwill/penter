import tensorflow as tf

# Define tensor constants.
a = tf.constant(2)
b = tf.constant(3)
c = tf.constant(5)

# Various tensor operations.
# Note: Tensors also support python operators (+, *, ...)
add = tf.add(a, b)
sub = tf.subtract(a, b)
mul = tf.multiply(a, b)
div = tf.divide(a, b)

# Access tensors value.
print("add =", add.numpy())
print("sub =", sub.numpy())
print("mul =", mul.numpy())
print("div =", div.numpy())

# Some more operations.
# 减少 平均值
mean = tf.reduce_mean([a, b, c])
# 减少 求和
sum = tf.reduce_sum([a, b, c])

# Access tensors value.
print("mean =", mean.numpy())
print("sum =", sum.numpy())

# Matrix multiplications.
matrix1 = tf.constant([[1., 2.], [3., 4.]])
matrix2 = tf.constant([[5., 6.], [7., 8.]])

product = tf.matmul(matrix1, matrix2) #矩阵相乘



# Convert Tensor to Numpy.
print( product.numpy())