# 中国福利彩票

from bs4 import BeautifulSoup  as bs
import requests
import os
import pandas as pd


# 遗漏分析
# 冷热分析
# 预测分析
# 号码走势

# 爬取数据
def Crawling_data(lottery="dlt"):
    """
    # url = "http://datachart.500.com/dlt/history/newinc/history.php?start=00001&end=99999"
    # 大乐透 http://datachart.500.com/dlt/history/history.shtml
    # 大乐透：第一列期号 第二到第六列 5个前区号码  第七到第八列 2个后区号码  最后一列（15）开奖日期
    <tr class="t_tr1"><td class="t_tr1">20058</td><td class="cfont2">01</td><td class="cfont2">15</td><td class="cfont2">19</td><td class="cfont2">26</td><td class="cfont2">27</td><td class="cfont4">05</td><td class="cfont4">10</td><td class="t_tr1">801,073,309</td><td class="t_tr1">5</td><td class="t_tr1">9,421,778</td><td class="t_tr1">137</td><td class="t_tr1">80,612</td><td class="t_tr1">311,403,757</td><td class="t_tr1">2020-07-04</td></tr>


    # url = "http://datachart.500.com/ssq/history/newinc/history.php?start=00001&end=99999"
    # 双色球 http://datachart.500.com/ssq/history/history.shtml
    # 双色球：第一列期号 第二到第七列 6个红球号码  第八列蓝球号码  最后一列（16）开奖日期
    <tr class="t_tr1"><td>20059</td><td class="t_cfont2">02</td><td class="t_cfont2">04</td><td class="t_cfont2">10</td><td class="t_cfont2">17</td><td class="t_cfont2">22</td><td class="t_cfont2">25</td><td class="t_cfont4">14</td><td class="t_cfont4">&nbsp;</td><td>1,002,178,704</td><td>4</td><td>10,000,000</td><td>190</td><td>147,308</td><td>386,807,160</td><td>2020-07-05</td></tr>
    """
    remove = -1
    url = "http://datachart.500.com/dlt/history/newinc/history.php?start=00001&end=99999"
    if lottery == "ssq":
        url = "http://datachart.500.com/ssq/history/newinc/history.php?start=00001&end=99999"
        remove = 8  # 移除 快乐星期天 的那一列

    data = requests.get(url).text
    data = bs(data, 'lxml')

    data = data.find("tbody", id="tdata").find_all('tr', **{"class": "t_tr1"})

    lo_data = []
    for content in data:
        row = []
        tds = content.find_all('td')
        for i in range(0, len(tds)):
            if i != remove:
                row.append(tds[i].get_text())
        lo_data.append(row)

    return pd.DataFrame(lo_data)


# python 交互环境有效
"""
解决办法:
恢复python的默认绘图figure窗口

如图:
点击File–>Settings–>Python Scientific, 然后将Show plots in tool window前面的勾勾去掉即可.
"""


def drow3d():
    import numpy as np
    import pandas as pd
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    dlt_df = pd.read_csv("大乐透.csv")

    fig = plt.figure(figsize=(10, 10))
    ax = fig.gca(projection='3d')
    a = np.random.randint(0, 5, size=100)
    for i in range(1, 8):
        z = dlt_df["num" + str(i)][:100]  # 前100
        y = np.full_like(a, i)
        x = range(100)  # 100
        ax.plot(x, y, z)
    ax.legend()
    # ax.set_xlim=[0,8]
    plt.tight_layout()
    # plt.savefig('img_3d.png')
    plt.show()


def dnn():
    import numpy as np
    import pandas as pd
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    dlt_df = pd.read_csv("大乐透.csv")
    data = dlt_df.values
    data = data[1:, 2:9]
    data = data.astype(np.float64)

    # 使用神经网络预测
    mean = data[:1500].mean(axis=0)
    std = data[:1500].std(axis=0)
    data1 = data.copy()
    data1 -= mean
    data1 /= std
    train_data = data1[:1400]
    train_data = np.expand_dims(train_data, axis=1)
    val_data = data1[1400:1550]
    val_data = np.expand_dims(val_data, axis=1)
    test_data = data1[1550:len(data) - 1]
    test_data = np.expand_dims(test_data, axis=1)
    red1_labels = data[:, 0]
    red2_labels = data[:, 1]
    red3_labels = data[:, 2]
    red4_labels = data[:, 3]
    red5_labels = data[:, 4]
    blue1_labels = data[:, 5]
    blue2_labels = data[:, 6]
    train_labels_1 = red1_labels[1:1401]
    train_labels_2 = red2_labels[1:1401]
    train_labels_3 = red3_labels[1:1401]
    train_labels_4 = red4_labels[1:1401]
    train_labels_5 = red5_labels[1:1401]
    train_labels_6 = blue1_labels[1:1401]
    train_labels_7 = blue2_labels[1:1401]
    val_labels_1 = red1_labels[1401:1551]
    val_labels_2 = red2_labels[1401:1551]
    val_labels_3 = red3_labels[1401:1551]
    val_labels_4 = red4_labels[1401:1551]
    val_labels_5 = red5_labels[1401:1551]
    val_labels_6 = blue1_labels[1401:1551]
    val_labels_7 = blue2_labels[1401:1551]
    test_labels_1 = red1_labels[1551:]
    test_labels_2 = red2_labels[1551:]
    test_labels_3 = red3_labels[1551:]
    test_labels_4 = red4_labels[1551:]
    test_labels_5 = red5_labels[1551:]
    test_labels_6 = blue1_labels[1551:]
    test_labels_7 = blue2_labels[1551:]

    from keras import layers
    from keras import Model
    from keras import Input
    from keras.optimizers import RMSprop

    post_input = Input(shape=(None, 7), name='post_input')
    lstm = layers.LSTM(150, dropout=0.2, recurrent_dropout=0.2, activation='relu', return_sequences=True)(post_input)
    lstm1 = layers.LSTM(250, dropout=0.2, recurrent_dropout=0.2, activation='relu')(lstm)
    x = layers.Dense(360, activation='relu')(lstm1)
    x = layers.Dense(250, activation='relu')(x)
    x = layers.Dense(250, activation='relu')(x)
    x = layers.Dense(250, activation='relu')(x)
    x = layers.Dense(250, activation='relu')(x)
    x = layers.Dense(250, activation='relu')(x)
    x = layers.Dense(140, activation='relu')(x)
    x = layers.Dense(70, activation='relu')(x)
    # x=layers.Dropout(0.3)(x)
    red1_predict = layers.Dense(1, name='red1')(x)
    red2_predict = layers.Dense(1, name='red2')(x)
    red3_predict = layers.Dense(1, name='red3')(x)
    red4_predict = layers.Dense(1, name='red4')(x)
    red5_predict = layers.Dense(1, name='red5')(x)
    blue1_predict = layers.Dense(1, name='blue1')(x)
    blue2_predict = layers.Dense(1, name='blue2')(x)
    model = Model(post_input,
                  [red1_predict, red2_predict, red3_predict, red4_predict, red5_predict, blue1_predict, blue2_predict])
    model.compile(optimizer=RMSprop(1e-4), loss=['mse', 'mse', 'mse', 'mse', 'mse', 'mse', 'mse'],
                  metrics=['acc', 'acc', 'acc', 'acc', 'acc', 'acc', 'acc'])

    history = model.fit(train_data,
                        [train_labels_1, train_labels_2, train_labels_3, train_labels_4, train_labels_5, train_labels_6,
                         train_labels_7],
                        batch_size=20, epochs=50,
                        validation_data=(val_data,
                                         [val_labels_1, val_labels_2, val_labels_3, val_labels_4, val_labels_5,
                                          val_labels_6, val_labels_7]))

    loss = history.history['loss']
    loss = loss[3:]
    val_loss = history.history['val_loss']
    val_loss = val_loss[3:]
    epochs = range(1, len(loss) + 1)
    plt.figure()
    plt.plot(epochs, loss, 'b', color='r', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.show()  # 损失图像
    # Keras如何保存和载入训练好的模型和参数:https://blog.csdn.net/qq_36142114/article/details/86929132
    model.save(filepath="dlt_model.h5", include_optimizer=False)

    # # 预测
    # predict_data = data1[1401]
    # print(data[1402])
    # predict_data = predict_data.reshape(1, 1, 7)
    # predict = model.predict(predict_data)
    # print(predict)


def predict():
    import keras
    import numpy as np
    model = keras.models.load_model("dlt_model.h5")
    print(model.predict(np.asarray([1, 15, 22, 28, 32, 3, 11]).reshape(1, 1, 7)))
    """
    载入模型:
    my_model = keras . models . load_model( filepath )    
    载入后可以继续训练：    
    my_model . fit( X_train_2，Y_train_2 )    
    也可以直接评估：    
    preds = my_model . evaluate( X_test, Y_test )    
    print ( "Loss = " + str( preds[0] ) )    
    print ( "Test Accuracy = " + str( preds[1] ) )
    """

"""
# Keras中Lstm方法进行时间序列预测 https://github.com/CasiaFan/time_seires_prediction_using_lstm/blob/master/neural_network_run.py
# 格式
#('2016-05-03', '09,12,24,28,29,30,02')

#('2016-05-01', '06,08,13,14,22,27,10')

#('2016-04-28', '03,08,13,14,15,30,04')
"""
if __name__ == '__main__':
    predict()
    # dnn()
# df =  Crawling_data("dlt")
# df.to_csv("dlt_data.csv")
