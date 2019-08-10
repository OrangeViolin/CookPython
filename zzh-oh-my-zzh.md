# zzh& oh my zzh

## 为什么要从 dash 转移到 zzh

## 安装 iTerm2

可以直接去官网安装下载：https://www.iterm2.com/

iTerm2 有要求的 Mac 版本，所以，我需要把系统升级一下。

![](https://ws3.sinaimg.cn/large/006tNc79ly1g5upfmpv7zj30na08s75p.jpg)

详细了解可参见：[如何升级到 macOS Mojave - Apple 支持](https://support.apple.com/zh-cn/HT201475)

要更新系统需要备份电脑上所有的文件，等我的心硬盘到了就用它来备份吧。

brew install zsh # mac安装

wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh

## Zsh

If necessary, follow these steps to install Zsh:

1. There are two main ways to install Zsh
    - with the package manager of your choice, *e.g.* `sudo apt install zsh` (see [below for more examples](https://github.com/robbyrussell/oh-my-zsh/wiki/Installing-ZSH#how-to-install-zsh-in-many-platforms))
    - from [source](http://zsh.sourceforge.net/Arc/source.html), following [instructions from the Zsh FAQ](http://zsh.sourceforge.net/FAQ/zshfaq01.html#l7)
2. Verify installation by running `zsh --version`. Expected result: `zsh 5.1.1` or more recent.
3. Make it your default shell: sudo`chsh -s $(which zsh)`
    - Note that this will not work if Zsh is not in your authorized shells list (`/etc/shells`) or if you don't have permission to use `chsh`. If that's the case [you'll need to use a different procedure](https://www.google.com/search?q=zsh+default+without+chsh).
4. Log out and login back again to use your new default shell.
5. Test that it worked with `echo $SHELL`. Expected result: `/bin/zsh` or similar.
6. Test with `$SHELL --version`. Expected result: 'zsh 5.1.1' or similar

- kg:
    - chsh: change shell
    - bin
    - $

## Oh My Zsh

- Oh My Zsh is a delightful, open source, community-driven framework  for managing your Zsh configuration. It comes bundled with thousand functions, helpers, themes, and a few things that make you shout…
    - functions
    - helper
    - plugins,
    - themes

## Plugins

[Plugins Overview · robbyrussell/oh-my-zsh Wiki](https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins-Overview#python)

## Themes

### **agnoster**

[Official repository](https://github.com/agnoster/agnoster-zsh-theme)

![](https://cloud.githubusercontent.com/assets/2618447/6316862/70f58fb6-ba03-11e4-82c9-c083bf9a6574.png)

Shown with [Solarized Dark colorscheme](http://ethanschoonover.com/solarized) and Powerline-patched Meslo 14pt in [iTerm 2](http://www.iterm2.com/).

Additional setup:

- Install one of the [patched fonts from Vim-Powerline](https://github.com/powerline/fonts) or [patch your own](https://github.com/powerline/fontpatcher) for the special characters.

        # 安装 powerline 
        # clone
        git clone https://github.com/powerline/fonts.git --depth=1
        # install
        cd fonts
        ./install.sh
        # clean-up a bit
        cd ..
        rm -rf fonts

- *Optionally* set `DEFAULT_USER` to your regular username followed by prompt_context(){} in `~/.zshrc` to hide the “user@hostname” info when you’re logged in as yourself on your local machine.

安装完成以后，调出配置文件,将ZSH_THEME后面的字段改为agnoster

    vi ~/.zshrc

![](Untitled-e8ef59c6-3dee-4e35-959a-b23e824575b0.png)

修改完成后按一下esc调出vi命令，输入:wq保存并退出vi模式。此时command+Q或source配置文件后，iTerm2变了模样：

- 在命令模式中，连按两次大写字母Z，若当前编辑的文件曾被修改过，则Vi保存该文件后退出，

最后的调试，把你的 item2 调试到匹配新的样式表

For iTerm 2 users, you have to set the font on : iTerm 2 -> Preferences -> Profiles -> Text and use one of the *Powerline* fonts :

![](Untitled-31a8277a-ad55-46e0-923d-a371b2e2f2e3.png)

我选择的是：Meslo LG S for Powerline

### Color

    cd ~/Desktop/OpenSource
    
    git clone https://github.com/altercation/solarized
    
    cd solarized/iterm2-colors-solarized/
    
    open .

在打开的finder窗口中，双击Solarized Dark.itermcolors和Solarized Light.itermcolors即可安装明暗两种配色：

![](Untitled-6712918a-0d8b-4c83-840d-6bb5d451aee6.png)

再次进入iTerm2 -> Preferences -> Profiles -> Colors -> Color Presets中根据个人喜好选择这两种配色中的一种即可：

![](Untitled-f012aa01-16f6-46c9-9e8c-6edd4aae6594.png)

## ZSH 配置文件

    vi ~/.zshrc
     
    # 输入 I 则可以插入
    # 更改之后，在文件下方加入你加入插件的位置 source ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
    # 大写 ZZ 保存并退出

## ref

- [https://github.com/sirius1024/iterm2-with-oh-my-zsh](https://github.com/sirius1024/iterm2-with-oh-my-zsh)
- [iTerm2 + Oh My Zsh 打造舒适终端体验 - 简书](https://www.jianshu.com/p/9c3439cc3bdb)

## Changelog

- Created: Jun 08, 2019 5:05 PM

