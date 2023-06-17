import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 解决下载资源报错：https://www.jianshu.com/p/7cd22c91d2fe
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# df_housing = pd.read_csv("https://raw.githubusercontent.com/huangjia2019/house/master/house.csv")
df_housing = pd.read_csv("./house.csv")  # 本地调试使用本地文件
df_housing.head
X = df_housing.drop("median_house_value", axis=1)
y = df_housing.median_house_value

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print('房价的真值（测试集）', y_test)
print('预测的房价（测试集）', y_pred)

print("给预测评分：", model.score(X_test, y_test))

plt.scatter(X_test.median_income, y_test, color="brown")
plt.plot(X_test.median_income, y_pred, color="green", linewidth=1)
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.show()
