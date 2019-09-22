# BeautifulSoup

代替 正则表达式 解析 html 的工具。

## 使用 

from bs4 import BeautifulSoup
soup = BeautifulSoup(变量,'lxml') #导入
print(soup.prettify)
print(soup.title)
print(soup.title.string)
print(soup.a)
print(soup.c)
……

看官方网站介绍：

[Beautiful Soup 4.2.0 文档 — Beautiful Soup 4.2.0 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

- 输入的 html 文件在哪里？

