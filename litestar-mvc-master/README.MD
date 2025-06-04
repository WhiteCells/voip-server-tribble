# litestar MVC 项目

### 环境

```sh
# 虚拟环境
conda create litestar-mcv-env_311 python=3.11

# 安装依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 运行

复制 `.env.example` 改名为 `.env`，修改配置。

```bash
python run.py
```

### 数据库表迁移

数据库表迁移

```sh
alembic revision --autogenerate -m "comment"
alembic upgrade head
```