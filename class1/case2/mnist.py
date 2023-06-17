from keras.datasets import mnist
from keras.utils import to_categorical
from keras import models  # 导入Keras模型, 和各种神经网络的层
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
import matplotlib.pyplot as plt  # 导入绘图工具包

# 解决下载资源报错：https://www.jianshu.com/p/7cd22c91d2fe
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data
(X_train_image, y_train_label), (X_test_image, y_test_label) = mnist.load_data()
print("特征集张量形状：", X_train_image.shape)  # 用shape方法显示张量的形状
print("第一个数据样本：\n", X_train_image[0])
print("第一个数据样本的标签：", y_train_label[0])

X_train = X_train_image.reshape(60000, 28, 28, 1)  # 给标签增加一个维度
X_test = X_test_image.reshape(10000, 28, 28, 1)  # 给标签增加一个维度
y_train = to_categorical(y_train_label, 10)  # 特征转换为one-hot编码
y_test = to_categorical(y_test_label, 10)  # 特征转换为one-hot编码
print("数据集张量形状：", X_train.shape)  # 特征集张量的形状
print("第一个数据标签：", y_train[0])  # 显示标签集的第一个数据

model = models.Sequential()  # 用序贯方式建立模型
model.add(Conv2D(32, (3, 3), activation='relu',  # 添加Conv2D层
                 input_shape=(28, 28, 1)))  # 指定输入数据样本张量的类型
model.add(MaxPooling2D(pool_size=(2, 2)))  # 添加MaxPooling2D层
model.add(Conv2D(64, (3, 3), activation='relu'))  # 添加Conv2D层
model.add(MaxPooling2D(pool_size=(2, 2)))  # 添加MaxPooling2D层
model.add(Dropout(0.25))  # 添加Dropout层
model.add(Flatten())  # 展平
model.add(Dense(128, activation='relu'))  # 添加全连接层
model.add(Dropout(0.5))  # 添加Dropout层
model.add(Dense(10, activation='softmax'))  # Softmax分类激活，输出10维分类码
# 编译模型
model.compile(optimizer='rmsprop',  # 指定优化器
              loss='categorical_crossentropy',  # 指定损失函数
              metrics=['accuracy'])  # 指定验证过程中的评估指标

model.fit(X_train, y_train,  # 指定训练特征集和训练标签集
          validation_split=0.3,  # 部分训练集数据拆分成验证集
          epochs=5,  # 训练轮次为5轮
          batch_size=128)  # 以128为批量进行训练

score = model.evaluate(X_test, y_test)  # 在测试集上进行模型评估
print('测试集预测准确率:', score[1])  # 打印测试集上的预测准确率

pred = model.predict(X_test[0].reshape(1, 28, 28, 1))  # 预测测试集第一个数据
print(pred[0], "转换一下格式得到：", pred.argmax())  # 把one-hot码转换为数字

plt.imshow(X_test[0].reshape(28, 28), cmap='Greys')  # 输出这个图片
