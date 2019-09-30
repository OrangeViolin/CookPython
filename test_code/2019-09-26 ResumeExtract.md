# 2019-09-26 ResumeExtract

## 任务定义

输入：一堆 jason 格式的文件，网络上爬取的数据

输出：把没有提对的出生日期替换掉，仍旧保存为 json 格式的文件

- 完整格式：XXXX年XX月XX日
- 没有日：XXXX年XX月
- 没有年：XXXX年

## 解决思路

任务拆解：

- 读取数据
- 提取数据
- 替换数据
- 写入数据

解决思路：

- 用 pandas 的 read_json函数可以将json数据转化为dataframe
- 用正则匹配
- 匹配到就放到一个list
- 用 pandas to_json 写入到 json

json load
json list
dict 
loop 
json 新的
for 循环

问题记录

- 怎么使用 pandas 读取数据？google pandas   json 详见：[pandas]()
  - pandas里的read_json函数可以将json数据转化为dataframe。 
  - OS 模块下用 os.listdir 以及 os.path.abspath 读取文件夹下所有文件的路径
  - 用 for 循环一个一个解析
  - 将数据保存在变量中

但感觉现在这样，我不知道要如何定位到要提取那一段文本，提取的结果，还要保存到一个特定的列，但是按照现在提取的颗粒度，基本上是不足够的。

pd.read_jason()

> pandas.read_json(path_or_buf=None, orient=None, typ='frame', dtype=None, convert_axes=None, convert_dates=True, keep_default_dates=True, numpy=False, precise_float=False, date_unit=None, encoding=None, lines=False, chunksize=None, compression='infer')[source]

转换成了 DataFrame 要如何处理？

DataFrame([data, index, columns, dtype, copy])
ref：[DataFrame — pandas 0.25.1 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)

- 先定位到 DataFrame 中的一个'个人简历'字段 
- 用正则表达式提取一下那和年龄有关的字段的值
- 然后再定位 DataFrame 的一个字段'出生日期'字段，输出进去

看文件，要把个人简历中的出生日期字段提取出来替换掉出生日期的value的值。

> "个人简历": "杜荣,男,1975年1月15日,1995年8月至2002年8月,就职于启东农药化工总长,担任技术人员,品质管理人员;2002年9月至2004年7月在西南交通大学经济管理学院,攻读研究生,2004年8月至2008年3月11日,江苏好收成韦恩化工有限责任公司任经理,2008年3月12日至今,任江苏好收成韦恩农化股份有限公司董事会秘书。"

要替换的值：

> "出生日期": "年"

## 


## ref

- [pandas处理json数据_ITPUB博客](http://blog.itpub.net/26736162/viewspace-2647241/)
- [pandas.read_json — pandas 0.25.1 documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)

## changelog



