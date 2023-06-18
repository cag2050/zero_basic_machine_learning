### 书籍《零基础学机器学习》的例子


### 使用 virtualenv/venv 和 pip 管理虚拟环境：
1. 进入项目的根目录，创建虚拟环境：`virtualenv --python=python3 venv`或`python3 -m venv ./venv`（venv不用安装，不过需要python3.3以上）
2. 进入虚拟环境：`source venv/bin/activate`
3. 安装依赖：`pip install -r requirements.txt`
4. 安装新包后，执行这个命令将包名和包版本信息写入 requirements.txt：`pip freeze > requirements.txt`
5. 使用`pip install <package_name>`安装不成功时，使用`pip3 install <package_name>`

### 相关资料

相关资料 | 说明
--- | ---
官方代码下载从【配套资源 】 | https://www.epubit.com/bookDetails?id=UB7245bf2ca7715
其它人整理的 | https://github.com/Vuean/Zero-Basic-Machine-Learning