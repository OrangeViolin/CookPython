# 2019-09-09 SQL、MySQL and PostgreSQL


## 基本概念

SQL（Structured Query Language） 是结构化查询语言的缩写，用来访问和操作数据库系统。

NoSQL数据库，也就是非SQL的数据库，包括MongoDB、Cassandra、Dynamo等等，发展过程特别逗，现在的 NoSQL 是  SQL 的补充。

* 1970: NoSQL = We have no SQL
* 1980: NoSQL = Know SQL
* 2000: NoSQL = No SQL!
* 2005: NoSQL = Not only SQL
* 2013: NoSQL = No, SQL!

MySQL 是最流行的开源关系数据库。

### 关系型数据库

数据库是专门用来管理数据的软件，有了它，就不再需要考虑数据如何存储，只需调用数据库的接口即可写入和读写数据。

数据库按照数据模型来存储和管理数据。

**数据模型**：

- 层次模型：上下级关系
- 网状模型：互相联系
- 关系模型：关系模型把数据看作是一个二维表格，任何数据都可以通过行号+列号来唯一确定，它的数据模型看起来就是一个Excel表

关系模型是最普遍的。

表的每一行称为记录（Record），记录是一个逻辑意义上的数据。
表的每一列称为字段（Column），同一个表的每一行记录都拥有相同的若干字段。

字段定义了数据类型（整型、浮点型、字符串、日期等），以及是否允许为NULL。注意NULL表示字段数据不存在。一个整型字段如果为NULL不表示它的值为0，同样的，一个字符串型字段为NULL也不表示它的值为空串''。

和Excel表有所不同的是，关系数据库的表和表之间需要建立“一对多”，“多对一”和“一对一”的关系，这样才能够按照应用程序的逻辑来组织和存储数据。

其实 excel 表中的迭代计算有一些类似。

在关系数据库中，关系是通过**主键**和**外键**来维护的。

- 对于关系表，有个很重要的约束，就是任意两条记录不能重复。不能重复不是指两条记录不完全相同，而是指能够通过某个字段唯一区分出不同的记录，这个字段被称为**主键**。选取主键的一个基本原则是：不使用任何业务相关的字段作为主键。作为主键最好是完全业务无关的字段，我们一般把这个字段命名为id。
  - 自增整数类型：数据库会在插入数据时自动为每一条记录分配一个自增整数，这样我们就完全不用担心主键重复，也不用自己预先生成主键；
  - 全局唯一GUID类型：使用一种全局唯一的字符串作为主键，类似8f55d96b-8acc-4636-8cb8-76bf8abc2f57。**GUID算法**通过网卡MAC地址、时间戳和随机数保证任意计算机在任意时间生成的字符串都是不同的，大部分编程语言都内置了GUID算法，可以自己预算出主键。how to？

- 把数据与另一张表关联起来，这种列称为**外键**。
  - 定义外键
    `ALTER TABLE students
    ADD CONSTRAINT fk_class_id
    FOREIGN KEY (class_id)
    REFERENCES classes (id);`
    删除外键
    `ALTER TABLE students
    DROP FOREIGN KEY fk_class_id;`
  
  问题：怎么设定主键呢
  
  ref:[外键 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1177760294764384/1218728424164736)

### 数据类型

数据类型，对于一个关系表，需要定义每一列的数据类型。关系数据库支持的标准数据类型包括数值、字符串、时间等。

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6tla8p3xkj31f80pgmyn.jpg)

BIGINT 能满足整数存储的需求，VARCHAR(N)能满足字符串存储的需求，这两种类型是使用最广泛的。

## 主流数据库

目前，主流的关系数据库主要分为以下几类：

商用数据库，例如：Oracle，SQL Server，DB2等；
开源数据库，例如：MySQL，PostgreSQL等；
桌面数据库，以微软Access为代表，适合桌面应用程序使用；
嵌入式数据库，以Sqlite为代表，适合手机应用和桌面程序。

各自都有什么优缺点呢？

## PostgreSQL

### 安装 PostgreSQL

根据系统选一个版本下载：https://www.enterprisedb.com/downloads/postgres-postgresql-downloads。

下载、安装 pgAdmin - PostgreSQL Tools ，pgAdmin 是免费的 PostgreSQL 数据库管理工具，还有很多其他的数据库管理工具。[PostgreSQL: File Browser](https://www.postgresql.org/ftp/source/)

发现还是没学会使用

[PostgreSQL 语法 | 菜鸟教程](https://www.runoob.com/postgresql/postgresql-syntax.html)

## MySQL

### 安装 MySQL

[mac下mysql的安装步骤 - 知乎](https://zhuanlan.zhihu.com/p/37942063)

### MySQL 最基本命令

#### 进入以及连接数据库

`PATH="$PATH":/usr/local/mysql/bin `
`mysql -u root -p`

注：现实中，管理登陆需要受到密切保护，因为对它的访问授予了创建表、删除整个数据库、更改登陆和口令等完全的权限。

mysql administrator

#### 创建与删除

列出所有数据库：`show databases;`

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.02 sec)

其中，information_schema、mysql、performance_schema和sys是系统库，不要去改动它们。其他的是用户创建的数据库。

* 创建数据库：`CREATE DATABASE test;`
* 删除数据库：`DROP DATABASE test;`
* 切换到数据库：`USE test;`

* 创建表使用`CREATE TABLE XXX`语句，而删除表使用`DROP TABLE XXX`语句

### 写入 sql 数据

最开始可以用编造数据的方式来玩耍，[Mockaroo - Random Data Generator and API Mocking Tool | JSON / CSV / SQL / Excel](https://mockaroo.com/)

下载了数据之后。

- 用`quit`退出 mysql 执行界面
- mysql -u root -p databasename（数据库名） < E:\MySQL\dataname.sql（文件地址）
 
 输入密码之后就完成了数据导入。
 
 进入 mysql 之后查询表格即可获取表格。
 
### 写入 excel 数据
 
 [MySQL导入Excel表格中数据 - 简书](https://www.jianshu.com/p/af280cea4128)

全局查询

* 列出当前数据库的所有表，使用命令：`SHOW TABLES;`
* 查看一个表的结构：`DESC XXXX;` 了解字段，数据类型
* 查看创建表的SQL语句:`SHOW CREATE TABLE XXXX;`

### SELECT 语句

`SELECT`是关键字，表示将要执行一个查询，`FROM`表示将要从哪个表查询

- `SELECT * FROM <表名>` ，`*`表示“所有列”,SELECT可以用作计算,SELECT查询的结果是一个二维表。
- `SELECT <columnname> FROM <表名>`

还有其他：投影查询、排序、分页查询、聚合查询、多表查询、连接查询等详见：[连接查询 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/1177760294764384/1179610888796448)

### 排序数据

ORDER BY <columnname> 以某一列字母排序，也可以按照多个列排序，只需要用逗号进行分隔。

### 过滤数据

WHERE 语句

- `SELECT * FROM <表名> WHERE <条件表达式>`SELECT语句可以通过WHERE条件来设定查询条件,`SELECT * FROM students WHERE score >= 80;` 
- 条件可以用 AND 连起来，`<条件1> AND <条件2>` 还可以用 `OR`；注意，在执行时，先操作 and 条件，再操作 or 条件
- 表达式中，注意 使用<>判断不相等
- between 和 IN `WHERE in (范围)` 匹配范围值，其中包括开始值以及结束值
- 用 is null 来检查空值
- 使用LIKE判断相似，%可以表示任意字符

注意：在 mysql 中默认不区分大小写。

### 搜索数据

用正则表达式进行搜索

WHERE columnname regexp '正则表达式'如：`SELECT * from MOCK_DATA WHERE id regexp '80';`

正则表达式在 mysql 中只能运用一小部分

- | 表示 or，匹配其中之一
- [] 匹配几个字符之一，比如 [123]匹配1或者2或者3

## 修改数据

* 修改表就比较复杂。如果要给students表新增一列birth，使用：`ALTER TABLE students ADD COLUMN birth VARCHAR(10) NOT NULL;`
* 要修改birth列，例如把列名改为birthday，类型改为VARCHAR(20)：`ALTER TABLE students CHANGE COLUMN birth birthday VARCHAR(20) NOT NULL;`
* 要删除列，使用：`ALTER TABLE students DROP COLUMN birthday;`

### 原理补充

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6x2jyxcgtj307p07ddfx.jpg)

MySQL逻辑架构整体分为三层，最上层为客户端层，并非MySQL所独有，诸如：连接处理、授权认证、安全等功能均在这一层处理。

MySQL大多数核心服务均在中间这一层，包括查询解析、分析、优化、缓存、内置函数(比如：时间、数学、加密等函数)。所有的跨存储引擎的功能也在这一层实现：存储过程、触发器、视图等。

最下层为存储引擎，其负责MySQL中的数据存储和提取。和Linux下的文件系统类似，每种存储引擎都有其优势和劣势。中间的服务层通过API与存储引擎通信，这些API接口屏蔽了不同存储引擎间的差异。

![](https://tva1.sinaimg.cn/large/006y8mN6ly1g6x2lw3kraj30xc0jjmyp.jpg)

很多的查询优化工作实际上就是遵循一些原则让 MySQL 的优化器能够按照预想的合理方式运行而已。

了解更多：[我必须得告诉大家的MySQL优化原理 - 简书](https://www.jianshu.com/p/d7665192aaaf)


## mysql 相关的资料

[零基础如何自学MySQL数据库？ - 知乎](https://www.zhihu.com/question/34840297/answer/272185020)
[mysql深入学习笔记及实战指南](http://www.notedeep.com/note/38/page/282)
[MySQL索引背后的数据结构及算法原理 - 匠心零度博客](http://www.jiangxinlingdu.com/mysql/2018/12/19/B-Tree.html)

## change log

- 2019-09-12 复习一遍查询语句的命令，要深入理解原理估计还比较难，能先用起来就行
- 2019-09-09 创建

