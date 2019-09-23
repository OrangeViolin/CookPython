# 2019-08-30 Git

教程原版本：[撤销修改 - 廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/896043488029600/897889638509536)

## 安装 Git

## 常用 Git 命令

开始一个工作区（参见：git help tutorial）
   clone      克隆仓库到一个新目录
   init       创建一个空的 Git 仓库或重新初始化一个已存在的仓库

在当前变更上工作（参见：git help everyday）
   add        添加文件内容至索引
   mv         移动或重命名一个文件、目录或符号链接
   reset      重置当前 HEAD 到指定状态
   rm         从工作区和索引中删除文件

检查历史和状态（参见：git help revisions）
   bisect     通过二分查找定位引入 bug 的提交
   grep       输出和模式匹配的行
   log        显示提交日志
   show       显示各种类型的对象
   status     显示工作区状态

扩展、标记和调校您的历史记录
   branch     列出、创建或删除分支
   checkout   切换分支或恢复工作区文件
   commit     记录变更到仓库
   diff       显示提交之间、提交和工作区之间等的差异
   merge      合并两个或更多开发历史
   rebase     在另一个分支上重新应用提交
   tag        创建、列出、删除或校验一个 GPG 签名的标签对象

协同（参见：git help workflows）
   fetch      从另外一个仓库下载对象和引用
   pull       获取并整合另外的仓库或一个本地分支
   push       更新远程引用和相关的对象
   
   
-------

   

## 创建版本库

版本库又名仓库，版本库：repository，你可以简单理解为一个目录，这个目录里面的所有文件都可以被 Git 管理起来，每个文件的修改、删除，Git 都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以“还原”。

### 在本地建立一个仓库

第一步，选择一个合适的地方，创建一个空目录：

```
(base) yushans-MBP:~ yushan$ mkdir FintechResearch
(base) yushans-MBP:~ yushan$ cd FintechResearch
(base) yushans-MBP:FintechResearch yushan$ pwd
/Users/yushan/FintechResearch
```

第二步，把这个文件夹变成 Git 可以管理的仓库

```
(base) yushans-MBP:FintechResearch yushan$ git init 
已初始化空的 Git 仓库于 /Users/yushan/FintechResearch/.git/
(base) yushans-MBP:FintechResearch yushan$ ls -ah
.	..	.git
```
这里会显示这是一个空文件夹。
`ls -ah` 这个是非必要的，用来看目录下的影藏目录

第三步：创建一个 txt 文件并且放入文件夹当中

最好是 txt 文件以及 md 文件

第四步：把这个文件夹放入仓库中

```
(base) yushans-MBP:FintechResearch yushan$ git add readme.txt
```
这一行命令不会有结果，Unix 的哲学是没有消息就是好消息。


> 关于版本管理要求文件的说明

> 注：首先这里再明确一下，所有的版本控制系统，其实只能跟踪文本文件的改动，比如TXT文件，网页，所有的程序代码等等，Git也不例外。版本控制系统可以告诉你每次的改动，比如在第5行加了一个单词“Linux”，在第8行删了一个单词“Windows”。而图片、视频这些**二进制文件**，虽然也能由版本控制系统管理，但没法跟踪文件的变化，只能把二进制文件每次改动串起来，也就是只知道图片从100KB改成了120KB，但到底改了啥，版本控制系统不知道，也没法知道。

> 二进制文件是什么？
> 都有哪些文件类型，各种文件类型之间区别是啥，为什么要有这么多文件类型？

> 不幸的是，Microsoft的Word格式是二进制格式，因此，版本控制系统是没法跟踪Word文件的改动的，前面我们举的例子只是为了演示，如果要真正使用版本控制系统，就要以纯文本方式编写文件。

> 因为文本是有编码的，比如中文有常用的**GBK编码**，日文有**Shift_JIS编码**，如果没有历史遗留问题，强烈建议使用标准的**UTF-8编码**，所有语言使用同一种编码，既没有冲突，又被所有平台所支持。

> 各种编码是什么？

第五步：把文件提交到仓库当中 

```
(base) yushans-MBP:FintechResearch yushan$ git commit -m "wrote a readme file"
[master（根提交） c026cba] wrote a readme file
 1 file changed, 8 insertions(+)
 create mode 100644 readme.txt
```

为什么需要 `git add`和`git commit`这两个步骤呢？
因为 `git add` 一次只能添加一个文件，`git commit` 可以提交多个。

单纯直说 git commit 会进入 vim 模式，你可以输入多行说明单如何退出是个问题，我搬过来了答案

> 今天用git commit -m “注释”提交的时候，注释写错了，于是各种查资料开始了和git bash vim的纠缠。。。（网上的资料我真是没操作成功，不过最后还是摸索出来了。

> 首先 使用 git commit --amend 命令（修改最近一次提交的注释信息），会进入到vim 编辑器

> 然后 你会发现编辑器里你怎么输入都没反应，这是因为vim处在不可编辑状态，

> 按下字母键 c（此时进入编辑状态），可以开始修改注释信息了

> 修改好后，你会发现怎么都退出不了，然后如下操作：

> 按下Esc (退出编辑状态)； 接着连按两次大写字母Z，你会惊喜的发现，终于保存好退出来了！



### 直接在 Github 上建好仓库clone（复制）到本地

这是我之前的操作，先暂时跳过不讲。

小结：这一小章节让我彻底明白了， git 和 github 真的不是一个东西，没有 github 单纯用 git 也可以管理版本信息的。

## 时光机穿梭

### 如何修改文件并且提交

先把文件改一改，然后运行 git status 看看结果

```
(base) yushans-MBP:FintechResearch yushan$ git status
位于分支 master
要提交的变更：
  （使用 "git reset HEAD <文件>..." 以取消暂存）

	修改：     readme.txt

(base) yushans-MBP:FintechResearch yushan$ 
```
这条命令显示，readme.txt 被修改过了

可以用 `git diff` 命令来查看修改痕迹

```
(base) yushans-MBP:FintechResearch yushan$ git diff readme.txt
diff --git a/readme.txt b/readme.txt
index 1b76c7b..f5812be 100644
--- a/readme.txt
+++ b/readme.txt
@@ -7,4 +7,4 @@
 \f0\fs24 \cf0 Fintech is an interesting choice.\
 Welcome!\
 Oh
-\f1 , come on, do not reject me!}
\ No newline at end of file
+\f1 , come on, do not reject me.}
\ No newline at end of file
```
红色的是原来的内容，绿色的是修改后的内容。

还是之前的操作三件套 `git add ``git commit``git status`

```
(base) yushans-MBP:FintechResearch yushan$ git add readme.txt
(base) yushans-MBP:FintechResearch yushan$ git commit -m "change comma"
[master 0a5ea6c] change comma
 1 file changed, 4 insertions(+), 2 deletions(-)
(base) yushans-MBP:FintechResearch yushan$ git status
位于分支 master
无文件要提交，干净的工作区
(base) yushans-MBP:FintechResearch yushan$ 
```

### 版本回退

每一次 commit 就提交了一次版本，一旦你把文件改乱了，或者误删了文件，可以从最近的一个 commit 回复，然后继续工作。

版本控制会被默默记录下来，我们可以用 git log 命令查看。

```
(base) yushans-MBP:FintechResearch yushan$ git log
commit 22f0997d39054c93141b09c4e2f951f34c9811e7 (HEAD -> master)
Author: OrangeViolin <shanzibnu@gmail.com>
Date:   Thu Aug 8 22:00:40 2019 +0800

    add a favrotate word of a lovely some

commit 0a5ea6c629dd2b18ee01f01f51ee83ab14c6d103
Author: OrangeViolin <shanzibnu@gmail.com>
Date:   Thu Aug 8 21:54:30 2019 +0800

    change comma

commit c026cba4a7a61c21a364f4fcb14d70d27b68ec36
Author: OrangeViolin <shanzibnu@gmail.com>
Date:   Thu Aug 8 21:14:40 2019 +0800

    wrote a readme file
```

如果嫌输出信息太多，看得眼花缭乱的，可以试试加上 --pretty=oneline 参数

```
(base) yushans-MBP:FintechResearch yushan$ git log --pretty=oneline
22f0997d39054c93141b09c4e2f951f34c9811e7 (HEAD -> master) add a favrotate word of a lovely some
0a5ea6c629dd2b18ee01f01f51ee83ab14c6d103 change comma
c026cba4a7a61c21a364f4fcb14d70d27b68ec36 wrote a readme file
```

此处注解，1094……这一些是 commit id（版本号），和 SVN 不一样，Git 的 commit id 不是 1234 递增的数字，而是一个 SHA1 计算出来的一个非常大的数字，用十六进制表示。

为什么 commit id 需要用这么大一串数字表示呢？因为 Git 是分布式的版本控制系统，后面要研究多人在同一个版本库里工作，如果大家都用 1234……作为版本号，那肯定冲突了。

没提交一个新版本，实际上 Git 就会把它们自动串联成一条时间线。

好了，终于可以开始启动时光穿梭机了。

在 Git 中，HEAD 代表当前版本，上一个版本就是 HEAD^，上上个版本就是 HEAD^^,往上 100 个版本，写成 HEAD~100

```
(base) yushans-MBP:FintechResearch yushan$ git reset --hard HEAD^
HEAD 现在位于 0a5ea6c change comma
```

可以查看一下是否回退到了指定的版本。

```
(base) yushans-MBP:FintechResearch yushan$ cat readme.txt
```
当你回到了上一个版本，点击 git log 查看当前状态，发现只剩下两个版本了，这是因为 git 的版本切换很快，如下图：

![](https://ws1.sinaimg.cn/large/006tNc79ly1g5snc3b5qqj30cx09xdg5.jpg)

如果你想要退回到之后的那个版本，找不到怎么办。可以直接记住 commit id

用 `git reflog` 可以记录你的每一次命令，找到你想要退回的 commit id 就可以用 reset 命令回退了。

```
(base) yushans-MBP:FintechResearch yushan$ git reflog
22f0997 (HEAD -> master) HEAD@{0}: reset: moving to 22f0997
0a5ea6c HEAD@{1}: reset: moving to 0a5ea6c
22f0997 (HEAD -> master) HEAD@{2}: reset: moving to 22f0997d39054c93141b09c4e2f951f34c9811e7
0a5ea6c HEAD@{3}: reset: moving to HEAD^
22f0997 (HEAD -> master) HEAD@{4}: commit: add a favrotate word of a lovely some
0a5ea6c HEAD@{5}: commit: change comma
c026cba HEAD@{6}: commit (initial): wrote a readme file
(base) yushans-MBP:FintechResearch yushan$ git reset --hard 22f0997
HEAD 现在位于 22f0997 add a favrotate word of a lovely some
```
### 工作区和暂存区

Git 和其他版本管理系统如 SVN 的一个不同之处就是有暂存区的概念。

工作区（Working Directory）：就是你在电脑里能看到的目录。
版本库（Repository）工作区有一个隐藏目录 .git，这个不算工作区，而是 Git 的版本库。Git 的版本库哩存了很多东西，其中最重要的就是成为 stage 或者叫 index 的暂存区，还有 Git 为我们自动创建的第一个分支 master，以及只想 master 的一个指针 HEAD

这里需要盗取一张图啊。

![](https://ws1.sinaimg.cn/large/006tNc79ly1g5snksxsphj30eo07a0tx.jpg)

之前我们把文件王 Git 版本库添加的时候，分两个步骤执行的：

第一步是用git add把文件添加进去，实际上就是把文件修改添加到暂存区；

第二步是用git commit提交更改，实际上就是把暂存区的所有内容提交到当前分支。

因为我们创建Git版本库时，Git自动为我们创建了唯一一个master分支，所以，现在，git commit就是往master分支上提交更改。

你可以简单理解为，需要提交的文件修改通通放到暂存区，然后，一次性提交暂存区的所有修改。

### 管理修改

为什么Git比其他版本控制系统设计得优秀，因为Git跟踪并管理的是修改，而非文件。

如果两次的操作过程是这样的:

第一次修改 -> git add -> 第二次修改 -> git commit

你看，我们前面讲了，Git管理的是修改，当你用git add命令后，在工作区的第一次修改被放入暂存区，准备提交，但是，在工作区的第二次修改并没有放入暂存区，所以，git commit只负责把暂存区的修改提交了，也就是第一次的修改被提交了，第二次的修改不会被提交。

用git diff HEAD -- readme.txt命令可以查看工作区和版本库里面最新版本的区别

### 撤销修改

### 删除文件 

## 远程仓库

### 将本地仓库同步到远程仓库

现在的情景是，你已经在本地创建了一个Git仓库后，又想在GitHub创建一个Git仓库，并且让这两个仓库进行远程同步，这样，GitHub上的仓库既可以作为备份，又可以让其他人通过该仓库来协作，真是一举多得。

在 GitHub 上建一个仓库，命名保持一致，其他保持默认设置。

最开始仓库是空的，GitHub告诉我们，可以从这个仓库克隆出新的仓库，也可以把一个已有的本地仓库与之关联，然后，把本地仓库的内容推送到GitHub仓库。

![](https://ws3.sinaimg.cn/large/006tNc79ly1g5so391qz6j30u20h4jua.jpg)

根据提示在 fintech 目录下运行

```
git remote add origin https://github.com/OrangeViolin/FintechResearch.git
```

添加后，远程库的名字就是origin，这是Git默认的叫法，也可以改成别的，但是origin这个名字一看就知道是远程库。

下一步可以把本地仓库的所有内容推送到远程仓库上

```
git push -u origin master
```

由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。

之后可以通过简化命令提交

```
git push origin master
```

### SSH 警告

我得到的警告是这样的：

```
(base) yushans-MBP:FintechResearch yushan$ git push -u origin master
remote: You must verify your email address.
remote: See https://github.com/settings/emails.
fatal: unable to access 'https://github.com/OrangeViolin/FintechResearch.git/': The requested URL returned error: 403
(base) yushans-MBP:FintechResearch yushan$ 
```
这个答案帮助了我
[github - Git push error "You must verify your email address." - Stack Overflow](https://stackoverflow.com/questions/40660326/git-push-error-you-must-verify-your-email-address/56625162#56625162?newreg=c9410c8a7c7f48538fa96995d1dd8ef3)

![](https://ws1.sinaimg.cn/large/006tNc79ly1g5sok9dfoyj30l808wwff.jpg)

```
(base) yushans-MBP:FintechResearch yushan$ git remote set-url origin https://OrangeViolin:2523842abcys@github.com/OrangeViolin/FintechResearch.git
```

终于可以用命令行提交到远程代码库了~  

## 分支管理

## 标签管理

## 自定义 Git

## 常用 Git 命令

## 将本地代码修改推送到远程仓库出现问题

```Python

```

## Commit message 和 Change log

Git 每次提交代码都要 Commit message（提交信息）否则，就不允许提交。

```
$ git commit -m "say it again"
```
-m 就是用来指定 

## 让命令行记住 github 密码

记住密码之后不用再重复输入

- 在命令行输入命令:
  `git config --global credential.helper store`
   ☞ 这一步会在用户目录下的.gitconfig文件最后添加:
   ```
    [credential]
        helper = store
    ```
- 现在push你的代码 (git push), 这时会让你输入用户名密码, 这一步输入的用户名密码会被记住, 下次再push代码时就不用输入用户名密码啦!
  ☞这一步会在用户目录下生成文件.git-credential记录用户名密码的信息.
  ☞ git config --global 命令实际上在操作用户目录下的.gitconfig文件, 我们cat一下此文件(cat .gitconfig), 其内容如下:
    ```
    [user]
        name = alice
        email = alice@aol.com
    [push]
        default = simple
    [credential]
        helper = store
    ```
git config --global user.email "alice@aol.com" 操作的就是上面的email
git config --global push.default matching 操作的就是上面的push段中的default字段
git config --global credential.helper store 操作的就是上面最后一行的值

## CHANGELOG

- 20190904 补上了git 的官方介绍，认为之前太过于详细的细节了
- 20190830 创建

