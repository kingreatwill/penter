def tf1():
    import tensorflow.compat.v1 as tf
    tf.disable_v2_behavior()  # 使用静态图模式运行以下代码
    assert tf.__version__.startswith('2.')

    # 1.创建计算图阶段
    # 创建2个输入端子，指定类型和名字
    a_ph = tf.placeholder(tf.float32, name='variable_a')
    b_ph = tf.placeholder(tf.float32, name='variable_b')
    # 创建输出端子的运算操作，并命名
    c_op = tf.add(a_ph, b_ph, name='variable_c')

    # 2.运行计算图阶段
    # 创建运行环境
    sess = tf.InteractiveSession()
    # 初始化操作也需要作为操作运行
    init = tf.global_variables_initializer()
    sess.run(init)  # 运行初始化操作，完成初始化
    # 运行输出端子，需要给输入端子赋值
    c_numpy = sess.run(c_op, feed_dict={a_ph: 2., b_ph: 4.})
    # 运算完输出端子才能得到数值类型的c_numpy
    print('a+b=', c_numpy)


def tf2():
    import tensorflow as tf
    assert tf.__version__.startswith('2.')

    # 1.创建输入张量
    a = tf.constant(2.)
    b = tf.constant(4.)

    # 2.直接计算并打印
    print('a+b=', tf.add(a, b).numpy())
    print('a+b=', a + b)
    print('a+b=', (a + b).numpy())


if __name__ == "__main__":
    tf2()
    tf1()
