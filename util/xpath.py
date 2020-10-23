from lxml import etree
from io import StringIO

test_html = '''
<html>
    <body>
        <div>
            <!-- 这里是注释 -->
            <h4>手机品牌商<span style="margin-left:10px">4</span></h4>
            <ul>
               <li>小米</li>
               <li>华为</li>
               <li class='blank'> OPPO </li>
               <li>苹果</li>
            </ul>
        </div>
        <div>
            <h4>电脑品牌商<span style="margin-left:10px">3</span></h4>
            <ul class="ul" style="color:red">
                <li>戴尔</li>
                <li>机械革命</li>
                <li>ThinkPad</li>
            </ul>
        </div>
    </body>
</html>'''

html = etree.parse(StringIO(test_html))




# 查找并设置第一个查询到的元素
first_ul = html.find("//ul")
ul_li = first_ul.xpath("li")
for li in ul_li:
    # 删除元素
    first_ul.remove(li)

ul_li = first_ul.xpath("li")
if len(ul_li) == 0:
    print("元素被删除了")


li_list = html.xpath('//li')

print("类型：")
print(type(li_list))

print("值：")
print(li_list)

print("个数：")
print(len(li_list))


for l in li_list:
    print("li文本为：" + l.text)


body = html.find("body")
for sub in body.iter():
    print(sub.tag)
    print(sub.text)