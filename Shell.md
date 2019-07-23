# Shell

一般说的“命令行”是指linux命令，linux命令是对Linux系统进行管理的命令。对于Linux系统来说，无论是中央处理器、内存、磁盘驱动器、键盘、鼠标，还是用户等都是文件，Linux系统管理的命令是它正常运行的核心，与之前的DOS命令类似。linux命令在系统中有两种类型：内置Shell（外壳）命令和Linux命令。

其中文件目录和文件搜索应该是最常用的两种

### 文件目录

*    cd /home 进入 '/ home' 目录'
* 　　cd .. 返回上一级目录
* 　　cd ../.. 返回上两级目录
* 　　cd 进入个人的主目录
* 　　cd ~user1 进入个人的主目录
* 　　cd - 返回上次所在的目录
* 　　pwd 显示工作路径
* 　　ls 查看目录中的文件
* 　　ls -F 查看目录中的文件
* 　　ls -l 显示文件和目录的详细资料
* 　　ls -a 显示隐藏文件
*    ls -R 显示目录结构和目录内文件
* 　　ls *[0-9]* 显示包含数字的文件名和目录名
* 　　tree 显示文件和目录由根目录开始的树形结构(1)
* 　　lstree 显示文件和目录由根目录开始的树形结构(2)
* 　　mkdir dir1 创建一个叫做 'dir1' 的目录'
* 　　mkdir dir1 dir2 同时创建两个目录
* 　　mkdir -p /tmp/dir1/dir2 创建一个目录树
* 　　rm -f file1 删除一个叫做 'file1' 的文件'
* 　　rmdir dir1 删除一个叫做 'dir1' 的目录'
* 　　rm -rf dir1 删除一个叫做 'dir1' 的目录并同时删除其内容
* 　　rm -rf dir1 dir2 同时删除两个目录及它们的内容
* 　　mv dir1 new_dir 重命名/移动 一个目录
* 　　cp file1 file2 复制一个文件
* 　　cp dir/* . 复制一个目录下的所有文件到当前工作目录
* 　　cp -a /tmp/dir1 . 复制一个目录到当前工作目录
* 　　cp -a dir1 dir2 复制一个目录
* 　　ln -s file1 lnk1 创建一个指向文件或目录的软链接
* 　　ln file1 lnk1 创建一个指向文件或目录的物理链接
* 　　touch -t 0712250000 file1 修改一个文件或目录的时间戳 - (YYMMDDhhmm)

### 文件搜索

* find / -name file1 从 '/' 开始进入根文件系统搜索文件和目录
* 　　find / -user user1 搜索属于用户 'user1' 的文件和目录
* 　　find /home/user1 -name \*.bin 在目录 '/ home/user1' 中搜索带有'.bin' 结尾的文件
* 　　find /usr/bin -type f -atime +100 搜索在过去100天内未被使用过的执行文件
* 　　find /usr/bin -type f -mtime -10 搜索在10天内被创建或者修改过的文件
* 　　find / -name \*.rpm -exec chmod 755 '{}' \; 搜索以 '.rpm' 结尾的文件并定义其权限
* 　　find / -xdev -name \*.rpm 搜索以 '.rpm' 结尾的文件，忽略光驱、捷盘等可移动设备
* 　　locate \*.ps 寻找以 '.ps' 结尾的文件 - 先运行 'updatedb' 命令
* 　　whereis halt 显示一个二进制文件、源码或man的位置
* 　　which halt 显示一个二进制文件或可执行文件的完整路径
　　
## mv

mv 操作文件时是移动并且重命名。

目标目录与原目录一致，指定了新文件名，效果就是仅仅重命名。

mv  /home/ffxhd/a.txt   /home/ffxhd/b.txt    
目标目录与原目录不一致，没有指定新文件名，效果就是仅仅移动。

mv  /home/ffxhd/a.txt   /home/ffxhd/test/ 
或者
mv  /home/ffxhd/a.txt   /home/ffxhd/test 
目标目录与原目录一致, 指定了新文件名，效果就是：移动 + 重命名。

mv  /home/ffxhd/a.txt   /home/ffxhd/test/c.txt
------------------------------------------------------

批量移动文件和文件夹：(在Ubuntu 18.04 奏效）

例如，将 /home/ffxhd/testThinkPHP5/tp5 目录里边的所有文件&文件夹 挪到 /home/ffxhd/testThinkPHP5

mv  /home/ffxhd/testThinkPHP5/tp5/*  /home/ffxhd/testThinkPHP5
注意：需要先执行显示隐藏文件命令，否则，隐藏文件以及隐藏文件夹不会被移动到新目录。

英语点号开头的文件会被作为隐藏文件处理，英语点号开头的文件夹也被作为隐藏文件夹处理。

例如：文件 .a.txt， 目录 .tp5。

## CHANGELOG

- 2019-07-23 创建

