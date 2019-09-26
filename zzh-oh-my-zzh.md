# 2019-08-29 zzh & oh my zzh & iTerm2 上手配置

属于命令行强化大类下。

* [ ] 还有还多概念没弄懂

## 为什么要从 bash 转移到 zzh

zzh 更好用？

比如，zzh 可以安装各种插件，命令补全插件就是一个。

## 安装 iTerm2

可以直接去官网安装下载：https://www.iterm2.com/


## 安装以及设置 zsh 

> Zsh 是一款强大的虚拟终端，既是一个[系统的虚拟终端]()，也可以作为一个[脚本语言的交互解析器]()。

brew install zsh # mac安装

- `zsh --version` 查看版本
- sudo`chsh -s /bin/zsh`设置为默认的程序
- 退出后登陆一下就可以看到界面改为 zsh 了
- 测试一下 `echo $SHELL` Test with `$SHELL --version`. 

- kg:
    - chsh: change shell
    - bin
    - $

## 安装以及设置 Oh My Zsh 

> oh my zsh 是什么？它是一款社区驱动的命令行工具。基于 zsh 命令行，提供了主题配置，插件机制，已经内置的便捷操作。给我们一种全新的方式使用命令行。

用 [curl]() 安装
```
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

oh-my-zsh开源地址：https://github.com/robbyrussell/oh-my-zsh


## 安装主题以及 iTerm2 设置

- 安装 powerline `pip install powerline-status --user`
- 安装 powerfonts 字体库并且设置字体
  - 在你习惯的位置新建一个文件夹 
  - 在这个文件夹下 git clone 项目至本地 https://github.com/powerline/fonts.git --depth=1
  - `cd fonts` 文件夹，安装上字体 `./install.sh`
  - 在 iTerm 中设置字体 iTerm2 -> Preferences -> Profiles -> Text 在 Font 区域选择 change font，然后找到 Meslo LG 字体
- 安装配色方案并且设置
  - `git clone https://github.com/altercation/solarized`
  - `cd solarized/iterm2-colors-solarized/`
  - `open .`
  - 再次进入iTerm2 -> Preferences -> Profiles -> Colors -> Color Presets中根据个人喜好选择这两种配色中的一种即可
- 设置一个你喜欢的主题吧，我设置的是 agnostr
  - `git clone https://github.com/fcamblor/oh-my-zsh-agnoster-fcamblor.git`
  - `cd oh-my-zsh-agnoster-fcamblor/`
  - `./install`
  - 打开配置文件，把 ZSH_THEME 后面的字段改为 agnoster
    - 首先打开iTerm,切到文件所在的文件夹目录下
      - cd xx 然后进入编辑模式vim ~/.zshrc
      - 然后插入修改 shift + i
      - 修改之后退出插入模式 esc
      - 保存退出 ZZ
    - 此时command+Q或source配置文件后，就可以更新主题啦
  - 安装高亮插件
    - `cd ~/.oh-my-zsh/custom/plugins/`
    - `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git`
    - `vi ~/.zshrc`
    - 这时我们再次打开zshrc文件进行编辑。找到plugins，此时plugins中应该已经有了git，我们需要把高亮插件也加上(请务必保证插件顺序，zsh-syntax-highlighting必须在最后一个。)
    - 然后在文件的最后一行添加：`source ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh`
    - 执行命令让刚才的操作生效 `source ~/.zshrc`
 - 安装补全插件
   - cd ~/.oh-my-zsh/custom/plugins/
   - git clone https://github.com/zsh-users/zsh-autosuggestions
   - vi ~/.zshrc
   - 找到 plugins 加入 zsh-autosuggestion
 - 更换背景图
   - https://pan.baidu.com/s/1LKd4ghGyyNI6UwHhOHvfaA  提取码: snrd
   - 更换背景图片方式：iTerm2 -> Preferences -> Profiles -> Window -> BackGround Image勾选图片即可。


![](https://cloud.githubusercontent.com/assets/2618447/6316862/70f58fb6-ba03-11e4-82c9-c083bf9a6574.png)

## ref

- [https://github.com/sirius1024/iterm2-with-oh-my-zsh](https://github.com/sirius1024/iterm2-with-oh-my-zsh)
- [iTerm2 + Oh My Zsh 打造舒适终端体验 - 知乎](https://zhuanlan.zhihu.com/p/37195261)
- [iTerm2 + Oh My Zsh 打造舒适终端体验 - 简书](https://www.jianshu.com/p/9c3439cc3bdb)

## Changelog

- 2019-08-29  重新看了一遍
- Created: Jun 08, 2019 5:05 PM

