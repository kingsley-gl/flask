
# 2018/1/8
  1.优化文件上传功能，文件缓存到临时文件夹，完成后删除文件
  2.添加日志雏形


# 2018/1/5
  1.重做文件上传功能
  2.添加本地缓存临时文件的文件夹
  3.添加mongodb文件储存线程
  4.新增数据库压力测试文件以及文件上传压力测试文件

安装依赖
运行 pip install -r requirements.txt 安装项目所需依赖

数据库迁移
1.运行 python db_manage.py db init 建立迁移文件
2.运行 python db_manage.py db migrate -m "inition migration" 在目标数据库中建立相应表
运行python db_manage.py db upgrade 更新在目标数据库中相应的表结构





开启celery服务
celery -A flask_app.tasks worker --loglevel=info -Q files,mega_task,web



框架架构示意图

![image](https://github.com/kingsley-gl/flask/tree/master/flask/architechture.png?raw=true)
