安装依赖
运行 pip install -r requirements.txt 安装项目所需依赖

数据库迁移
1.运行 python db_manage.py db init 建立迁移文件
2.运行 python db_manage.py db migrate -m "inition migration" 在目标数据库中建立相应表
运行python db_manage.py db upgrade 更新在目标数据库中相应的表结构

celery
celery -A flask_app.task worker --loglevel=info