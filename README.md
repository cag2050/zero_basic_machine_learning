


### 使用 virtualenv/venv 和 pip 管理虚拟环境：
1. 进入项目的根目录，创建虚拟环境：`virtualenv --python=python3 venv`或`python3 -m venv ./venv`（venv不用安装，不过需要python3.3以上）
2. 进入虚拟环境：`source venv/bin/activate`
3. 安装依赖：`pip install -r requirements.txt`
4. 安装新包后，执行这个命令将包名和包版本信息写入 requirements.txt：`pip freeze > requirements.txt`