# 抓取文因的图书馆的教程篇

```
import requests, re  # #用来解释代码 import 简单理解为导入  requests re bs4 BeautifulSoup 可以理解为写爬虫常用工具，拿来用就行
from bs4 import BeautifulSoup  
# 以下这一大块代码都在定义一个函数，可以理解为一个小工具
def get_wenyin_booklist():  # 名字你来定

    # 以下几行表示开始抓取第一个页面了
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'} # 通过这个来模拟浏览器访问，告诉浏览器你是一个正常访问者
    url = r'http://book.duyima.com/web/libraryshow/more?keywords=&code=mWksP80d&type=1&limit=24' # 输入你想爬取的网址
    r = requests.get(url,headers=headers,timeout = 60) 
    r.encoding = 'UTF-8'
    
    # 以下代码用来抓取书籍的本书和总共页面的页数
    total_number = re.search(r'<b style="color:green">([^<>]+?)</b>', r.text).group(1)
    total_page = int(int(total_number) / 24) + 1
    print('一共 ' + str(total_number) + ' 本 ' +  str(total_page) + ' 页')
    
    book_title_all = []
    for page_num in range(1, total_page+1): # 以下三行代码用来一页一页地抓取数据
        url_page = url + '&page=' + str(page_num)
        html_doc = requests.get(url_page,headers=headers,timeout = 60)
        html_doc.encoding = 'UTF-8'
        # 以下代码从网页中找到标题
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        page_book = soup.find_all(name='p',attrs={"class":"book-title"}) 
        for book_item in page_book:
            book_title = re.sub(r'<[^<>]+?>', '', str(book_item))
            book_title_all.append(book_title.strip())
    num = 1
    # 以下代码用于给书籍加上序号
    for item in book_title_all:
        print( '- ' + str(num).zfill(4) + ' :: ' + item.replace('\n',''))
        num+=1
            
       # 以下两行代码用于执行上面定义的函数，或者说调用一个工具包
if __name__ == "__main__":
    get_wenyin_booklist()
```

