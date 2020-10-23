from selenium import webdriver
from selenium.webdriver.chrome.options import Options # => 引入Chrome的配置
import time

# 配置
ch_options = Options()
ch_options.add_argument("--headless")  # => 为Chrome配置无头模式 # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
ch_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
ch_options.add_argument('window-size=1400x900')  # 指定浏览器分辨率
ch_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
ch_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
ch_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
#ch_options.binary_location = r"E://Program Files//Python//Python38//Scripts//chromedriver.exe"  # 手动指定使用的浏览器位置

# 在启动浏览器时加入配置
driver = webdriver.Chrome(chrome_options=ch_options) # => 注意这里的参数

driver.get('http://baidu.com')
driver.find_element_by_id('kw').send_keys('测试')
driver.find_element_by_id('su').click()

time.sleep(2)

# 只有截图才能看到效果咯
driver.save_screenshot('./测试留痕.png')

driver.quit()