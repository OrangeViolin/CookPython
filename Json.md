# Json(未完)

Created: Jun 09, 2019 4:26 PM

# what is json

[JSON - Wikipedia](https://en.wikipedia.org/wiki/JSON)

In [computing](https://en.wikipedia.org/wiki/Computing), **JavaScript Object Notation** (**JSON**) ([/ˈdʒeɪsən/](https://en.wikipedia.org/wiki/Help:IPA/English) "Jason",[[1]](https://en.wikipedia.org/wiki/JSON#cite_note-Pronunciation-1) [/ˈdʒeɪsɒn/](https://en.wikipedia.org/wiki/Help:IPA/English)) is an [open-standard](https://en.wikipedia.org/wiki/Open_standard) [file format](https://en.wikipedia.org/wiki/File_format) that uses [human-readable](https://en.wikipedia.org/wiki/Human-readable_medium) text to transmit data objects consisting of [attribute–value pairs](https://en.wikipedia.org/wiki/Attribute%E2%80%93value_pair) and [array data types](https://en.wikipedia.org/wiki/Array_data_type) (or any other [serializable](https://en.wikipedia.org/wiki/Serialization) value). It is a very common [data](https://en.wikipedia.org/wiki/Data) format used for [asynchronous](https://en.wikipedia.org/wiki/Asynchronous_I/O) browser–server communication, including as a replacement for [XML](https://en.wikipedia.org/wiki/XML) in some [AJAX](https://en.wikipedia.org/wiki/Ajax_(programming))-style systems.[[2]](https://en.wikipedia.org/wiki/JSON#cite_note-2)

JSON is a [language-independent](https://en.wikipedia.org/wiki/Language-independent_specification) data format. It was derived from [JavaScript](https://en.wikipedia.org/wiki/JavaScript), but as of 2017 many [programming languages](https://en.wikipedia.org/wiki/Programming_language) include code to generate and [parse](https://en.wikipedia.org/wiki/Parsing) JSON-format data. The official Internet [media type](https://en.wikipedia.org/wiki/Media_type) for JSON is `application/json`. JSON filenames use the extension `.json`.

[Douglas Crockford](https://en.wikipedia.org/wiki/Douglas_Crockford) originally specified the JSON format in the early 2000s; two competing standards, [RFC](https://en.wikipedia.org/wiki/Request_for_Comments_(identifier)) [8259](https://tools.ietf.org/html/rfc8259) and ECMA-404,[[3]](https://en.wikipedia.org/wiki/JSON#cite_note-3) defined it in 2017. The [ECMA](https://en.wikipedia.org/wiki/Ecma_International) standard describes only the allowed syntax, whereas the RFC covers some security and interoperability considerations.[[4]](https://en.wikipedia.org/wiki/JSON#cite_note-4)

A restricted profile of JSON, known as **I-JSON** (short for "Internet JSON"), seeks to overcome some of the interoperability problems with JSON. It is defined in [RFC](https://en.wikipedia.org/wiki/Request_for_Comments_(identifier)) [7493](https://tools.ietf.org/html/rfc7493).[[5]](https://en.wikipedia.org/wiki/JSON#cite_note-RFC7493-5)

[What is JSON](https://www.w3schools.com/whatis/whatis_json.asp)

    JSON: javascript Object Notation 格式编码的数据 
    JSON stands for JavaScript Object Notation
    JSON is a lightweight format for storing and transporting data
    JSON is often used when data is sent from a server to a web page
    JSON is "self-describing" and easy to understand

JSON建构于两种结构：

- “名称/值”对的集合（A collection of name/value pairs）。不同的语言中，它被理解为对象（object），纪录（record），结构（struct），字典（dictionary），哈希表（hash table），有键列表（keyed list），或者关联数组 （associative array）。
- 值的有序列表（An ordered list of values）。在大部分语言中，它被理解为数组（array）。

这些都是常见的数据结构。事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。

k-v 格式，key 对应 value 用逗号隔开，key和value的对应关系用：，如果一个key 对应多个 value 则value 用序列的[]来表示。

JSON相对于XML来讲，数据的体积小，传递的速度更快些。

总结：

- Json **JavaScript Object Notation，来源于 JavaScript 一种编程语言，但与JavaScript Object 的格式又有一点区别**
- 可读性高
- 仅有文本格式，**经常被用来服务器和浏览器之间数据交换**

- 拓展点

    JavaScript Object 和 Json 的区别

    [JavaScript Objects](https://www.w3schools.com/js/js_objects.asp) ：In real life, a car is an **object**. A car has **properties** like weight and color, and **methods** like start and stop.JavaScript objects are containers for named values called properties or methods.  like  

        var car = { type:"Fiat", model:"500", color:"white"}       

    JSON - Evaluates to JavaScript Objects

    In JavaScript, keys can be strings, numbers, or identifier names {name:"John"}

    In JSON, keys must be strings, written with double quotes： {"name"="John"}

    In **JSON**, *values* must be one of the following data types:

    - a string
    - a number
    - an object (JSON object)
    - an array
    - a boolean
    - null

    In **JavaScript** values can be all of the above, plus any other valid JavaScript expression, including:

    - a function
    - a date
    - undefined

    Json 是怎么创造出来的

## Json 数据类型以及常用规范

    """
    数字型（Number）       JavaScript 中的双精度浮点型格式
    字符串型（String）     双引号包裹的 Unicode 字符和反斜杠转义字符
    布尔型（Boolean）      true 或 false
    数组（Array）          有序的值序列
    值（Value）            可以是字符串，数字，true 或 false，null 等等
    对象（Object）       无序的键:值对集合
    空格（Whitespace）   可用于任意符号对之间
    null    空
    """

JSON syntax is derived from JavaScript object notation syntax:

- **Data is in name/value pairs**
- Data is separated by commas
- Curly braces hold objects {}
- Square brackets hold arrays[]

    {"employees:[
    {"firstName"="John", "Lastname":"Doe"},
    {"firstName"="Anna", "Lastname":"Smith"}
    {"firstName"="Peter", "Lastname":"Jones"}
    ]}

Numbers in JSON must be an integer or a floating point.

    {"age"= 30}

Strings in JSON must be written in double quotes.

    {"name"="John"}

Values in JSON can be objects.Objects as values in JSON must follow the same rules as JSON objects.

    {
    "employee"={"name"="Jone", "age"=30, "city":"New York"}
    }

Values in JSON can be arrays.

    {
    "employees":["John", "Anee","Peter"]
    }

Values in JSON can be true/false.

    {"sale"= true}

Values in JSON can be null.

    {"middlename"= null}

## Python 编码和解码 encoder and decoder

ref:[json — JSON encoder and decoder — Python 3.7.3 documentation](https://docs.python.org/3.7/library/json.html)

json 模块提供了一种很简单的方式来编码和解码JSON数据。 其中两个主要的函数是 json.dumps() 和 json.loads() ， 要比其他序列化函数库如pickle的接口少得多。

需要

    import json

### 编码：json.dumps(obj)

编码函数的括号中能够写点啥？

Json编码支持的基本类型：
None、bool、int、float、str、list、tuple、dict
对于字典，Json会假设Key是字符串（任何非字符串都会在编码时转换为字符串）

重点：
  1、为了符合规范，应该只对Python中的list和dict进行编码
  2、在web应用中，把最顶层对象定义为字典是一种标准做法

    json.dumps(['foo', {'bar':('baz, None, 1.0, 2')}])
    '["foo", {"bar": "baz, None, 1.0, 2"}]'
    # 输出 json 格式的数据，双引号对上了，但为啥 None 没有变成 null？ 为啥“foo”可以单独出现？
    
    print(json.dumps("\"foo\bar"))
    "\"foo\bar"
    
    print(json.dumps({"c":"0","b":0,"a":0}, sort_key=True))
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
      File "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/json/__init__.py", line 238, in dumps
        **kw).encode(obj)
    TypeError: __init__() got an unexpected keyword argument 'sort_key'
    print(json.dumps({"c":"0","b":0,"a":0}, sort_keys=True))
    {"a": 0, "b": 0, "c": "0"}
    
    # 为什么 sort_key 不行 sort_keys 可以
    # 答：json.dumps方法提供了很多好用的参数可供选择，比较常用的有sort_keys（对dict对象进行排序，我们知道默认dict是无序存放的），separators，indent等参数。排序功能使得存储的数据更加有利于观察，也使得对json输出的对象进行比较，例如

    >>> from io import StringIO
    >>> io = StringIO()
    >>> json.dump(['streaming API'], io)
    >>> io.getvalue()
    '["streaming API"]'
    
    # 这个还不太懂是啥

 Compact encoding

    jason.dumps([1,2,3,{'4':5,'6':7}, separators=(',', ':')])
      File "<input>", line 1
        jason.dumps([1,2,3,{'4':5,'6':7}, separators=(',', ':')])
                                                    ^
    SyntaxError: invalid syntax
    # 把 json 写成了 jason
    
    json.dumps([1,2,3,{'4':5,'6':7}, separators=(',', ':')])
      File "<input>", line 1
        json.dumps([1,2,3,{'4':5,'6':7}, separators=(',', ':')])
                                                   ^
    SyntaxError: invalid syntax
    
    #逗号之后要空格，[] {} 都要打全不能只打一半
    
    json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
    '[1,2,3,{"4":5,"6":7}]'
    json.dumps([1, 2, 3, {'4': 5, '6': 7}])
    '[1, 2, 3, {"4": 5, "6": 7}]'
    
    # 紧凑编码和不紧凑

 Pretty printing

    print(json.dumps({"4":5, "6":7}, sort_keys=True, indent=5))
    {
         "4": 5,
         "6": 7
    }
    
    # indent 是缩进
    # sort_keys 是排序

### 解码：json.loads()

    json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
    ['foo', {'bar': ['baz', None, 1.0, 2]}]

- 其他疑问
    - 什么是参数
    - 什么是 dict 数据格式
    - None、bool、int、float、str、list、tuple、dict 这些数据形式需要了解一下

### Json 数据类型和 Python 数据类型的区别

    """
    json格式和python语法的区别：
    true  映射为 True
    false 映射为 False
    null  映射为 None 
    object 映射为 dict
    array  映射为 list，tuple
    string 映射为 str，Unicode
    number 映射为 int，long，float
    """
    
    再写一遍
    """
    数字型（Number）       JavaScript 中的双精度浮点型格式
    字符串型（String）     双引号包裹的 Unicode 字符和反斜杠转义字符
    布尔型（Boolean）      true 或 false
    数组（Array）          有序的值序列
    值（Value）            可以是字符串，数字，true 或 false，null 等等
    对象（Object）       无序的键:值对集合
    空格（Whitespace）   可用于任意符号对之间
    null    空
    """
    
    
    >>> json.loads('false')
    False
    >>> json.loads('true')
    True
    >>> print(json.loads('null'))
    None
    
    # 注意 单引号 和 双引号
    >>> py_dict = {'a':True, 'b':None, 'c':'Hi'}
    >>> json.dumps(py_dict)
    '{"a": true, "b": null, "c": "Hi"}'

### **字符串 <—编码/解码—> Json**

    """
    两个主要函数实现：
    编码：json.dumps()
    解码：json.loads()
    """
    >>> import json
    >>> data = {"name": "lin", ["email":"xiaoqinglin2018@gmail.com](mailto:%22email%22:%22xiaoqinglin2018@gmail.com)"}
    >>> json_str = json.dumps(data) # py数据结构 --> json编码的字符串
    >>> json_str
    '{"name": "lin", "email": ["xiaoqinglin2018@gmail.com](mailto:%22xiaoqinglin2018@gmail.com)"}'
    >>> data = json.loads(json_str) # json
    >>> data # json编码的字符串 --> py数据结构dict
    {'name': 'lin', 'email': 'xiaoqinglin2018@gmail.com'}

我的操作

    import json
      File "<input>", line 1
        import json
        ^
    IndentationError: unexpected indent
    import json
    person = {"name":"Sandy", "age":25, "compandy":"Memect"}
    jason_str = json.dumps(person)# py数据结构 --> json编码的字符串
    jason_str
    '{"name": "Sandy", "age": 25, "compandy": "Memect"}'
    
    person = json.load(json_str)
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    NameError: name 'json_str' is not defined
    person = json.loads(jason_str)
    person # json编码的字符串 --> py数据结构dict
    {'name': 'Sandy', 'age': 25, 'compandy': 'Memect'}

- 问题
    - py 有哪几种数据结构，数列和字典有什么区别？
        - 字典是无序
        - 字典用{} 数列用[]
    - 怎么判断那种是 json 的数据结构那种是 python 数据结构
    - 遇到的一个小问题，错误的缩进，完全是意外错误

            import json
              File "<input>", line 1
                import json
                ^
            IndentationError: unexpected indent

    - json.load()  json.loads 不是一个，需要注意
    - 为什么要变为字符串，为什么要有这么一个  jason_str ?

### 文件**<—编码/解码—> Json**

read JSON from a file or write JSON to a file

The easiest way to write your data in the JSON format to a file using Python is to **use store your data in a dict object**, which can contain other nested dicts, arrays, booleans, or other primitive types like integers and strings. You can find a more detailed list of data types supported here. [https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/](https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/)

    """
    两个主要函数：
        编码：json.dump()
        解码：json.load()
    """
    data = {'name': 'lin', 'email': 'xiaoqinglin2018@gmail.com'}
    with open('json_note.json', 'w') as f: # writing Json data
      json.dump(data, f)
    
    json_note.json
    {"name": "lin", "email": "xiaoqinglin2018@gmail.com"}
    
    with open('json_note', 'r') as f: # 解码json
        data = json.load(f)
        data
    {'name': 'lin', 'email': 'xiaoqinglin2018@gmail.com'}

我的操作

    data = {'name': 'lin', 'email': 'xiaoqinglin2018@gmail.com'}
    with open ('json_note.json', 'w') as f:
        a = json.dump(data, f)
        
    a
    print(a)
    None
    
    json_note.json
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    NameError: name 'json_note' is not defined
    
    with open('json_note.json', 'r') as f:
        k = json.load(f)
        
    k
    {'name': 'lin', 'email': 'xiaoqinglin2018@gmail.com'}

- 问题
    - [ ]  写入一个 json 文件后，我怎么查看这个文件呢？查看不了。我命名了一个变量，但是返回值是 None。
    - json_note.json 这个文件是怎么定义的
        - 是自己定义的
    - 文件编码解码的过程不是很懂

- 问题
    - 为什么 json 中 True 会变为 true？ 那么布尔值还是布尔值吗？如何和单纯的单词区分
    - python 里面单引号和双引号都是一样的呀，不是吗？

## 检查 Json 解码得到的数据

    """
    解决问题：深层次的嵌套结构或有很多字段时，查看数据的结构
    """
    >>> import json
    >>> from urllib.request import urlopen 
    # google 搜免费接口 https://www.sojson.com/api/qqmusic.html
    >>> data = urlopen('https://www.sojson.com/api/qqmusic/8446666/json') 
    >>> pprint(data.read().decode('utf-8'))
    ('{"data":{"curtime":"1555001724","issmarter":"0","xmusicnum":"4","picurl":[],"playlist":[{"xqusic_mid":"002NkERn2LNVI4 '
     '","xqusic_id":"105030812","xctype":"3","xexpire_time":"0","xdesc":" '
     '","xsong_name":"Faded ","xsinger_name":"Alan Walker '
     '","xsong_url":"http://stream8.qqmusic.qq.com/117030812.wma '
     '","xsong_size":"1834194","xsong_playtime":"212","xsong_diskname":"Faded '
     '","xsong_dissmid":["002Nt51E0q8Zoo ","002Nt51E0q8Zoo '
     '"],"xsong_dissid":"1211728","xis_word":"0","xcopy_right":"0","xsinger_id":"944940","xsinger_mid":"0020PeOh4ZaCw1 '
     '"},{"xqusic_mid":"000aB5HG4dioBi '
     '","xqusic_id":"4831024","xctype":"3","xexpire_time":"0","xdesc":" '
     '","xsong_name":"海誓山盟亦会分开 ","xsinger_name":"本兮 '
     '","xsong_url":"http://stream6.qqmusic.qq.com/16831024.wma '
     '","xsong_size":"2496570","xsong_playtime":"289","xsong_diskname":"无底线 '
     '","xsong_dissmid":["004LrhoF44bRf2 ","004LrhoF44bRf2 '
     '"],"xsong_dissid":"193826","xis_word":"0","xcopy_right":"0","xsinger_id":"4545","xsinger_mid":"003LaMHm42u7qS '
     '"},{"xqusic_mid":"0019kz9c1QBWNA '
     '","xqusic_id":"2633764432","xctype":"1","xexpire_time":"0","xdesc":" '
     '","xsinger_name":"文艺范电台 ","xsong_name":"文艺范电台 '
     '","xsong_url":"http://img.wenyifan.net/20131221/5/1387627094890.mp3 '
     '","xsong_size":"0","xsong_playtime":"0","xsong_diskname":"0","xsong_dissmid":"0047airw212ppN '
     '","xsong_dissid":"0","xis_word":"-999","xcopy_right":"-999","xsinger_id":"-999"},{"xqusic_mid":"001rVHgt15aRmM '
     '","xqusic_id":"699379606","xctype":"5","xexpire_time":"0","xdesc":" '
     '","xsinger_name":"soso ","xsong_name":"8446666&#46;mp3 '
     '","xsong_url":"http://streamrdt.music.qq.com/8138.83a798500d5cb2b63f442ec3ee215a8d/1081067841555001724/8138.83a798500d.html '
     '","xsong_size":"0","xsong_playtime":"0","xsong_diskname":"0","xsong_dissmid":"0047airw212ppN '
     '","xsong_dissid":"0","xis_word":"-999","xcopy_right":"-999","xsinger_id":"-999"}],"systemtime":"1555001724"},"type":"json","status":200}')

我的运行是错误的

    from urllib.request import urlopen 
    data = urlopen('https://www.sojson.com/api/qqmusic/8446666/json') 
    pprint(data.read().decode('utf-8'))
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: 'module' object is not callable
    
    import read
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
      File "/Applications/PyCharm.app/Contents/helpers/pydev/_pydev_bundle/pydev_import_hook.py", line 21, in do_import
        module = self._system_import(name, *args, **kwargs)
    ModuleNotFoundError: No module named 'read'
    import decode
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
      File "/Applications/PyCharm.app/Contents/helpers/pydev/_pydev_bundle/pydev_import_hook.py", line 21, in do_import
        module = self._system_import(name, *args, **kwargs)
    ModuleNotFoundError: No module named 'decode'

错误类型：TypeError: 'module' object is not callable

- 问题
    - 按照你的代码敲但是发生了错误，不知道怎么检查

## Json 创建其他类型对象

    """
    通常情况下
    Json解码时会从所提供的数据中创建字典(dict)或者列表(list)
    解决方法：
        json.loads()方法提供的object_pairs_hook 或 object_hook参数
    """
    # 将json数据解码为OrderedDict(有序字典)
    >>> from collections import OrderedDict
    >>> msg = '{"name": "lin","age":"24","email":"xiaoqinglin2018@gmail.com"}'
    >>> data = json(msg, objects_pairs_hook = OrderedDict)
    >>> data = json.loads(msg, object_pairs_hook = OrderedDict) # 解码 
    >>> data 
    OrderedDict([('name', 'lin'), ('age', '24')('email','xiaoqinglin2018@gmail.com')])
    
    """
    JSON字典 转为 Python对象
    """
    class JSONObjects:
      def __init__(self,b):
        self.__dict__ = b
    
    >>> class JSONObjects:
    ...   def __init__(self,b):
    ...     self.__dict__ = b
    ... 
    >>> data = json.loads(msg, object_hook=JSONObjects)
    >>> data.name
    'lin'
    >>> data.email
    'xiaoqinglin2018@gmail.com'
    >>> data.age 
    '24'

    import collections
    from collections import OrderedDict
    msg = '{"name"="Sandy", "age"= 25}'
    data = json(msg, objects_pairs_hook = OrderedDict)
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    TypeError: 'module' object is not callable

错误类型：

- TypeError: 'module' object is not callable

## 常用的编码 Json 的选项

    """
    让输出格式变得漂亮一些
    解决方法：json.dumps()函数使用indent参数  # 类似pprint
    """
    json.dumps(data)
    >>> msg = {"name": "lin", "age":"24", "email":"xiaoqinglin2018@gmail.com"}
    >>> print(json.dumps(msg, indent=4)) 
    {
        "name": "lin",
        "age": "24",
        "email": "xiaoqinglin2018@gmail.com"
    }
    
    """
    输出中对key进行排序处理
    解决方法：sort_keys 参数
    
    >>> print(json.dumps(msg,sort_keys=True))
    {"age": "24", "email": "xiaoqinglin2018@gmail.com", "name": "lin"}
    """

## 如何序列化实例

    """
    类实例一般是无法序列化为JSON
    """
    >>> class MSG:
    ...     def __init__(self, name, age):
    ...             self.name = name 
    ...             self.age = age 
    ... 
    >>> msg = MSG('lin', 24)
    >>> json.dumps(msg)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/Users/xiaoqinglin-guanliyuan/.pyenv/versions/3.6.6/lib/python3.6/json/__init__.py", line 231, in dumps
        return _default_encoder.encode(obj)
      File "/Users/xiaoqinglin-guanliyuan/.pyenv/versions/3.6.6/lib/python3.6/json/encoder.py", line 199, in encode
        chunks = self.iterencode(o, _one_shot=True)
      File "/Users/xiaoqinglin-guanliyuan/.pyenv/versions/3.6.6/lib/python3.6/json/encoder.py", line 257, in iterencode
        return _iterencode(o, 0)
      File "/Users/xiaoqinglin-guanliyuan/.pyenv/versions/3.6.6/lib/python3.6/json/encoder.py", line 180, in default
        o.__class__.__name__)
    TypeError: Object of type 'MSG' is not JSON serializable
    >>> 
    
    """
    序列化实例
    解决办法：提供一个函数将类实例作为输入并返回一个可以被序列化处理的dict
    明确两点：
            输入： 类实例
            返回： dict 
    """
    def serializer_instance(obj):
        """
        序列化类实例
        """
      msg = {"__classname__": type(obj).__name__}
      msg.update(vars(obj))
      return msg 
    
    >>> classes = {'MSG':MSG}
    
    def unserializer_instance(msg)
        cls_name = msg.pop('__classname__', None)
      if cls_name:
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in msg.items():
          setattr(obj, key, value)
          return obj
        else:
        return msg
    
    >>> p = MSG('lin', 24)
    >>> s = json.dumps(p, default=serializer_instance)
    >>> s
    '{"__classname__": "MSG", "name": "lin", "age": 24}'
    >>> a = json.loads(s, object_hook=unserializer_objece)
    >>> a
    <__main__.MSG object at 0x10cb62320>
    >>> a.name
    'lin'

这个我就敲一遍代码吧

    def serializer_instance(obj):
        msg = {"__classname__": tpye(obj).__name__}
        msg.update(var(obj))
        return msg
    classes = {'MSG':MSG}
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    NameError: name 'MSG' is not defined
    class MSG:
        def __int__(self, name, age):
            self.name = name
            self.age = age
            
    msg = Msg('Sadny', 25)
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    NameError: name 'Msg' is not defined

错误原因：NameError: name 'Msg' is not defined

