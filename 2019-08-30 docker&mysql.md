# 2019-08-30 docker&mysql


## 任务目标

通过本教程，培训人员可以基本掌握docker的基本使用命令，mysq的基本使用技能，docker-compose的基本配置命令。

最终培训通过标准：培训人员可以搭建一套 http://39.97.229.21/123456/home/shenhuagu 一样的环境。

## 登陆阿里云服务器

登陆阿里云服务器，下载文件以及解压缩文件。

登陆服务器命令

```
ssh -i  Traing.pem  root@ECS_IP_ADDRESS
```

提问：
- 什么是密钥
- chmod 400 是什么
- tar 
- tree -L 3

## MySQL 基础知识培训

主要掌握知识点：

* 创建数据库，表。
* 创建用户和设置用户权限。
* 备份 MySQL 数据库数据。
* Docker 的镜像，容器，端口映射，Dockerfile 的概念

自己的理解：

用 docker 来创建**镜像**，可以理解为复制，然后创建 mysql 数据库，可以不用安装很多依赖，更加简洁。镜像就是一个虚拟环境，可以用于打包本地数据库，类似于文件压缩打包工具。

mysql 是**关系型数据库**，通过在 docker 中创建 mysql 数据库的镜像，来完成数据库的初始化操作，以及后续操作。

常用 docker 命令：
- docker pull 用来创建镜像，如 docker pull mysql:5.7.27
- docker images 检查自己下载的镜像，用这个命令可以看到…… 可以看到
- docker ps 能看见自己创建的容器
- docker ps -a 查看容器的状态
- docker run -d  -e  MYSQL_ROOT_PASSWORD="Train-2019"  -p 3306:3306  --name training_mysql  mysql:5.7.27   创建容器
- docker exec -it 执行，-it 是交互，后面跟上容器和命令  进入容器
- docker rm +容器名  删除容器

常用 mysql 命令

- mysql -uroot -pTrain-2019  进入数据库
- create database db_training default character set utf8mb4 collate utf8mb4_unicode_ci;  创建数据库
- use 进入数据库


docker 命令，结尾打上 ; 
操作要进入相应的文件夹中

提问：

- 在创建镜像的时候，初始文件怎么设置？培训中，主要是使用已经配置好的，比如 /opt/projects/db
- 什么是端口
- Train-2019  是什么？可以创建容器，可以进入数据库？

## 相关术语

- ecs ip
- [2019-08-26 [培训][目标] mysq数据库和docker培训大纲 - Quip](https://memect.quip.com/VrPBAXOmsSIZ/2019-08-26-mysqdocker)


